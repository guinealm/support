# Fase 7B.2 — Perfil medio de la población

Se incorporó un bloque visible después del mapa y antes de la tabla comparativa en `projects/mapa-mundi/index.html`.

## Implementación

- `mapa.js` reutiliza `indicatorAreas` ya cargado por la aplicación.
- Se muestran nueve tarjetas ordenadas por `area.orden_visual`.
- Indicadores: `TERR_DENS`, `POB_EDAD`, `HUM_EV`, `ECO_PC`, `HUM_IDH`.
- `POB_URB` aparece como «Pendiente de incorporación».
- `ECO_PC/MDE` muestra advertencia de cobertura incompleta y comparabilidad limitada.
- Fuentes, años y observaciones se consultan mediante `<details>`.
- `mapa.css` añade diseño de tres, dos y una columna, sin desplazamiento horizontal.

No se modificaron API, MySQL, SQL ni datos de origen. No se realizaron pruebas visuales con navegador controlable en este entorno.

Corrección posterior: el perfil no podía usar `indicatorAreas`, porque esa colección solo contenía las métricas principales solicitadas por `mapa.js`. Se añadió una única petición general sin parámetro `indicador`, normalizada desde `payload.data`, para obtener expresamente los cinco códigos del perfil. No se añadieron valores al JSON local.

La corrección requiere validación visual en navegador para confirmar nueve registros por indicador y el caso `ECO_PC/MDE`. Resultado técnico provisional: **NO-GO hasta completar esa verificación visual**.

## Validación pública y cierre — Fase 7B.3

- URL pública validada: https://support.jumalenin.com/projects/mapa-mundi/
- Fecha de validación: 30 de julio de 2026.
- Se confirmaron las nueve tarjetas de macroárea.
- Se confirmaron valores para `TERR_DENS`, `POB_EDAD`, `HUM_EV`, `ECO_PC` y `HUM_IDH`.
- `POB_URB` se muestra como «Pendiente de incorporación», sin valor numérico.
- `ECO_PC/MDE` muestra valor, advertencia de cobertura incompleta y comparabilidad limitada, fuente Banco Mundial, año 2024 y observación metodológica desplegable.
- Fuentes, años y observaciones se consultan mediante elementos `<details>`.
- El mapa y la comparación de macroáreas continúan funcionando.
- No se modificaron MySQL, API, SQL ni metodología.
- Commit funcional: `5b1e106` — `Corrige carga del perfil medio de población`.

**GO — Fase 7B cerrada.**
