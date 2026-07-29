# Cierre Fase 7A — 2026-07-29

## Decisión

**CIERRE PARCIAL — NO-GO PARA LA AMPLIACIÓN MYSQL.**

## Estado de datos

Los cinco indicadores complementarios actualmente disponibles permanecen estables en `RG2025_V1`, con nueve áreas activas cada uno:

- `TERR_DENS` — densidad de población.
- `POB_EDAD` — edad mediana aproximada.
- `HUM_EV` — esperanza de vida.
- `HUM_IDH` — IDH medio ponderado.
- `ECO_PC` — PIB nominal por habitante.

La urbanización (`POB_URB`) quedó preparada en CSV y documentación, pero no se incorporó a MySQL. No existe actualmente en el catálogo ni tiene filas cargadas.

`ECO_PC/MDE` conserva la limitación existente: fila 95 activa, estado `LIMITACION`, cobertura parcial. No se publicó una sustitución ni se alteró su valor.

## Estado técnico

- MySQL permanece en el estado anterior: 45 filas activas.
- El respaldo versionado de 45 filas sigue siendo válido.
- La carga fallida no modificó MySQL.
- API y web no fueron modificadas por la carga fallida.
- Los archivos `32A_7a8_carga_y_commit.sql` y `32B_7a8_reversion_inmediata.sql` quedan fuera de ejecución.
- No se realizarán más intentos de carga durante esta fase.

Cualquier recuperación futura partirá de los CSV y documentos preparados, no de los SQL `32A/32B`.

## Próximo trabajo

El siguiente trabajo del proyecto será funcional y visible en el navegador, utilizando los datos actualmente disponibles. No se inicia ninguna tarea posterior en este cierre.
