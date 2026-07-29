# Validación técnica y carga controlada — Fase 7A.4

Fecha: 2026-07-28  
Proyecto: Retícula Global 2025 — Support  
Periodo requerido: `RG2025_V1`

## Decisión

**NO-GO**

La carga se detuvo en el preflight. No se abrió una transacción de escritura, no se ejecutó el SQL 7A.3 y MySQL permanece en su estado anterior.

No es posible cumplir simultáneamente estas dos condiciones aprobadas:

1. cargar seis indicadores con nueve áreas; y
2. no cargar resultados con cobertura insuficiente, pendientes o no calculables.

## Copia de seguridad

No se creó una copia nueva porque la carga fue rechazada antes de cualquier escritura. Tampoco se generó un volcado completo.

El respaldo propuesto por 7A.3 no se ejecutó. Crear una tabla de respaldo habría modificado MySQL innecesariamente después de conocerse el NO-GO. Cualquier futuro volcado completo deberá guardarse fuera de Git.

## Tablas afectadas

Ninguna.

- `rg_datos_area`: sin cambios.
- `rg_indicadores`: sin cambios.
- `rg_periodos`: sin cambios.
- `rg_fuentes`: sin cambios.

Registros insertados: **0**.  
Registros actualizados: **0**.  
Registros eliminados: **0**.

## SQL revisado

Se revisaron íntegramente:

- `28_carga_indicadores_complementarios_7a3.sql`;
- `94_reversion_indicadores_complementarios_7a3.sql`;
- el esquema de `rg_datos_area`;
- los 54 resultados de `datos-area-indicadores-complementarios-7a3.csv`;
- las incidencias y criterios metodológicos 7A.2.

No se ejecutó SQL contra MySQL. Las comprobaciones del estado actual se realizaron mediante lecturas de la API pública, sin modificarla.

`28_carga_indicadores_complementarios_7a4.sql` conserva las consultas SELECT de preflight y no contiene sentencias de escritura. `94_reversion_indicadores_complementarios_7a4.sql` es deliberadamente una comprobación de solo lectura, porque no existe una carga 7A.4 que revertir.

## Admisibilidad de los resultados 7A.3

| Indicador | Filas preparadas | Admisibles | Rechazadas | Resultado |
|---|---:|---:|---:|---|
| `TERR_DENS` | 9 | 9 | 0 | Completo, con observación temporal registrada |
| `POB_URB` | 9 | 0 | 9 | PENDIENTE DE DATO; valores ausentes |
| `POB_EDAD` | 9 | 9 | 0 | Completo, denominado aproximación |
| `HUM_EV` | 9 | 9 | 0 | Completo, con método ponderado registrado |
| `ECO_PC` | 9 | 7 | 2 | APC y MDE con cobertura insuficiente |
| `HUM_IDH` | 9 | 8 | 1 | APC con cobertura insuficiente |
| **Total** | **54** | **42** | **12** | Carga completa imposible |

Filas expresamente prohibidas:

- `POB_URB`: las nueve áreas, porque no existe una serie nacional incorporada;
- `ECO_PC/APC`: cobertura 94,8447 %;
- `ECO_PC/MDE`: cobertura 82,9370 %;
- `HUM_IDH/APC`: cobertura 94,7568 %.

No se transformó ninguna ausencia en cero.

## Estado actual comprobado

La lectura pública del 2026-07-28 confirmó:

| Indicador | HTTP | Filas actuales | Áreas únicas | Duplicados | Nulos | Fuente | Periodo |
|---|---:|---:|---:|---:|---:|---|---|
| `TERR_DENS` | 200 | 9 | 9 | 0 | 0 | `OWID` | `RG2025_V1`, congelado |
| `POB_URB` | 200 | 0 | 0 | 0 | 0 | Sin registro | `RG2025_V1`, congelado |
| `POB_EDAD` | 200 | 9 | 9 | 0 | 0 | `OWID` | `RG2025_V1`, congelado |
| `HUM_EV` | 200 | 9 | 9 | 0 | 0 | `WB_WDI` | `RG2025_V1`, congelado |
| `ECO_PC` | 200 | 9 | 9 | 0 | 0 | `WB_WDI` | `RG2025_V1`, congelado |
| `HUM_IDH` | 200 | 9 | 9 | 0 | 0 | `UNDP_HDR` | `RG2025_V1`, congelado |

Estas lecturas confirman el estado previo, no la carga 7A.4.

## Validaciones técnicas

- Los CSV de 7A.3 contienen exactamente 54 claves únicas: seis indicadores por nueve áreas.
- Los códigos territoriales son exclusivamente `AFR`, `APC`, `CHN`, `EUR`, `MDE`, `NAC`, `RUE`, `SAI` y `SAM`.
- Los códigos de indicador se mantienen sin alternativas.
- Los valores calculables cumplen sus rangos técnicos:
  - densidad mayor que cero;
  - edad mediana entre 10 y 60 años;
  - esperanza de vida entre 40 y 90 años;
  - PIB por habitante mayor que cero;
  - IDH entre 0 y 1.
- Urbanización no puede someterse al rango 0–100 porque no tiene valores; no se interpreta su ausencia como cero.
- Las observaciones de densidad, edad, esperanza de vida, PIB por habitante e IDH quedan incluidas en cada fila candidata.

## Incidencias del SQL 7A.3

1. Solo contiene 42 valores candidatos y, por tanto, no puede producir seis bloques completos de nueve.
2. Excluye correctamente las tres celdas calculadas bajo el 95 %, pero una actualización parcial dejaría en MySQL valores anteriores con otra metodología para esas áreas.
3. `POB_URB` no existe materializado y no contiene valores.
4. La creación de `rg_backup_datos_area_7a3` ocurre antes de `START TRANSACTION`. En MySQL, el DDL no forma parte de una transacción atómica equivalente a las actualizaciones posteriores.
5. La reversión 7A.3 elimina las 45 filas completas de cinco indicadores y las restaura desde una tabla persistente. Aunque los códigos están acotados, no protege frente a cambios legítimos realizados entre carga y reversión.
6. Cambiar `anio_referencia` exige una comprobación directa previa de la clave única `(area_id, indicador_id, periodo_id, anio_referencia)`.

Estas incidencias impiden ejecutar el SQL provisional como carga controlada definitiva.

## Instrucciones de reversión

No debe ejecutarse `94_reversion_indicadores_complementarios_7a3.sql`, porque la carga asociada no se ejecutó.

`94_reversion_indicadores_complementarios_7a4.sql` solo devuelve un estado `NO_OP` y permite comprobar, mediante SELECT, que siguen existiendo las filas activas anteriores. No realiza cambios.

## Requisitos antes de reintentar

Para obtener GO en una fase futura será necesario:

1. incorporar y validar datos nacionales de urbanización para las nueve áreas;
2. elevar al menos al 95 % la cobertura de `ECO_PC` en APC y MDE;
3. elevar al menos al 95 % la cobertura de `HUM_IDH` en APC;
4. regenerar los cálculos y las incidencias;
5. preparar un mecanismo de respaldo y reversión atómico o inequívocamente versionado;
6. validar en una copia o transacción de prueba las 54 filas antes del COMMIT.

No se han buscado sustituciones improvisadas ni datos de años incompatibles.
