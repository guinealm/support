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

Resultado técnico: **GO CON OBSERVACIONES**; requiere validación visual de escritorio y móvil.
