# Resolucion de incidencias territorio y poblacion - Fase 1C.2A

## Estado general

- Incidencias iniciales: **10**
- Incidencias pendientes tras 1C.2A: **0**
- Entidades con estado LIMITACION_DOCUMENTADA: **10**
- Copia de seguridad de salida previa: **backup_1c2a_20260715-160342**
- Base comparativa de agregados previos: **backup_1c2a_20260715-160121**

## Inventario inicial de incidencias

| ISO3   | Entidad                        | Area   | Tipo de entidad        | Inclusion    |   Poblacion 2025 |   Poblacion 2050 |   Superficie | Motivo probable                                                                                                        | Campo faltante exacto                        |
|:-------|:-------------------------------|:-------|:-----------------------|:-------------|-----------------:|-----------------:|-------------:|:-----------------------------------------------------------------------------------------------------------------------|:---------------------------------------------|
| ALA    | Åland Islands                  | EUR    | TERRITORIO_DEPENDIENTE | SEGUN_FUENTE |              nan |              nan |          nan | No aparece separado en fuente usada; se considera integrado en Finlandia para evitar duplicidad.                       | poblacion_2025,poblacion_2050,superficie_km2 |
| CCK    | Cocos (Keeling) Islands        | APC    | TERRITORIO_DEPENDIENTE | SEGUN_FUENTE |              nan |              nan |          nan | No aparece separado en fuente usada; se considera integrado en Australia para evitar duplicidad.                       | poblacion_2025,poblacion_2050,superficie_km2 |
| CXR    | Christmas Island               | APC    | TERRITORIO_DEPENDIENTE | SEGUN_FUENTE |              nan |              nan |          nan | No aparece separado en fuente usada; se considera integrado en Australia para evitar duplicidad.                       | poblacion_2025,poblacion_2050,superficie_km2 |
| GGY    | Guernsey                       | EUR    | TERRITORIO_DEPENDIENTE | SEGUN_FUENTE |            64498 |            62823 |          nan | Poblacion separada disponible; superficie ausente en fuente principal para este codigo.                                | superficie_km2                               |
| IOT    | British Indian Ocean Territory | AFR    | TERRITORIO_DEPENDIENTE | SEGUN_FUENTE |              nan |              nan |          nan | Territorio sin poblacion permanente en la fuente principal; sin superficie separada.                                   | poblacion_2025,poblacion_2050,superficie_km2 |
| JEY    | Jersey                         | EUR    | TERRITORIO_DEPENDIENTE | SEGUN_FUENTE |           104002 |           104780 |          nan | Poblacion separada disponible; superficie ausente en fuente principal para este codigo.                                | superficie_km2                               |
| NFK    | Norfolk Island                 | APC    | TERRITORIO_DEPENDIENTE | SEGUN_FUENTE |              nan |              nan |           40 | Poblacion no separada en fuente principal; superficie separada potencialmente no comparable con inclusion en soberano. | poblacion_2025,poblacion_2050                |
| PCN    | Pitcairn                       | APC    | TERRITORIO_DEPENDIENTE | SEGUN_FUENTE |              nan |              nan |           47 | Sin dato poblacional en la fuente principal y poblacion minima no estable para proyeccion homogenea.                   | poblacion_2025,poblacion_2050                |
| SJM    | Svalbard and Jan Mayen         | EUR    | TERRITORIO_DEPENDIENTE | SEGUN_FUENTE |              nan |              nan |          nan | No aparece separado en fuente usada; posible integracion en Noruega en series oficiales.                               | poblacion_2025,poblacion_2050,superficie_km2 |
| XKX    | Kosovo                         | EUR    | ENTIDAD_ESTADISTICA    | SEGUN_FUENTE |              nan |              nan |          nan | Entidad estadistica auxiliar; sin registro separado en fuente usada y riesgo de duplicidad con Serbia.                 | poblacion_2025,poblacion_2050,superficie_km2 |

## Decisiones por entidad

