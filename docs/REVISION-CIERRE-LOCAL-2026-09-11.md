# Revisión de cierre local — Retícula Global 2025

## Integración final en el repositorio principal

Las correcciones documental y PHP se integran en `C:/jumalenin-ecosistema/sites/support` junto con este informe y el inventario. La integración comprueba previamente que los dos archivos de destino mantienen el contenido revisado y que los entregables no existen, para preservar otros cambios del usuario. No se modifica ninguna otra ruta.

El inventario adjunto pasa a ser la lista final de **281 rutas**: ocho modificaciones, 258 bajas y 15 archivos nuevos, sin preparar el índice. Incluye ahora el PHP corregido y los dos entregables. Esta sección sustituye las referencias posteriores a integración pendiente y al inventario original de 278 rutas.

Validación de cierre: correspondencia de los cuatro archivos integrados con este worktree y `git diff --check` del repositorio principal. Las limitaciones de lint PHP y validación dinámica permanecen. La integración local no autoriza commit, push ni despliegue.

## Estado vigente tras autorización del fallback PHP

El usuario autorizó expresamente modificar únicamente el fallback de `api/reticula/v1/bootstrap.php`, sin ejecutar API ni SQL. Se cambió `dirname(__DIR__, 2)` por `dirname(__DIR__)` en este worktree: la alternativa local ahora resuelve a `api/reticula/config/reticula-db.local.php`, conforme al README y a la plantilla. Las ramas de configuración externa y privada no se modificaron.

Las incidencias P2 y P3 quedan corregidas en este worktree, pendientes de integración en el repositorio principal. Validación: diff PHP limitado a una línea, comprobación estática de la ruta y `git diff --check` sin errores. PHP sigue sin estar disponible en PATH, por lo que `php -l` queda pendiente; no se instaló PHP ni se ejecutó la API o ninguna conexión a base de datos.

La propuesta actual comprende las 278 rutas del inventario original, más `api/reticula/v1/bootstrap.php` y los dos entregables de revisión: **281 rutas** en total. El inventario original conserva la fotografía del repositorio principal; esta adición identifica exactamente la única ruta nueva de código. El documento de estado ya figuraba entre las 278 rutas. Antes de un eventual commit se deben integrar y revisar los cambios de este worktree, y obtener autorización expresa para el alcance completo. No se preparó el índice ni se hizo commit, push o despliegue.

Los apartados siguientes conservan la cronología y los resultados de la revisión anterior; sus pendientes PHP/documentales quedan sustituidos por este estado vigente. Se mantienen las limitaciones de lint PHP, validación dinámica y portabilidad de generación.

## Actualización posterior — corrección documental

Tras la indicación de continuar, se preparó en este worktree la corrección de `docs/ESTADO-PROGRAMA-RETICULA-GLOBAL-2026.md`, tomando como base su contenido pendiente del repositorio principal. La decisión vigente ahora refleja A1, G1 y H1 completados. También se precisó que la lista de operaciones no realizadas corresponde a la actualización documental, para no contradecir los lotes ejecutados.

La incidencia P3 queda corregida en este worktree, pendiente de integración en el repositorio principal. El informe original que sigue conserva la fotografía de la revisión. La incidencia PHP permanece abierta y sin modificaciones. El inventario de 278 rutas no cambia: el documento corregido ya estaba incluido. `git diff --check` se volvió a comprobar tras esta corrección.

Fecha: 11 de septiembre de 2026. Fase: revisión local de cierre / expediente de Fase 8 tras G1 y H1.

## Dictamen

Revisión completada con incidencias. No se otorga un GO incondicional a la versión ni se ejecuta ninguna operación Git de escritura. La propuesta de commit de reorganización queda condicionada a resolver la contradicción documental y a una autorización expresa del usuario que incluya las bajas históricas. El fallo PHP debe resolverse en un alcance API/PHP separado antes de considerar validada la configuración local documentada.

