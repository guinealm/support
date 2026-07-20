# Retícula Global 2025 — Primera edición de datos

Versión: **RG2025-V1**. Estado documental y MySQL: **congelada**.

## Alcance

La primera edición contiene nueve áreas, 244 países y territorios, ocho bloques, 27 indicadores activos y 243 registros activos de área.

Bloques incluidos: territorio, población, economía, desarrollo humano y desigualdad, capacidad militar, energía y autonomía energética, clima y emisiones, y tecnología, digitalización e innovación.

## Indicadores incluidos

| Bloque | Indicadores |
|---|---|
| TERR | TERR_SUP, TERR_PCT, TERR_DENS |
| POB | POB_TOTAL, POB_PCT, POB_EDAD, POB_2050, POB_VAR_2050 |
| ECO | ECO_PIB, ECO_PIB_PCT, ECO_PC |
| HUM | HUM_IDH, HUM_GINI, HUM_EV |
| MIL | MIL_GASTO, MIL_PCT, MIL_PIB, MIL_PC, MIL_NUC |
| ENE | ENE_CONS, ENE_PC, ENE_DEP, ENE_AUTO, ENE_ELEC_LC |
| CLI | CLI_CO2, CLI_CO2_PC |
| TEC | TEC_NET |

## Indicadores aplazados

- `ENE_FOS`: cobertura comparable insuficiente en cuatro áreas; no creado en MySQL.
- `TEC_ID`: cobertura insuficiente; no creado en MySQL.
- `TEC_PESO`: metodología insuficientemente definida; no creado en MySQL.

## Principios metodológicos

- Se conservan el año y la fuente reales de cada dato nacional.
- Las ausencias permanecen ausentes y nunca se convierten automáticamente en cero.
- Los ceros publicados se conservan únicamente cuando la fuente los proporciona y quedan documentados.
- Las sumas se usan para magnitudes aditivas; los porcentajes y medias se ponderan por población, PIB, consumo, generación u otro denominador metodológicamente apropiado.
- Los agregados de fuente no se cargan como países.
- Las entidades especiales y dependientes conservan su tratamiento territorial explícito.
- Ningún valor extremo se corrige sin revisión de fuente.

## Fuentes principales

ONU WPP, FAOSTAT, Banco Mundial WDI/PIP, PNUD, SIPRI, FAS, Energy Institute, Eurostat, Global Carbon Budget, Our World in Data y UIT. El inventario exacto de fuentes y vínculos se audita mediante `26_rg_comprobacion_integral_1c9.sql`.

## Limitaciones conocidas

- `HUM_GINI` combina últimos años disponibles y presenta dispersión temporal.
- `ENE_DEP` y `ENE_AUTO` son aproximaciones derivadas de balances comparables disponibles.
- `ENE_ELEC_LC` depende de cobertura de generación eléctrica.
- `CLI_CO2` excluye cambio de uso del suelo y emisiones de consumo.
- `TEC_NET` utiliza el último dato oficial disponible; algunas entidades presentan años antiguos.
- La cobertura y el tratamiento de China, Hong Kong, Macao, Taiwán, Rusia, Kosovo, Serbia, Corea del Norte y territorios dependientes requieren conservar las notas de fuente.

## Estado MySQL

El usuario confirmó la ejecución manual y satisfactoria de los SQL 23, 24 y 25: 8 bloques, 27 indicadores, 215 filas nacionales TEC_NET, 9 filas tecnológicas de área y 243 filas activas de área. Codex no ejecutó MySQL.

SQL 26 fue ejecutado manualmente y confirmó los conteos, las nueve filas por indicador, la ausencia de duplicidades, las fuentes vinculadas y los cálculos clave. La estructura real de `rg_periodos` contiene únicamente `id`, `codigo`, `nombre`, `estado` y `activo`; por ello SQL 27 solo puede registrar `estado='congelado'` y `activo=1`. La fecha y las observaciones de cierre permanecen en esta documentación.

Fecha documental de congelación: 20 de julio de 2026.

SQL 27 fue ejecutado manualmente por el usuario. La selección final confirmó `RG2025_V1`, `estado='congelado'` y `activo=1`.

## Reglas para futuras actualizaciones

1. No sobrescribir RG2025-V1: abrir una nueva versión o migración trazable.
2. Conservar fuente, año, unidad, transformación y cobertura.
3. Repetir la auditoría integral antes de publicar cambios.
4. No activar indicadores aplazados sin metodología y cobertura aprobadas.
5. Mantener scripts de reversión y copia de seguridad fuera del repositorio cuando contengan datos privados.
