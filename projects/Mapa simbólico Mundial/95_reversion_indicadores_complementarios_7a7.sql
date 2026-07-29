-- FASE 7A.7. REVERSIÓN NO EJECUTADA.
-- Requiere que exista el respaldo versionado creado por 29_carga...7a7.sql.
USE `u794456529_map_sim_Mund`;
SET NAMES utf8mb4;
START TRANSACTION;
DELETE da FROM rg_datos_area da JOIN rg_indicadores i ON i.id=da.indicador_id JOIN rg_periodos p ON p.id=da.periodo_id
WHERE p.codigo='RG2025_V1' AND i.codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH');
INSERT INTO rg_datos_area SELECT * FROM rg_backup_datos_area_7a7_20260729;
DELETE i FROM rg_indicadores i JOIN rg_backup_indicadores_7a7_20260729 b ON b.codigo=i.codigo WHERE i.codigo='POB_URB' AND b.existia=0;
-- NO HAY COMMIT AUTOMATICO: revisar la restauración y confirmar manualmente.
-- DROP TABLE rg_backup_datos_area_7a7_20260729;
-- DROP TABLE rg_backup_indicadores_7a7_20260729;
