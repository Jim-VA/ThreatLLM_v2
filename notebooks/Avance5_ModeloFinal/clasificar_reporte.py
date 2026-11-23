"""Clasifica las oraciones de un reporte de inteligencia de amenazas como ataque o contexto.

Entrada:
  * Un archivo .txt con el texto del reporte. Se segmenta con la regla del pipeline heredado
    (corte tras . ! ? o en saltos de línea) y se descartan los fragmentos de 3 palabras o menos.
  * Un archivo .csv con una oración por fila (columna 'texto' o 'text', o la que indique --columna).

Salida: un CSV con cada oración, su probabilidad de ataque y la decisión (ataque/contexto)
según el umbral guardado con el modelo (0.325), más un resumen en pantalla. La decisión es una
sugerencia: el analista revisa las oraciones marcadas y una muestra de las descartadas.

Uso:
    python clasificar_reporte.py reporte.txt
    python clasificar_reporte.py oraciones.csv --columna texto --salida resultado.csv
    python clasificar_reporte.py reporte.txt --umbral 0.40      # umbral acordado con el laboratorio

Seguridad: joblib.load ejecuta código al cargar; use solo el archivo de modelo entregado por el equipo.

Equipo 55 · Proyecto Integrador · Maestría en Inteligencia Artificial Aplicada.
Declaración de uso de IA: script generado con apoyo de Claude (Opus 5.5); el equipo verificó sus resultados.
"""
import argparse
import re
import sys
import warnings
from datetime import datetime
from pathlib import Path

import joblib
import pandas as pd
import sklearn

AQUI = Path(__file__).resolve().parent
PALABRAS_MINIMAS = 4   # se descartan fragmentos de 3 palabras o menos


def segmentar(texto: str) -> list:
    """Regla de segmentación del pipeline heredado (Avances 2 y 3)."""
    partes = re.split(r"(?<=[.!?])\s+|\n+", texto.strip())
    return [p.strip() for p in partes if len(p.strip().split()) >= PALABRAS_MINIMAS]


def leer_oraciones(ruta: Path, columna: str | None) -> list:
    if ruta.suffix.lower() == ".csv":
        df = pd.read_csv(ruta)
        col = columna or next((c for c in ("texto", "text", "oracion") if c in df.columns), None)
        if col is None or col not in df.columns:
            sys.exit(f"No se encontró la columna de texto en {ruta.name}; use --columna. Columnas: {list(df.columns)}")
        return [str(t).strip() for t in df[col].dropna() if str(t).strip()]
    return segmentar(ruta.read_text(encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entrada", type=Path, help="reporte .txt u oraciones .csv")
    ap.add_argument("--modelo", type=Path, default=AQUI / "modelo_final_stacking.joblib")
    ap.add_argument("--umbral", type=float, default=None, help="sustituye el umbral guardado con el modelo")
    ap.add_argument("--columna", default=None, help="columna de texto si la entrada es .csv")
    ap.add_argument("--salida", type=Path, default=None, help="CSV de salida (por omisión, <entrada>_clasificado.csv)")
    args = ap.parse_args()

    if not args.entrada.exists():
        sys.exit(f"No existe el archivo de entrada: {args.entrada}")
    if not args.modelo.exists():
        sys.exit(f"No existe el modelo: {args.modelo}. Genérelo con entrenar_modelo_final.py.")

    paquete = joblib.load(args.modelo)
    version_guardada = paquete["versiones"]["scikit-learn"]
    if version_guardada != sklearn.__version__:
        warnings.warn(f"El modelo se guardó con scikit-learn {version_guardada} y se está usando "
                      f"{sklearn.__version__}; si hay errores, reentrene con entrenar_modelo_final.py.")
    umbral = paquete["umbral"] if args.umbral is None else args.umbral

    oraciones = leer_oraciones(args.entrada, args.columna)
    if not oraciones:
        sys.exit("No se encontraron oraciones para clasificar.")

    prob = paquete["modelo"].predict_proba(oraciones)[:, 1]
    resultado = pd.DataFrame({
        "id": range(1, len(oraciones) + 1),
        "oracion": oraciones,
        "probabilidad_ataque": prob.round(4),
        "decision": ["ataque" if p >= umbral else "contexto" for p in prob],
    })
    resultado["umbral"] = round(umbral, 4)
    resultado["modelo_entrenado"] = paquete["fecha_entrenamiento"]
    resultado["fecha_clasificacion"] = datetime.now().isoformat(timespec="seconds")

    salida = args.salida or args.entrada.with_name(f"{args.entrada.stem}_clasificado.csv")
    resultado.to_csv(salida, index=False, encoding="utf-8")

    marcadas = resultado[resultado["decision"] == "ataque"]
    print(f"Oraciones clasificadas: {len(resultado)} | marcadas como ataque: {len(marcadas)} "
          f"({len(marcadas) / len(resultado):.1%}) | umbral: {umbral:.4f}")
    print("Las 5 con mayor probabilidad de ataque:")
    for _, fila in resultado.nlargest(5, "probabilidad_ataque").iterrows():
        print(f"  {fila.probabilidad_ataque:.3f}  {fila.oracion[:100]}")
    print(f"Resultado guardado en: {salida}")
    print("Recuerde: revisar las oraciones marcadas y auditar una muestra de 10 descartadas.")


if __name__ == "__main__":
    main()
