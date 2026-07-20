-- 20_rg_catalogo_clima.sql
SET NAMES utf8mb4;
START TRANSACTION;

SET @next_bloque := (SELECT COALESCE(MAX(id),0) FROM rg_bloques);
INSERT INTO rg_bloques (id,codigo,nombre,activo)
SELECT (@next_bloque := @next_bloque + 1), 'CLI', 'Emisiones y clima', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_bloques WHERE codigo='CLI');
SET @bloque_cli := (SELECT id FROM rg_bloques WHERE codigo='CLI');
SET @next_indicador := (SELECT COALESCE(MAX(id),0) FROM rg_indicadores);

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'CLI_CO2', @bloque_cli, 'Emisiones territoriales de CO2', 'toneladas_co2', 'Emisiones de combustibles fosiles e industria; excluye cambio de uso del suelo', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='CLI_CO2');
INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'CLI_CO2_PC', @bloque_cli, 'Emisiones territoriales de CO2 por habitante', 'toneladas_co2_habitante', 'CLI_CO2 dividido por poblacion cubierta 2025', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='CLI_CO2_PC');

SET @next_fuente := (SELECT COALESCE(MAX(id),0) FROM rg_fuentes);
INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1), 'GCB2025_OWID', 'Global Carbon Budget (2025), con procesamiento de Our World in Data', 'procesado', 'https://ourworldindata.org/grapher/annual-co2-emissions-per-country', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='GCB2025_OWID');
COMMIT;
