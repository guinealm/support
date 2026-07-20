-- 27_rg_congelar_periodo_1c9.sql
-- Ejecutar solo tras aprobar la auditoria integral 1C.9.
-- La tabla rg_periodos no contiene columnas de fecha_cierre ni observaciones.
USE `u794456529_map_sim_Mund`;
SET NAMES utf8mb4;
START TRANSACTION;

UPDATE rg_periodos
SET estado='congelado',activo=1
WHERE codigo='RG2025_V1' AND activo=1;

SELECT ROW_COUNT() AS filas_actualizadas;
COMMIT;

SELECT id,codigo,nombre,estado,activo
FROM rg_periodos
WHERE codigo='RG2025_V1';
