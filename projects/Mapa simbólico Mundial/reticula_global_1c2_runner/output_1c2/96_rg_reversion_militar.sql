-- 96_rg_reversion_militar.sql
SET NAMES utf8mb4;
START TRANSACTION;

SET @ind_mil_gasto := (SELECT id FROM rg_indicadores WHERE codigo='MIL_GASTO');
SET @ind_mil_pct := (SELECT id FROM rg_indicadores WHERE codigo='MIL_PCT');
SET @ind_mil_pib := (SELECT id FROM rg_indicadores WHERE codigo='MIL_PIB');
SET @ind_mil_pc := (SELECT id FROM rg_indicadores WHERE codigo='MIL_PC');
SET @ind_mil_nuc := (SELECT id FROM rg_indicadores WHERE codigo='MIL_NUC');
SET @src_milex := (SELECT id FROM rg_fuentes WHERE codigo='SIPRI_MILEX_2026');
SET @src_nuc := (SELECT id FROM rg_fuentes WHERE codigo='SIPRI_YB26_NUC');
SET @blk_mil := (SELECT id FROM rg_bloques WHERE codigo='MIL');

DELETE FROM rg_datos_area WHERE indicador_id IN (@ind_mil_gasto,@ind_mil_pct,@ind_mil_pib,@ind_mil_pc,@ind_mil_nuc);
DELETE FROM rg_datos_pais WHERE indicador_id IN (@ind_mil_gasto,@ind_mil_pib,@ind_mil_nuc);

DELETE FROM rg_indicadores WHERE codigo IN ('MIL_GASTO','MIL_PCT','MIL_PIB','MIL_PC','MIL_NUC');

DELETE FROM rg_bloques
WHERE codigo='MIL'
  AND NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE bloque_id=@blk_mil);

DELETE FROM rg_fuentes
WHERE codigo='SIPRI_MILEX_2026'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_milex)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_milex);

DELETE FROM rg_fuentes
WHERE codigo='SIPRI_YB26_NUC'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_nuc)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_nuc);

COMMIT;
