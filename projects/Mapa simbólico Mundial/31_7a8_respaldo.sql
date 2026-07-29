-- MODIFICA LA BASE: crea tablas de respaldo. Ejecutar antes de cualquier transacción.
USE `u794456529_map_sim_Mund`;
CREATE TABLE rg_backup_datos_area_7a7_20260729 LIKE rg_datos_area;
CREATE TABLE rg_backup_indicadores_7a7_20260729 (codigo VARCHAR(40) PRIMARY KEY, existia TINYINT NOT NULL);
INSERT INTO rg_backup_indicadores_7a7_20260729 SELECT codigo,1 FROM rg_indicadores WHERE codigo IN ('TERR_DENS','POB_EDAD','ECO_PC','HUM_IDH','HUM_EV');
INSERT INTO rg_backup_indicadores_7a7_20260729 SELECT 'POB_URB',0 WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='POB_URB');
INSERT INTO rg_backup_datos_area_7a7_20260729 SELECT da.* FROM rg_datos_area da JOIN rg_indicadores i ON i.id=da.indicador_id JOIN rg_periodos p ON p.id=da.periodo_id WHERE p.codigo='RG2025_V1' AND i.codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH');
SELECT COUNT(*) respaldo_filas FROM rg_backup_datos_area_7a7_20260729;
-- Debe devolver 45. Si no, detenerse.
