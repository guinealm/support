# Cierre del lote G1 — generadores y fuente cartográfica

**Fecha:** 11 de septiembre de 2026
**Autorización:** mover los tres generadores y sus fuentes cartográficas, actualizar rutas y no ejecutar scripts ni modificar datos

## Resultado

- Los tres generadores están en `projects/mapa-mundi/tools/generacion/`.
- Natural Earth está en `projects/mapa-mundi/tools/generacion/fuentes/natural-earth-source/`.
- Las salidas apuntan a la raíz de la aplicación activa.
- El CSV territorial y los tres agregados congelados se conservan en el archivo histórico y se referencian desde allí, ya que otros procesos documentados dependen de ellos.

## Validación

- sintaxis Python compilada en memoria para los tres archivos;
- existencia comprobada para el CSV maestro, los tres agregados, el Shapefile y `areas.json`;
- rutas de salida comprobadas estáticamente;
- los cuatro archivos públicos principales conservaron su contenido y no aparecen modificados en Git.

## Exclusiones respetadas

No se ejecutaron generadores, no se modificaron JSON, GeoJSON, CSV, indicadores o metodología y no se ejecutaron SQL, base de datos, API, commit, push ni despliegue.

Las copias históricas de JSON/GeoJSON no se retiraron: esa eliminación no estaba incluida en la autorización recibida. H1 conserva una puerta independiente.
