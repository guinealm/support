# Fase 8B — Prototipo separado de portada

**Estado:** prototipo funcional, pendiente de revisión visual del usuario  
**Aplicación activa:** sin sustituir  
**URL local de prototipo:** `http://127.0.0.1:8089/projects/mapa-mundi/portada-prototipo.html`

> Integrada mediante el lote W1 el 2 de septiembre de 2026. La portada ocupa ahora `index.html` y el explorador se conserva en `explorar.html`.

## Objetivo

Materializar la dirección de 8A en una ruta independiente y reversible antes de renombrar o mover la entrada actual.

## Archivos creados

- `projects/mapa-mundi/portada-prototipo.html`;
- `projects/mapa-mundi/portada-prototipo.css`;
- `projects/mapa-mundi/portada-prototipo.js`.

## Resultado

- portada editorial con título, explicación y llamada al explorador;
- mapa Equal Earth construido desde `world.geojson` y `paleta.json` existentes;
- nueve enlaces de macroárea generados desde `areas.json`;
- acceso directo a las fichas dinámicas;
- segunda llamada hacia comparación y metodología del explorador;
- respuesta adaptable a escritorio y móvil;
- foco visible y contenido esencial independiente del puntero;
- tratamiento de error si los recursos del mapa no cargan.

## Límites aplicados

- no se modificó `index.html`, el explorador actual;
- no se modificaron JSON, GeoJSON, indicadores ni metodología;
- no se consultó la API ni se ejecutó el proxy;
- no se añadieron frameworks, paquetes, gráficos ni iconografía humana;
- no se ejecutaron SQL, commit, push ni despliegue.

## Evidencia técnica

- sintaxis de `portada-prototipo.js` validada con el runtime Node incluido en Codex;
- nueve códigos leídos de `areas.json`: `AFR`, `APC`, `CHN`, `EUR`, `MDE`, `NAC`, `RUE`, `SAI`, `SAM`;
- HTML, CSS, JavaScript, `areas.json`, `paleta.json` y `world.geojson` respondieron HTTP 200;
- el navegador solicitado por Codex cargó la página y pidió los seis recursos esperados;
- `git diff --check` sin errores.

## Pendientes antes de integrar

1. revisión visual del usuario;
2. autorización para renombrar el explorador a `explorar.html` y convertir la portada en `index.html`;
3. actualización de enlaces de retorno desde fichas;
4. control local esencial después de la integración.

## Criterio de cierre

El prototipo es reconocible, carga por HTTP y conserva intacta la aplicación vigente. La integración pertenece al lote W1 y no está autorizada todavía.
