-- FASE 7A.4 — REVERSIÓN NO OPERATIVA.
-- La carga 7A.4 no se ejecutó: no hay filas que revertir ni tabla de respaldo.
-- Archivo deliberadamente de solo lectura.
USE `u794456529_map_sim_Mund`;
SET NAMES utf8mb4;

SELECT 'NO_OP' AS resultado,
       '7A.4 finalizo en NO-GO antes de modificar MySQL' AS detalle;

-- Verificación opcional del estado existente, sin cambios.
SELECT i.codigo,COUNT(*) AS filas_activas
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
WHERE da.activo=1
  AND p.codigo='RG2025_V1'
  AND i.codigo IN ('TERR_DENS','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH')
GROUP BY i.codigo
ORDER BY i.codigo;
