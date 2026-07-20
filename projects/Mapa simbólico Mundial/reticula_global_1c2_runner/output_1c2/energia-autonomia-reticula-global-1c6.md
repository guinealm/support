# Energia y autonomia - Reticula Global 1C.6

## Fuentes
- U.S. Energy Information Administration (2026); Energy Institute Statistical Review of World Energy (2025), con procesamiento de Our World in Data
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
- ENE_FOS se aplaza por cobertura insuficiente y falta de fuente complementaria comparable para cuatro areas.
- Los datos ENE_FOS del CSV son exclusivamente material de investigacion y no se cargan en MySQL.
- ENE_ELEC_LC = (renovable + nuclear) / electricidad total *100.
- Conversion fija: 1 EJ = 277.777778 TWh.

## Cobertura
- Entidades con consumo: 209
- Entidades con dependencia: 138
- Entidades con fosil: 79
- Entidades con electricidad baja carbono: 194
- Incidencias: 177

| Area | Consumo TWh | kWh/hab | Dependencia % | Autosuficiencia % | Fosiles % | Electricidad baja carbono % | Cobertura ENE_CONS-pop % | Cobertura ENE_FOS-pop % |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AFR | 5762.02 | 3720.46 | -39.29 | 139.29 | 95.27 | 27.33 | 99.92 | 17.37 |
| APC | 21066.58 | 21615.33 | 27.15 | 72.85 | 85.74 | 31.50 | 97.26 | 86.98 |
| CHN | 49274.01 | 34597.33 | 24.80 | 75.20 | 79.53 | 41.51 | 100.00 | 99.95 |
| EUR | 19759.68 | 33428.61 | 38.89 | 61.11 | 65.66 | 71.80 | 99.92 | 97.07 |
| MDE | 13764.29 | 35457.83 | -109.37 | 209.37 | 94.60 | 14.36 | 100.00 | 76.30 |
| NAC | 33686.71 | 54569.99 | -14.75 | 114.75 | 79.01 | 45.70 | 99.83 | 84.38 |
| RUE | 11729.55 | 46224.92 | -71.49 | 171.49 | 89.21 | 34.13 | 100.00 | 90.21 |
| SAI | 12982.51 | 6514.74 | 36.85 | 63.15 | 88.87 | 28.82 | 100.00 | 96.25 |
| SAM | 7591.98 | 17329.11 | -23.36 | 123.36 | 60.47 | 79.58 | 99.93 | 94.35 |

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
- Indicadores: +5
- Datos de area: +45
- rg_datos_area esperado tras 1C.6: 216 (171 + 45)

## Orden de ejecucion
1. 17_rg_catalogo_energia.sql
2. 18_rg_datos_energia.sql
3. 19_rg_comprobaciones_energia.sql

## Decision GO/NO-GO
- GO para ejecutar 17/18/19 en el orden previsto. ENE_FOS queda aplazado y fuera de la primera edicion.