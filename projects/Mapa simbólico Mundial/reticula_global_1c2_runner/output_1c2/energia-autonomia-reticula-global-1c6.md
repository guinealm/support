# Energia y autonomia - Reticula Global 1C.6

## Fuentes
- Energy Institute - Statistical Review of World Energy 2026 (via Our World in Data)
- Ember - Global Electricity Review 2026 / Electricity Data Explorer (via Our World in Data)
- International Energy Agency (via World Development Indicators - Banco Mundial EG.IMP.CONS.ZS)
- Our World in Data (procesamiento reproducible de series energeticas)

## Años
- Consumo/fosil: 2025, fallback 2024 cuando no hay dato 2025 comparable.
- Dependencia: 2023, fallback 2022.
- Electricidad baja carbono: 2025, fallback 2024.

## Definiciones y conversiones
- ENE_CONS en TWh.
- ENE_PC en kWh/habitante.
- ENE_DEP como importaciones netas/consumo *100 (aprox. ponderada por consumo).
- ENE_AUTO = 100 - ENE_DEP.
- ENE_FOS = (carbon + petroleo + gas) / consumo total *100.
- ENE_ELEC_LC = (renovable + nuclear) / electricidad total *100.
- Conversion fija: 1 EJ = 277.777778 TWh.

## Cobertura
- Entidades con consumo: 79
- Entidades con dependencia: 138
- Entidades con fosil: 79
- Entidades con electricidad baja carbono: 194
- Incidencias: 177

| Area | Consumo TWh | kWh/hab | Dependencia % | Autosuficiencia % | Fosiles % | Electricidad baja carbono % | Cobertura consumo-pop % |
|---|---:|---:|---:|---:|---:|---:|---:|
| AFR | 3,524.83 | 2,275.94 | -18.914 | 118.914 | 95.274 | 27.332 | 17.37 |
| APC | 20,540.39 | 21,075.42 | 29.410 | 70.590 | 85.737 | 31.496 | 86.98 |
| CHN | 49,260.03 | 34,587.52 | 24.803 | 75.197 | 79.532 | 41.507 | 99.95 |
| EUR | 19,388.99 | 32,801.50 | 38.183 | 61.817 | 65.659 | 71.804 | 97.07 |
| MDE | 13,135.71 | 33,838.57 | -115.345 | 215.345 | 94.595 | 14.364 | 76.30 |
| NAC | 32,884.80 | 53,270.96 | -16.703 | 116.703 | 79.014 | 45.699 | 84.38 |
| RUE | 11,499.81 | 45,319.53 | -74.037 | 174.037 | 89.213 | 34.126 | 90.21 |
| SAI | 12,864.84 | 6,455.69 | 36.888 | 63.112 | 88.874 | 28.819 | 96.25 |
| SAM | 7,340.44 | 16,754.96 | -23.353 | 123.353 | 60.467 | 79.578 | 94.35 |

## Archivos generados
- rg_energia_pais.csv
- rg_agregados_energia.csv
- incidencias-energia-1c6.csv
- validacion-energia-1c6.md
- energia-autonomia-reticula-global-1c6.md
- 17_rg_catalogo_energia.sql
- 18_rg_datos_energia.sql
- 19_rg_comprobaciones_energia.sql
- 95_rg_reversion_energia.sql

## Inserciones previstas
- Bloques: +1 (ENE)
- Indicadores: +6
- Datos de area: +54
- rg_datos_area esperado tras 1C.6: 225 (171 + 54)

## Orden de ejecucion
1. 17_rg_catalogo_energia.sql
2. 18_rg_datos_energia.sql
3. 19_rg_comprobaciones_energia.sql

## Decision GO/NO-GO
- GO condicionado tras revisar incidencias de cobertura y faltantes antes de ejecutar en phpMyAdmin.