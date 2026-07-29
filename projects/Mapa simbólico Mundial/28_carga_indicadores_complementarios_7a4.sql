-- FASE 7A.4 — PREFLIGHT DE CARGA. RESULTADO: NO-GO.
-- Archivo deliberadamente de solo lectura: no existe una carga admisible completa.
-- No se ha ejecutado contra MySQL.
USE `u794456529_map_sim_Mund`;
SET NAMES utf8mb4;

-- 1. Periodo requerido: exactamente uno, activo y congelado.
SELECT id,codigo,nombre,estado,activo
FROM rg_periodos
WHERE codigo='RG2025_V1';

-- 2. Los seis códigos deben existir una sola vez.
WITH requeridos AS (
  SELECT 'TERR_DENS' AS codigo
  UNION ALL SELECT 'POB_URB'
  UNION ALL SELECT 'POB_EDAD'
  UNION ALL SELECT 'HUM_EV'
  UNION ALL SELECT 'ECO_PC'
  UNION ALL SELECT 'HUM_IDH'
)
SELECT r.codigo,COUNT(i.id) AS coincidencias_catalogo,
       GROUP_CONCAT(i.unidad ORDER BY i.id) AS unidades
FROM requeridos r
LEFT JOIN rg_indicadores i ON i.codigo=r.codigo
GROUP BY r.codigo
ORDER BY r.codigo;

-- 3. Inventario actual por indicador y periodo.
SELECT i.codigo,COUNT(da.id) AS filas,
       COUNT(DISTINCT da.area_id) AS areas,
       SUM(da.valor IS NULL) AS valores_nulos,
       MIN(da.porcentaje_cobertura) AS cobertura_minima,
       MIN(da.anio_minimo) AS anio_minimo,
       MAX(da.anio_maximo) AS anio_maximo,
       GROUP_CONCAT(DISTINCT f.codigo ORDER BY f.codigo) AS fuentes
FROM rg_indicadores i
LEFT JOIN rg_datos_area da
  ON da.indicador_id=i.id
 AND da.activo=1
 AND da.periodo_id=(SELECT id FROM rg_periodos WHERE codigo='RG2025_V1')
LEFT JOIN rg_fuentes f ON f.id=da.fuente_principal_id
WHERE i.codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH')
GROUP BY i.codigo
ORDER BY i.codigo;

-- 4. Duplicidades activas: debe devolver cero filas.
SELECT a.codigo AS codigo_area,i.codigo AS codigo_indicador,
       p.codigo AS periodo,COUNT(*) AS repeticiones
FROM rg_datos_area da
JOIN rg_areas a ON a.id=da.area_id
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
WHERE da.activo=1
  AND p.codigo='RG2025_V1'
  AND i.codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH')
GROUP BY a.codigo,i.codigo,p.codigo
HAVING COUNT(*)<>1;

-- 5. Códigos territoriales no autorizados: debe devolver cero filas.
SELECT DISTINCT a.codigo
FROM rg_datos_area da
JOIN rg_areas a ON a.id=da.area_id
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
WHERE da.activo=1
  AND p.codigo='RG2025_V1'
  AND i.codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH')
  AND a.codigo NOT IN ('AFR','APC','CHN','EUR','MDE','NAC','RUE','SAI','SAM');

-- 6. Rangos técnicos actuales: cualquier fila devuelta requiere revisión.
SELECT a.codigo AS codigo_area,i.codigo AS codigo_indicador,da.valor
FROM rg_datos_area da
JOIN rg_areas a ON a.id=da.area_id
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
WHERE da.activo=1 AND p.codigo='RG2025_V1'
  AND (
    (i.codigo='TERR_DENS' AND da.valor<=0)
    OR (i.codigo='POB_URB' AND (da.valor<0 OR da.valor>100))
    OR (i.codigo='POB_EDAD' AND (da.valor<10 OR da.valor>60))
    OR (i.codigo='HUM_EV' AND (da.valor<40 OR da.valor>90))
    OR (i.codigo='ECO_PC' AND da.valor<=0)
    OR (i.codigo='HUM_IDH' AND (da.valor<0 OR da.valor>1))
  );

-- 7. Bloqueos conocidos de la preparación 7A.3.
-- POB_URB: 0/9 valores; no existe serie nacional incorporada.
-- ECO_PC: APC=94.8447 % y MDE=82.9370 %; prohibidos por cobertura.
-- HUM_IDH: APC=94.7568 %; prohibido por cobertura.
--
-- Con estos bloqueos no pueden obtenerse seis indicadores con nueve áreas
-- cumpliendo el umbral >=95 %. No se incluye INSERT, UPDATE, DELETE, CREATE,
-- ALTER ni DROP. No ejecutar 28_carga_indicadores_complementarios_7a3.sql.
