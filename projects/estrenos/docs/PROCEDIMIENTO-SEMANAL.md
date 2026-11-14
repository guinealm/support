# Procedimiento semanal vigente — 14/11/2026

Por instrucción de Luis, cada revisión consta de cinco pasos:

1. Valorar los estrenos en FilmAffinity con los criterios vigentes y guardar el informe, las evidencias y la cobertura real.
2. Enviar el resultado por correo una sola vez, con comprobación de duplicados y confirmación persistida.
3. Entregar los archivos directamente en `C:/jumalenin-ecosistema/sites/support/projects/estrenos`: fuente Markdown en `docs/`, página semanal, portada, selectores históricos y catálogo acumulado. Usar `tools/generar.py`; conservar los estilos y JavaScript existentes salvo necesidad concreta. Un informe fuera del repositorio o un ZIP no sustituye esta entrega.
4. Validar y dejar los cambios locales revisables en VSCode, sin commit. Comprobar estado y diff desde `C:/jumalenin-ecosistema/sites/support`, preservar cambios ajenos y registrar archivos, pruebas y limitaciones en `docs/ENTREGA-YYYY-MM-DD.md`.
5. Avisar en el cierre: «Abre estrenos.code-workspace en VSCode, revisa las fuentes y tramita su paso a GitHub y Hostinger». Enlazar el workspace y resumir qué está preparado. No afirmar entrega completa si faltan archivos o validaciones.

La automatización existente conserva el viernes a las 09:00, Europe/Madrid. No se crea otra ni se añaden reintentos de fin de semana. Si informe y correo ya están terminados, continuar solo los pasos locales pendientes, sin repetir consultas ni envíos. La publicación manual no bloquea la revisión siguiente.

## Validación y cierre

Comparar filas, seleccionados y cobertura con el Markdown. Ejecutar `python tools/validar_recomendados.py` y `node tools/validar_vistas.cjs`, comprobar enlaces locales y fecha de portada y revisar el diff. Comprobar en navegador local cuando esté disponible, indicando si solo se hicieron verificaciones estructurales o simuladas.

Los pendientes sin ID de ficha conservan su enlace de origen y no tienen marca Vista hasta disponer de identidad verificada. No inventar IDs. Las seleccionadas con advertencias siguen siendo seleccionadas.

GitHub y Hostinger corresponden al usuario. Sin SQL, API, commit, push ni despliegue por el asistente. El historial operativo y los correos privados no se incorporan a la web ni al repositorio. El aviso final no requiere un segundo correo.
