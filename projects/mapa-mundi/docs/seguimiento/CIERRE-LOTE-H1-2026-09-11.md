# Cierre del lote H1 — archivo histórico

**Fecha:** 11 de septiembre de 2026
**Destino autorizado:** `C:\jumalenin-ecosistema\archivo\reticula-global-2025\`

## Resultado

- El antiguo `projects/Mapa simbólico Mundial/` se trasladó fuera de `sites/support` y de la ruta pública.
- El archivo conserva 243 archivos históricos, metodológicos y de preparación.
- Se conservaron los prototipos v1–v5, documentos, informes, scripts, CSV, SQL y fuentes no reproducibles.
- Antes del traslado se retiraron seis copias idénticas a archivos canónicos de `projects/mapa-mundi/`: `areas.json`, `territorios.json`, `paleta.json`, `datos-indicadores.json`, `correspondencias-cartograficas.json` y `world.geojson`.
- La identidad de cada pareja se verificó mediante SHA-256 y el original canónico permanece en la aplicación activa.

## Ajustes de referencias

Los tres generadores canónicos apuntan ahora al archivo externo para el maestro territorial y los agregados congelados. `AGENTS.md`, la guía de migración y la tarea de inventario de VS Code reflejan la topología nueva. Los informes históricos conservan las rutas antiguas como evidencia de su fecha.

## Validación

- el origen público ya no existe;
- el destino autorizado existe y contiene 243 archivos;
- maestro territorial, tres agregados y prototipos v1 y v5 comprobados;
- sintaxis Python válida en los tres generadores, compilada en memoria;
- los seis archivos canónicos no aparecen modificados en Git.

## Operaciones no realizadas

No se ejecutaron scripts, API, SQL ni conexiones a base de datos. No se modificaron datos o metodología. No se hizo commit, push ni despliegue.
