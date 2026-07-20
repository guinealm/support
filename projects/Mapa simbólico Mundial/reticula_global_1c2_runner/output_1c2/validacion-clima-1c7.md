# Validacion emisiones y clima 1C.7

- Entidades del maestro: 244 (esperado 244)
- Entidades con CLI_CO2: 214
- Entidades con CLI_CO2_PC: 213
- Incidencias: 31
- Nueve areas: OK
- Anio de emisiones: 2024.
- Emisiones negativas: ninguna.
- Ausencias conservadas como NULL: OK.
- CXR=0 procede expresamente de la fuente y no representa una imputacion.
- CXR no tiene poblacion 2025 en el maestro: CLI_CO2_PC queda ausente y no se imputa ni se convierte en cero.
- Agregados regionales de fuente excluidos: OK.
- CHN/HKG/MAC separados; RUS solo en RUE: OK.

## Cobertura

| Area | CO2 Mt | t/hab | Cobertura poblacional % | Entidades |
|---|---:|---:|---:|---:|
| AFR | 1502.099 | 0.971 | 99.88 | 55/59 |
| APC | 4412.572 | 4.529 | 99.97 | 36/43 |
| CHN | 12323.417 | 8.653 | 100.00 | 3/3 |
| EUR | 3036.121 | 5.140 | 99.94 | 41/51 |
| MDE | 2968.607 | 7.647 | 100.00 | 15/15 |
| NAC | 6084.277 | 9.923 | 99.33 | 34/41 |
| RUE | 2425.144 | 9.557 | 100.00 | 10/10 |
| SAI | 3535.988 | 1.774 | 100.00 | 8/8 |
| SAM | 1109.841 | 2.535 | 99.93 | 12/14 |

## Decision
- GO para preparar 20/21/22. No ejecutar MySQL hasta revision manual.