| Entidad                        | ISO maestro   | Codigo fuente         | Fuente                               | Indicador            | Tratamiento             | Nota                                                                                         |
|:-------------------------------|:--------------|:----------------------|:-------------------------------------|:---------------------|:------------------------|:---------------------------------------------------------------------------------------------|
| British Indian Ocean Territory | IOT           | SIN_CODIGO_SEPARADO   | OWID/UN WPP 2024 + OWID/FAOSTAT 2025 | POBLACION,SUPERFICIE | EXCLUIR_INDICADOR       | Se mantiene en maestro y mapa; no se imputa cero.                                            |
| Christmas Island               | CXR           | INTEGRADO_EN_AUS      | OWID/UN WPP 2024 + OWID/FAOSTAT 2025 | POBLACION,SUPERFICIE | EXCLUIR_INDICADOR       | Sin registro separado comparable para 2025/2050.                                             |
| Cocos (Keeling) Islands        | CCK           | INTEGRADO_EN_AUS      | OWID/UN WPP 2024 + OWID/FAOSTAT 2025 | POBLACION,SUPERFICIE | EXCLUIR_INDICADOR       | Sin registro separado comparable para 2025/2050.                                             |
| Åland Islands                  | ALA           | INTEGRADO_EN_FIN      | OWID/UN WPP 2024 + OWID/FAOSTAT 2025 | POBLACION,SUPERFICIE | EXCLUIR_INDICADOR       | Sin registro separado comparable para 2025/2050.                                             |
| Norfolk Island                 | NFK           | INTEGRADO_EN_AUS      | OWID/UN WPP 2024 + OWID/FAOSTAT 2025 | POBLACION,SUPERFICIE | EXCLUIR_INDICADOR       | Se excluye superficie para evitar riesgo de doble conteo.                                    |
| Pitcairn                       | PCN           | SIN_CODIGO_SEPARADO   | OWID/UN WPP 2024 + OWID/FAOSTAT 2025 | POBLACION,SUPERFICIE | EXCLUIR_INDICADOR       | Se excluye superficie para consistencia de tratamiento.                                      |
| Svalbard and Jan Mayen         | SJM           | INTEGRADO_EN_NOR      | OWID/UN WPP 2024 + OWID/FAOSTAT 2025 | POBLACION,SUPERFICIE | EXCLUIR_INDICADOR       | Sin separacion comparable en la fuente principal.                                            |
| Guernsey                       | GGY           | GGY                   | OWID/UN WPP 2024 + OWID/FAOSTAT 2025 | POBLACION,SUPERFICIE | INCLUIR_POB_EXCLUIR_SUP | No se imputa superficie alternativa sin comparabilidad metodologica cerrada.                 |
| Jersey                         | JEY           | JEY                   | OWID/UN WPP 2024 + OWID/FAOSTAT 2025 | POBLACION,SUPERFICIE | INCLUIR_POB_EXCLUIR_SUP | No se imputa superficie alternativa sin comparabilidad metodologica cerrada.                 |
| Kosovo                         | XKX           | NO_PRESENTE_EN_FUENTE | OWID/UN WPP 2024 + OWID/FAOSTAT 2025 | POBLACION,SUPERFICIE | EXCLUIR_INDICADOR       | Se mantiene SEGUN_FUENTE; excluido temporalmente del agregado hasta resolver sin duplicidad. |

## Cobertura por area

| area_codigo   | area_nombre                   |   entidades |   con_poblacion |   con_superficie |   cobertura_poblacion_pct |   cobertura_superficie_pct |
|:--------------|:------------------------------|------------:|----------------:|-----------------:|--------------------------:|---------------------------:|
| AFR           | África                        |          59 |              58 |               58 |                   98.3051 |                    98.3051 |
| APC           | Asia-Pacífico                 |          43 |              39 |               39 |                   90.6977 |                    90.6977 |
| CHN           | China                         |           3 |               3 |                3 |                  100      |                   100      |
| EUR           | Europa                        |          51 |              48 |               46 |                   94.1176 |                    90.1961 |
| MDE           | Oriente Medio                 |          15 |              15 |               15 |                  100      |                   100      |
| NAC           | Norteamérica y Caribe         |          41 |              41 |               41 |                  100      |                   100      |
| RUE           | Rusia y Eurasia postsoviética |          10 |              10 |               10 |                  100      |                   100      |
| SAI           | Subcontinente indio           |           8 |               8 |                8 |                  100      |                   100      |
| SAM           | Sudamérica                    |          14 |              14 |               14 |                  100      |                   100      |

