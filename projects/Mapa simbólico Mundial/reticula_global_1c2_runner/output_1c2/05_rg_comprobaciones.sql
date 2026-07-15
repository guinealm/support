-- 05_rg_comprobaciones.sql
SET NAMES utf8mb4;

-- Nueve areas
SELECT COUNT(*) AS total_areas FROM rg_areas WHERE activo = 1;

-- Numero de paises y territorios
SELECT COUNT(*) AS total_paises FROM rg_paises WHERE activo = 1;

-- Numero de indicadores y fuentes
SELECT COUNT(*) AS total_indicadores FROM rg_indicadores WHERE activo = 1;
SELECT COUNT(*) AS total_fuentes FROM rg_fuentes WHERE activo = 1;

-- Datos por indicador (pais)
SELECT i.codigo, COUNT(*) AS registros
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id = dp.indicador_id
WHERE dp.activo = 1
GROUP BY i.codigo
ORDER BY i.codigo;

-- Agregados por area
SELECT a.codigo AS area, i.codigo AS indicador, da.valor
FROM rg_datos_area da
JOIN rg_areas a ON a.id = da.area_id
JOIN rg_indicadores i ON i.id = da.indicador_id
WHERE da.activo = 1
ORDER BY a.codigo, i.codigo;

-- Registros ausentes en fuente de entidad
SELECT
  COUNT(*) AS paises_sin_poblacion_2025
FROM rg_paises p
LEFT JOIN rg_datos_pais dp ON dp.pais_id = p.id
  AND dp.indicador_id = (SELECT id FROM rg_indicadores WHERE codigo='POB_TOTAL')
WHERE p.activo = 1 AND dp.id IS NULL;

SELECT
  COUNT(*) AS paises_sin_superficie
FROM rg_paises p
LEFT JOIN rg_datos_pais dp ON dp.pais_id = p.id
  AND dp.indicador_id = (SELECT id FROM rg_indicadores WHERE codigo='TERR_SUP')
WHERE p.activo = 1 AND dp.id IS NULL;

-- Duplicidades ISO3
SELECT codigo_iso3, COUNT(*) AS repeticiones
FROM rg_paises
GROUP BY codigo_iso3
HAVING COUNT(*) > 1;

-- Porcentajes mundiales por area
SELECT
  SUM(CASE WHEN i.codigo='POB_PCT' THEN da.valor ELSE 0 END) AS suma_pob_pct,
  SUM(CASE WHEN i.codigo='TERR_PCT' THEN da.valor ELSE 0 END) AS suma_terr_pct
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id = da.indicador_id
WHERE da.activo = 1;

-- Poblacion total mundial 2025 y 2050
SELECT
  SUM(CASE WHEN i.codigo='POB_TOTAL' THEN da.valor ELSE 0 END) AS poblacion_2025,
  SUM(CASE WHEN i.codigo='POB_2050' THEN da.valor ELSE 0 END) AS poblacion_2050
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id = da.indicador_id
WHERE da.activo = 1;
