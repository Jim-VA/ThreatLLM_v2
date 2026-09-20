# ThreatLLM

## Descripción del proyecto
ThreatLLM automatiza la **primera fase del triage de ciberseguridad**.

Consiste en un sistema de 2 etapas para la detección, clasificación y priorización de amenazas descritas en reportes de inteligencia de amenazas cibernéticas (CTI), en conjunto con un pipeline de aprendizaje supervisado sobre representaciones semánticas del texto con un módulo de triage final asistido por un modelo de lenguaje (LLM).

Su funcionamiento se puede resumir en 3 pasos:
```
Reporte CTI crudo (texto libre)
        │
        ▼
[1] Clasificador de oraciones  →  ¿es una descripción de ataque?
        │
        ▼
[2] Matching semántico con MITRE ATT&CK  →  ¿qué técnica es?
        │
        ▼
[3] JSON estructurado + prompt  →  LLM asigna severidad final

```

## Objetivo
Minimizar el tiempo que los analistas de un Centro de Operaciones de Seguridad (SOC) tardan en responder ante amenazas, automatizando la interpretación de datos masivos no estructurados y acelerando la velocidad de respuesta ante incidentes.

## Integrantes
El equipo 55 está conformado por:
* Edson Garduño 
* Ada Vargas
* Irving García

## Estructura del repositorio
```
ThreatLLM_v2/
├── data/                                   # Datasets utilizados (LADDER Attack Pattern Dataset, MITRE ATT&CK mapping)
│   ├── sentence_classification      
│   ├── entity_extraction       
│   ├── attack-pattern-matching-gt.csv       
├── documentation/                          # Documento de planteamiento, plan de entregables, artículo de investigación
│   ├── DatosGenerales.55.md   
├── notebooks/                              # Notebooks del proyecto (EDA, feature engineering, modelado, comparación)
│   ├── preassigned_notebooks               # Notebooks preasignados
└── README.md

```
