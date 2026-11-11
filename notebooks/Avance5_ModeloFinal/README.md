Aquí se encuentran:
* Notebook `Avance5_55.ipynb` con código ejecutado y salidas visibles
* Carpeta `data.zip` (LADDER: train, dev y test)
* `oraciones_kaspersky.csv` (96 oraciones del reporte de Kaspersky)
* Embeddings MiniLM en caché: `emb_minilm_{train,dev,test,kaspersky}.npy` (si no están, se recalculan)
* Resultados de la búsqueda de hiperparámetros: `busqueda_randomforestclassifier_1166b855.joblib` y `busqueda_extratreesclassifier_1771e223.joblib` (evitan repetir ~20 min por modelo)
* `automl_flaml_5cab405b.joblib` (resultado de FLAML; si no está, la búsqueda se repite, ~5 min)

**Cómo ejecutar:** subir todos los archivos a `/content` en Colab y quitar el `#` de los `pip install` de las celdas 8 (`flaml[automl]`) y 9 (`sentence-transformers`) la primera vez.

**Contenido:** 3.1 ensambles heterogéneos (Voting, Stacking), 3.2 homogéneos (RF, Extra Trees, Gradient Boosting, Bagging), 3.3 AutoML (FLAML), 4 modelo final: Stacking (LogReg + CNB calibrado) con umbral 0.325. 

**Material complementario**: Script adicional al Avance 5, independiente. Entrena con train de LADDER y evalúa el modelo final en las 96 oraciones del reporte Kaspersky. Requiere data.zip, oraciones_kaspersky.csv y anotacion_referencia.csv. Anotación de referencia preparada por el asesor con apoyo de IA. Se reporta en el Av.6 (artículo)
