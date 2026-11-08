# Estrenos: diagnóstico del atasco y procedimiento de recuperación

Fecha de redacción: 08/11/2026. Incidente: revisión de la semana del 06/11/2026.
Horas de este documento: Europe/Madrid.

## Leer primero si la revisión vuelve a atascarse

**No equiparar un error de la herramienta de consulta con una caída de FilmAffinity.
No cerrar un turno diciendo «sigue pendiente» si existe una vía de consulta que ya
funciona y trabajo autorizado que se puede continuar.**

1. Consultar el viernes de referencia, el estado persistente y las entregas de ese
   periodo. Si ya se publicó el informe, no volver a investigar ni enviar otro.
2. Si hay un comando en ejecución, esperar su resultado mediante la herramienta
   correspondiente. «En ejecución» o una espera agotada no equivalen a fallo.
3. Ante un 503 de consulta web, registrar URL, herramienta y error. Hacer como máximo
   un reintento idéntico en esa ejecución; después comprobar la misma URL en el
   navegador disponible. Este límite es una regla de diagnóstico por ejecución,
   no una modificación del calendario autorizado.
4. Si el navegador carga los datos, continuar allí el inventario y las fichas.
   Si la pestaña anterior no existe, obtener una pestaña válida conforme a la
   documentación de la herramienta, en lugar de volver a la vía que ya falló.
5. Guardar avances por lotes pequeños y continuar con el siguiente título pendiente.
   No reiniciar el inventario ni gastar toda la ejecución comprobando el mismo fallo.
6. Separar las fases: investigación, informe, generación local, correo y publicación
   manual. Una publicación manual pendiente no bloquea las otras fases.
7. Si quedan datos imposibles de verificar, entregar el informe parcial autorizado
   con cobertura y pendientes explícitos. No anunciar revisión completa.
8. Guardar el correo preparado, comprobar duplicados, enviar una vez y registrar
   el ID confirmado. Ante respuesta ambigua, buscar en Enviados antes de repetir.

Las instrucciones más recientes del usuario prevalecen. Este documento no cambia
la automatización ni autoriza nuevas consultas sobre una semana ya entregada.

## Alcance de esta investigación

Objetivo: explicar por qué se atascó la entrega y dejar un procedimiento reutilizable.
Fuentes: lectura de los dos chats implicados, comandos registrados, nota provisional,
historial operativo, informe final y código del generador local.
Rutas modificadas por esta investigación: este documento, su referencia en README.md
y una instrucción de lectura en AGENTS.md de estrenos.
Exclusiones: nuevas consultas de películas, correos, cambios de automatización,
datos del informe, API, SQL, commits, push, despliegues y otros proyectos.
Cierre: diagnóstico con evidencias y límites, procedimiento accesible y referencias
locales comprobadas. No se abre otra fase de trabajo.

## Qué pasó realmente

El fallo inicial de acceso se convirtió en un atasco de ejecución. Se repitieron
consultas que fallaban, se generalizó demasiado su diagnóstico y no se mantuvo el
trabajo hasta producir la entrega cuando el navegador ya había dado acceso.
Son errores de actuación del asistente; no exigían que Luis arreglara FilmAffinity
ni publicara previamente el código.

| Hallazgo | Evidencia | Grado de certeza e implicación |
|---|---|---|
| Se cerró una ejecución considerando inaccesible el historial, aunque el comando acabó bien. | El turno del 06/11 a las 21:03:56 dijo que el historial seguía sin responder. En ese mismo turno consta Get-Content terminado con exitCode 0 en 33.514 ms y ultima_revision=2026-10-30. | Hecho comprobado. La explicación probable es que no se incorporó el resultado tardío antes del cierre; no se ha demostrado un fallo del archivo. |
| El sábado el historial ya era legible. | El 07/11 a las 22:24:21, el comando devolvió el mismo estado correctamente en 5.620 ms. El cierre informó de errores de consulta en dos plataformas, sin informe ni correo. | Hecho comprobado. El bloqueo de lectura local ya no justificaba detener el trabajo. Los resúmenes recuperados no incluyen toda la respuesta HTTP original del sábado. |
| La consulta web y la consulta por navegador dieron resultados distintos. | El domingo a las 07:15 se repitió el acceso web a Netflix con resultado comunicado como 503. A las 07:17:55 se abrió Netflix por navegador y se leyeron títulos y fechas; a las 07:24 se confirmaron las cuatro plataformas. | Hecho comprobado de acceso por vías diferentes. No demuestra cuál fue el componente que originó el 503. |
| Una pestaña que dejó de existir se trató como bloqueo del trabajo. | El turno del 08/11 a las 07:19:37 contiene una llamada de navegador fallida, vuelta a la consulta web y cierre indicando que la pestaña previa ya no estaba disponible. | Hecho comprobado. Recuperar una pestaña válida era un paso operativo pendiente, no prueba de caída del sitio. |
| Hubo ejecuciones sin continuación efectiva después de recuperar el acceso. | A las 07:24 las cuatro listas estaban accesibles. A las 07:26:23 se respondió «sigo con la comprobación» sin herramientas. Los disparos de las 07:37 y 07:45 terminaron «sin cambios» sin llamadas de trabajo; el de las 07:38 solo leyó/actualizó la nota. | Hecho comprobado en los turnos consultados. Se confundió no notificar con no continuar el trabajo autorizado. |
| La frecuencia de cinco minutos no aseguró progreso. | Los mensajes de recuperación repetidos coexistieron con inventarios ya accesibles y un informe sin preparar. | Factor operativo comprobado. No hay medición que permita atribuir un número exacto de tokens desperdiciados. |
| No se había preparado la entrega, por lo que no había correo ni web nueva. | La nota provisional decía expresamente «Correo no preparado ni enviado». El último intento sí generó el informe, HTML y paquete, y Gmail confirmó un ID. | Hecho comprobado. No hay evidencia en los registros examinados de que un fallo de Gmail causara el atasco anterior. |

