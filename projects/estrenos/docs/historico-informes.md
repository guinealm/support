# Archivo semanal — 18/10/2026

Fase: selector local de informes. Alcance: Estrenos; sin API, SQL, datos de origen, automatizaciones ni publicación.

Se incorpora un desplegable nativo en la fecha del informe, con enlaces a cuatro instantáneas completas. Funciona sin JavaScript y usa las mismas claves de marcas Vista. El viernes es la fecha de referencia de la semana; se mantienen las fechas de consulta originales, algunas de sábado.

Fuente de lectura: seguimiento-estrenos de la tarea original, en `.codex/visualizations/2026/09/14/01a09f8c-7cc3-7f70-a97d-95ddb3c3b057`. No se importan los archivos de estado ni los párrafos operativos de correo.

| Viernes | Registros | Seleccionados |
|---|---:|---:|
| 25/09/2026 | 72 | 12 |
| 02/10/2026 | 77 | 3 |
| 09/10/2026 | 98 | 8 |
| 16/10/2026 | 127 | 9 |

Validación local completada: comparación de todas las celdas de las tablas con el Markdown original, recuentos, enlaces a las cuatro semanas, una única semana activa por página y ausencia de destinatarios e identificadores Gmail. index.html coincide con el informe del 16/10 incluso tras regenerar el del 02/10.

Limitaciones: la política del navegador integrado bloqueó la vista previa mediante file://; pendiente comprobación visual y manual de teclado, móvil y marcas Vista. Una prueba adicional en directorio temporal no pudo ejecutarse por permisos del entorno. No está disponible en este checkout el documento docs/MIGRACION-CODEX-RETICULA-GLOBAL.md; no se intervino en Retícula Global.

Archivos: index.html, los cuatro informe-YYYY-MM-DD.html, assets/estrenos.css, tools/generar.py, README.md y este documento. No se modificó assets/estrenos.js. No se ejecutaron SQL, API, proxy, commit, push ni despliegue.