## Alcance y copia examinada

Objetivo: revisar aplicación, cambios pendientes y tareas de VS Code; comprobar sintaxis disponible, rutas y estado Git; entregar inventario exacto para una decisión posterior de commit.

Rutas: `projects/mapa-mundi/`, `api/reticula/`, `docs/`, `.vscode/`, `AGENTS.md` y estado Git completo. Las bajas históricas se inventariaron y contrastaron en lectura para explicar el estado Git, sin reorganizar el archivo.

Repositorio revisado: `C:/jumalenin-ecosistema/sites/support`, rama `main`, HEAD `99417ec51ffe2c3f38477389ba94b614fee7c8f0`. Esta tarea se abrió en `C:/Users/guine/.codex/worktrees/4730/support`, inicialmente limpio y con HEAD separado en el mismo commit. Los cambios pendientes del repositorio principal no están presentes en este worktree. Las lecturas de revisión se hicieron sobre el repositorio principal; estos dos entregables se guardaron únicamente en el worktree de la tarea.

Exclusiones respetadas: no ejecutar generadores, proxy, API, SQL, conexiones a bases de datos, commit, push ni despliegue; no modificar PHP, datos, JSON, GeoJSON, metodología ni indicadores. Criterio de cierre: informe con resultados, límites y propuesta explícitamente condicionada, sin continuar a otra fase.

## Hallazgos

1. **P2 — Fallback de configuración PHP incorrecto.** `api/reticula/v1/bootstrap.php:95` utiliza `dirname(__DIR__, 2)`: desde `api/reticula/v1` resuelve a `api`, por lo que busca `api/config/reticula-db.local.php`. El README y la plantilla indican `api/reticula/config/reticula-db.local.php`. Sin variable `RETICULA_DB_CONFIG` ni configuración privada detectada, seguir el README termina en `CONFIGURATION_ERROR`. La resolución relativa debería subir un nivel, sujeto a autorización específica para modificar PHP. Es un defecto ya presente en HEAD, no introducido por los cambios pendientes. No se ejecutó PHP ni se abrió configuración privada.

2. **P3 — Estado documental contradictorio.** `docs/ESTADO-PROGRAMA-RETICULA-GLOBAL-2026.md:43` conserva «los generadores y fuentes de G1 siguen pendientes», mientras su tabla y los cierres G1/H1 los dan por completados. Corregir esa frase antes de aprobar el expediente como coherente. No se corrigió dentro de esta revisión de solo lectura.

3. **Limitación de portabilidad de generación.** Los tres generadores calculan `HISTORICAL_ROOT` desde `APP_ROOT.parents[3]`. Resuelve correctamente en la topología principal del ecosistema, pero una copia en un worktree de Codex apuntaría a otro directorio bajo `.codex`, sin el archivo externo. No afecta a la aplicación servida; el commit no será un paquete autosuficiente de regeneración. Los scripts no se ejecutaron.

## Evidencia local

- `git diff --check` y `git diff --cached --check`: sin errores; avisos LF → CRLF en siete archivos modificados. Índice sin archivos preparados.
- PHP no disponible mediante `Get-Command php`; no se instaló ni se ejecutó `php -l`. No se afirma que PHP esté ausente de todo el equipo. Queda pendiente lint de los PHP cuando exista un ejecutable disponible.
- `node --check`: correctos `portada.js`, `mapa.js` y `area.js` del repositorio principal.
- AST de los tres generadores Python analizado en memoria, sin importarlos, ejecutarlos ni crear cachés. Diff revisado: reubicación de fuentes, salidas y referencias de procedencia; no cambios en cálculos.
- Los seis JSON/GeoJSON de la raíz de la aplicación se parsean correctamente. `.vscode/tasks.json` también es JSON válido.
- Referencias estáticas `href`/`src` locales de `index.html`, `explorar.html` y `area.html`: ningún archivo de destino ausente. Se mantiene portada → explorador → ficha → explorador; los recursos CSS/JS están presentes.
- API canónica: ambos endpoints incluyen el `bootstrap.php` vecino. No se encontraron dependencias operativas hacia el antiguo directorio histórico en los scripts revisados. No existe `reticula-db.local.php` versionado.
- No hay diff pendiente en API ni en HTML, JavaScript, CSS o datos públicos de la aplicación. Se conserva el cierre histórico GO de 7E; esta revisión no sustituye aquella validación visual. `POB_URB` sigue fuera del cierre y no se altera `ECO_PC/MDE`.
- Tareas VS Code: estado Git, inventario actualizado y servidor estático. Se inspeccionaron sus definiciones; no se ejecutó el servidor.

