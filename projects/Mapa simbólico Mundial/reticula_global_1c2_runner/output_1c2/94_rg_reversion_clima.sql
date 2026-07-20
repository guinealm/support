-- 94_rg_reversion_clima.sql
SET NAMES utf8mb4;
START TRANSACTION;
SET @ind_co2 := (SELECT id FROM rg_indicadores WHERE codigo='CLI_CO2');
SET @ind_co2_pc := (SELECT id FROM rg_indicadores WHERE codigo='CLI_CO2_PC');
SET @bloque_cli := (SELECT id FROM rg_bloques WHERE codigo='CLI');
SET @src_gcb := (SELECT id FROM rg_fuentes WHERE codigo='GCB2025_OWID');
DELETE FROM rg_datos_area WHERE indicador_id IN (@ind_co2,@ind_co2_pc);
DELETE FROM rg_datos_pais WHERE indicador_id IN (@ind_co2,@ind_co2_pc);
DELETE FROM rg_indicadores WHERE codigo IN ('CLI_CO2','CLI_CO2_PC');
DELETE FROM rg_bloques WHERE codigo='CLI' AND NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE bloque_id=@bloque_cli);
DELETE FROM rg_fuentes WHERE codigo='GCB2025_OWID' AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_gcb) AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_gcb);
COMMIT;
