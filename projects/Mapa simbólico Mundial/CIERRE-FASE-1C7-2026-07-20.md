# Cierre de la Fase 1C.7 — Emisiones y clima

Fecha de cierre: 20 de julio de 2026.

## Decisión

La Fase 1C.7 queda cerrada con **GO** para los indicadores:

- `CLI_CO2`: emisiones territoriales de CO2 de combustibles fósiles e industria;
- `CLI_CO2_PC`: emisiones territoriales de CO2 por habitante.

`CLI_VUL` se aplaza por metodología pendiente. No se incluyen cambio de uso del suelo, emisiones de consumo ni otros gases de efecto invernadero.

## Fuente y tratamiento

- Fuente: Global Carbon Budget 2025, distribuido y procesado por Our World in Data.
- Año de emisiones: 2024.
- `CLI_CO2`: toneladas de CO2.
- `CLI_CO2_PC`: toneladas de CO2 divididas por la población cubierta de 2025.
- No se estimaron ni imputaron ausencias.
- `CXR` conserva `CLI_CO2 = 0`, publicado expresamente por la fuente.
- `CXR` no recibe `CLI_CO2_PC` porque no dispone de población 2025 en el maestro; la ausencia no se convirtió en cero.

## Implantación MySQL

El usuario ejecutó manualmente en phpMyAdmin:

1. `20_rg_catalogo_clima.sql`;
2. `21_rg_datos_clima.sql`;
3. `22_rg_comprobaciones_clima.sql`.

Tras corregir la expectativa de `CLI_CO2_PC` de 214 a 213, el usuario volvió a ejecutar el SQL 22. Todas las comprobaciones finales fueron satisfactorias.

## Resultado validado

- 7 bloques activos.
- 26 indicadores activos.
- 2 indicadores climáticos nuevos.
- 427 registros nacionales climáticos:
  - `CLI_CO2`: 214;
  - `CLI_CO2_PC`: 213.
- 18 registros climáticos de área: 9 por indicador.
- 216 registros de área anteriores conservados.
- 234 registros de área activos totales.
- Cobertura poblacional superior al 99,32 % en las nueve áreas.
- Año 2024 confirmado en todas las filas agregadas.
- Sin emisiones negativas.
- Sin duplicidades.
- Ausencias conservadas como ausencias.

## Límites respetados

- Codex no ejecutó MySQL; la ejecución fue realizada por el usuario.
- No se modificó la web pública.
- La copia local `u794456529_map_sim_Mund.sql` queda excluida de Git.

## Estado para retomar

La Fase 1C.7 está implantada, validada y cerrada formalmente. El siguiente bloque solo debe iniciarse como una fase nueva conforme al plan del proyecto.
