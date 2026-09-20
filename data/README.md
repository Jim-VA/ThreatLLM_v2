# Sobre los datos
Comprende toda la información utilizada en el proyecto.

## Origen
Los datos empleados provienen del framework **LADDER** (Looking Beyond IoCs: Automatically Extracting Attack Patterns from External CTI) presentado por Alam et al. (2023) en RAID 2023.

* Paper: https://arxiv.org/abs/2211.01753
* Repositorio oficial del framework: https://github.com/aiforsec/LADDER
  - Ruta en repo oficial: /attack_pattern/data

## Estructura
El proyecto usa 3 datasets complementarios, correspondientes a las etapas del pipeline TTPClassifier descrito en la Sección 4.3 del paper.

| Dataset  | Propósito | Formato |
| ---- | ---- | ---- |
| `sentence_classification` | Clasificación binaria (ataque o no) | CSV, separador TAB (text,label) |
|`entity_extraction`|Extracción del span exacto de la acción maliciosa|IOB/IOB2, un token por línea|
|`attack-pattern-matching-gt`|Mapeo a técnicas MITRE ATT&ACK|CSV (text, malware, label)|

## Forma de acceso
* Acceso: público / open-access, sin restricciones de uso para fines de investigación académica.
* Condiciones: ninguna adicional; no contiene información confidencial ni credenciales.
