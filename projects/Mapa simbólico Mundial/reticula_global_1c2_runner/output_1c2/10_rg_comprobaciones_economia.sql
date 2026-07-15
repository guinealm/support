-- 10_rg_comprobaciones_economia.sql
SET NAMES utf8mb4;

-- Bloque economico y tres indicadores
SELECT COUNT(*) AS bloques_eco FROM rg_bloques WHERE codigo='ECO' AND activo=1;
SELECT COUNT(*) AS indicadores_eco FROM rg_indicadores WHERE codigo IN ('ECO_PIB','ECO_PIB_PCT','ECO_PC') AND activo=1;

-- Numero de datos nacionales de PIB
SELECT COUNT(*) AS datos_nacionales_eco_pib
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
WHERE i.codigo='ECO_PIB' AND dp.activo=1;

-- 27 nuevos registros de area y 99 total esperado
SELECT COUNT(*) AS datos_area_eco
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo IN ('ECO_PIB','ECO_PIB_PCT','ECO_PC') AND da.activo=1;

SELECT COUNT(*) AS total_datos_area_activos FROM rg_datos_area WHERE activo=1;

-- Conservacion de 72 registros anteriores (no ECO)
SELECT COUNT(*) AS datos_area_no_eco
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo NOT IN ('ECO_PIB','ECO_PIB_PCT','ECO_PC') AND da.activo=1;

-- Porcentajes ECO al ~100
SELECT SUM(da.valor) AS suma_eco_pib_pct
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo='ECO_PIB_PCT' AND da.activo=1;

-- PIB mundial agregado y PIB por habitante por area
SELECT SUM(da.valor) AS pib_mundial_agregado
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo='ECO_PIB' AND da.activo=1;

SELECT a.codigo AS area, da.valor AS pib_por_habitante
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo='ECO_PC' AND da.activo=1
ORDER BY a.codigo;

-- Cobertura por area
SELECT a.codigo AS area, da.paises_totales, da.paises_con_dato, da.porcentaje_cobertura
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo='ECO_PIB' AND da.activo=1
ORDER BY a.codigo;

-- Duplicidades pais+indicador+anio en ECO_PIB
SELECT p.codigo_iso3, dp.anio, COUNT(*) AS repeticiones
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo='ECO_PIB' AND dp.activo=1
GROUP BY p.codigo_iso3, dp.anio
HAVING COUNT(*) > 1;
