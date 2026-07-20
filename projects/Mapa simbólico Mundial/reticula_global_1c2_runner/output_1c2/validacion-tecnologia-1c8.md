# Validacion tecnologia 1C.8

- Entidades del maestro: 244 (esperado 244).
- Entidades con TEC_NET: 215.
- Incidencias: 34.
- Nueve areas: OK.
- Valores fuera de 0-100: ninguno.
- Ausencias conservadas como NULL: OK.
- Ceros publicados documentados: OK.
- Ponderacion: poblacion 2025 del maestro; no se usa media simple.

## Resultados

| Area | TEC_NET % | Cobertura % | Entidades con dato | Anos |
|---|---:|---:|---:|---|
| AFR | 39.672 | 99.88 | 54/59 | 2017-2024 |
| APC | 75.640 | 100.00 | 35/43 | 1990-2024 |
| CHN | 91.621 | 100.00 | 3/3 | 2024-2025 |
| EUR | 91.409 | 99.96 | 46/51 | 2016-2025 |
| MDE | 77.719 | 100.00 | 15/15 | 2018-2025 |
| NAC | 88.049 | 99.86 | 32/41 | 1990-2024 |
| RUE | 89.116 | 100.00 | 10/10 | 2016-2025 |
| SAI | 65.201 | 100.00 | 8/8 | 2024-2025 |
| SAM | 83.756 | 99.93 | 12/14 | 2023-2024 |

## Base incremental corregida

- Antes de tecnologia: 7 bloques, 26 indicadores y 234 registros de area.
- Despues de tecnologia: 8 bloques, 27 indicadores y 243 registros de area.
- La expectativa 216 + 9 = 225 omitia los 18 registros climaticos ya implantados.

## Decision
- GO para ejecucion manual de 23/24/25. Codex no ha ejecutado MySQL.