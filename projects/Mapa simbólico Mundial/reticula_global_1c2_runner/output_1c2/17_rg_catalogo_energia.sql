-- 17_rg_catalogo_energia.sql
SET NAMES utf8mb4;
START TRANSACTION;

SET @next_bloque := (SELECT COALESCE(MAX(id),0) FROM rg_bloques);

INSERT INTO rg_bloques (id,codigo,nombre,activo)
SELECT (@next_bloque := @next_bloque + 1), 'ENE', 'Energia y autonomia energetica', 1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_bloques WHERE codigo='ENE');

SET @bloque_ene := (SELECT id FROM rg_bloques WHERE codigo='ENE' LIMIT 1);
SET @next_indicador := (SELECT COALESCE(MAX(id),0) FROM rg_indicadores);

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'ENE_CONS', @bloque_ene, 'Consumo de energia primaria', 'twh', 'Consumo de energia primaria en TWh', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ENE_CONS');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'ENE_PC', @bloque_ene, 'Consumo de energia primaria por habitante', 'kwh_habitante', 'Consumo de energia primaria por habitante en kWh/habitante', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ENE_PC');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'ENE_DEP', @bloque_ene, 'Dependencia energetica exterior', 'porcentaje', 'Dependencia energetica neta aproximada ponderada por consumo', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ENE_DEP');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'ENE_AUTO', @bloque_ene, 'Autosuficiencia energetica aproximada', 'porcentaje', 'Autosuficiencia energetica neta aproximada (100 - dependencia)', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ENE_AUTO');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'ENE_FOS', @bloque_ene, 'Combustibles fosiles en energia primaria', 'porcentaje', 'Participacion de carbon, petroleo y gas en energia primaria', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ENE_FOS');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'ENE_ELEC_LC', @bloque_ene, 'Electricidad baja en carbono', 'porcentaje', 'Porcentaje de generacion electrica de fuentes bajas en carbono', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ENE_ELEC_LC');

SET @next_fuente := (SELECT COALESCE(MAX(id),0) FROM rg_fuentes);

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1), 'EI_SR2026', 'Energy Institute Statistical Review of World Energy 2026', 'oficial', 'https://www.energyinst.org/statistical-review', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='EI_SR2026');

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1), 'EMBER_GER2026', 'Ember Global Electricity Review 2026 / Electricity Data Explorer', 'oficial', 'https://ember-energy.org/data/electricity-data-explorer/', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='EMBER_GER2026');

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1), 'WB_IEA_ENEDEP', 'IEA via World Development Indicators EG.IMP.CONS.ZS', 'oficial', 'https://api.worldbank.org/v2/country/all/indicator/EG.IMP.CONS.ZS', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='WB_IEA_ENEDEP');

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1), 'OWID_ENERGY_PROC', 'Our World in Data energy dataset (processor)', 'procesado', 'https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='OWID_ENERGY_PROC');

COMMIT;
