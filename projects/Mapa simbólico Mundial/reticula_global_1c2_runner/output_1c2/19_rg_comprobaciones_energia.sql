-- 19_rg_comprobaciones_energia.sql
SET NAMES utf8mb4;

-- Bloques e indicadores esperados tras 1C.6
SELECT COUNT(*) AS bloques_activos FROM rg_bloques WHERE activo=1;
SELECT COUNT(*) AS indicadores_activos FROM rg_indicadores WHERE activo=1;
SELECT COUNT(*) AS bloques_ene FROM rg_bloques WHERE codigo='ENE' AND activo=1;
SELECT COUNT(*) AS indicadores_ene FROM rg_indicadores WHERE codigo IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC') AND activo=1;

-- Registros nacionales por indicador ENE
SELECT i.codigo, COUNT(*) AS registros
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
WHERE i.codigo IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC') AND dp.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

-- 54 nuevos registros de area y total esperado
SELECT COUNT(*) AS datos_area_ene
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC') AND da.activo=1;

SELECT COUNT(*) AS total_datos_area_activos FROM rg_datos_area WHERE activo=1;

SELECT COUNT(*) AS datos_area_no_ene
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo NOT IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC') AND da.activo=1;

-- Nueve filas por indicador
SELECT i.codigo, COUNT(*) AS filas_por_indicador
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC') AND da.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

-- Consumo no negativo y ausentes no convertidos en cero
SELECT p.codigo_iso3, dp.valor
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo='ENE_CONS' AND dp.activo=1 AND dp.valor < 0;

SELECT p.codigo_iso3
FROM rg_paises p
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.activo=1
LEFT JOIN rg_indicadores i ON i.id=d.indicador_id AND i.codigo='ENE_CONS'
GROUP BY p.codigo_iso3
HAVING SUM(CASE WHEN i.codigo='ENE_CONS' THEN 1 ELSE 0 END)=0;

-- Coherencia EJ/TWh (1 EJ = 277.777778 TWh) en agregados
SELECT a.codigo AS area, da.valor AS twh,
       (da.valor / 277.777778) AS ej_estimado,
       ((da.valor / 277.777778) * 277.777778 - da.valor) AS delta_twh
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo='ENE_CONS' AND da.activo=1
ORDER BY a.codigo;

-- ENE_PC recalculable
SELECT a.codigo AS area, cons.valor AS consumo_twh, pc.valor AS pc_kwh
FROM rg_datos_area cons
JOIN rg_datos_area pc ON pc.area_id=cons.area_id AND pc.periodo_id=cons.periodo_id AND pc.anio_referencia=cons.anio_referencia
JOIN rg_indicadores ic ON ic.id=cons.indicador_id
JOIN rg_indicadores ip ON ip.id=pc.indicador_id
JOIN rg_areas a ON a.id=cons.area_id
WHERE ic.codigo='ENE_CONS' AND ip.codigo='ENE_PC' AND cons.activo=1 AND pc.activo=1
ORDER BY a.codigo;

-- ENE_DEP ponderado y ENE_AUTO = 100 - ENE_DEP
SELECT a.codigo AS area, dep.valor AS dep, auto.valor AS auto_calc, (100 - dep.valor) AS auto_esperado
FROM rg_datos_area dep
JOIN rg_datos_area auto ON auto.area_id=dep.area_id AND auto.periodo_id=dep.periodo_id AND auto.anio_referencia=dep.anio_referencia
JOIN rg_indicadores idp ON idp.id=dep.indicador_id
JOIN rg_indicadores iau ON iau.id=auto.indicador_id
JOIN rg_areas a ON a.id=dep.area_id
WHERE idp.codigo='ENE_DEP' AND iau.codigo='ENE_AUTO' AND dep.activo=1 AND auto.activo=1
ORDER BY a.codigo;

-- Exportadores netos (autosuficiencia > 100)
SELECT a.codigo AS area, da.valor AS autosuficiencia
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo='ENE_AUTO' AND da.valor > 100 AND da.activo=1
ORDER BY da.valor DESC;

-- Rangos de porcentaje y calculo desde absolutos
SELECT p.codigo_iso3, i.codigo, dp.valor
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo IN ('ENE_FOS','ENE_ELEC_LC') AND dp.activo=1 AND (dp.valor < 0 OR dp.valor > 100);

-- Anios, datos 2024 y duplicidades
SELECT i.codigo, MIN(dp.anio) AS anio_min, MAX(dp.anio) AS anio_max
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
WHERE i.codigo IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC') AND dp.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

SELECT i.codigo, COUNT(*) AS filas_2024
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
WHERE i.codigo='ENE_ELEC_LC' AND dp.anio=2024 AND dp.activo=1;

SELECT p.codigo_iso3, i.codigo, dp.anio, COUNT(*) AS repeticiones
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC') AND dp.activo=1
GROUP BY p.codigo_iso3, i.codigo, dp.anio
HAVING COUNT(*) > 1;

-- Controles territoriales
SELECT p.codigo_iso3, a.codigo AS area
FROM rg_paises p
JOIN rg_areas a ON a.id=p.area_id
WHERE p.codigo_iso3 IN ('CHN','HKG','MAC','TWN','RUS','XKX','PRK') AND p.activo=1
ORDER BY p.codigo_iso3;
