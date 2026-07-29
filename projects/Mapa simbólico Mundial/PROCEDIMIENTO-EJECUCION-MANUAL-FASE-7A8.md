# Procedimiento de ejecución manual — Fase 7A.8

No ejecutar desde Codex. El operador debe copiar cada bloque en phpMyAdmin y guardar sus resultados.

1. **Bloque 1:** `30_7a8_preflight_inmediato.sql`. Debe confirmar POB_URB ausente, cinco indicadores, tres fuentes, periodo, nueve áreas, 45 filas activas, fila 95 activa y cero duplicidades.
2. **Bloque 2:** `31_7a8_respaldo.sql`. `respaldo_filas` debe ser exactamente 45; cualquier otro número bloquea.
3. **Bloque 3:** `32_7a8_carga_sin_commit.sql`, incorporando únicamente el DML de `29_carga...7a7.sql`; no copiar DDL ni COMMIT.
4. **Bloque 4:** `33_7a8_validacion_precommit.sql`. Debe resultar 9/9/9/9/9/8, total 53, `ECO_PC/MDE=0`, sin duplicidades, nulos ni ceros.
5. **Bloque 5:** si todo coincide, ejecutar `34_7a8_commit.sql`; si algo difiere, `35_7a8_rollback.sql`. No decidir ante advertencias ambiguas.
6. **Bloque 6:** tras COMMIT, `36_7a8_validacion_postcommit.sql`; debe confirmar 53 activos, 9 POB_URB, ECO_PC/MDE inactivo y respaldo con 45 filas.
7. **Bloque 7:** usar `95_reversion_indicadores_complementarios_7a7.sql` solo para restaurar; detenerse antes de confirmar.

MySQL no ha sido modificado. Ningún archivo SQL fue ejecutado.
