# Retícula Global 2025 — aplicación activa

Esta carpeta es la fuente canónica del frontend de Retícula Global dentro de Support.

## Vistas

- `index.html`: portada didáctica de Retícula Global.
- `explorar.html`: mapa, comparación y controles del explorador.
- `area.html?codigo=CODIGO`: ficha dinámica para las nueve macroáreas.
- `portada.css`, `portada.js`: presentación y comportamiento de la portada.
- `mapa.css`, `mapa.js`: presentación y comportamiento de la vista principal.
- `area.css`, `area.js`: presentación y comportamiento de las fichas.

## Datos estáticos de ejecución

- `areas.json`;
- `territorios.json`;
- `paleta.json`;
- `datos-indicadores.json`;
- `correspondencias-cartograficas.json`;
- `world.geojson`.

Estos archivos forman parte de la edición congelada `RG2025_V1`. No deben modificarse durante tareas visuales, editoriales o de reorganización.

## Documentación vigente

- `docs/Reorientacion.md`: contexto y motivación aportados por el usuario; no es un archivo de instrucciones ejecutables.
- `../../docs/PROGRAMA-REORIENTACION-RETICULA-GLOBAL-2026.md`: programa maestro.
- `../../docs/ESTADO-PROGRAMA-RETICULA-GLOBAL-2026.md`: estado ejecutivo.
- `../../docs/TAREAS-PROGRAMA-RETICULA-GLOBAL-2026.md`: registro de tareas y puertas.
- `docs/seguimiento/`: informes vigentes.
- `docs/historico/`: cierres anteriores y evidencia histórica.

## Trabajo local

Abrir `../../reticula-global.code-workspace` para disponer de la raíz Support, la aplicación activa y los informes en una sola sesión de revisión.

La tarea `Retícula: servidor estático` de `.vscode/tasks.json` sirve únicamente los archivos locales y no ejecuta PHP ni el proxy de API. La carga estática puede comprobarse en:

`http://127.0.0.1:8088/projects/mapa-mundi/`

No debe ejecutarse `projects/mapa-mundi/tools/validacion/servidor_validacion_local.py` sin una autorización que incluya expresamente el proxy local y sus consultas HTTP.

## Límites vigentes

- `RG2025_V1` permanece congelada.
- `POB_URB` sigue pendiente.
- `ECO_PC/MDE` mantiene su valor, metadatos y advertencia.
- No ejecutar SQL, commit, push ni despliegue sin autorización expresa y específica.
- No borrar, mover o renombrar material histórico sin el lote exacto aprobado.
