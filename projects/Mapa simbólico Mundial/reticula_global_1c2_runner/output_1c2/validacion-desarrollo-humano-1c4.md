# validacion-desarrollo-humano-1c4.md

## Resumen

- Areas detectadas: **9**
- Entidades maestras: **244**
- Entidades con IDH: **193**
- Entidades con Gini: **151**
- Entidades con esperanza de vida: **216**
- Incidencias totales: **205**

## Comprobaciones

1. Nueve areas: **OK**.
2. IDH en [0,1]: **OK** (fuera de rango: 0).
3. Gini en [0,100]: **OK** (fuera de rango: 0).
4. Esperanza de vida razonable [20,95]: **OK** (fuera de rango: 0).
5. Ausentes convertidos en cero: **NO**.
6. Codigos ISO3 duplicados: **0**.
7. Anios reales conservados: **OK** (columnas anio_* por indicador). IDH min/max: **2023/2023**.
8. Taiwan y Kosovo tratados expresamente: **OK**.
9. China/Hong Kong/Macao sin duplicidad: **OK**.
10. Serbia y Kosovo sin duplicidad: **OK**.
11. Cobertura por poblacion: **OK**.
12. Paises con Gini antiguo (<2019): **25**.
13. Agregados recalculables desde nacionales: **OK**.
14. Diferencia conceptual media ponderada vs indicador regional documentada: **OK**.

## Entidades sensibles

### China / Hong Kong / Macao

| codigo_iso3   |     idh |   gini |   esperanza_vida | observaciones                                                                                                                                                                                              |
|:--------------|--------:|-------:|-----------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CHN           |   0.797 |     36 |          77.953  | CHN tratado separado de HKG y MAC.                                                                                                                                                                         |
| HKG           |   0.955 |    nan |          85.2473 | Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin Gini 2015-2024 usable en WDI/PIP. HKG tratado separado de CHN.                                                            |
| MAC           | nan     |    nan |          83.1805 | Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. MAC tratado separado de CHN. |

### Serbia / Kosovo

| codigo_iso3   |     idh |   gini |   esperanza_vida | observaciones                                                                                                                                                                                               |
|:--------------|--------:|-------:|-----------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRB           |   0.833 |   32.8 |          76.1415 | SRB revisado expresamente junto con XKX.                                                                                                                                                                    |
| XKX           | nan     |   38.3 |          78.033  | Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. XKX revisado expresamente; mantener separado de SRB sin duplicidad. |

### Taiwan / Kosovo

| codigo_iso3   |   idh |   gini |   esperanza_vida | observaciones                                                                                                                                                                                                                                                                                          |
|:--------------|------:|-------:|-----------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TWN           |   nan |  nan   |          nan     | Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI. TWN revisado expresamente; mantener criterio SEGUN_FUENTE sin duplicidad. |
| XKX           |   nan |   38.3 |           78.033 | Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. XKX revisado expresamente; mantener separado de SRB sin duplicidad.                                                                                            |

## Gini antiguo (<2019)

