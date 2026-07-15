-- 97_rg_reversion_desarrollo_humano.sql
SET NAMES utf8mb4;
START TRANSACTION;

SET @ind_hum_idh := (SELECT id FROM rg_indicadores WHERE codigo='HUM_IDH');
SET @ind_hum_gini := (SELECT id FROM rg_indicadores WHERE codigo='HUM_GINI');
SET @ind_hum_ev := (SELECT id FROM rg_indicadores WHERE codigo='HUM_EV');
SET @src_undp := (SELECT id FROM rg_fuentes WHERE codigo='UNDP_HDR');
SET @src_pip := (SELECT id FROM rg_fuentes WHERE codigo='WB_PIP');
SET @src_wdi := (SELECT id FROM rg_fuentes WHERE codigo='WB_WDI');
SET @blk_hum := (SELECT id FROM rg_bloques WHERE codigo='HUM');

DELETE FROM rg_datos_area WHERE indicador_id IN (@ind_hum_idh,@ind_hum_gini,@ind_hum_ev);
DELETE FROM rg_datos_pais WHERE indicador_id IN (@ind_hum_idh,@ind_hum_gini,@ind_hum_ev);

DELETE FROM rg_indicadores WHERE codigo IN ('HUM_IDH','HUM_GINI','HUM_EV');

DELETE FROM rg_bloques
WHERE codigo='HUM'
  AND NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE bloque_id=@blk_hum);

DELETE FROM rg_fuentes
WHERE codigo='UNDP_HDR'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_undp)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_undp);

DELETE FROM rg_fuentes
WHERE codigo='WB_PIP'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_pip)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_pip);

DELETE FROM rg_fuentes
WHERE codigo='WB_WDI'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_wdi)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_wdi);

COMMIT;