La afirmación anterior de la nota provisional, «los 503 eran un fallo de la herramienta
web, no de FilmAffinity», es demasiado concluyente. La formulación acreditada es:
**la vía de consulta web fallaba mientras el navegador sí permitía leer FilmAffinity**.
Un intermediario, la ruta de acceso, una respuesta selectiva del origen o un problema
temporal son hipótesis posibles; no se han confirmado mediante cabeceras o trazas.

## Cronología mínima comprobada

- **06/11, 21:03:** cierre prematuro sobre el historial; el comando asociado terminó
  correctamente después de unos 33,5 segundos.
- **07/11, 22:24:** historial leído correctamente; se notificaron errores al consultar
  dos plataformas. Informe del 06/11 todavía pendiente.
- **08/11, 07:17–07:24:** acceso directo por navegador confirmado, primero Netflix
  y luego las cuatro plataformas. Se guardó el inventario provisional.
- **08/11, 07:26–07:45:** varios cierres sin completar las fichas ni producir entrega;
  algunos turnos no realizaron llamadas de trabajo.
- **08/11, 07:48:** consta una candidata verificada, Un amor posible, pero aún sin
  informe semanal. Una candidata no equivalía a la entrega solicitada.
- **08/11, ejecución iniciada a las 19:12:52:** el último intento dominical continuó
  las consultas por navegador, guardó resultados, generó el informe y los archivos,
  y envió el correo confirmado. Las 19:12:52 son el inicio del turno, no la hora de envío.

Resultado de esa entrega: 58 fichas del periodo abiertas, 7 seleccionadas, 21 no
cumplen y 30 pendientes. Quedaron 107 pendientes antiguos sin nueva consulta; por eso
el resultado se declaró parcial. La recuperación técnica no acredita cobertura total.

## Qué cambió en el intento que sí produjo una entrega

1. Se continuó en el navegador que ya funcionaba, en lugar de depender de la consulta
   web que estaba dando errores.
2. Se leyeron las fichas por lotes, extrayendo campos concretos del DOM visible:
   nota, votos, leyenda profesional completa y bloques de disponibilidad.
3. Se comprobó la carga antes de interpretar valores vacíos. En una ocasión la
   espera de carga venció, pero la página sí tenía contenido legible después.
4. Se contrastó el inventario con las fechas de corte. Se excluyeron dos entradas
   del 07/11 y la revisión final de cine encontró Isla indómita, que faltaba en la
   lista provisional. Se pasó de 57 a 58 títulos.
5. Se guardaron informe, evidencia y estado; se generó HTML con el generador existente.
6. Se resolvió el permiso de escritura del historial original, que estaba fuera de
   las raíces escribibles de esa sesión. La autorización del encargo no ampliaba
   por sí sola los permisos del sistema de archivos.
7. Se buscó el asunto semanal en Enviados, se guardó el cuerpo preparado y se envió
   una vez mediante Gmail. Después se registró la confirmación y se validó el ZIP.

## Distinguir los fallos antes de actuar

| Síntoma | Comprobación concreta | Acción |
|---|---|---|
| Comando devuelve sesión o ejecución pendiente | Consultar su resultado con el identificador recibido | Esperar de forma acotada; no anunciar fallo antes del resultado |
| 503 en la herramienta web | Misma URL en navegador disponible | Si carga, continuar allí; documentar fallo de vía, no caída general |
| Pestaña no encontrada | Inventario actual de pestañas y documentación de recuperación | Obtener o crear una pestaña válida; no reutilizar indefinidamente un identificador caducado |
| Espera de carga agotada | Encabezado y contenido actual de la página | Leer lo que realmente está cargado; no declarar inexistentes los datos |
| Selector devuelve cero elementos | Árbol accesible o DOM visible de esa página | Ajustar el selector a esa estructura; cine y plataformas no tienen por qué compartirla |
| Nota o leyenda profesional vacía | Ficha cargada y sección correspondiente | Mantener NC y pendiente si no hay dato verificable; no sustituir por cero |
| Proveedores mezclados | Cada bloque Suscripción, Alquiler y Compra | Leerlos por separado; comprobar plan independiente de Movistar |
| Historial legible, escritura denegada | Raíces escribibles y ruta canónica | Preparar localmente y pedir la elevación concreta si el entorno la exige; no enviar hasta persistir |
| Gmail responde ambiguamente | Enviados por asunto y destinatario | Resolver si ya salió antes de volver a enviar |
| Inventario accesible pero trabajo sin terminar | Siguiente ficha pendiente y avances persistidos | Continuar el trabajo, aunque no corresponda notificar al usuario |

