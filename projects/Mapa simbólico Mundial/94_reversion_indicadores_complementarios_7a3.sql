-- REVERSION ASOCIADA A 28_carga_indicadores_complementarios_7a3.sql.
-- NO EJECUTADA. Verificar primero que rg_backup_datos_area_7a3 existe y contiene 45 filas.
USE `u794456529_map_sim_Mund`;
SET NAMES utf8mb4;

SELECT COUNT(*) AS filas_respaldo FROM rg_backup_datos_area_7a3;

START TRANSACTION;
DELETE da
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
WHERE p.codigo='RG2025_V1'
  AND i.codigo IN ('TERR_DENS','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH');

INSERT INTO rg_datos_area
SELECT * FROM rg_backup_datos_area_7a3;

SELECT COUNT(*) AS filas_restauradas
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
WHERE p.codigo='RG2025_V1'
  AND i.codigo IN ('TERR_DENS','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH');
COMMIT;

-- Ejecutar DROP solo despues de comprobar la restauracion:
-- DROP TABLE rg_backup_datos_area_7a3;
