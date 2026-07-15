-- 11_rg_catalogo_desarrollo_humano.sql
SET NAMES utf8mb4;

START TRANSACTION;

SET @next_bloque := (SELECT COALESCE(MAX(id),0) FROM rg_bloques);

INSERT INTO rg_bloques (id,codigo,nombre,activo)
SELECT (@next_bloque := @next_bloque + 1), 'HUM', 'Desarrollo humano y desigualdad', 1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_bloques WHERE codigo='HUM');

SET @bloque_hum := (SELECT id FROM rg_bloques WHERE codigo='HUM' LIMIT 1);
SET @next_indicador := (SELECT COALESCE(MAX(id),0) FROM rg_indicadores);

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1),
       'HUM_IDH',
       @bloque_hum,
       'Indice de Desarrollo Humano',
       'indice_0_1',
       'Indice de Desarrollo Humano (PNUD) escala 0-1',
       1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='HUM_IDH');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1),
       'HUM_GINI',
       @bloque_hum,
       'Indice de Gini aproximado',
       'puntos_0_100',
       'Indice de Gini (PIP/Banco Mundial) escala 0-100',
       1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='HUM_GINI');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1),
       'HUM_EV',
       @bloque_hum,
       'Esperanza de vida al nacer',
       'anios',
       'Esperanza de vida al nacer en anios',
       1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='HUM_EV');

SET @next_fuente := (SELECT COALESCE(MAX(id),0) FROM rg_fuentes);

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1),
       'UNDP_HDR',
       'PNUD - Human Development Report 2025',
       'oficial',
       'https://hdr.undp.org/sites/default/files/2025_HDR/HDR25_Statistical_Annex_HDI_Table.xlsx',
       1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='UNDP_HDR');

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1),
       'WB_PIP',
       'Banco Mundial - Poverty and Inequality Platform',
       'oficial',
       'https://api.worldbank.org/v2/country/all/indicator/SI.POV.GINI',
       1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='WB_PIP');

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1),
       'WB_WDI',
       'Banco Mundial - World Development Indicators',
       'oficial',
       'https://api.worldbank.org/v2/country/all/indicator/SP.DYN.LE00.IN',
       1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='WB_WDI');

COMMIT;