Las estructuras observadas en noviembre de 2026 pueden cambiar. Los selectores
usados (`#movie-rat-avg`, `#movie-count-rat [itemprop="ratingCount"]`, la leyenda
`.pro-reviews-chart` y los bloques de `#stream-wrapper`) son referencias de aquella
lectura, no un contrato del sitio. Comprobarlos en el DOM actual antes de usarlos.
El selector `.col[data-movie-id]` utilizado en plataformas devolvió cero en la página
de cine durante la recuperación: el contenido sí estaba presente en otra estructura.

Estos problemas de carga y selectores se observaron al recuperar el domingo.
No se presentan como causas demostradas del fallo inicial del sábado.

## Evitar repetir el gasto sin resultado

- Leer solo periodo, entrega y pendientes del estado; evitar volcar todo el historial
  en cada ejecución. En el incidente hubo lecturas masivas con salida truncada.
- Obtener campos o fragmentos relevantes de las páginas; evitar árboles completos
  con publicidad cuando una lectura dirigida responde a la siguiente comprobación.
- Registrar por lote: IDs consultados, fuente, fecha, cifras verificadas, lo que falta
  y siguiente acción. Conservar los valores anteriores y su fecha si la nueva consulta falla.
- No reintentar el mismo error sin cambiar la hipótesis o incorporar evidencia nueva.
- DONT_NOTIFY decide si se avisa al usuario; no significa abandonar la revisión.
- No decir «sigo trabajando» al cerrar un turno sin haber continuado ni disponer de
  una ejecución real en curso. Expresar con precisión el estado que queda guardado.
- No cambiar de nuevo la periodicidad a partir de este documento. Cualquier cambio
  debe seguir la autorización vigente y utilizar la herramienta de automatizaciones.
- Un informe parcial entregado y un correo confirmado son estados distintos de una
  investigación exhaustiva. Mantener esa diferencia en el historial y en el mensaje.
- No volver a ejecutar `cerrar_revision.py` como reparación genérica: fue un script
  de cierre específico del 06/11, con datos y controles propios de ese periodo.

## Evidencias y referencias para consultar

1. Chat «Diseña sistema de estrenos», ID `01a09f8c-7cc3-7f70-a97d-95ddb3c3b057`.
   Turnos `01a1b275-f10d-7da0-adb5-83fed605f5a9` (06/11) y
   `01a1b7e5-e3ea-7e52-8a0b-95c640eb2685` (07/11), recuperados con read_thread.
2. Chat «Configura revisión semanal de estrenos», ID
   `01a1b9bf-4bfd-7212-a382-78504c558891`. Turnos de las 07:17, 07:19, 07:24,
   posteriores disparos y último intento del 08/11, recuperados con read_thread.
3. [Nota provisional de recuperación](C:/Users/guine/.codex/visualizations/2026/11/08/01a1b9bf-4bfd-7212-a382-78504c558891/recuperacion-2026-11-06.md).
   Es una instantánea anterior al cierre; no usarla como estado actual ni aceptar
   su atribución del 503 como diagnóstico de causa raíz.
4. [Historial operativo canónico](C:/Users/guine/.codex/visualizations/2026/09/14/01a09f8c-7cc3-7f70-a97d-95ddb3c3b057/seguimiento-estrenos/estado.json).
   El periodo 06/11 consta con envío confirmado. No reenviarlo al consultar esta guía.
5. [Informe recuperado](informe-2026-11-06.md),
   [cifras conservadas](evidencia-2026-11-06.tsv) y
   [generador local](../tools/generar.py). El generador convierte Markdown en HTML:
   no hace consultas HTTP, no envía correo y no explica por sí mismo un error 503.
6. [OpenAI: Troubleshooting](https://learn.chatgpt.com/docs/reference/troubleshooting),
   consultado el 08/11/2026. Referencia general sobre estados atascados, comprobación
   de aprobaciones y registros de sesión; no diagnostica este incidente concreto.

No se dispone en esta investigación de una traza HTTP completa de la petición fallida
del sábado ni de métricas de tokens por ejecución. No se puede concluir que hubiera
una caída global de FilmAffinity, un bloqueo antibot, una avería de Gmail, una query
mal formada o una regresión de una versión concreta de Codex.

## Validación del documento

Diagnóstico contrastado con comandos y cierres de ambos chats, nota provisional,
estado persistido y resultado de la recuperación. Referencias locales verificadas.
Sin cambios en informes, cifras, generador, calendario o envíos. Sin SQL, commits,
push ni despliegues.
