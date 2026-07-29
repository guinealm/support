# Inventario de indicadores complementarios — Fase 7A.1

Fecha de revisión: 2026-07-28  
Proyecto: Retícula Global 2025 — Support  
Edición válida: `RG2025_V1`

## Objetivo y alcance

Este documento identifica los datos disponibles para completar el perfil medio de población de las nueve macroáreas. La revisión ha sido exclusivamente de lectura: catálogo y scripts SQL existentes, salidas CSV reproducibles, documentación metodológica, volcado de referencia y respuestas de la API pública. No se ha modificado MySQL, la API ni la aplicación web.

La API pública confirma que `RG2025_V1` está activa y en estado `congelado`. El volcado SQL conservado en `output_1c2` es una instantánea anterior a la congelación y todavía muestra el periodo en `preparacion`; el cierre 1C.9 y la respuesta actual de la API confirman la ejecución posterior de la congelación.

## Resultado del inventario

| Código | Indicador | Existe en catálogo | Datos país | Datos área | Periodo | Fuente | Estado | Acción necesaria |
|---|---|---:|---:|---:|---|---|---|---|
| `TERR_DENS` | Densidad de población | Sí | 234 activos | 9 activos | Población 2025 / superficie 2023; `RG2025_V1` | OWID; superficie FAOSTAT procesada por OWID y población UN WPP 2024 procesada por OWID | VALIDADO | Utilizar el indicador existente. Mantener visible que es un cociente calculado y no un dato regional independiente. |
| `POB_URB` | Población urbana | No; solo figura en el diccionario conceptual | 0 | 0 | No incorporado | Sin fuente registrada en el catálogo actual | AÑADIR NUEVO | En una fase posterior, seleccionar una fuente comparable, definir si se expresa como personas o porcentaje, cargar datos nacionales y generar los nueve agregados. |
| `POB_EDAD` | Edad mediana | Sí | 236 activos | 9 activos | Datos nacionales 2023; ponderación con población 2025; `RG2025_V1` | OWID | VALIDADO | Reutilizar el indicador y conservar la advertencia de que el agregado es una aproximación ponderada, no una mediana recalculada sobre la distribución conjunta del área. |
| `HUM_EV` | Esperanza de vida al nacer | Sí | 216 activos | 9 activos | 2023; ponderación con población 2025; `RG2025_V1` | Banco Mundial, WDI (`WB_WDI`) | VALIDADO | Reutilizar el indicador. Identificarlo como media nacional ponderada y mantener la cobertura de cada área. |
| `ECO_PC` | PIB por habitante | Sí | 0 almacenados con este código; derivable para 203 entidades con PIB y población | 9 activos | PIB mayoritariamente 2024, un dato de respaldo 2023; población 2025; `RG2025_V1` | Banco Mundial, WDI, más población UN WPP/OWID | DERIVABLE | Usar los nueve agregados existentes. Si se necesita el nivel nacional, calcular `ECO_PIB / POB_TOTAL` sin interpretar ausencias como cero y documentar el desfase temporal. |
| `HUM_IDH` | Índice de Desarrollo Humano | Sí | 193 activos | 9 activos | IDH 2023; ponderación con población 2025; `RG2025_V1` | PNUD, *Human Development Report 2025* (`UNDP_HDR`) | VALIDADO | Reutilizar el indicador con su cobertura. Indicar expresamente que el valor de macroárea no es un IDH regional oficial, sino una media nacional ponderada. |

## Comprobaciones

### Catálogo y códigos

Los códigos exactos existentes en `rg_indicadores` son:

- `TERR_DENS`
- `POB_EDAD`
- `ECO_PC`
- `HUM_EV`
- `HUM_IDH`

`POB_URB` aparece como código previsto en el diccionario inicial, pero no está presente en el catálogo materializado ni tiene registros nacionales o de área. No se localizaron códigos alternativos activos para ninguno de los seis conceptos. Las coincidencias `MIL_PC` y `ENE_PC` son indicadores por habitante de otros bloques y no son duplicados de `ECO_PC`.

### Cobertura y duplicidades

Los cinco indicadores existentes devuelven exactamente las nueve macroáreas `AFR`, `APC`, `CHN`, `EUR`, `MDE`, `NAC`, `RUE`, `SAI` y `SAM` desde la API pública, sin códigos duplicados. `POB_URB` devuelve una colección vacía.

Los scripts de comprobación preparados para la edición congelada controlan la unicidad nacional por país, indicador y año, y la unicidad agregada por área, indicador y periodo. En los materiales revisados no aparecen duplicidades para los cinco códigos existentes.

La cobertura nacional no equivale siempre a las 244 entidades del maestro:

