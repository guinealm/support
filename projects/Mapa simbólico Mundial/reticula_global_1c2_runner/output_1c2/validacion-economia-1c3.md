# validacion-economia-1c3.md

## Resumen

- Areas detectadas: **9**
- Entidades maestras: **244**
- Entidades con PIB: **203**
- Entidades sin PIB: **41**
- Suma PIB mundial agregado (nueve areas): **110,633,680,289,696.14**
- Suma porcentajes PIB: **100.000000**

## Comprobaciones

1. Nueve areas: **OK**.
2. Ausentes convertidos a cero: **NO**.
3. Porcentajes suman ~100: **OK**.
4. PIB por habitante derivado de totales: **OK** (calculado como PIB area / poblacion 2025 area).
5. Codigos duplicados en salida nacional: **0**.
6. Agregados WDI como paises: **NO** (se cruza solo contra maestro ISO3).
7. China/Hong Kong/Macao (revision duplicidad):

| codigo_iso3   |     pib_usd |   anio_pib | observaciones                                               |
|:--------------|------------:|-----------:|:------------------------------------------------------------|
| CHN           | 1.87297e+13 |       2024 | WDI reporta CHN separado; revisar consistencia con HKG/MAC. |
| HKG           | 4.08369e+11 |       2024 | WDI reporta HKG separado de CHN.                            |
| MAC           | 4.94673e+10 |       2024 | WDI reporta MAC separado de CHN.                            |

8. Serbia/Kosovo (revision duplicidad):

| codigo_iso3   |     pib_usd |   anio_pib | observaciones                                                      |
|:--------------|------------:|-----------:|:-------------------------------------------------------------------|
| SRB           | 9.00884e+10 |       2024 |                                                                    |
| XKX           | 1.1203e+10  |       2024 | WDI publica XKX separado; mantener separado de SRB sin duplicidad. |

9. Datos con anio 2023 (fallback): **3**.
10. Cobertura por area: ver tabla de agregados economicos.
11. Entidades sin dato listadas abajo.
12. Valores extremos/unidades: registrados en incidencias.

## Entidades sin dato

| codigo_iso3   | pais                                         | area_codigo   |
|:--------------|:---------------------------------------------|:--------------|
| ASM           | American Samoa                               | APC           |
| IOT           | British Indian Ocean Territory               | AFR           |
| VGB           | Virgin Islands, British                      | NAC           |
| TWN           | Taiwan, Province of China                    | APC           |
| CXR           | Christmas Island                             | APC           |
| CCK           | Cocos (Keeling) Islands                      | APC           |
| MYT           | Mayotte                                      | AFR           |
| COK           | Cook Islands                                 | APC           |
| CUB           | Cuba                                         | NAC           |
| ERI           | Eritrea                                      | AFR           |
| FLK           | Falkland Islands (Malvinas)                  | SAM           |
| ALA           | Åland Islands                                | EUR           |
| GUF           | French Guiana                                | SAM           |
| GIB           | Gibraltar                                    | EUR           |
| GLP           | Guadeloupe                                   | NAC           |
| GUM           | Guam                                         | APC           |
| VAT           | Holy See (Vatican City State)                | EUR           |
| PRK           | Corea del Norte                              | APC           |
| MTQ           | Martinique                                   | NAC           |
| MSR           | Montserrat                                   | NAC           |
| BES           | Bonaire, Sint Eustatius and Saba             | NAC           |
| NIU           | Niue                                         | APC           |
| NFK           | Norfolk Island                               | APC           |
| MNP           | Northern Mariana Islands                     | APC           |
| PCN           | Pitcairn                                     | APC           |
| REU           | Réunion                                      | AFR           |
| BLM           | Saint Barthélemy                             | NAC           |
| SHN           | Saint Helena, Ascension and Tristan da Cunha | AFR           |
| AIA           | Anguilla                                     | NAC           |
| MAF           | Saint Martin (French part)                   | NAC           |
| SPM           | Saint Pierre and Miquelon                    | NAC           |
| SSD           | South Sudan                                  | AFR           |
| ESH           | Western Sahara                               | AFR           |
| SJM           | Svalbard and Jan Mayen                       | EUR           |
| SYR           | Siria                                        | MDE           |
| TKL           | Tokelau                                      | APC           |
| GGY           | Guernsey                                     | EUR           |
| JEY           | Jersey                                       | EUR           |
| VIR           | Virgin Islands, U.S.                         | NAC           |
| WLF           | Wallis and Futuna                            | APC           |
| YEM           | Yemen                                        | MDE           |

## Tabla de areas

| area_codigo   | area_nombre                   |     pib_usd |   pib_mundial_pct |   poblacion_2025 |   pib_por_habitante_usd |   entidades_totales |   entidades_con_pib |   poblacion_cubierta_pct |   anio_minimo |   anio_maximo | observaciones                                                                                           |
|:--------------|:------------------------------|------------:|------------------:|-----------------:|------------------------:|--------------------:|--------------------:|-------------------------:|--------------:|--------------:|:--------------------------------------------------------------------------------------------------------|
| AFR           | África                        | 2.90169e+12 |           2.62279 |      1.54874e+09 |                 1873.58 |                  59 |                  52 |                  98.8622 |          2024 |          2024 | Cobertura incompleta en entidades. Cobertura poblacional alta.                                          |
| APC           | Asia-Pacífico                 | 1.21786e+13 |          11.0081  |      9.74613e+08 |                12495.9  |                  43 |                  30 |                  94.8727 |          2024 |          2024 | Cobertura incompleta en entidades. Cobertura poblacional aceptable.                                     |
| CHN           | China                         | 1.91875e+13 |          17.3433  |      1.42421e+09 |                13472.3  |                   3 |                   3 |                 100      |          2024 |          2024 | Cobertura poblacional alta.                                                                             |
| EUR           | Europa                        | 2.51307e+13 |          22.7152  |      5.91101e+08 |                42515    |                  51 |                  45 |                  99.9646 |          2023 |          2024 | Cobertura incompleta en entidades. Cobertura poblacional alta. Mezcla de anios 2023/2024 por faltantes. |
| MDE           | Oriente Medio                 | 5.09492e+12 |           4.60522 |      3.88187e+08 |                13124.9  |                  15 |                  13 |                  82.6387 |          2024 |          2024 | Cobertura incompleta en entidades. Cobertura poblacional condicionada.                                  |
| NAC           | Norteamérica y Caribe         | 3.41761e+13 |          30.8912  |      6.17312e+08 |                55362.7  |                  41 |                  30 |                  98.0775 |          2023 |          2024 | Cobertura incompleta en entidades. Cobertura poblacional alta. Mezcla de anios 2023/2024 por faltantes. |
| RUE           | Rusia y Eurasia postsoviética | 2.8893e+12  |           2.61159 |      2.5375e+08  |                11386.4  |                  10 |                  10 |                 100      |          2024 |          2024 | Cobertura poblacional alta.                                                                             |
| SAI           | Subcontinente indio           | 4.75378e+12 |           4.29687 |      1.99279e+09 |                 2385.49 |                   8 |                   8 |                 100      |          2024 |          2024 | Cobertura poblacional alta.                                                                             |
| SAM           | Sudamérica                    | 4.32109e+12 |           3.90577 |      4.38105e+08 |                 9863.14 |                  14 |                  12 |                  99.9276 |          2024 |          2024 | Cobertura incompleta en entidades. Cobertura poblacional alta.                                          |

## Incidencias

Total incidencias registradas: **46**.
