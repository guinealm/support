# Implantacion MySQL minima - Reticula Global 1C.2B

## Alcance

Prueba tecnica minima para territorio y poblacion (sin datos economicos y sin tocar la web publica).

## Tablas creadas

- `rg_areas`
- `rg_paises`
- `rg_bloques`
- `rg_indicadores`
- `rg_fuentes`
- `rg_periodos`
- `rg_datos_pais`
- `rg_datos_area`

## Vistas creadas

- `rg_v_datos_consolidados`
- `rg_v_portada_territorio_poblacion`

## Relaciones principales

- `rg_paises.area_id` -> `rg_areas.id`
- `rg_indicadores.bloque_id` -> `rg_bloques.id`
- `rg_datos_pais.pais_id` -> `rg_paises.id`
- `rg_datos_pais.indicador_id` -> `rg_indicadores.id`
- `rg_datos_pais.fuente_id` -> `rg_fuentes.id`
- `rg_datos_area.area_id` -> `rg_areas.id`
- `rg_datos_area.indicador_id` -> `rg_indicadores.id`
- `rg_datos_area.periodo_id` -> `rg_periodos.id`
- `rg_datos_area.fuente_principal_id` -> `rg_fuentes.id`

## Archivos de entrada usados

- `rg_paises_areas.csv`
- `rg_paises_areas_operativo.csv`
- `output_1c2\rg_territorio_poblacion_pais.csv`
- `output_1c2\rg_agregados_territorio_poblacion.csv`
- `output_1c2\fuentes_1c2.json`
- `output_1c2\validacion-territorio-poblacion-1c2.md`
- `output_1c2\resolucion-incidencias-territorio-poblacion-1c2a.md`
- `output_1c2\correspondencias-especiales-1c2.csv`

## Transformacion aplicada

- Carga de catalogos minimos (areas, bloques, indicadores, fuentes, periodo).
- Carga de paises y territorios desde maestro operativo final.
- Carga de datos de entidad desde `rg_territorio_poblacion_pais.csv`.
- Carga de agregados por area desde `rg_agregados_territorio_poblacion.csv`.
- Conservacion de ausencias como `NULL`.
- Indicadores calculados: `TERR_DENS` y `POB_VAR_2050` cuando existen insumos.

## Numero de registros previstos

- `rg_areas`: **9**
- `rg_paises`: **244**
- `rg_bloques`: **2**
- `rg_indicadores`: **8**
- `rg_fuentes`: **3**
- `rg_periodos`: **1**
- `rg_datos_pais`: **1176**
- `rg_datos_area`: **72**

## Ausencias conservadas

- No se convierten faltantes a cero.
- Las limitaciones 1C.2A se preservan como `NULL` y notas en observaciones.

## Orden de ejecucion en phpMyAdmin

1. `01_rg_estructura_minima.sql`
2. `02_rg_catalogos_iniciales.sql`
3. `03_rg_paises.sql`
4. `04_rg_datos_territorio_poblacion.sql`
5. `05_rg_comprobaciones.sql`

## Reversion

- Ejecutar `99_rg_reversion_prueba.sql` para eliminar solo vistas/tablas `rg_` de esta prueba.

## Riesgos

- Si existen tablas `rg_` previas no compatibles, revisar antes de ejecutar.
- `rg_datos_pais` no carga indicadores de porcentaje por entidad (no estan en fuentes base).
- Cualquier ajuste semantico adicional debe hacerse en una fase posterior, no en esta prueba minima.

## Decision tecnica para ejecucion manual en phpMyAdmin

**GO** para entorno de prueba, con ejecucion manual y validacion con `05_rg_comprobaciones.sql`.
