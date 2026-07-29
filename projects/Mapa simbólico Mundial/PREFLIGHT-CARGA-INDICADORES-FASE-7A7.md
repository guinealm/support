# Preflight de carga de indicadores — Fase 7A.7

Fecha: 2026-07-29  
Edición objetivo: `RG2025_V1`

## Alcance y limitación

Se revisaron el esquema SQL versionado, los CSV y los tres SQL preparados. No se ejecutó ninguna sentencia contra MySQL: por tanto, los controles que requieren `SELECT` sobre la base desplegada quedan pendientes y la decisión es **NO-GO PARA EJECUCIÓN** hasta obtener esas evidencias.

## Resultados

| Control | Resultado | Evidencia | Riesgo | Acción necesaria | Estado |
|---|---|---|---|---|---|
| Esquema `rg_datos_area` | Revisado en el DDL local | `01_rg_estructura_minima.sql`: columnas `area_id`, `indicador_id`, `periodo_id`, `anio_referencia`, `valor`, método, cobertura, fuente, estado, observaciones y `activo`; clave única `(area_id,indicador_id,periodo_id,anio_referencia)` | El esquema desplegado podría diferir | Ejecutar `SHOW CREATE TABLE` y `SHOW INDEX` mediante SELECT/consulta administrativa | APTO CON AJUSTE |
| `POB_URB` en catálogo | No confirmado en la base actual | Inventario previo indicaba ausencia; el SQL usa código aprobado y lo crea condicionalmente | Duplicidad o campos obligatorios distintos | `SELECT` de `rg_indicadores`, `rg_bloques` y restricciones antes de cargar | BLOQUEANTE |
| Fuentes `WB_WDI`, `OWID`, `UNDP_HDR` | Confirmadas documentalmente, no mediante SELECT real | Referencias en SQL/README | Código o ID diferente en producción | Consultar código, ID y duplicados en `rg_fuentes` | BLOQUEANTE |
| Periodo y áreas | Confirmados en archivos, no en servidor | `RG2025_V1` y nueve códigos en los artefactos | Periodo no activo/congelado o área duplicada | Consultar `rg_periodos` y `rg_areas` | BLOQUEANTE |
| CSV publicable | Apto | 53 filas, 53 claves únicas; 9 filas para cada uno de `TERR_DENS`, `POB_URB`, `POB_EDAD`, `HUM_EV`, `HUM_IDH`; 8 para `ECO_PC`; ninguna `ECO_PC/MDE` | Ninguno detectado localmente | Repetir comprobación en preflight SQL | APTO |
| Tipos y precisión | Apto provisional | Valores decimales compatibles con `DECIMAL(22,10)`; años enteros | DDL real distinto | Comparar con `SHOW CREATE TABLE` | APTO CON AJUSTE |
| Observaciones | Apto provisional | Longitudes compatibles con `TEXT` en DDL | Columna real más corta | Confirmar tipo real | APTO CON AJUSTE |
| `ECO_PC/MDE` | Retirada prevista | SQL limita la actualización a `RG2025_V1`, `ECO_PC`, área `MDE`, con `activo=0` y `NO_PUBLICABLE` | Si no existe `activo` o el registro no es único, la retirada no será segura | Consultar fila, clave y estado actuales | BLOQUEANTE |
| Respaldo | Diseño apto | Tablas versionadas `rg_backup_datos_area_7a7_20260729` y `rg_backup_indicadores_7a7_20260729`, creadas antes de la transacción | DDL no es transaccional en muchos MySQL | Crear/verificar respaldo antes de `START TRANSACTION`; conservar también volcado externo | APTO CON AJUSTE |
| Transacción | Apta en el SQL preparado | No hay DDL después de `START TRANSACTION`; DML y `COMMIT` al final | El operador podría confirmar sin revisar los SELECT | Detenerse ante resultados no esperados y ejecutar `ROLLBACK` | APTO CON AJUSTE |
| Reversión | Parcialmente apta | Restaura `rg_datos_area` desde el respaldo y elimina `POB_URB` solo si no existía | Requiere que el respaldo exista y no cambie | Verificar el respaldo y ejecutar reversión en transacción | APTO CON AJUSTE |

## Comprobaciones de archivos

- `datos-area-publicables-7a7.csv`: exactamente 53 claves únicas.
- Distribución: cinco indicadores con 9 filas y `ECO_PC` con 8.
- `datos-area-no-publicables-7a7.csv`: una fila exacta `RG2025_V1/MDE/ECO_PC`.
- Las nueve áreas usadas son `AFR, APC, CHN, EUR, MDE, NAC, RUE, SAI, SAM`.
- No hay valores cero usados para representar ausencias.
- Las fuentes indicadas son `WB_WDI`, `OWID` y `UNDP_HDR`; su existencia/ID real aún requiere SELECT.

## Consultas obligatorias antes de autorizar

Ejecutar únicamente las consultas de `validaciones_indicadores_complementarios_7a7.sql` y, adicionalmente, `SHOW CREATE TABLE rg_datos_area`, `SHOW INDEX FROM rg_datos_area`, y SELECT sobre catálogo, fuentes, periodo, áreas y la fila `ECO_PC/MDE`. No ejecutar todavía los SQL de carga ni reversión.

## Decisión

**NO-GO PARA EJECUCIÓN.** El único bloqueo es la ausencia de evidencia SELECT sobre la base real (catálogo `POB_URB`, fuentes, periodo/áreas, esquema y fila actual `ECO_PC/MDE`). Los archivos de carga no deben ejecutarse hasta resolverlo.

