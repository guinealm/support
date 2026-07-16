-- 95_rg_reversion_energia.sql
SET NAMES utf8mb4;
START TRANSACTION;

SET @ind_ene_cons := (SELECT id FROM rg_indicadores WHERE codigo='ENE_CONS');
SET @ind_ene_pc := (SELECT id FROM rg_indicadores WHERE codigo='ENE_PC');
SET @ind_ene_dep := (SELECT id FROM rg_indicadores WHERE codigo='ENE_DEP');
SET @ind_ene_auto := (SELECT id FROM rg_indicadores WHERE codigo='ENE_AUTO');
SET @ind_ene_fos := (SELECT id FROM rg_indicadores WHERE codigo='ENE_FOS');
SET @ind_ene_elec_lc := (SELECT id FROM rg_indicadores WHERE codigo='ENE_ELEC_LC');
SET @blk_ene := (SELECT id FROM rg_bloques WHERE codigo='ENE');

SET @src_ei := (SELECT id FROM rg_fuentes WHERE codigo='EI_SR2026');
SET @src_ember := (SELECT id FROM rg_fuentes WHERE codigo='EMBER_GER2026');
SET @src_dep := (SELECT id FROM rg_fuentes WHERE codigo='WB_IEA_ENEDEP');
SET @src_owid := (SELECT id FROM rg_fuentes WHERE codigo='OWID_ENERGY_PROC');

DELETE FROM rg_datos_area WHERE indicador_id IN (@ind_ene_cons,@ind_ene_pc,@ind_ene_dep,@ind_ene_auto,@ind_ene_fos,@ind_ene_elec_lc);
DELETE FROM rg_datos_pais WHERE indicador_id IN (@ind_ene_cons,@ind_ene_pc,@ind_ene_dep,@ind_ene_auto,@ind_ene_fos,@ind_ene_elec_lc);

DELETE FROM rg_indicadores WHERE codigo IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC');

DELETE FROM rg_bloques
WHERE codigo='ENE'
  AND NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE bloque_id=@blk_ene);

DELETE FROM rg_fuentes
WHERE codigo='EI_SR2026'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_ei)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_ei);

DELETE FROM rg_fuentes
WHERE codigo='EMBER_GER2026'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_ember)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_ember);

DELETE FROM rg_fuentes
WHERE codigo='WB_IEA_ENEDEP'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_dep)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_dep);

DELETE FROM rg_fuentes
WHERE codigo='OWID_ENERGY_PROC'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_owid)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_owid);

COMMIT;
