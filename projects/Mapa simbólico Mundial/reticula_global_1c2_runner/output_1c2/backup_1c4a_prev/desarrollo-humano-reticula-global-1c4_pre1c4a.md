# desarrollo-humano-reticula-global-1c4.md

## Fuentes

- PNUD Human Development Reports: IDH oficial (2023 si esta publicado; si no, ultimo oficial disponible).
- Banco Mundial / Poverty and Inequality Platform: SI.POV.GINI (escala 0-100).
- Banco Mundial / WDI: SP.DYN.LE00.IN (esperanza de vida).

## Años y reglas de seleccion

- IDH: anio objetivo 2023; en esta extraccion se usa 2022 cuando 2023 no aparece publicado en la serie oficial.
- Gini: ultimo 2019-2024; fallback ultimo 2015-2018 marcado como antiguo; <2015 se deja ausente.
- Esperanza de vida: 2023; fallback 2022; si no existe, ausente.

## Metodologia de agregacion

- IDH area (aprox): sum(IDH nacional * poblacion_2025) / sum(poblacion cubierta).
- Gini area (aprox): sum(Gini nacional * poblacion_2025) / sum(poblacion cubierta).
- EV area (aprox): sum(EV nacional * poblacion_2025) / sum(poblacion cubierta).

## Advertencias conceptuales

- Los tres resultados de area son medias nacionales ponderadas, no indicadores regionales oficiales exactos.
- Gini aproximado no representa la desigualdad conjunta de todos los habitantes del area.
- Cobertura alta no implica comparabilidad plena cuando hay dispersion temporal (especialmente Gini).

## Cobertura por indicador y area

| area_codigo   | area_nombre                   |   idh_aprox |   gini_aprox |   esperanza_vida_aprox |   cobertura_idh_pct |   cobertura_gini_pct |   cobertura_esperanza_vida_pct | observaciones                                                                                                                                                                                                                                                                                                                                                                                    |
|:--------------|:------------------------------|------------:|-------------:|-----------------------:|--------------------:|---------------------:|-------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AFR           | África                        |    0.555241 |      38.3921 |                64.1741 |             99.8821 |              88.5998 |                        99.8821 | Cobertura IDH alta. Cobertura Gini condicionada. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 17 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada.  |
| APC           | Asia-Pacífico                 |    0.762787 |      34.929  |                74.5058 |             94.8134 |              90.4189 |                        97.6255 | Cobertura IDH aceptable. Cobertura Gini aceptable. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 1 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada. |
| CHN           | China                         |    0.788873 |      36      |                77.9935 |             99.9493 |              99.43   |                       100      | Cobertura IDH alta. Cobertura Gini alta. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area.                                                                                                                     |
| EUR           | Europa                        |    0.899998 |      31.2945 |                80.7576 |             99.9344 |              99.9079 |                        99.9714 | Cobertura IDH alta. Cobertura Gini alta. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 1 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada.           |
| MDE           | Oriente Medio                 |    0.746863 |      36.1316 |                76.0025 |            100      |              74.2328 |                       100      | Cobertura IDH alta. Cobertura Gini insuficiente. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 2 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada.   |
| NAC           | Norteamérica y Caribe         |    0.85918  |      41.46   |                77.1472 |             99.2311 |              94.0357 |                        99.8734 | Cobertura IDH alta. Cobertura Gini aceptable. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 4 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada.      |
| RUE           | Rusia y Eurasia postsoviética |    0.790194 |      32.5033 |                73.1843 |            100      |              92.8999 |                       100      | Cobertura IDH alta. Cobertura Gini aceptable. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini con dispersion temporal relevante; comparabilidad condicionada.                                           |
| SAI           | Subcontinente indio           |    0.629961 |      27.2505 |                71.5915 |            100      |              97.7999 |                       100      | Cobertura IDH alta. Cobertura Gini alta. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini con dispersion temporal relevante; comparabilidad condicionada.                                                |
| SAM           | Sudamérica                    |    0.768165 |      48.0056 |                76.2398 |             99.9276 |              93.2276 |                        99.9276 | Cobertura IDH alta. Cobertura Gini aceptable. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area.                                                                                                                |

## Incidencias

- Total incidencias: **205**.
- Gini anteriores a 2019: **25**.
- Nota metodologica: la API WDI usada no explicita por observacion si la medicion Gini es por ingreso o consumo.

## Ordenes auxiliares

### Areas por IDH aprox (desc)

| area_codigo   |   idh_aprox |
|:--------------|------------:|
| EUR           |    0.899998 |
| NAC           |    0.85918  |
| RUE           |    0.790194 |
| CHN           |    0.788873 |
| SAM           |    0.768165 |
| APC           |    0.762787 |
| MDE           |    0.746863 |
| SAI           |    0.629961 |
| AFR           |    0.555241 |

### Areas por desigualdad (Gini aprox desc)

| area_codigo   |   gini_aprox |
|:--------------|-------------:|
| SAM           |      48.0056 |
| NAC           |      41.46   |
| AFR           |      38.3921 |
| MDE           |      36.1316 |
| CHN           |      36      |
| APC           |      34.929  |
| RUE           |      32.5033 |
| EUR           |      31.2945 |
| SAI           |      27.2505 |

### Areas por esperanza de vida aprox (desc)

| area_codigo   |   esperanza_vida_aprox |
|:--------------|-----------------------:|
| EUR           |                80.7576 |
| CHN           |                77.9935 |
| NAC           |                77.1472 |
| SAM           |                76.2398 |
| MDE           |                76.0025 |
| APC           |                74.5058 |
| RUE           |                73.1843 |
| SAI           |                71.5915 |
| AFR           |                64.1741 |

## Archivos generados

- output_1c2/rg_desarrollo_humano_pais.csv
- output_1c2/rg_agregados_desarrollo_humano.csv
- output_1c2/incidencias-desarrollo-humano-1c4.csv
- output_1c2/validacion-desarrollo-humano-1c4.md
- output_1c2/11_rg_catalogo_desarrollo_humano.sql
- output_1c2/12_rg_datos_desarrollo_humano.sql
- output_1c2/13_rg_comprobaciones_desarrollo_humano.sql
- output_1c2/97_rg_reversion_desarrollo_humano.sql

## Inserciones previstas

- rg_datos_pais HUM_IDH: +193
- rg_datos_pais HUM_GINI: +151
- rg_datos_pais HUM_EV: +216
- rg_datos_area HUM: +27

## Orden de ejecucion manual (phpMyAdmin)

1. 11_rg_catalogo_desarrollo_humano.sql
2. 12_rg_datos_desarrollo_humano.sql
3. 13_rg_comprobaciones_desarrollo_humano.sql

## Decision

**GO** para ejecucion manual, condicionado a revisar incidencias `REVISAR` (especialmente vacios por fuente y dispersion temporal de Gini).
