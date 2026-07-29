# Preflight MySQL real â€” Fase 7A.7B

Fecha: 2026-07-29  
EdiciÃ³n: `RG2025_V1`

## DecisiÃ³n actualizada

**GO PARA AJUSTAR LOS SQL, PERO TODAVÃA NO GO PARA EJECUTARLOS.** Se recibieron evidencias manuales de phpMyAdmin sobre MySQL real. La carga sigue sin autorizaciÃ³n de ejecuciÃ³n.

## Estado de comprobaciones

| Control | Consulta ejecutada | Resultado real | ComparaciÃ³n con SQL | Riesgo | Ajuste necesario | Estado |
|---|---|---|---|---|---|---|
| Esquema `rg_datos_area` | Evidencia phpMyAdmin | `DECIMAL(22,6)`, `DECIMAL(8,4)`, `fuente_principal_id`, `activo` | Compatible tras ajuste | Mantener precisiÃ³n real | Ajustar SQL, ya realizado | APTO CON AJUSTE |
| CatÃ¡logo de indicadores | Evidencia phpMyAdmin | Cinco existen; `POB_URB` no existe | CreaciÃ³n condicional necesaria | Duplicidad o restricciones | Crear solo cÃ³digo aprobado en bloque 2 | APTO CON AJUSTE |
| Bloque POB | Evidencia phpMyAdmin | `POB`, id 2, activo | Compatible | Ninguno | Ninguno | APTO |
| Fuentes | Evidencia phpMyAdmin | `OWID=3`, `WB_WDI=4`, `UNDP_HDR=5`, Ãºnicas y activas | Compatible | Ninguno | Ninguno | APTO |
| Periodo | Evidencia phpMyAdmin | `RG2025_V1`, id 1, congelado y activo | Compatible | Ninguno | Ninguno | APTO |
| Ãreas | Evidencia phpMyAdmin | Nueve Ã¡reas Ãºnicas, activas, ids 1â€“9 | Compatible | Ninguno | Ninguno | APTO |
| Estado actual de indicadores | Evidencia phpMyAdmin | 45 filas activas, sin duplicados, nulos ni ceros | Respaldo exacto | Error de conteo | Respaldar exactamente 45 | APTO |
| `ECO_PC/MDE` | Evidencia phpMyAdmin | Fila id 95, activa, estado `LIMITACION` | DesactivaciÃ³n prevista | Debe quedar no publicable | `activo=0`, `NO_PUBLICABLE` | APTO CON AJUSTE |
| Compatibilidad local | RevisiÃ³n de archivos | CSV: 53 claves pÃºblicas y 1 no pÃºblica | Coincide con la propuesta | No sustituye evidencia de producciÃ³n | Mantener SQL sin ejecutar hasta obtener SELECT | APTO CON AJUSTE |

## Consultas que deben ejecutarse en la sesiÃ³n autorizada

```sql
SHOW CREATE TABLE rg_datos_area;
SHOW INDEX FROM rg_datos_area;
SHOW COLUMNS FROM rg_datos_area;

SELECT * FROM rg_indicadores
 WHERE codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH');
SELECT * FROM rg_bloques WHERE codigo='POB';
SELECT * FROM rg_fuentes WHERE codigo IN ('WB_WDI','OWID','UNDP_HDR');
SELECT * FROM rg_periodos WHERE codigo='RG2025_V1';
SELECT * FROM rg_areas
 WHERE codigo IN ('AFR','APC','CHN','EUR','MDE','NAC','RUE','SAI','SAM');
```

Las consultas agregadas y la consulta detallada de `ECO_PC/MDE` ya fueron ejecutadas manualmente en phpMyAdmin y sus resultados constan en este documento. Debe conservarse la revisiÃ³n manual antes de autorizar cualquier DML.

## Cambios realizados

Ninguno en MySQL, API, web o Hostinger. No se modificaron los SQL locales porque no existe evidencia real que justifique un ajuste.

## Evidencia MySQL real confirmada

Se recibieron resultados ejecutados sobre `u794456529_map_sim_Mund` para `RG2025_V1`:

| Indicador | Filas totales | Activas | Ãreas activas | Nulos | Ceros | AÃ±os |
|---|---:|---:|---:|---:|---:|---|
| `ECO_PC` | 9 | 9 | 9 | 0 | 0 | 2024 |
| `HUM_EV` | 9 | 9 | 9 | 0 | 0 | 2023 |
| `HUM_IDH` | 9 | 9 | 9 | 0 | 0 | 2023 |
| `POB_EDAD` | 9 | 9 | 9 | 0 | 0 | 2025 |
| `TERR_DENS` | 9 | 9 | 9 | 0 | 0 | 2025 |

La consulta de duplicidades activas devolviÃ³ un conjunto vacÃ­o. El conteo de respaldo devolviÃ³ `45` filas totales y `45` activas. Por tanto, el respaldo previsto debe contener exactamente 45 filas actuales; `POB_URB estÃ¡ confirmado como inexistente en `rg_indicadores` y no tiene filas en `rg_datos_area`.

Estos datos permiten clasificar el preflight como **APTO CON AJUSTE**.

### Confirmaciones adicionales

- `rg_datos_area.valor` es `DECIMAL(22,6)` y `porcentaje_cobertura` es `DECIMAL(8,4)`.
- La columna de fuente correcta es `fuente_principal_id`.
- Indicadores existentes: `TERR_DENS=3`, `POB_EDAD=6`, `ECO_PC=11`, `HUM_IDH=12`, `HUM_EV=14`; `POB_URB` no existe.
- Bloque `POB=2`, activo.
- Fuentes Ãºnicas y activas: `OWID=3`, `WB_WDI=4`, `UNDP_HDR=5`.
- Periodo Ãºnico `RG2025_V1=1`, congelado y activo.
- Ãreas Ãºnicas y activas: `AFR=1`, `APC=2`, `CHN=3`, `EUR=4`, `MDE=5`, `NAC=6`, `RUE=7`, `SAI=8`, `SAM=9`.
- `ECO_PC/MDE`: fila `id=95`, `area_id=5`, `indicador_id=11`, `periodo_id=1`, aÃ±o 2024, valor `13124.895709`, cobertura `82.6387`, fuente `WB_WDI`, estado `LIMITACION`, activo `1`.
- Respaldo exacto requerido: **45 filas**.

## Ajustes realizados en SQL locales

1. `29_carga_indicadores_complementarios_7a7.sql`: se cambiÃ³ la tabla temporal a `DECIMAL(22,6)`; se mantiene `DECIMAL(8,4)` para cobertura; se conserva `fuente_principal_id`; se deja la creaciÃ³n condicional de `POB_URB` en `bloque_id=2`; se aÃ±ade una parada explÃ­cita sin `COMMIT` automÃ¡tico.
2. `95_reversion_indicadores_complementarios_7a7.sql`: se eliminÃ³ el `COMMIT` automÃ¡tico para permitir revisiÃ³n manual antes de confirmar.
3. `validaciones_indicadores_complementarios_7a7.sql`: se aÃ±adieron controles de total esperado y de cero activos para `ECO_PC/MDE`.

Ninguno de estos SQL ha sido ejecutado.