- densidad: 234 entidades con población y superficie;
- edad mediana: 236;
- esperanza de vida: 216;
- IDH: 193;
- PIB por habitante: no se almacena como fila nacional propia; existen 203 entidades con PIB que pueden combinarse con población.

Los nueve agregados conservan sus campos de cobertura (`paises_totales`, `paises_con_dato` y porcentaje). Una fila agregada no implica cobertura nacional completa.

### Métodos actuales

**Densidad.** Se calcula como población total 2025 dividida por superficie terrestre 2023. El método agregado registrado es `Poblacion area / superficie area`. Es derivable con `POB_TOTAL / TERR_SUP`, pero ya existe materializado como `TERR_DENS`.

**PIB por habitante.** El método agregado registrado es `PIB area / poblacion 2025 area`. El numerador procede de `ECO_PIB`; los datos son principalmente de 2024 y existe al menos un respaldo de 2023. El cociente no debe presentarse como una observación homogénea de 2025.

**Edad mediana.** Se usa la media ponderada aproximada de las edades medianas nacionales de 2023 con población de 2025. No es la mediana demográfica que resultaría de unir las distribuciones de edad de todos los países.

**Esperanza de vida.** Se usa la media de los valores nacionales de 2023 ponderada por población 2025.

**IDH.** Se usa la media de los IDH nacionales de 2023 ponderada por población 2025. La metodología almacenada advierte que no constituye un IDH oficial de la macroárea.

## Fuentes y periodos

- Superficie: FAOSTAT 2025 procesada por Our World in Data; observación nacional 2023.
- Población: UN World Population Prospects 2024 procesada por Our World in Data; estimación 2025.
- Edad mediana: Our World in Data; dato 2023.
- PIB nominal: Banco Mundial, World Development Indicators; principalmente 2024, con respaldo 2023 cuando falta 2024.
- Esperanza de vida: Banco Mundial, World Development Indicators; 2023.
- IDH: PNUD, *Human Development Report 2025*; dato 2023.
- Población urbana: no hay fuente materializada ni periodo registrado.

## Conclusión operativa

Cinco de los seis indicadores pueden utilizarse sin crear códigos nuevos. Cuatro están almacenados tanto a nivel nacional como agregado; `ECO_PC` está materializado únicamente para las nueve áreas, aunque puede derivarse a nivel nacional de datos ya cargados. La población urbana es el único indicador que requiere una incorporación futura de fuente, registros nacionales y agregación.

No debe recalcularse silenciosamente la edad mediana como si fuera una mediana regional, ni presentarse el IDH agregado como índice oficial de la macroárea. Los cocientes de densidad y PIB por habitante deben conservar sus años de numerador y denominador.

## Archivos y respuestas consultados

- `reticula_global_1c2_runner/output_1c2/01_rg_estructura_minima.sql`
- `reticula_global_1c2_runner/output_1c2/02_rg_catalogos_iniciales.sql`
- `reticula_global_1c2_runner/output_1c2/04_rg_datos_territorio_poblacion.sql`
- `reticula_global_1c2_runner/output_1c2/06_rg_correccion_edad_mediana.sql`
- `reticula_global_1c2_runner/output_1c2/07_rg_comprobacion_edad_mediana.sql`
- `reticula_global_1c2_runner/output_1c2/08_rg_catalogo_economia.sql`
- `reticula_global_1c2_runner/output_1c2/09_rg_datos_economia.sql`
- `reticula_global_1c2_runner/output_1c2/10_rg_comprobaciones_economia.sql`
- `reticula_global_1c2_runner/output_1c2/11_rg_catalogo_desarrollo_humano.sql`
- `reticula_global_1c2_runner/output_1c2/12_rg_datos_desarrollo_humano.sql`
- `reticula_global_1c2_runner/output_1c2/13_rg_comprobaciones_desarrollo_humano.sql`
- `reticula_global_1c2_runner/output_1c2/26_rg_comprobacion_integral_1c9.sql`
- `reticula_global_1c2_runner/output_1c2/27_rg_congelar_periodo_1c9.sql`
- `reticula_global_1c2_runner/output_1c2/u794456529_map_sim_Mund.sql`
- CSV nacionales y agregados de territorio/población, economía y desarrollo humano de `output_1c2`
- `# Fase 1B.2 — Diccionario inicial de indicadores.md`
- `# Fase 1B.3 — Fuentes, fecha de corte y metodología.md`
- API pública `https://support.jumalenin.com/api/reticula/v1/datos.php`, consultada por código de indicador el 2026-07-28

## Estado de la fase

**GO CON OBSERVACIONES**

Observaciones no bloqueantes: `POB_URB` todavía no existe; `ECO_PC` no tiene filas nacionales propias; y los indicadores agregados de edad, esperanza de vida e IDH son medias nacionales ponderadas cuya naturaleza aproximada debe permanecer visible.
