Aquí se encuentran:
* Notebook con código ejecutado y salidas visibles
* Carpeta data.zip (necesaria para la parte A)
* Embeddings obtenidos para la parte A y B (train,dev,test, kaspersky y enterprise)
* JSON con técnicas Enterprise (parte B)
* CSVs necesarios: anotación_referencia.csv y oraciones_kaspersky.csv

> **Nota sobre el alcance de este avance.**

Los criterios de evaluación del Avance 4 (comparativa de algoritmos, ajuste fino y modelo individual) se cubren en la **Parte A**. 
Las **Partes B y C** son trabajo adicional del equipo, fuera de esos criterios, pero tienen valor para las siguientes etapas del proyecto:
> - **Parte B (similitud):** evalúa si la técnica MITRE correcta se puede recuperar a partir de la oración con TF-IDF y con MiniLM, es decir, la etapa que sigue al clasificador en el pipeline.
> - **Parte C (Composite Threat Score):** analiza qué tan sensible es la calificación de peligrosidad a la fórmula elegida, de modo que la etapa de severidad no dependa de pesos arbitrarios.

Ambas se incluyen como contexto y como insumo para decisiones posteriores; no sustituyen ni modifican los resultados de la Parte A.
