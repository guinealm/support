# Cierre de la Fase 1C.9 — Primera edición de datos

Fecha de cierre: 20 de julio de 2026.

## Decisión

La Fase 1C.9 queda cerrada con **GO**. La primera edición de datos se identifica como `RG2025-V1` y el periodo `RG2025_V1` quedó congelado y activo en MySQL.

## Resultado validado

- 9 áreas.
- 244 países y territorios.
- 8 bloques activos.
- 27 indicadores activos.
- 243 registros activos de área.
- 9 registros de área por indicador.
- Sin códigos ni filas activas duplicadas.
- Sin datos activos carentes de fuente vinculada.
- Porcentajes mundiales de territorio, población, PIB y gasto militar coherentes con 100 %.
- Inventario nuclear de 12.187 ojivas distribuido entre nueve Estados.
- Cálculos económicos, militares, energéticos, climáticos y tecnológicos revisados.
- `rg_v_datos_consolidados` conservada sin cambios.
- `rg_v_primera_edicion` documentada, pero no creada.

## Advertencias conservadas

- `HUM_GINI`: dispersión temporal 2015–2024.
- `TEC_NET`: dispersión temporal 1990–2025.
- `ENE_DEP` puede ser negativo y `ENE_AUTO` superar 100 % para exportadores netos.
- Los valores cero publicados se conservan con trazabilidad y no representan ausencias imputadas.
- `rg_periodos` no dispone de columnas para fecha de cierre u observaciones; esos metadatos permanecen en la documentación.

## Indicadores aplazados

- `ENE_FOS`: cobertura comparable insuficiente.
- `TEC_ID`: cobertura insuficiente.
- `TEC_PESO`: metodología pendiente.

Ninguno fue creado en MySQL.

## Ejecución MySQL

El usuario ejecutó manualmente `26_rg_comprobacion_integral_1c9.sql` y `27_rg_congelar_periodo_1c9.sql`. La selección final de SQL 27 confirmó:

- código: `RG2025_V1`;
- estado: `congelado`;
- activo: `1`.

Codex no ejecutó MySQL.

## Límites respetados

- No se modificó la web pública.
- No se inició el desarrollo visual ni la conexión PHP/API.
- No se inició una fase posterior.
- El volcado local de MySQL permanece fuera de Git.
