-- 98_rg_reversion_economia.sql
SET NAMES utf8mb4;
START TRANSACTION;

SET @eco_pib := (SELECT id FROM rg_indicadores WHERE codigo='ECO_PIB');
SET @eco_pct := (SELECT id FROM rg_indicadores WHERE codigo='ECO_PIB_PCT');
SET @eco_pc := (SELECT id FROM rg_indicadores WHERE codigo='ECO_PC');
SET @src_wb := (SELECT id FROM rg_fuentes WHERE codigo='WB_WDI');
SET @blk_eco := (SELECT id FROM rg_bloques WHERE codigo='ECO');

DELETE FROM rg_datos_area WHERE indicador_id IN (@eco_pib,@eco_pct,@eco_pc);
DELETE FROM rg_datos_pais WHERE indicador_id=@eco_pib;

DELETE FROM rg_indicadores WHERE codigo IN ('ECO_PIB','ECO_PIB_PCT','ECO_PC');

DELETE FROM rg_bloques
WHERE codigo='ECO'
  AND NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE bloque_id=@blk_eco);

DELETE FROM rg_fuentes
WHERE codigo='WB_WDI'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_wb)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_wb);

COMMIT;
