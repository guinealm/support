# Preparación de carga con dato no publicable — Fase 7A.7

Fecha: 2026-07-29  
Periodo: `RG2025_V1`

## Resultado preparado

Se preparan **53 valores publicables** y una combinación separada `ECO_PC/MDE` marcada `NO PUBLICABLE`. No se ejecutó ningún SQL de escritura y MySQL permanece sin cambios.

`POB_URB` no existía aún en el catálogo; el SQL usa el código aprobado y lo inserta condicionalmente dentro de la transacción solo si falta, sin crear un código alternativo. La fuente auxiliar de Taiwán se atribuye al código registrado `WB_WDI` a nivel de área y se conserva en las observaciones, porque el esquema actual no contiene códigos separados para DGBAS.

## Archivos de datos

- `datos-area-publicables-7a7.csv`: exactamente 53 claves.
- `datos-area-no-publicables-7a7.csv`: exactamente una fila, `ECO_PC/MDE`, sin valor público.

No se almacena cero ni una fila nula para representar Siria.

## Plan de operación futura

1. Crear, antes de la transacción, las tablas versionadas `rg_backup_datos_area_7a7_20260729` y `rg_backup_indicadores_7a7_20260729`.
2. Respaldar todas las filas existentes de `RG2025_V1` para `TERR_DENS`, `POB_URB`, `POB_EDAD`, `HUM_EV`, `ECO_PC` y `HUM_IDH`, incluidas las nueve áreas de `ECO_PC`.
3. Iniciar transacción.
4. Insertar `POB_URB` solo si el catálogo aún no lo contiene.
5. Actualizar los 44 registros existentes publicables y añadir las nueve filas `POB_URB`.
6. Desactivar el registro anterior `ECO_PC/MDE` con `activo=0` y `estado_dato=NO_PUBLICABLE`; no se reemplaza por cero ni por NULL.
7. Ejecutar validaciones y confirmar únicamente si el operador obtiene 53 activos y cero activos en `ECO_PC/MDE`.

El respaldo se identifica por fase y fecha y no se comparte con otros procesos. No se ejecuta DDL después de `START TRANSACTION`; la creación del respaldo ocurre antes de ella.

## Resultado esperado

| Indicador | Activos esperados |
|---|---:|
| `TERR_DENS` | 9 |
| `POB_URB` | 9 |
| `POB_EDAD` | 9 |
| `HUM_EV` | 9 |
| `HUM_IDH` | 9 |
| `ECO_PC` | 8 |
| **Total** | **53** |

`ECO_PC/MDE` debe devolver cero registros activos. Debe existir cero duplicidad, cero nulos cargados y cero ausencias convertidas en cero.

## Reversión

`95_reversion_indicadores_complementarios_7a7.sql` elimina únicamente las filas activas de los seis códigos en `RG2025_V1`, restaura el respaldo exacto y elimina el catálogo `POB_URB` solo si el marcador confirma que no existía antes. Los `DROP TABLE` del respaldo quedan comentados hasta verificar la restauración.

## Limitaciones del esquema

- `rg_datos_area` no tiene un estado específico `NO_PUBLICABLE`; se usa `activo=0`, `estado_dato=NO_PUBLICABLE` y una observación explícita.
- `rg_datos_area` exige `fuente_principal_id`, pero no tiene URL ni fuente auxiliar por fila; la procedencia auxiliar se conserva en `observaciones`.
- La clave única es `(area_id, indicador_id, periodo_id, anio_referencia)`; el preflight debe confirmar que no existe una segunda fila para esa combinación.
- La creación condicional de `POB_URB` solo es válida porque el código está aprobado y no hay duplicado de catálogo.

## Archivos SQL

- `29_carga_indicadores_complementarios_7a7.sql`: propuesta de carga, no ejecutada.
- `95_reversion_indicadores_complementarios_7a7.sql`: reversión exacta, no ejecutada.
- `validaciones_indicadores_complementarios_7a7.sql`: preflight y validaciones, no ejecutado.

## Estado

**PREPARACIÓN COMPLETADA — pendiente de aprobación para ejecutar la futura carga.**
