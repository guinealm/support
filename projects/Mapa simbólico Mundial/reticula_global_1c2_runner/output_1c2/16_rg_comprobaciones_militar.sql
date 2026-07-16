-- 16_rg_comprobaciones_militar.sql
SET NAMES utf8mb4;

-- Bloques e indicadores esperados tras 1C.5
SELECT COUNT(*) AS bloques_activos FROM rg_bloques WHERE activo=1;
SELECT COUNT(*) AS indicadores_activos FROM rg_indicadores WHERE activo=1;
SELECT COUNT(*) AS bloques_mil FROM rg_bloques WHERE codigo='MIL' AND activo=1;
SELECT COUNT(*) AS indicadores_mil FROM rg_indicadores WHERE codigo IN ('MIL_GASTO','MIL_PCT','MIL_PIB','MIL_PC','MIL_NUC') AND activo=1;

-- Registros nacionales por indicador MIL
SELECT i.codigo, COUNT(*) AS registros
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
WHERE i.codigo IN ('MIL_GASTO','MIL_PIB','MIL_NUC') AND dp.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

-- 45 registros de area militares y total esperado
SELECT COUNT(*) AS datos_area_mil
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo IN ('MIL_GASTO','MIL_PCT','MIL_PIB','MIL_PC','MIL_NUC') AND da.activo=1;

SELECT COUNT(*) AS total_datos_area_activos FROM rg_datos_area WHERE activo=1;

SELECT COUNT(*) AS datos_area_no_mil
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo NOT IN ('MIL_GASTO','MIL_PCT','MIL_PIB','MIL_PC','MIL_NUC') AND da.activo=1;

-- Nueve filas por indicador militar
SELECT i.codigo, COUNT(*) AS filas_por_indicador
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo IN ('MIL_GASTO','MIL_PCT','MIL_PIB','MIL_PC','MIL_NUC') AND da.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

-- Porcentaje mundial y gasto total
SELECT SUM(da.valor) AS suma_mil_pct
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo='MIL_PCT' AND da.activo=1;

SELECT SUM(da.valor) AS gasto_militar_mundial_agregado
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo='MIL_GASTO' AND da.activo=1;

-- Gasto por habitante y porcentaje PIB por area
SELECT a.codigo AS area, i.codigo AS indicador, da.valor
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo IN ('MIL_PC','MIL_PIB') AND da.activo=1
ORDER BY i.codigo, a.codigo;

-- Arsenal nuclear por area y total mundial
SELECT a.codigo AS area, da.valor AS ojivas_estimadas
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo='MIL_NUC' AND da.activo=1
ORDER BY a.codigo;

SELECT SUM(da.valor) AS ojivas_mundial_estimadas
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo='MIL_NUC' AND da.activo=1;

-- Cobertura y anios
SELECT a.codigo AS area, i.codigo AS indicador, da.paises_totales, da.paises_con_dato, da.porcentaje_cobertura, da.anio_minimo, da.anio_maximo
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo IN ('MIL_GASTO','MIL_PCT','MIL_PIB','MIL_PC','MIL_NUC') AND da.activo=1
ORDER BY i.codigo, a.codigo;

-- Duplicidades nacionales
SELECT p.codigo_iso3, i.codigo AS indicador, dp.anio, COUNT(*) AS repeticiones
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo IN ('MIL_GASTO','MIL_PIB','MIL_NUC') AND dp.activo=1
GROUP BY p.codigo_iso3, i.codigo, dp.anio
HAVING COUNT(*) > 1;

-- PRK: sin gasto/pib y con nuclear
SELECT p.codigo_iso3, i.codigo, dp.anio, dp.valor, dp.estado_dato
FROM rg_paises p
LEFT JOIN rg_datos_pais dp ON dp.pais_id = p.id AND dp.activo = 1
LEFT JOIN rg_indicadores i ON i.id = dp.indicador_id
WHERE p.codigo_iso3 = 'PRK'
    AND (i.codigo IN ('MIL_GASTO','MIL_PIB','MIL_NUC') OR i.codigo IS NULL);

-- Inventario nuclear mundial nacional (control SIPRI 12.187)
SELECT SUM(dp.valor) AS inventario_nuclear_mundial
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id = dp.indicador_id
WHERE i.codigo = 'MIL_NUC'
    AND dp.activo = 1;

-- Nueve Estados nucleares esperados
SELECT p.codigo_iso3, p.nombre, dp.valor
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id = dp.indicador_id
JOIN rg_paises p ON p.id = dp.pais_id
WHERE i.codigo = 'MIL_NUC'
    AND dp.valor > 0
    AND dp.activo = 1
ORDER BY dp.valor DESC;

-- MIL_NUC por area y controles de cero/consistencia
SELECT COUNT(*) AS filas_area_mil_nuc
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo='MIL_NUC' AND da.activo=1;

SELECT a.codigo AS area, da.valor
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo='MIL_NUC' AND da.activo=1 AND a.codigo IN ('AFR','SAM')
ORDER BY a.codigo;

SELECT
    (SELECT SUM(dp.valor)
     FROM rg_datos_pais dp
     JOIN rg_indicadores i ON i.id=dp.indicador_id
     WHERE i.codigo='MIL_NUC' AND dp.activo=1) AS total_nacional,
    (SELECT SUM(da.valor)
     FROM rg_datos_area da
     JOIN rg_indicadores i ON i.id=da.indicador_id
     WHERE i.codigo='MIL_NUC' AND da.activo=1) AS total_area;
