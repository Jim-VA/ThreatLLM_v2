# Planteamiento del proyecto

**Tecnológico de Monterrey**

*TC5035.10 Proyecto Integrador*

**Prof. Titular**

Dra. Grettel Barceló Alonso

**Prof. Asesor**

Dr. Victor Munguia

**Equipo 55**
* Edson Garduño Nolasco – A01795770
* Irving Alan García Zapata – A01796793
* Ada Jimena Vargas Aguirre – A01701619

---
# Índice
- [Título del proyecto](https://github.com/Jim-VA/ThreatLLM_v2/blob/main/documentation/DatosGenerales.55.md#t%C3%ADtulo-del-proyecto)
- [Información General](https://github.com/Jim-VA/ThreatLLM_v2/blob/main/documentation/DatosGenerales.55.md#informaci%C3%B3n-general)
  * [Empresa/ Institución](#empresa--instituci-n)
  * [Sector industrial](#sector-industrial)
  * [Lugar de aplicación](#lugar-de-aplicaci-n)
  * [Patrocinador / Sponsor](#patrocinador---sponsor)
  * [Datos del sponsor](#datos-del-sponsor)
  * [Dominio de aplicación](https://github.com/Jim-VA/ThreatLLM_v2/blob/main/documentation/DatosGenerales.55.md#dominio-de-aplicaci%C3%B3n)
- [Detalles del proyecto]()
  * [Descripción de la necesidad y objetivo del proyecto]()
  * [Requerimientos]()
  * [Beneficios del proyecto]()
  * [Descripción del producto]()
  * [Alcance]()
  * [Recursos preasignados]()
- [Consideraciones del proyecto]()
  * [Riesgos]()
  * [Criterios de aceptación]()
  * [Suposiciones]()
  * [Limitantes]()
- [Plan de entregables](https://github.com/Jim-VA/ThreatLLM_v2/blob/main/documentation/DatosGenerales.55.md#plan-de-entregables)
- [Repositorio del proyecto]()
---
# Título del proyecto
ThreatLLM: Clasificación de Ciberataques mediante Modelos de Lenguaje

---

# Información General
## Empresa/ Institución
Laboratorio de Ciberseguridad del Centro de Investigación en Computación del Instituto Politécnico Nacional (CISEG-CIC-IPN)

## Sector industrial 
Sector SCIAN: 541712 

“Servicios de investigación científica y desarrollo en ciencias naturales y exactas, ingeniería, y ciencias de la vida, prestados por el sector público”

## Lugar de aplicación
Laboratorio de Ciberseguridad (CISEG), Centro de Investigación en Computación del Instituto Politécnico Nacional, Ciudad de México, México.

## Patrocinador/ Sponsor
Hub de Ciencia de Datos del Tec de Monterrey

## Datos del sponsor
Dr. Juan Arturo Nolazco Flores
* Director del Hub de Ciencia de Datos
* jnolazco@tec.mx 

## Dominio de aplicación
Procesamiento de lenguaje natural (NLP)

El proyecto está enfocado en el procesamiento de reportes de inteligencia de amenazas redactados en lenguaje natural, por medio de técnicas de comprensión semántica (ej.: embeddings, similitud coseno) y modelos de lenguaje, con la finalidad de extraer, clasificar y priorizar automáticamente contenido de amenaza. Por ende, el procesamiento de lenguaje natural representa el eje principal que habilita todas las etapas subsecuentes del sistema.

---
# Detalles del proyecto
## Descripción de la necesidad y objetivo del proyecto
Los analistas de Centros de Operaciones de Seguridad (SOC) lidian con una sobrecarga creciente de reportes de amenazas en formato no estructurado, lo que ralentiza su capacidad de respuesta.

El objetivo es contribuir a minimizar el tiempo que los analistas SOC tardan en responder ante amenazas, por medio de la detección, clasificación y priorización de dicha información.

## Requerimientos
* Programación en Python.
* Uso de arquitecturas generativas de Machine Learning (ML clásico, Deep Learning, Transformers).
* Métodos de Aprendizaje (Fine-Tunning, Supervisado)

## Beneficios del proyecto
Brindar un recurso de referencia para que los SOC puedan automatizar la interpretación de datos masivos no estructurados y acelerar la velocidad de respuesta ante incidentes.

## Descripción del producto
Artículo de investigación que documenta el diseño, desarrollo y evaluación de un sistema de procesamiento avanzado de eventos de seguridad mediante modelos de lenguaje natural, incluyendo el análisis exploratorio de datos, la ingeniería de características, la comparación de modelos de clasificación y el módulo de triage asistido por LLM.

## Alcance
El proyecto incluye:
* Análisis exploratorio del conjunto de datos LADDER Attack Pattern Dataset
* Ingeniería de características: construcción, fundamentación de la métrica threat_composite_score, análisis de interacción entre variables
* Evaluación del pipeline heredado mediante diversas métricas
* Exploración y comparación de algoritmos de clasificación, apoyada en herramientas de AutoML como H2O para una exploración inicial amplia, seguida de ajuste fino documentado manualmente sobre los modelos finalistas
* Integración de representaciones semánticas (embeddings) para comparar con el enfoque basado en TF-IDF
* Diseño y prueba de un prompt de triage final asistido por un modelo de lenguaje

No se incluye:
* Despliegue en producción del sistema dentro de la infraestructura real del SOC de un cliente
* Calibración de la métrica threat_composite_score  con retroalimentación operativa de un cliente SOC
* Extracción de patrones de ataque desde logs de kernel o registros de sistema en tiempo real
* Desarrollo de una interfaz de usuario para analistas → prioridad secundaria ante pipeline funcional (demostración)

## Recursos preasignados
[Notebooks heredados](https://github.com/Jim-VA/ThreatLLM_v2/tree/main/notebooks/preassigned_notebooks) del equipo que trabajó en la primera etapa del proyecto durante el trimestre anterior.

---
# Consideraciones del proyecto
## Riesgos
* Calidad insuficiente de los datos. 
* Desbalance entre categorías de amenazas. 
* Limitaciones de cómputo para fine-tuning. 
* Tiempo limitado para experimentar múltiples modelos.

## Criterios de aceptación
* El modelo clasifica amenazas con métricas documentadas. 
* Se entrega comparación entre enfoques TF-IDF y embeddings. 
* Se documenta el proceso experimental. 
* Se genera un flujo de triage asistido por LLM.

## Suposiciones
* El dataset proporcionado es suficiente para entrenamiento. 
* Los datos están correctamente etiquetados. 
* Los notebooks heredados son funcionales.

## Limitantes
* No habrá despliegue en producción. 
* No se tendrá acceso a eventos en tiempo real. 
* El proyecto se limita a datos históricos.

---
# Plan de entregables
| Semana | Entregables de referencia del curso | Entregable comprometido para el proyecto | Justificación / Propuesta | Formato |
| ---- | ---- | ---- |----| ---- |
| 1 | Planteamiento del proyecto | Planteamiento, plan y repositorio de GitHub |Entregable obligatorio del curso| MD/PDF |
| 2 | Propuesta de proyecto y firma de convenios | Propuesta y convenios aplicables |Entregable obligatorio del curso| MD/PDF |
| 3 | Análisis exploratorio de datos | Análisis exploratorio del dataset LADDER |Adaptado al análisis del dataset LADDER utilizado en el proyecto| Notebook .ipynb |
| 4 | Ingeniería de características |Ingeniería de características y construcción de embeddings |Se amplía para incluir la fundamentación teórica de la métrica de severidad, embeddings y representación semántica de amenazas.| Notebook .ipynb |
| 5 | Baseline | Modelo baseline TF-IDF + clasificación|El baseline se orienta a técnicas clásicas de NLP basadas en TF-IDF.| Notebook .ipynb |
| 6 | Modelos alternativos | Comparativa de modelos alternativos y AutoM |Se incorporan AutoML y modelos alternativos para comparación experimental.| Notebook .ipynb |
| 7 | Modelo final | Modelo final y evaluación |Considera la selección y evaluación del modelo final para ThreatLLM.| Notebook .ipynb |
| 8 |  Producto de difusión  | Borrador de E6 y diapositivas para revisión |Entregables obligatorios del curso| MD/PDF/PPT |
| 9 | Resumen ejecutivo| Artículo y Resumen Ejecutivo |Entregables obligatorios del curso| MD/PDF/PPT |
| 10 | Presentación final|Presentación y defensa final| Entregable obligatorio del curso | MD/PDF/PPT |

---
# Repositorio del proyecto
[Enlace a página principal](https://github.com/Jim-VA/ThreatLLM_v2 )
