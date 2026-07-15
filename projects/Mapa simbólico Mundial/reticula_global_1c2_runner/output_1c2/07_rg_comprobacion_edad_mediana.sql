-- 07_rg_comprobacion_edad_mediana.sql
SET NAMES utf8mb4;

SELECT i.codigo, COUNT(*) AS registros,
       COUNT(dp.valor) AS valores_no_nulos
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id = dp.indicador_id
WHERE i.codigo = 'POB_EDAD'
GROUP BY i.codigo;

SELECT a.codigo AS area, da.valor, da.metodo_calculo,
       da.paises_totales, da.paises_con_dato,
       da.porcentaje_cobertura
FROM rg_datos_area da
JOIN rg_areas a ON a.id = da.area_id
JOIN rg_indicadores i ON i.id = da.indicador_id
WHERE i.codigo = 'POB_EDAD'
ORDER BY a.codigo;

-- Debe seguir habiendo 72 filas en rg_datos_area
SELECT COUNT(*) AS total_rg_datos_area FROM rg_datos_area WHERE activo=1;

-- No debe haber duplicidades nacionales de POB_EDAD por (pais,anio)
SELECT p.codigo_iso3, dp.anio, COUNT(*) AS repeticiones
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo='POB_EDAD' AND dp.activo=1
GROUP BY p.codigo_iso3, dp.anio
HAVING COUNT(*)>1;

-- Control de los 8 indicadores de area (deben quedar 9 cada uno)
SELECT i.codigo, COUNT(*) AS registros_area
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE da.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

-- Poblacion y porcentajes mundiales deben mantenerse
SELECT
  SUM(CASE WHEN i.codigo='POB_PCT' THEN da.valor ELSE 0 END) AS suma_pob_pct,
  SUM(CASE WHEN i.codigo='TERR_PCT' THEN da.valor ELSE 0 END) AS suma_terr_pct,
  SUM(CASE WHEN i.codigo='POB_TOTAL' THEN da.valor ELSE 0 END) AS poblacion_2025,
  SUM(CASE WHEN i.codigo='POB_2050' THEN da.valor ELSE 0 END) AS poblacion_2050
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE da.activo=1;