## Trazabilidad del archivo

Estado observado: **278 entradas pendientes: 7 modificadas, 258 eliminadas y 13 sin seguimiento**, todas fuera del índice.

Las 258 bajas se explican por 242 archivos conservados en `C:/jumalenin-ecosistema/archivo/reticula-global-2025`, siete fuentes Natural Earth trasladadas, tres generadores trasladados y seis copias sustituidas por los canónicos existentes. Ninguna baja quedó sin destino identificado.

De los 242 archivos archivados, 94 coinciden byte a byte con HEAD y 148 coinciden tras normalizar únicamente CRLF/LF; no se detectaron otras diferencias. Las siete fuentes cartográficas y los seis duplicados coinciden byte a byte con sus correspondientes contenidos de HEAD. Los cambios en los tres generadores se revisaron por diff.

El archivo externo contiene 243 archivos: el adicional es `reticula_global_1c2_runner/output_1c2/u794456529_map_sim_Mund.sql`, que no figura en el conjunto histórico versionado. Solo se identificó su nombre; no se inspeccionó su contenido y se excluye de cualquier propuesta de commit. El destino externo no quedará incorporado al historial de Support por registrar las bajas.

## Propuesta exacta para una posterior autorización

Título sugerido: **Consolidar generadores y archivar el histórico de Retícula Global 2025**.

La lista exhaustiva y literal es `docs/REVISION-CIERRE-LOCAL-2026-09-11-INVENTARIO.txt`: sus 278 líneas identifican cada ruta y su estado. ` M` propone incluir la modificación, ` D` registrar la baja y `??` incluir el archivo nuevo. No es una orden de staging ni autoriza ninguna acción.

El eventual alcance de autorización debe nombrar expresamente esas 278 rutas, incluidas las 258 bajas bajo `projects/Mapa simbólico Mundial/`, además de estos dos entregables si se decide integrarlos en el repositorio principal:

- `docs/REVISION-CIERRE-LOCAL-2026-09-11.md`
- `docs/REVISION-CIERRE-LOCAL-2026-09-11-INVENTARIO.txt`

Serían 280 rutas con los entregables. La corrección documental de la incidencia 2 afectaría a una ruta ya inventariada, pero requeriría volver a revisar su diff. La corrección PHP no está incluida en este conjunto; si se autoriza y ejecuta posteriormente, habrá que actualizar el expediente y el inventario antes del commit. No incluir el archivo externo, credenciales, configuración privada ni archivos adicionales mediante una selección global.

## Límites y cierre

No se abrió VS Code ni se inspeccionaron buffers sin guardar; se revisó su configuración persistida y el estado en disco. No hubo validación HTTP ni sesión de navegador: el explorador y las fichas intentan consultar `/__reticula_api__/datos.php` en localhost y las llamadas a API están excluidas. Quedan sin revalidar visualmente teclado, foco, responsive, zoom, movimiento reducido y estados dinámicos. No se comprobó remoto ni producción.

Se crearon solamente este informe y su inventario en el worktree de la tarea. No se modificó el repositorio principal ni se preparó el índice. La revisión solicitada queda cerrada; el commit exige una autorización posterior explícita de operación y alcance. Push y despliegue mantienen autorizaciones independientes.
