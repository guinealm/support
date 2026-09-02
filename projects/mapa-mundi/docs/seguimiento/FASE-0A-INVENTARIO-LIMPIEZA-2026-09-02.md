# Fase 0A — Inventario previo a reorganización y limpieza

**Estado:** preparada, no ejecutada  
**Dedicación:** 6 horas  
**Tipo:** inspección local de solo lectura

## Objetivo concreto

Determinar qué elementos de Retícula Global siguen teniendo una función, cuáles están duplicados y cuáles pueden retirarse sin romper la aplicación, la API o la trazabilidad metodológica.

## Rutas incluidas

- `projects/mapa-mundi/` — aplicación activa;
- `projects/mapa-mundi/docs/` y `projects/mapa-mundi/tools/validacion/` — destinos autorizados de seguimiento y validación;
- `projects/Mapa simbólico Mundial/` — archivo histórico y dependencias heredadas;
- `api/reticula/` — solo inspección de referencias en código;
- documentos de raíz que enlacen esas rutas.

## Exclusiones

- ejecución o modificación de API, PHP, SQL o bases de datos;
- modificación de JSON, GeoJSON, indicadores, datos o metodología;
- movimientos, renombrados y borrados;
- commit, push y despliegue.

## Clasificación obligatoria

Cada elemento relevante recibirá una de estas decisiones:

- `CONSERVAR`: forma parte del producto o de su trazabilidad necesaria;
- `MOVER`: es útil pero está en una ubicación incorrecta;
- `ARCHIVAR`: no está activo, pero merece conservación histórica;
- `BORRAR`: duplicado, temporal o sustituido, sin dependencia viva;
- `REVISAR`: no hay evidencia suficiente para decidir.

## Hallazgo inicial crítico

`api/reticula/v1/datos.php` contiene una dependencia hacia:

`projects/Mapa simbólico Mundial/api/reticula/v1/datos.php`

Por tanto, el directorio histórico no puede borrarse en bloque. Extraer o cambiar esa dependencia sería otra actuación, con autorización específica para modificar PHP/API.

## Entregables

1. inventario tabulado por ruta, tamaño, función y decisión propuesta;
2. mapa de dependencias vivas;
3. lista exacta de candidatos a borrar;
4. lista exacta de movimientos propuestos;
5. estimación de espacio recuperable;
6. orden de ejecución y plan de reversión;
7. solicitud separada de autorización para los borrados y movimientos.

## Evidencia esperada

- búsquedas de referencias locales;
- comparación por nombre, tamaño y, cuando sea necesario, hash;
- identificación de archivos seguidos y no seguidos por Git;
- comprobación de que los candidatos no participan en rutas activas.

## Criterio de cierre

Existe una propuesta exacta y verificable de reorganización, pero todavía no se ha movido ni borrado ningún elemento.
