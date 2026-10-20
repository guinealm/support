# Estrenos · Jumalenin
Versión local preparada el 17/10/2026. Informe inicial: 16/10/2026.
Destino: support.jumalenin.com/projects/estrenos/ (pendiente de publicación).

## Contenido y fuentes
El generador convierte el mismo informe Markdown utilizado para el correo en HTML.
Conserva textos, tablas, enlaces, advertencias y cifras, sin consultar ni recalcular FilmAffinity.
Sólo omite el párrafo operativo sobre el envío anterior y su identificador Gmail, que no pertenece al contenido público.
No se publica estado.json: contiene historial operativo y datos del destinatario.
Cada informe es una instantánea semanal, no un catálogo acumulado. El histórico original permanece en la carpeta seguimiento-estrenos. El desplegable «Última versión del informe / Elegir informe» permite abrir las copias HTML semanales, también sin JavaScript.
El archivo local incluye los viernes 25/09, 02/10, 09/10 y 16/10/2026; el primero contiene la recuperación del 14 al 25/09. La fecha del selector identifica el viernes de referencia: la fecha efectiva de consulta, cuando es distinta, se conserva dentro del informe.
Desde el 19/10/2026 incluye también el 18/09 como reconstrucción retrospectiva parcial: 39 registros del 14 al 18/09 extraídos sin alterar sus celdas del informe del 25/09 (consulta del 26/09). No es un informe generado el 18/09 ni acredita valoraciones o disponibilidad a esa fecha. Fuente reproducible: docs/informe-2026-09-18.md; 5 seleccionados, 18 no cumplen y 16 pendientes. Se genera con el mismo comando, usando --fecha 2026-09-18.

## Actualización local
Ampliación del 20/10/2026: los informes del 18/09, 25/09, 02/10 y 09/10 incorporan series con el formato y los filtros del 16/10. Las fuentes completas actualizadas están en `docs/informe-YYYY-MM-DD.md`; para regenerar estas cuatro páginas se deben usar esas copias locales. Las películas conservan sus cifras originales. Las series se evalúan retrospectivamente con consulta del 20/10 y balance separado: 10, 20, 8 y 14 registros, respectivamente. El 25/09 conserva su periodo acumulado 14–25/09, por lo que incluye también las series del 18/09. Cobertura parcial; no se presentan las valoraciones como históricas.

Desde esta carpeta:
python tools/generar.py --informe "RUTA/informe-YYYY-MM-DD.md" --fecha YYYY-MM-DD
Validar que el número de filas, seleccionados y matriz coincide con el informe.
La fecha es la del informe comprobado, no la fecha del reloj al abrir la página.
Si falla la investigación, conservar versión anterior o publicar expresamente la cobertura parcial; nunca anunciar una revisión completa.
El generador conserva informe-YYYY-MM-DD.html, actualiza el selector de todos los informes e index.html y no toca las marcas personales. index.html siempre muestra la fecha más reciente, aunque se incorpore después una semana anterior. Cada archivo se sustituye de forma atómica; el conjunto no constituye una transacción. Hay que conservar los HTML históricos al actualizar la carpeta.
También reconoce las cabeceras y estados de selección de los primeros informes, sin recalcular sus valoraciones ni cambiar sus advertencias.

## Marcas Vista
localStorage por origen y navegador, sin cuentas ni servidor.
Clave estable: jumalenin:estrenos:vistas:v1:fa:ID; temporadas identificadas añaden :tN.
Una película repetida en varias plataformas comparte marca; una temporada concreta no comparte la de otra.
Las marcas se conservan aunque el título desaparezca temporalmente del informe.
Vista: seleccionado en letra normal; sin marcar: seleccionado en negrita.
No seleccionados conservan letra normal en ambos casos.
Cambios sincronizados entre filas repetidas y pestañas del mismo origen.
Si no hay almacenamiento, aviso visible y funcionamiento temporal en memoria.
Las marcas de una vista previa local no se trasladan automáticamente al dominio público.
La valoración de temporadas continúa siendo la de la serie completa cuando así lo indique FilmAffinity.

## Diseño y alcance
HTML, CSS y JavaScript sin dependencias. CSS y logo de common mediante las mismas URLs que support/index.html.
assets/estrenos.css sólo aporta estilos locales.
Sin cambios en common, NHMA, API, SQL, Git ni hosting.
La automatización actual y el correo siguen vigentes hasta completar la transición y autorizar la publicación.

## Traslado de la tarea
La tarea existente Diseña sistema de estrenos ya es de tipo Codex y conserva el historial.
El proyecto local Jumalenin/estrenos todavía debe añadirse en la aplicación apuntando a esta carpeta.
Después mover esta misma tarea desde la barra lateral al proyecto, conservando el historial y la automatización existente.
No crear otra automatización ni una segunda tarea que envíe correos duplicados.
El archivo estrenos.code-workspace facilita abrir la carpeta en un editor; no registra por sí solo un proyecto en Codex.

## Paso de correo a web
Tras revisar y autorizar publicación de esta ruta, actualizar la automatización existente:
1. Mantener criterios, horario, recuperación, historial y comprobación de duplicados.
2. Generar index.html con el informe semanal validado.
3. Publicar exclusivamente los archivos de esta página mediante el procedimiento autorizado de Support.
4. Confirmar publicación y sólo entonces registrar entrega web. Si falla, conservar la versión pública anterior y notificar el fallo.
5. Sustituir el correo completo por la web conforme a la decisión del usuario.
No activar este cambio antes de contar con un destino publicado y verificado.
