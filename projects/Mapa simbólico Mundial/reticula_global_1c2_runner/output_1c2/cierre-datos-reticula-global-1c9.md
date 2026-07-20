# Cierre de datos Retícula Global — Fase 1C.9

Estado: **auditoría integral y congelación completadas**.

## Inventario previsto y confirmado hasta 1C.8

- 9 áreas.
- 244 países y territorios.
- 8 bloques activos.
- 27 indicadores activos.
- 243 registros activos de área: nueve por indicador.
- 215 registros nacionales TEC_NET.

SQL 26 confirmó el inventario dinámico de nombre, unidad, años, filas nacionales, nueve filas de área y cobertura mínima de los 27 indicadores.

## Comprobaciones preparadas

`26_rg_comprobacion_integral_1c9.sql` revisa estructura, periodo, vista existente, conteos, catálogo, fuentes, años, cobertura, duplicidades, ceros, rangos, extremos, porcentajes mundiales, inventario nuclear, coherencia energética, indicadores derivados y territorios especiales.

## Incidencias y riesgos abiertos

1. `rg_periodos` no contiene fecha de cierre ni observaciones; estos metadatos quedan documentados fuera de MySQL.
2. Los 17 ceros nacionales y dos ceros de área revisados son valores publicados o resultados metodológicamente válidos; no representan ausencias convertidas en cero.
3. `ENE_DEP` puede ser negativo y `ENE_AUTO` superar 100 % en exportadores netos. Son resultados algebraicos válidos de `ENE_AUTO = 100 - ENE_DEP`, no porcentajes de composición restringidos a 0–100.
4. `TEC_NET` presenta dispersión 1990–2025 y `HUM_GINI` 2015–2024; ambos conservan el año real y requieren advertencia visible.
5. La primera ejecución del control de `CLI_CO2_PC` produjo cinco falsos `NO_OK` porque usó población total. El SQL 26 quedó corregido para utilizar exclusivamente población cubierta, coherente con SQL 22 y con la metodología climática validada.
6. Existen fuentes históricas activas sin uso actual (`EI_SR2026`, `OWID_ENERGY_PROC`); no hay datos activos sin fuente vinculada. No bloquean la congelación, pero pueden depurarse en una migración futura.

## Indicadores aplazados

- ENE_FOS: cobertura insuficiente y falta de fuente comparable complementaria.
- TEC_ID: cobertura insuficiente.
- TEC_PESO: metodología no definida suficientemente.

No se crean ni recuperan durante 1C.9.

## SQL y documentos

- `26_rg_comprobacion_integral_1c9.sql`: preparado, solo lectura.
- `27_rg_congelar_periodo_1c9.sql`: preparado para actualizar exclusivamente `estado` y `activo` de `RG2025_V1`.
- `reticula-global-primera-edicion-2025.md`: ficha de congelación preparada.
- `propuesta-rg-v-primera-edicion-1c9.md`: propuesta documental, no ejecutada.

## Decisión actual

- **SQL 26 ejecutado y revisado**.
- **SQL 27 ejecutado manualmente**: la interfaz informó una fila afectada y la selección final confirmó `RG2025_V1`, `congelado`, activo.
- **Fase 1C.9 cerrada con GO**.

Codex no ejecutó MySQL, no modificó la web pública y no inició desarrollo visual ni una fase posterior.
