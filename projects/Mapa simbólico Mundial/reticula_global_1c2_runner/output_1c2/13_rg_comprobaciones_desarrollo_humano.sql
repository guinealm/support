-- 13_rg_comprobaciones_desarrollo_humano.sql
SET NAMES utf8mb4;

-- Bloques e indicadores esperados tras 1C.4
SELECT COUNT(*) AS bloques_activos FROM rg_bloques WHERE activo=1;
SELECT COUNT(*) AS indicadores_activos FROM rg_indicadores WHERE activo=1;
SELECT COUNT(*) AS bloques_hum FROM rg_bloques WHERE codigo='HUM' AND activo=1;
SELECT COUNT(*) AS indicadores_hum FROM rg_indicadores WHERE codigo IN ('HUM_IDH','HUM_GINI','HUM_EV') AND activo=1;

-- Registros nacionales por indicador HUM
SELECT i.codigo, COUNT(*) AS registros
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
WHERE i.codigo IN ('HUM_IDH','HUM_GINI','HUM_EV') AND dp.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

-- Control de anio en HUM_IDH (esperado 2023)
SELECT MIN(dp.anio) AS anio_min_idh,
             MAX(dp.anio) AS anio_max_idh,
             COUNT(*) AS registros_idh
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id = dp.indicador_id
WHERE i.codigo = 'HUM_IDH'
    AND dp.activo = 1;

-- Nuevos registros de area HUM y total esperado
SELECT COUNT(*) AS datos_area_hum
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo IN ('HUM_IDH','HUM_GINI','HUM_EV') AND da.activo=1;

SELECT COUNT(*) AS total_datos_area_activos FROM rg_datos_area WHERE activo=1;

SELECT i.codigo, COUNT(*) AS filas_por_indicador
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo IN ('HUM_IDH','HUM_GINI','HUM_EV') AND da.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

-- Conservacion de territorio/poblacion/economia (debe seguir en 99)
SELECT COUNT(*) AS datos_area_no_hum
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo NOT IN ('HUM_IDH','HUM_GINI','HUM_EV') AND da.activo=1;

-- Cobertura y rangos temporales por area/indicador HUM
SELECT a.codigo AS area, i.codigo AS indicador, da.paises_totales, da.paises_con_dato, da.porcentaje_cobertura, da.anio_minimo, da.anio_maximo
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo IN ('HUM_IDH','HUM_GINI','HUM_EV') AND da.activo=1
ORDER BY i.codigo, a.codigo;

-- Valores fuera de rango
SELECT p.codigo_iso3, dp.anio, dp.valor
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo='HUM_IDH' AND dp.activo=1 AND (dp.valor < 0 OR dp.valor > 1);

SELECT p.codigo_iso3, dp.anio, dp.valor
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo='HUM_GINI' AND dp.activo=1 AND (dp.valor < 0 OR dp.valor > 100);

SELECT p.codigo_iso3, dp.anio, dp.valor
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo='HUM_EV' AND dp.activo=1 AND (dp.valor < 20 OR dp.valor > 95);

-- Duplicidades pais+indicador+anio
SELECT p.codigo_iso3, i.codigo AS indicador, dp.anio, COUNT(*) AS repeticiones
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo IN ('HUM_IDH','HUM_GINI','HUM_EV') AND dp.activo=1
GROUP BY p.codigo_iso3, i.codigo, dp.anio
HAVING COUNT(*) > 1;
