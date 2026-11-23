"""Entrena el modelo final de ThreatLLM y lo guarda en un archivo .joblib.

Modelo: stacking de regresión logística y Complement Naive Bayes calibrado, con los
hiperparámetros de los Avances 4 y 5. El umbral de decisión se fija solo con la partición
de entrenamiento: el valor más alto que mantiene un recall fuera de pliegue >= META_RECALL.

Antes de guardar, el script comprueba que el modelo reproduce las cifras de referencia
en la partición de prueba de LADDER (F1 = 0.836, recall = 0.943). Si no las reproduce,
no guarda nada.

Uso:
    python entrenar_modelo_final.py
    python entrenar_modelo_final.py --datos data/ladder/sentence_classification --salida modelo_final_stacking.joblib

Equipo 55 · Proyecto Integrador · Maestría en Inteligencia Artificial Aplicada.
Declaración de uso de IA: script generado con apoyo de Claude (Opus 5.5) a partir del código
del cuaderno complementario del Avance 5; el equipo verificó las cifras de referencia.
"""
import argparse
import hashlib
import platform
import sys
import time
import warnings
import zipfile
from datetime import date
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import sklearn
from sklearn.base import clone
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import StackingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, precision_recall_curve, precision_score, recall_score
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.naive_bayes import ComplementNB
from sklearn.pipeline import make_pipeline

warnings.filterwarnings("ignore")

SEED = 42
META_RECALL = 0.95
REFERENCIA_TEST = {"f1": 0.836, "recall": 0.943}   # cifras del artículo (Tabla 6)
TOLERANCIA = 0.001
AQUI = Path(__file__).resolve().parent


def construir_modelo():
    """Stacking final del Avance 5 con los hiperparámetros afinados del Avance 4."""
    lr_f = make_pipeline(
        TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 7), min_df=2, sublinear_tf=True),
        LogisticRegression(C=3.382387201936218, penalty="l2", class_weight="balanced",
                           solver="liblinear", max_iter=5000, random_state=SEED))
    nb_f = make_pipeline(
        TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 5), min_df=2, sublinear_tf=True),
        ComplementNB(alpha=0.11040511903162252, norm=True))
    nb_cal = CalibratedClassifierCV(nb_f, method="sigmoid", cv=5)
    return StackingClassifier(estimators=[("lr", lr_f), ("nb", nb_cal)],
                              final_estimator=LogisticRegression(), cv=5)


def localizar_datos(carpeta: Path) -> Path:
    """Devuelve la carpeta con train.csv y test.csv; si falta, descomprime data.zip junto al script."""
    if (carpeta / "train.csv").exists():
        return carpeta
    zip_path = AQUI / "data.zip"
    if zip_path.exists():
        with zipfile.ZipFile(zip_path) as z:
            z.extractall(AQUI)
        alterna = AQUI / "data/ladder/sentence_classification"
        if (alterna / "train.csv").exists():
            return alterna
    sys.exit(f"No se encontró train.csv en {carpeta} ni en data.zip.")


def huella(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--datos", type=Path, default=AQUI / "data/ladder/sentence_classification",
                    help="carpeta con train.csv y test.csv de LADDER (separados por tabulador)")
    ap.add_argument("--salida", type=Path, default=AQUI / "modelo_final_stacking.joblib")
    args = ap.parse_args()

    datos = localizar_datos(args.datos)
    tr = pd.read_csv(datos / "train.csv", sep="\t")
    te = pd.read_csv(datos / "test.csv", sep="\t")
    ytr, yte = tr["label"].to_numpy(), te["label"].to_numpy()
    print(f"train: {len(tr)} oraciones | test: {len(te)} oraciones")

    modelo = construir_modelo()

    t0 = time.time()
    cv = StratifiedKFold(5, shuffle=True, random_state=SEED)
    p_oof = cross_val_predict(clone(modelo), tr["text"], ytr, cv=cv, method="predict_proba")[:, 1]
    _, rec, umbrales = precision_recall_curve(ytr, p_oof)
    umbral = float(umbrales[rec[:-1] >= META_RECALL].max())
    print(f"Umbral fijado con train (recall fuera de pliegue >= {META_RECALL}): {umbral:.4f}  ({time.time() - t0:.0f} s)")

    t0 = time.time()
    modelo.fit(tr["text"], ytr)
    print(f"Modelo entrenado en {time.time() - t0:.1f} s")

    pred = (modelo.predict_proba(te["text"])[:, 1] >= umbral).astype(int)
    metricas = {"f1": f1_score(yte, pred), "recall": recall_score(yte, pred),
                "precision": precision_score(yte, pred)}
    print("Test LADDER: " + " | ".join(f"{k} {v:.3f}" for k, v in metricas.items()))

    fallas = [k for k, ref in REFERENCIA_TEST.items() if abs(round(metricas[k], 3) - ref) > TOLERANCIA]
    if fallas:
        sys.exit(f"REVISAR: el modelo no reproduce las cifras de referencia ({', '.join(fallas)}). No se guardó.")
    print("Control: reproduce las cifras de referencia (F1 0.836, recall 0.943). OK")

    paquete = {
        "modelo": modelo,
        "umbral": umbral,
        "meta_recall": META_RECALL,
        "metricas_test_ladder": {k: round(v, 4) for k, v in metricas.items()},
        "huella_train_sha256": huella(datos / "train.csv"),
        "versiones": {"python": platform.python_version(), "scikit-learn": sklearn.__version__,
                      "numpy": np.__version__, "pandas": pd.__version__, "joblib": joblib.__version__},
        "fecha_entrenamiento": date.today().isoformat(),
        "descripcion": "Stacking (LogReg + Complement NB calibrado) sobre TF-IDF de n-gramas de "
                       "caracteres; clasifica oraciones de reportes CTI como ataque (1) o contexto (0).",
    }
    joblib.dump(paquete, args.salida, compress=3)
    print(f"Guardado: {args.salida} ({args.salida.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
