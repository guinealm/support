# Maestro territorial de Retícula Global 2025 — Fase 1C.1

## Estado

Se ha generado el maestro completo y su versión operativa.

## Regla aplicada

- Europa: M49 Europe menos Rusia y Bielorrusia, más Chipre.
- Norteamérica y Caribe: Northern America, Central America y Caribbean.
- Sudamérica: South America.
- Rusia-Eurasia: Rusia, Bielorrusia, Asia Central y Cáucaso.
- China: China, Hong Kong y Macao.
- Subcontinente indio: Southern Asia menos Irán.
- Oriente Medio: Western Asia menos Cáucaso y Chipre, más Irán.
- Asia-Pacífico: resto de Asia oriental y sudoriental más Oceanía; Taiwán como entidad estadística.
- África: M49 Africa.
- Antártida: sin área estadística.

## Archivos

- `rg_paises_areas.csv`: maestro completo.
- `rg_paises_areas_operativo.csv`: entidades utilizables en la primera carga, incluidos casos `SEGUN_FUENTE`.
- `excepciones-territoriales-reticula-global.md`: decisiones especiales.
- `informe-validacion-maestro-territorial.md`: controles y recuentos.

## Decisión

**GO condicionado para cerrar 1C.1.**

La estructura y asignación están completas. Antes de importar en MySQL conviene una revisión manual de:

- nombres visibles en español;
- territorios dependientes y Estado soberano asociado;
- Kosovo;
- cobertura concreta de China, Hong Kong, Macao y Taiwán en cada fuente.