## Agregados actualizados

| area_codigo   | area_nombre                   |   superficie_km2 |   superficie_mundial_pct |   poblacion_2025 |   poblacion_mundial_pct |   densidad_2025 | edad_mediana_2025_aprox   |   poblacion_2050 |   variacion_2025_2050_pct |   entidades_totales |   entidades_con_poblacion |   entidades_con_superficie |
|:--------------|:------------------------------|-----------------:|-------------------------:|-----------------:|------------------------:|----------------:|:--------------------------|-----------------:|--------------------------:|--------------------:|--------------------------:|---------------------------:|
| AFR           | África                        |      2.99335e+07 |                 22.9962  |      1.54874e+09 |                18.8209  |         51.7393 |                           |      2.46502e+09 |                  59.1634  |                  59 |                        58 |                         58 |
| APC           | Asia-Pacífico                 |      1.50969e+07 |                 11.598   |      9.74613e+08 |                11.8439  |         64.5573 |                           |      1.03225e+09 |                   5.91364 |                  43 |                        39 |                         39 |
| CHN           | China                         |      9.38929e+06 |                  7.21324 |      1.42421e+09 |                17.3077  |        151.685  |                           |      1.26705e+09 |                 -11.0353  |                   3 |                         3 |                          3 |
| EUR           | Europa                        |      5.55119e+06 |                  4.26465 |      5.91101e+08 |                 7.18331 |        106.482  |                           |      5.59306e+08 |                  -5.37882 |                  51 |                        48 |                         46 |
| MDE           | Oriente Medio                 |      6.22487e+06 |                  4.7822  |      3.88187e+08 |                 4.71742 |         62.3607 |                           |      5.0229e+08  |                  29.3936  |                  15 |                        15 |                         15 |
| NAC           | Norteamérica y Caribe         |      2.10222e+07 |                 16.1501  |      6.17312e+08 |                 7.50184 |         29.3648 |                           |      6.87963e+08 |                  11.4449  |                  41 |                        41 |                         41 |
| RUE           | Rusia y Eurasia postsoviética |      2.07011e+07 |                 15.9034  |      2.5375e+08  |                 3.08367 |         12.2578 |                           |      2.74583e+08 |                   8.21016 |                  10 |                        10 |                         10 |
| SAI           | Subcontinente indio           |      4.76993e+06 |                  3.66446 |      1.99279e+09 |                24.2172  |        417.782  |                           |      2.40398e+09 |                  20.6336  |                   8 |                         8 |                          8 |
| SAM           | Sudamérica                    |      1.74785e+07 |                 13.4277  |      4.38105e+08 |                 5.32404 |         25.0653 |                           |      4.68675e+08 |                   6.97757 |                  14 |                        14 |                         14 |

## Diferencias respecto a agregados previos

| area_codigo   |   delta_poblacion_2025 |   delta_poblacion_2050 |   delta_superficie_km2 |   delta_densidad_2025 |
|:--------------|-----------------------:|-----------------------:|-----------------------:|----------------------:|
| AFR           |                      0 |                      0 |                      0 |           0           |
| APC           |                      0 |                      0 |                    -87 |           0.000372027 |
| CHN           |                      0 |                      0 |                      0 |           0           |
| EUR           |                      0 |                      0 |                      0 |           1.42109e-14 |
| MDE           |                      0 |                      0 |                      0 |          -7.10543e-15 |
| NAC           |                      0 |                      0 |                      0 |           0           |
| RUE           |                      0 |                      0 |                      0 |           0           |
| SAI           |                      0 |                      0 |                      0 |           0           |
| SAM           |                      0 |                      0 |                      0 |           0           |

## Validaciones finales

1. Nueve areas: **9**.
2. Suma mundial poblacion 2025: **8,228,810,343**.
3. Suma mundial poblacion 2050: **9,661,111,277**.
4. Suma porcentaje poblacion: **100.000000**.
5. Suma porcentaje superficie: **100.000000**.
6. Ausentes convertidos en cero: **no**.
7. China/Hong Kong/Macao/Taiwan: **sin cambios de regla territorial**.
8. Serbia/Kosovo: Kosovo excluido temporalmente para evitar duplicidad.
9. Territorios dependientes: tratamiento por indicador documentado en correspondencias.
