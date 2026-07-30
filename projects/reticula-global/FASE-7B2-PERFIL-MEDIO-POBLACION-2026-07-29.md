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