| codigo_iso3   | pais                  |   anio_gini |   gini | area_codigo   |
|:--------------|:----------------------|------------:|-------:|:--------------|
| AGO           | Angola                |        2018 |   51.3 | AFR           |
| BRB           | Barbados              |        2016 |   34.1 | NAC           |
| BWA           | Botswana              |        2015 |   54.9 | AFR           |
| BLZ           | Belize                |        2018 |   39.9 | NAC           |
| MMR           | Myanmar               |        2017 |   30.7 | APC           |
| CPV           | Cabo Verde            |        2015 |   42.4 | AFR           |
| DJI           | Djibouti              |        2017 |   41.6 | AFR           |
| GAB           | Gabon                 |        2017 |   38   | AFR           |
| GHA           | Ghana                 |        2016 |   43.5 | AFR           |
| GRD           | Grenada               |        2018 |   43.8 | NAC           |
| GIN           | Guinea                |        2018 |   29.6 | AFR           |
| HUN           | Hungary               |        2017 |   30.6 | EUR           |
| LSO           | Lesotho               |        2017 |   44.9 | AFR           |
| LBR           | Liberia               |        2016 |   35.3 | AFR           |
| MUS           | Mauritius             |        2017 |   36.8 | AFR           |
| NAM           | Namibia               |        2015 |   59.1 | AFR           |
| QAT           | Qatar                 |        2017 |   35.1 | MDE           |
| LCA           | Saint Lucia           |        2015 |   43.7 | NAC           |
| STP           | Sao Tome and Principe |        2017 |   40.7 | AFR           |
| SYC           | Seychelles            |        2018 |   32.1 | AFR           |
| SLE           | Sierra Leone          |        2018 |   35.7 | AFR           |
| SSD           | South Sudan           |        2016 |   44   | AFR           |
| SWZ           | Esuatini              |        2016 |   54.6 | AFR           |
| ARE           | United Arab Emirates  |        2018 |   26.4 | MDE           |
| TZA           | Tanzania              |        2018 |   40.5 | AFR           |

## Cobertura por area

| area_codigo   |   cobertura_idh_pct |   cobertura_gini_pct |   cobertura_esperanza_vida_pct |
|:--------------|--------------------:|---------------------:|-------------------------------:|
| AFR           |             99.8821 |              88.5998 |                        99.8821 |
| APC           |             94.8134 |              90.4189 |                        97.6255 |
| CHN           |             99.9493 |              99.43   |                       100      |
| EUR           |             99.9344 |              99.9079 |                        99.9714 |
| MDE           |            100      |              74.2328 |                       100      |
| NAC           |             99.2311 |              94.0357 |                        99.8734 |
| RUE           |            100      |              92.8999 |                       100      |
| SAI           |            100      |              97.7999 |                       100      |
| SAM           |             99.9276 |              93.2276 |                        99.9276 |

## Diferencias IDH 2022 vs 2023

Comparacion contra el snapshot previo `backup_1c4a_prev/rg_agregados_desarrollo_humano_pre1c4a.csv`.

| area_codigo   |   idh_aprox_2022 |   idh_aprox_2023 |   delta_idh |   entidades_con_idh_2022 |   entidades_con_idh_2023 |   cobertura_idh_2022 |   cobertura_idh_2023 |
|:--------------|-----------------:|-----------------:|------------:|-------------------------:|-------------------------:|---------------------:|---------------------:|
| AFR           |         0.555241 |         0.575088 |    0.019847 |                       54 |                       54 |            99.882126 |            99.882126 |
| APC           |         0.762787 |         0.775012 |    0.012225 |                       28 |                       28 |            94.813404 |            94.813404 |
| CHN           |         0.788873 |         0.797821 |    0.008948 |                        2 |                        2 |            99.949304 |            99.949304 |
| EUR           |         0.899998 |         0.913656 |    0.013658 |                       41 |                       41 |            99.934413 |            99.934413 |
| MDE           |         0.746863 |         0.762542 |    0.015679 |                       15 |                       15 |           100.000000 |           100.000000 |
| NAC           |         0.859180 |         0.869890 |    0.010710 |                       23 |                       23 |            99.231083 |            99.231083 |
| RUE           |         0.790194 |         0.805611 |    0.015417 |                       10 |                       10 |           100.000000 |           100.000000 |
| SAI           |         0.629961 |         0.662935 |    0.032974 |                        8 |                        8 |           100.000000 |           100.000000 |
| SAM           |         0.768165 |         0.792403 |    0.024238 |                       12 |                       12 |            99.927607 |            99.927607 |

Notas:
- Todos los agregados IDH pasan a anio minimo/maximo 2023.
- No se detectan cambios en Gini ni en esperanza de vida frente al snapshot previo.

## Tabla de areas

