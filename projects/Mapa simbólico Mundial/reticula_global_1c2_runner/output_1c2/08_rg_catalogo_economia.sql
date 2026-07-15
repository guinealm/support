-- 08_rg_catalogo_economia.sql
SET NAMES utf8mb4;

START TRANSACTION;

INSERT INTO rg_bloques (id,codigo,nombre,activo)
SELECT COALESCE(MAX(id),0)+1, 'ECO', 'Economia', 1
FROM rg_bloques
WHERE NOT EXISTS (SELECT 1 FROM rg_bloques WHERE codigo='ECO');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT COALESCE(MAX(i.id),0)+1,
       'ECO_PIB',
       b.id,
       'PIB nominal',
       'USD_corrientes',
       'PIB nominal en dolares corrientes',
       1
FROM rg_indicadores i
JOIN rg_bloques b ON b.codigo='ECO'
WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ECO_PIB');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT COALESCE(MAX(i.id),0)+1,
       'ECO_PIB_PCT',
       b.id,
       'PIB mundial %',
       '%',
       'Participacion del PIB del area sobre el total agregado de las nueve areas',
       1
FROM rg_indicadores i
JOIN rg_bloques b ON b.codigo='ECO'
WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ECO_PIB_PCT');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT COALESCE(MAX(i.id),0)+1,
       'ECO_PC',
       b.id,
       'PIB por habitante',
       'USD_corrientes_por_hab',
       'PIB total del area dividido por poblacion 2025 del area',
       1
FROM rg_indicadores i
JOIN rg_bloques b ON b.codigo='ECO'
WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ECO_PC');

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT COALESCE(MAX(id),0)+1,
       'WB_WDI',
       'Banco Mundial - World Development Indicators',
       'oficial',
       'https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD',
       1
FROM rg_fuentes
WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='WB_WDI');

COMMIT;
