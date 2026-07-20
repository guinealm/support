# Emisiones y clima - Reticula Global 1C.7

## Alcance
- CLI_CO2: emisiones territoriales de CO2 de combustibles fosiles e industria.
- CLI_CO2_PC: CLI_CO2 dividido por poblacion cubierta 2025.
- Excluye cambio de uso del suelo, emisiones de consumo y otros gases de efecto invernadero.
- CLI_VUL queda aplazado por metodologia pendiente.

## Fuente y transformacion
- Global Carbon Budget (2025), con procesamiento de Our World in Data.
- Ano: 2024. Unidad original: toneladas de CO2.
- Agregado CLI_CO2: suma nacional.
- Agregado CLI_CO2_PC: toneladas cubiertas / poblacion cubierta.

## Resultados

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

## Implantacion prevista
- 1 bloque nuevo.
- 2 indicadores nuevos.
- 427 registros nacionales previstos (214 CLI_CO2 + 213 CLI_CO2_PC).
- CXR conserva CLI_CO2=0 publicado por la fuente, pero no recibe CLI_CO2_PC por ausencia de poblacion 2025.
- 18 registros de area nuevos.
- 234 registros de area activos esperados (216 + 18).

## Decision
- GO metodologico para la implantacion. La ejecucion y el cierre formal de MySQL se documentan fuera del artefacto reproducible.
