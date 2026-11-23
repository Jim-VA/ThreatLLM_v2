Aquí se encuentran:
* Notebook `Avance5_55.ipynb` con código ejecutado y salidas visibles
* Carpeta `data.zip` (LADDER: train, dev y test)
* `oraciones_kaspersky.csv` (96 oraciones del reporte de Kaspersky)
* Embeddings MiniLM en caché: `emb_minilm_{train,dev,test,kaspersky}.npy` (si no están, se recalculan)
* Resultados de la búsqueda de hiperparámetros: `busqueda_randomforestclassifier_1166b855.joblib` y `busqueda_extratreesclassifier_1771e223.joblib` (evitan repetir ~20 min por modelo)
* `automl_flaml_5cab405b.joblib` (resultado de FLAML; si no está, la búsqueda se repite, ~5 min)

**Cómo ejecutar:** subir todos los archivos a `/content` en Colab y quitar el `#` de los `pip install` de las celdas 8 (`flaml[automl]`) y 9 (`sentence-transformers`) la primera vez.

**Contenido:** 3.1 ensambles heterogéneos (Voting, Stacking), 3.2 homogéneos (RF, Extra Trees, Gradient Boosting, Bagging), 3.3 AutoML (FLAML), 4 modelo final: Stacking (LogReg + CNB calibrado) con umbral 0.325. 

**Modelo final para el laboratorio (entregables):**
* `modelo_final_stacking.joblib`: modelo final entrenado (Stacking LogReg + CNB calibrado) con su umbral (0.3247), la huella SHA-256 de `train.csv`, las métricas en test (F1 0.836, recall 0.943, precisión 0.752) y las versiones de librerías usadas: Python 3.13, scikit-learn 1.9.1, numpy 2.5.5, pandas 3.1.1, joblib 1.6.0.
* `clasificar_reporte.py`: clasifica un reporte nuevo. Acepta un `.txt` (lo segmenta con la regla del pipeline y descarta fragmentos de 3 palabras o menos) o un `.csv` con una oración por fila; genera `<entrada>_clasificado.csv` con la probabilidad de ataque y la decisión de cada oración.
  * `python clasificar_reporte.py reporte.txt`
  * `python clasificar_reporte.py oraciones.csv --columna texto --umbral 0.40`
* `entrenar_modelo_final.py`: vuelve a entrenar y guardar el modelo (≈1.5 min con CPU). Solo guarda si reproduce las cifras de referencia en test. Úselo si su versión de scikit-learn es distinta de la del archivo `.joblib`: `python entrenar_modelo_final.py` (descomprime `data.zip` si hace falta).
* Seguridad: `joblib.load` ejecuta código al cargar; use solo el `.joblib` entregado por el equipo.

**Material complementario**: Script adicional al Avance 5, independiente. Entrena con train de LADDER y evalúa el modelo final en las 96 oraciones del reporte Kaspersky. Requiere data.zip, oraciones_kaspersky.csv y anotacion_referencia.csv. Anotación de referencia preparada por el asesor con apoyo de IA. Se reporta en el Av.6 (artículo)
