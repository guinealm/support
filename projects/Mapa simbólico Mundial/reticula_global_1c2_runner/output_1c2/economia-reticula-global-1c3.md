# economia-reticula-global-1c3.md

## Fuente y anio

- Fuente principal: Banco Mundial WDI (API oficial)
- Indicador: NY.GDP.MKTP.CD (GDP current US$)
- Politica temporal: 2024 preferente, 2023 fallback, ausente si no comparable

## Tratamiento territorial

- Maestro usado: rg_paises_areas_operativo.csv
- China/Hong Kong/Macao: se cargan por codigo separado (CHN/HKG/MAC) segun WDI; sin cargar agregados regionales WDI.
- Taiwan: sin valor separado en esta extraccion WDI, se mantiene ausente.
- Kosovo: se usa codigo separado de WDI cuando existe; se mantiene separado de Serbia para evitar duplicidad.
- Territorios SEGUN_FUENTE: se respetan ausencias, sin imputacion.

## Cobertura y calculos

- Entidades con PIB: **203** de **244**.
- PIB mundial agregado (nueve areas): **110,633,680,289,696.14**.
- PIB area: suma nacional incluida.
- PIB % mundial: PIB area / PIB total nueve areas * 100.
- PIB por habitante: PIB area / poblacion_2025 area.

## Tabla de nueve areas

| area_codigo   | area_nombre                   |     pib_usd |   pib_mundial_pct |   pib_por_habitante_usd |   poblacion_cubierta_pct |   anio_minimo |   anio_maximo | observaciones                                                                                           |
|:--------------|:------------------------------|------------:|------------------:|------------------------:|-------------------------:|--------------:|--------------:|:--------------------------------------------------------------------------------------------------------|
| AFR           | África                        | 2.90169e+12 |           2.62279 |                 1873.58 |                  98.8622 |          2024 |          2024 | Cobertura incompleta en entidades. Cobertura poblacional alta.                                          |
| APC           | Asia-Pacífico                 | 1.21786e+13 |          11.0081  |                12495.9  |                  94.8727 |          2024 |          2024 | Cobertura incompleta en entidades. Cobertura poblacional aceptable.                                     |
| CHN           | China                         | 1.91875e+13 |          17.3433  |                13472.3  |                 100      |          2024 |          2024 | Cobertura poblacional alta.                                                                             |
| EUR           | Europa                        | 2.51307e+13 |          22.7152  |                42515    |                  99.9646 |          2023 |          2024 | Cobertura incompleta en entidades. Cobertura poblacional alta. Mezcla de anios 2023/2024 por faltantes. |
| MDE           | Oriente Medio                 | 5.09492e+12 |           4.60522 |                13124.9  |                  82.6387 |          2024 |          2024 | Cobertura incompleta en entidades. Cobertura poblacional condicionada.                                  |
| NAC           | Norteamérica y Caribe         | 3.41761e+13 |          30.8912  |                55362.7  |                  98.0775 |          2023 |          2024 | Cobertura incompleta en entidades. Cobertura poblacional alta. Mezcla de anios 2023/2024 por faltantes. |
| RUE           | Rusia y Eurasia postsoviética | 2.8893e+12  |           2.61159 |                11386.4  |                 100      |          2024 |          2024 | Cobertura poblacional alta.                                                                             |
| SAI           | Subcontinente indio           | 4.75378e+12 |           4.29687 |                 2385.49 |                 100      |          2024 |          2024 | Cobertura poblacional alta.                                                                             |
| SAM           | Sudamérica                    | 4.32109e+12 |           3.90577 |                 9863.14 |                  99.9276 |          2024 |          2024 | Cobertura incompleta en entidades. Cobertura poblacional alta.                                          |

## Incidencias

- Total registradas: **46** (ver incidencias-economia-1c3.csv).

## Archivos generados

- output_1c2/rg_economia_pais.csv
- output_1c2/rg_agregados_economia.csv
- output_1c2/incidencias-economia-1c3.csv
- output_1c2/validacion-economia-1c3.md
- output_1c2/08_rg_catalogo_economia.sql
- output_1c2/09_rg_datos_economia.sql
- output_1c2/10_rg_comprobaciones_economia.sql
- output_1c2/98_rg_reversion_economia.sql

## Inserciones previstas

- rg_bloques: +1 (si ECO no existe)
- rg_indicadores: +3 (si no existen)
- rg_fuentes: +1 (si WB_WDI no existe)
- rg_datos_pais: +203 (ECO_PIB)
- rg_datos_area: +27 (ECO_PIB, ECO_PIB_PCT, ECO_PC)

## Orden de ejecucion manual

1. 08_rg_catalogo_economia.sql
2. 09_rg_datos_economia.sql
3. 10_rg_comprobaciones_economia.sql

## Decision

**GO** para ejecucion manual en phpMyAdmin, condicionado a revisar incidencias REVISAR.
