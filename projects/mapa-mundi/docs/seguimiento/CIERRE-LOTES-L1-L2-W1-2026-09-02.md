# Cierre de lotes L1, L2 y W1

**Fecha:** 2 de septiembre de 2026  
**Fase:** reorganización e integración local  
**Autorización:** L1, L2 y W1 con el alcance documentado

**Conformidad del usuario:** otorgada el 2 de septiembre de 2026 tras la revisión local.

## Resultado

- L1: retirados los dos residuos históricos aprobados y la caché Python. Espacio recuperado aproximado: 4,73 MB.
- L2: informes vigentes reubicados en `docs/seguimiento/`, cierres anteriores en `docs/historico/` y la herramienta local en `tools/validacion/`.
- W1: `index.html` es la portada didáctica, `explorar.html` conserva el mapa y la comparación, y `area.html` vuelve al explorador.

## Rutas retiradas en L1

- `projects/Mapa simbólico Mundial/ne_10m_admin_0_countries.zip`;
- `projects/Mapa simbólico Mundial/Mapa simbólico v1.html.txt`;
- `projects/reticula-global/__pycache__/`.

Los tres elementos estaban versionados y son recuperables desde el historial Git. No se hizo commit.

## Rutas funcionales después de W1

- Portada: `projects/mapa-mundi/index.html`;
- Explorador: `projects/mapa-mundi/explorar.html`;
- Fichas: `projects/mapa-mundi/area.html?codigo=AFR` (y los otros ocho códigos válidos);
- estilos y lógica de portada: `portada.css` y `portada.js`;
- estilos y lógica del explorador: `mapa.css` y `mapa.js`.

## Exclusiones respetadas

No se modificaron la API, PHP, SQL, bases de datos, metodología, indicadores ni JSON de datos. No se realizó commit, push ni despliegue. Los lotes A1, G1 y H1 siguen fuera del alcance ejecutado.

## Criterio de cierre

El lote queda cerrado cuando las tres vistas principales y sus recursos responden por HTTP local, los JavaScript superan la comprobación de sintaxis, los JSON cargan correctamente y la navegación portada → explorador → ficha → explorador no contiene destinos ausentes.

## Evidencia de validación

- `portada.js`, `mapa.js` y `area.js`: sintaxis válida con Node.
- Todos los JSON de la raíz de la aplicación: parseo correcto.
- Portada, explorador, ficha AFR, CSS, JavaScript, `areas.json` y `world.geojson`: HTTP 200 en servidor estático local.
- URL probada: `http://127.0.0.1:8089/projects/mapa-mundi/`.
