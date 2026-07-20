-- 93_rg_reversion_tecnologia.sql
SET NAMES utf8mb4;
START TRANSACTION;
SET @ind_net := (SELECT id FROM rg_indicadores WHERE codigo='TEC_NET');
SET @bloque_tec := (SELECT id FROM rg_bloques WHERE codigo='TEC');
SET @src_wb := (SELECT id FROM rg_fuentes WHERE codigo='ITU_WB_NET');
SET @src_itu := (SELECT id FROM rg_fuentes WHERE codigo='ITU_DATAHUB');
DELETE FROM rg_datos_area WHERE indicador_id=@ind_net;
DELETE FROM rg_datos_pais WHERE indicador_id=@ind_net;
DELETE FROM rg_indicadores WHERE codigo='TEC_NET';
DELETE FROM rg_bloques WHERE codigo='TEC' AND NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE bloque_id=@bloque_tec);
DELETE FROM rg_fuentes WHERE codigo='ITU_WB_NET' AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_wb) AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_wb);
DELETE FROM rg_fuentes WHERE codigo='ITU_DATAHUB' AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_itu) AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_itu);
COMMIT;