| area_codigo   | area_nombre                   |   idh_aprox |   gini_aprox |   esperanza_vida_aprox |   entidades_totales |   entidades_con_idh |   entidades_con_gini |   entidades_con_esperanza_vida |   cobertura_idh_pct |   cobertura_gini_pct |   cobertura_esperanza_vida_pct |   anio_min_idh |   anio_max_idh |   anio_min_gini |   anio_max_gini |   anio_min_esperanza_vida |   anio_max_esperanza_vida | observaciones                                                                                                                                                                                                                                                                                                                                                                                    |
|:--------------|:------------------------------|------------:|-------------:|-----------------------:|--------------------:|--------------------:|---------------------:|-------------------------------:|--------------------:|---------------------:|-------------------------------:|---------------:|---------------:|----------------:|----------------:|--------------------------:|--------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AFR           | África                        |    0.575088 |      38.3921 |                64.1741 |                  59 |                  54 |                   47 |                             54 |             99.8821 |              88.5998 |                        99.8821 |           2023 |           2023 |            2015 |            2024 |                      2023 |                      2023 | Cobertura IDH alta. Cobertura Gini condicionada. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 17 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada.  |
| APC           | Asia-Pacífico                 |    0.775012 |      34.929  |                74.5058 |                  43 |                  28 |                   16 |                             34 |             94.8134 |              90.4189 |                        97.6255 |           2023 |           2023 |            2017 |            2024 |                      2023 |                      2023 | Cobertura IDH aceptable. Cobertura Gini aceptable. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 1 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada. |
| CHN           | China                         |    0.797821 |      36      |                77.9935 |                   3 |                   2 |                    1 |                              3 |             99.9493 |              99.43   |                       100      |           2023 |           2023 |            2022 |            2022 |                      2023 |                      2023 | Cobertura IDH alta. Cobertura Gini alta. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area.                                                                                                                     |
| EUR           | Europa                        |    0.913656 |      31.2945 |                80.7576 |                  51 |                  41 |                   39 |                             46 |             99.9344 |              99.9079 |                        99.9714 |           2023 |           2023 |            2017 |            2023 |                      2023 |                      2023 | Cobertura IDH alta. Cobertura Gini alta. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 1 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada.           |
| MDE           | Oriente Medio                 |    0.762542 |      36.1316 |                76.0025 |                  15 |                  15 |                    9 |                             15 |            100      |              74.2328 |                       100      |           2023 |           2023 |            2017 |            2023 |                      2023 |                      2023 | Cobertura IDH alta. Cobertura Gini insuficiente. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 2 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada.   |
| NAC           | Norteamérica y Caribe         |    0.86989  |      41.46   |                77.1472 |                  41 |                  23 |                   14 |                             34 |             99.2311 |              94.0357 |                        99.8734 |           2023 |           2023 |            2015 |            2024 |                      2023 |                      2023 | Cobertura IDH alta. Cobertura Gini aceptable. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 4 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada.      |
| RUE           | Rusia y Eurasia postsoviética |    0.805611 |      32.5033 |                73.1843 |                  10 |                  10 |                    8 |                             10 |            100      |              92.8999 |                       100      |           2023 |           2023 |            2020 |            2024 |                      2023 |                      2023 | Cobertura IDH alta. Cobertura Gini aceptable. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini con dispersion temporal relevante; comparabilidad condicionada.                                           |
| SAI           | Subcontinente indio           |    0.662935 |      27.2505 |                71.5915 |                   8 |                   8 |                    7 |                              8 |            100      |              97.7999 |                       100      |           2023 |           2023 |            2019 |            2024 |                      2023 |                      2023 | Cobertura IDH alta. Cobertura Gini alta. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini con dispersion temporal relevante; comparabilidad condicionada.                                                |
| SAM           | Sudamérica                    |    0.792403 |      48.0056 |                76.2398 |                  14 |                  12 |                   10 |                             12 |             99.9276 |              93.2276 |                        99.9276 |           2023 |           2023 |            2022 |            2024 |                      2023 |                      2023 | Cobertura IDH alta. Cobertura Gini aceptable. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area.                                                                                                                |
