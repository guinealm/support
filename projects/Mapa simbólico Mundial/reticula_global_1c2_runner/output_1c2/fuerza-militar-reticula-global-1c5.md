# Fuerza militar y capacidad estrategica - Reticula Global 1C.5

## Fuentes
- SIPRI Military Expenditure Database, edición abril 2026 (v1.2), año 2025
- SIPRI Yearbook 2026, chapter 8 World nuclear forces, inventarios enero 2026

## Anios
- Gasto militar: 2025 con conservacion separada de 2024 cuando 2025 no esta publicado.
- Inventario nuclear: enero 2026 (estimaciones de fuentes abiertas).

## Definiciones
- MIL_GASTO: gasto militar nacional o agregado (USD corrientes).
- MIL_PCT: participacion del area en el gasto militar mundial de las nueve areas.
- MIL_PIB: gasto militar agregado respecto al PIB agregado comparable cubierto.
- MIL_PC: gasto militar agregado por habitante del area (poblacion 2025 validada en 1C.2).
- MIL_NUC: inventario nuclear total estimado (ojivas, columna inventario total estimado de SIPRI).

## Tratamiento territorial
- RUS solo en RUE.
- USA solo en NAC.
- CHN solo en CHN; HKG/MAC sin reasignacion automatica.
- FRA y GBR en EUR; territorios dependientes sin reparto proporcional.
- IND y PAK en SAI.
- PRK en APC.
- ISR en MDE.

## Metodologia de agregacion
- MIL_GASTO area: suma de gasto nacional incluido.
- MIL_PCT area: MIL_GASTO area / suma de MIL_GASTO de las 9 areas x 100.
- MIL_PC area: MIL_GASTO area / poblacion_2025 area.
- MIL_PIB area: MIL_GASTO area / PIB comparable cubierto del area x 100.
- MIL_NUC area: suma de ojivas estimadas de los Estados nucleares del area.

## Cobertura
- Paises con gasto: 153
- Paises con porcentaje PIB: 153
- Incidencias: 3
- Control inventario nuclear mundial: 12187 (objetivo SIPRI: 12187)

| Area | Gasto militar | % mundial | % PIB aprox | USD/hab | Ojivas estimadas | Cobertura poblacion % |
|---|---:|---:|---:|---:|---:|---:|
| AFR | 59,039,714,638 | 2.063 | 2.111 | 38.12 | 0 | 95.68 |
| APC | 233,313,499,425 | 8.153 | 1.922 | 239.39 | 50 | 96.19 |
| CHN | 335,524,155,624 | 11.725 | 1.791 | 235.59 | 620 | 99.43 |
| EUR | 662,803,047,288 | 23.162 | 2.641 | 1,121.30 | 515 | 99.91 |
| MDE | 194,221,701,115 | 6.787 | 4.506 | 500.33 | 90 | 77.47 |
| NAC | 1,008,974,702,326 | 35.259 | 2.969 | 1,634.46 | 5,132 | 97.25 |
| RUE | 201,833,931,182 | 7.053 | 7.410 | 795.41 | 5,430 | 82.40 |
| SAI | 109,574,048,555 | 3.829 | 2.319 | 54.99 | 350 | 97.73 |
| SAM | 56,299,416,494 | 1.967 | 1.342 | 128.51 | 0 | 93.27 |

## Rankings auxiliares

### Areas por gasto militar
- NAC: 1,008,974,702,326
- EUR: 662,803,047,288
- CHN: 335,524,155,624
- APC: 233,313,499,425
- RUE: 201,833,931,182
- MDE: 194,221,701,115
- SAI: 109,574,048,555
- AFR: 59,039,714,638
- SAM: 56,299,416,494

### Areas por porcentaje del PIB
- RUE: 7.410%
- MDE: 4.506%
- NAC: 2.969%
- EUR: 2.641%
- SAI: 2.319%
- AFR: 2.111%
- APC: 1.922%
- CHN: 1.791%
- SAM: 1.342%

### Areas por gasto por habitante
- NAC: 1,634.46 USD/hab
- EUR: 1,121.30 USD/hab
- RUE: 795.41 USD/hab
- MDE: 500.33 USD/hab
- APC: 239.39 USD/hab
- CHN: 235.59 USD/hab
- SAM: 128.51 USD/hab
- SAI: 54.99 USD/hab
- AFR: 38.12 USD/hab

### Areas por inventario nuclear
- RUE: 5,430 ojivas
- NAC: 5,132 ojivas
- CHN: 620 ojivas
- EUR: 515 ojivas
- SAI: 350 ojivas
- MDE: 90 ojivas
- APC: 50 ojivas
- AFR: 0 ojivas
- SAM: 0 ojivas

## Archivos generados
- rg_militar_pais.csv
- rg_nuclear_pais.csv
- rg_inventario_nuclear_2026.csv
- rg_agregados_militar.csv
- incidencias-militar-1c5.csv
- validacion-militar-1c5.md
- 14_rg_catalogo_militar.sql
- 15_rg_datos_militar.sql
- 16_rg_comprobaciones_militar.sql
- 96_rg_reversion_militar.sql

## Inserciones previstas
- Bloques: +1 (MIL)
- Indicadores: +5
- Datos de area: +45 (9 por indicador militar)
- rg_datos_area esperado: 171 activos (126 previos + 45 militares)

## Orden de ejecucion
1. 14_rg_catalogo_militar.sql
2. 15_rg_datos_militar.sql
3. 16_rg_comprobaciones_militar.sql

## Limitaciones
- El inventario nuclear se mantiene como estimacion abierta SIPRI.
- Algunas entidades quedan en 2024 por ausencia de dato 2025 en SIPRI.
- PRK queda en AUSENTE_DOCUMENTADO para gasto y porcentaje PIB por falta de comparabilidad temporal reciente.

## Decision GO/NO-GO
- GO para ejecutar los SQL 1C.5A en phpMyAdmin.