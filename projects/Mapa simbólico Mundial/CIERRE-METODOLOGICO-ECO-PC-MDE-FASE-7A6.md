# Cierre metodológico de `ECO_PC/MDE` — Fase 7A.6

Fecha: 2026-07-28  
Edición: `RG2025_V1`  
Proyecto: Retícula Global 2025 — Support

## Decisión final

**NO-GO metodológico para publicar `ECO_PC/MDE` bajo el criterio estricto del 95 %.**

No se ha encontrado un PIB nominal de Siria para 2024 que sea compatible con el resto del bloque económico. La fila se conserva en el CSV de 54 claves, pero queda marcada como `NO PUBLICABLE`. No se modifica MySQL, la API ni la web y no se prepara SQL de carga.

## Fuentes examinadas

| Fuente | Año | Valor | Unidad | Tipo de PIB | Compatibilidad | Decisión | Observaciones |
|---|---:|---:|---|---|---|---|---|
| Banco Mundial WDI `NY.GDP.MKTP.CD` | 2024 | `null` | USD corrientes | PIB nominal | Compatible en definición, pero sin observación para Siria | RECHAZADO | La respuesta oficial de WDI no contiene valor para 2024. |
| FMI, WEO/DataMapper | 2024 | Sin dato para Siria | USD corrientes | PIB nominal | No hay observación institucional recuperable para Siria | RECHAZADO | El perfil WEO muestra Siria sin datos; no se usa un agregado regional ni una proyección. |
| Naciones Unidas | 2024 | Sin dato comparable localizado | USD corrientes | PIB nominal | No se obtuvo una fila verificable para Siria en los materiales consultados | RECHAZADO | La ausencia no se convierte en cero. |
| Banco Mundial WDI `NY.GDP.MKTP.CD` | 2023 | `null` | USD corrientes | PIB nominal | Compatible en definición, pero sin observación | RECHAZADO | La respuesta oficial WDI tampoco ofrece 2023. |
| Banco Mundial WDI `NY.GDP.MKTP.CD` | 2022 | `23.737.634.644,3994` | USD corrientes | PIB nominal | Definición compatible, año incompatible con el bloque 2024 | RECHAZADO PARA CARGA | Se conserva como referencia de sensibilidad; no se incorpora automáticamente. |
| Organismo estadístico oficial sirio | 2022–2024 | Sin dato verificable localizado | — | — | No evaluable | RECHAZADO | No se sustituye por una estimación no documentada. |

Fuentes directas conservadas o consultadas:

- [Banco Mundial WDI, PIB corriente](https://api.worldbank.org/v2/country/syr/indicator/NY.GDP.MKTP.CD?date=2022%26format=json%26per_page=100)
- [FMI, perfil WEO de Siria](https://www.imf.org/external/datamapper/profile/SYR)
- [FMI, informe de Yemen 2025 Article IV](https://www.imf.org/en/news/articles/2026/04/02/pr-26106-yemen-imf-executive-board-concludes-2025-article-iv-consult)

## Magnitudes de MDE

Con la regeneración 7A.5:

- población total MDE en 2024: **382.442.216 habitantes**;
- población cubierta: **357.769.458 habitantes**;
- cobertura: **93,5486 %**;
- población de Siria usada para medir el peso demográfico: **24.672.758 habitantes**;
- peso demográfico de Siria sobre MDE: **6,4514 %**;
- PIB por habitante regional sin Siria: **14.263,430493 USD corrientes/hab.**;
- código ausente: `SYR`.

El peso demográfico explica por qué no es correcto presentar la fila como plenamente representativa, aunque el valor sea aritméticamente reproducible para la población cubierta.

## Efecto del dato de 2022

El valor WDI 2022 de Siria equivale a 23.737.634.644,3994 USD corrientes. Si se añadiera únicamente para medir sensibilidad, manteniendo los demás PIB de 2024 y usando la población MDE 2024 como denominador, el resultado sería aproximadamente **13.405,312533 USD/hab.** y la cobertura nominal alcanzaría el 100 %.

Ese cálculo no es admisible para la carga: mezcla PIB sirio de 2022 con PIB del resto de MDE de 2024. No se presenta como valor válido ni se incorpora al CSV como dato nacional 2024.

## Escenarios

### Escenario A — criterio estricto (recomendado)

`ECO_PC/MDE` queda **NO PUBLICABLE** hasta disponer de PIB nominal sirio del mismo año y definición compatible. Se mantiene el valor calculado para la población cubierta únicamente como resultado interno de preparación, no como dato público.

Texto exacto de observación web:

> PIB nominal por habitante de MDE: NO DISPONIBLE. La cobertura actual es 93,5486 %; Siria no está incluida por falta de un dato institucional comparable para 2024. Yemen sí está incluido con fuente FMI. La fila no se publica bajo el umbral metodológico del 95 %.

### Escenario B — excepción específica (no recomendado)

Podría marcarse `VALIDADO CON EXCEPCIÓN` y mostrar 14.263,430493 USD/hab. con cobertura 93,5486 %, sin Siria. Esta excepción solo afectaría a `ECO_PC/MDE`; no rebajaría el umbral general ni permitiría usar el dato sirio de 2022.

Texto exacto de observación web en ese caso:

> PIB nominal por habitante de MDE: 14.263 USD. Cobertura 93,5486 %. Siria no está incluida por falta de un dato institucional comparable para 2024; Yemen sí está incluido con fuente FMI. Este valor se muestra mediante una excepción metodológica y no es plenamente comparable.

Se recomienda el **Escenario A** porque evita presentar como comparable una magnitud que omite una población equivalente al 6,4514 % del área y mantiene la regla común de cobertura.

## Archivo de datos 7A.6

`datos-area-indicadores-complementarios-7a6.csv` conserva exactamente:

- seis indicadores;
- nueve áreas por indicador;
- 54 claves únicas;
- ningún valor nulo convertido en cero.

Solo cambia la clasificación de `ECO_PC/MDE` a `NO PUBLICABLE` y su observación metodológica. Las otras 53 filas conservan sus valores y estados de 7A.5.

## Estado y límites

- MySQL: sin modificaciones.
- API: sin modificaciones.
- Web: sin modificaciones.
- SQL de carga: no preparado.
- Despliegue: no realizado.
- Decisión: **NO-GO metodológico limitado exclusivamente a `ECO_PC/MDE`**.

