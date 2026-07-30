# Fase 7C — Perfil medio en las fichas de macroárea

## Objetivo

Conectar las tarjetas del perfil de la página principal con la plantilla única de fichas y mostrar en cada ficha el mismo resumen demográfico.

## Archivos modificados

- `projects/mapa-mundi/mapa.js`
- `projects/mapa-mundi/mapa.css`
- `projects/mapa-mundi/area.html`
- `projects/mapa-mundi/area.js`
- `projects/mapa-mundi/area.css`

## Implementación

Cada tarjeta enlaza mediante el nombre y un enlace visible «Ver ficha» a `area.html?codigo=...`. La tarjeta completa no es un enlace, por lo que `<details>` conserva su interacción.

Las fichas muestran `TERR_DENS`, `POB_EDAD`, `HUM_EV`, `ECO_PC` y `HUM_IDH`, reutilizando el mapa de registros que ya devuelve la consulta de área. `POB_URB` permanece como «Pendiente de incorporación». Los valores ausentes se presentan como «Dato no disponible».

Para `ECO_PC/MDE` se detecta el código del área o `estado_dato === 'LIMITACION'` y se muestra la advertencia de comparabilidad limitada. Fuente, año, cobertura, estado y observación se conservan en un `<details>`.

## Pruebas

- Revisión estática de las nueve rutas `area.html?codigo=...`: correcta.
- `git diff --check`: sin errores.
- Se confirmó que la ficha reutiliza los registros completos de su consulta por área y conserva metadatos.
- Se confirmó la salida alternativa «Dato no disponible» y la ausencia de ceros inventados.
- No fue posible realizar pruebas visuales: la conexión con el navegador integrado no estaba disponible.

## Resultado

**GO CON OBSERVACIONES** técnico. Queda pendiente la validación visual en escritorio y móvil antes de crear el commit.
