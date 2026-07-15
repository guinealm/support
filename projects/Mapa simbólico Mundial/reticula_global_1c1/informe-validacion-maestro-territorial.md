# Informe de validación del maestro territorial

Fecha: 2026-07-15

## Resumen

- Registros totales: **250**
- Registros operativos: **244**
- Países soberanos: **196**
- Territorios dependientes: **44**
- Regiones especiales: **2**
- Entidades estadísticas: **2**
- Territorios sin población permanente: **6**
- Excepciones documentadas: **11**

## Controles

- Duplicados M49: **0**
- Duplicados ISO3: **0**
- Registros sin área no justificados: **0**
- Excepciones sin motivo: **0**

## Registros por área

| area_codigo   | area_nombre                   |   registros |
|:--------------|:------------------------------|------------:|
|               | Sin área estadística          |           1 |
| AFR           | África                        |          60 |
| APC           | Asia-Pacífico                 |          45 |
| CHN           | China                         |           3 |
| EUR           | Europa                        |          51 |
| MDE           | Oriente Medio                 |          15 |
| NAC           | Norteamérica y Caribe         |          41 |
| RUE           | Rusia y Eurasia postsoviética |          10 |
| SAI           | Subcontinente indio           |           8 |
| SAM           | Sudamérica                    |          16 |

## Observaciones

1. Antártida se conserva para cartografía, pero queda fuera de las nueve áreas estadísticas.
2. Kosovo se añade como entidad estadística auxiliar con código técnico `XKX`; no es una entrada principal M49.
3. Los territorios dependientes y regiones especiales quedan como `SEGUN_FUENTE`.
4. La lista utiliza códigos numéricos ISO/M49 de `pycountry`, contrastados con la tabla oficial M49; la asignación regional se ha normalizado para aplicar las nueve reglas del proyecto.
5. Debe realizarse una revisión editorial posterior de nombres españoles y relaciones de soberanía de territorios dependientes.
