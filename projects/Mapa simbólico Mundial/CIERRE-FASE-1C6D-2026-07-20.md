# Cierre de la Fase 1C.6D — Primera edición energética

Fecha de cierre: 20 de julio de 2026.

## Decisión

La Fase 1C.6D queda cerrada con **GO**.

La primera edición del bloque energético publica cinco indicadores:

- `ENE_CONS`: consumo de energía primaria;
- `ENE_PC`: consumo de energía primaria por habitante;
- `ENE_DEP`: dependencia energética exterior aproximada;
- `ENE_AUTO`: autosuficiencia energética aproximada;
- `ENE_ELEC_LC`: electricidad baja en carbono.

`ENE_FOS` se aplaza por cobertura insuficiente y falta de fuente complementaria comparable para cuatro áreas. Sus CSV, incidencias y documentación de investigación se conservan, pero el indicador no forma parte del catálogo ni de las cargas MySQL de esta edición.

## Implantación MySQL

El usuario ejecutó, en este orden:

1. `17_rg_catalogo_energia.sql`;
2. `18_rg_datos_energia.sql`;
3. `19_rg_comprobaciones_energia.sql`.

Tras corregir un falso positivo del control de valores cero, el usuario volvió a ejecutar solamente el SQL 19. La validación final fue satisfactoria.

## Resultado validado

- 6 bloques activos.
- 24 indicadores activos.
- 5 indicadores energéticos nuevos.
- 45 registros energéticos de área: 9 por indicador.
- 171 registros de área anteriores conservados.
- 216 registros de área activos totales.
- 888 registros nacionales energéticos:
  - `ENE_CONS`: 209;
  - `ENE_PC`: 209;
  - `ENE_DEP`: 138;
  - `ENE_AUTO`: 138;
  - `ENE_ELEC_LC`: 194.
- `ENE_AUTO = 100 - ENE_DEP` validado en las nueve áreas.
- Sin consumos negativos.
- Sin porcentajes fuera de rango.
- Sin duplicidades.
- 35 ausencias de `ENE_CONS` conservadas como ausencias, nunca como cero.
- Años reales, correspondencias territoriales y conversión EJ/TWh validados.

Los valores publicados `ENE_ELEC_LC = 0` son ceros reales de la fuente y no imputaciones de ausencias.

## Copia de seguridad

Se verificó un volcado SQL posterior a la implantación:

- archivo local: `u794456529_map_sim_Mund.sql`;
- tamaño: 644.721 bytes (629,6 KB);
- contiene cabecera SQL, estructuras `CREATE TABLE`, datos `INSERT INTO`, `rg_datos_area` y `rg_datos_pais`.

El volcado contiene datos de base de datos y no debe incorporarse al repositorio Git.

## Límites respetados

- Codex no ejecutó MySQL; la ejecución fue realizada por el usuario.
- No se modificó la web pública.
- No se inició ni se recuperó la Fase 1C.7.

## Estado para retomar

La Fase 1C.6 está cerrada. La primera edición energética está implantada y validada. Cualquier trabajo futuro sobre `ENE_FOS` debe abrirse como una edición posterior independiente y exigir cobertura comparable suficiente.
