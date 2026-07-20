-- 26_rg_comprobacion_integral_1c9.sql
-- Fase 1C.9: auditoria integral de solo lectura. No inserta, actualiza ni elimina.
USE `u794456529_map_sim_Mund`;
SET NAMES utf8mb4;

-- A. Periodo. La inspeccion de information_schema se ejecuta al final para evitar
-- que phpMyAdmin cambie el contexto activo antes de las consultas del proyecto.
SELECT id,codigo,nombre,estado,activo FROM rg_periodos WHERE codigo='RG2025_V1';

-- B. Conteos generales confirmados para RG2025-V1.
SELECT
 (SELECT COUNT(*) FROM rg_areas WHERE activo=1) AS areas_activas,
 (SELECT COUNT(*) FROM rg_paises WHERE activo=1) AS entidades_activas,
 (SELECT COUNT(*) FROM rg_bloques WHERE activo=1) AS bloques_activos,
 (SELECT COUNT(*) FROM rg_indicadores WHERE activo=1) AS indicadores_activos,
 (SELECT COUNT(*) FROM rg_datos_area WHERE activo=1) AS datos_area_activos;
SELECT CASE WHEN
 (SELECT COUNT(*) FROM rg_areas WHERE activo=1)=9 AND
 (SELECT COUNT(*) FROM rg_paises WHERE activo=1)=244 AND
 (SELECT COUNT(*) FROM rg_bloques WHERE activo=1)=8 AND
 (SELECT COUNT(*) FROM rg_indicadores WHERE activo=1)=27 AND
 (SELECT COUNT(*) FROM rg_datos_area WHERE activo=1)=243
 THEN 'OK' ELSE 'NO_OK' END AS conteos_generales;

-- C. Bloques: deben ser exactamente los ocho previstos.
SELECT codigo,nombre,activo FROM rg_bloques ORDER BY codigo;
SELECT e.codigo AS bloque_esperado,CASE WHEN b.id IS NOT NULL AND b.activo=1 THEN 'OK' ELSE 'NO_OK' END AS estado
FROM (SELECT 'TERR' codigo UNION ALL SELECT 'POB' UNION ALL SELECT 'ECO' UNION ALL SELECT 'HUM' UNION ALL SELECT 'MIL' UNION ALL SELECT 'ENE' UNION ALL SELECT 'CLI' UNION ALL SELECT 'TEC') e
LEFT JOIN rg_bloques b ON b.codigo=e.codigo ORDER BY e.codigo;

-- D. Inventario real de indicadores.
SELECT b.codigo AS bloque,i.codigo,i.nombre,i.unidad,
 MIN(dp.anio) AS anio_minimo,MAX(dp.anio) AS anio_maximo,
 COUNT(DISTINCT dp.id) AS datos_nacionales,COUNT(DISTINCT da.id) AS registros_area,
 MIN(da.porcentaje_cobertura) AS cobertura_minima,
 CASE
  WHEN i.codigo IN ('HUM_GINI','ENE_DEP','ENE_AUTO','ENE_ELEC_LC','TEC_NET') THEN 'CONSOLIDADO_CON_ADVERTENCIA'
  ELSE 'CONSOLIDADO'
 END AS estado
FROM rg_indicadores i JOIN rg_bloques b ON b.id=i.bloque_id
LEFT JOIN rg_datos_pais dp ON dp.indicador_id=i.id AND dp.activo=1
LEFT JOIN rg_datos_area da ON da.indicador_id=i.id AND da.activo=1
WHERE i.activo=1
GROUP BY b.codigo,i.id,i.codigo,i.nombre,i.unidad ORDER BY b.codigo,i.codigo;

-- E. Cada indicador activo debe tener exactamente nueve filas de area.
SELECT i.codigo,COUNT(da.id) AS filas_area,CASE WHEN COUNT(da.id)=9 THEN 'OK' ELSE 'NO_OK' END AS estado
FROM rg_indicadores i LEFT JOIN rg_datos_area da ON da.indicador_id=i.id AND da.activo=1
WHERE i.activo=1 GROUP BY i.id,i.codigo ORDER BY i.codigo;

-- F. Unicidad y duplicidades. Las consultas de incidencias deben devolver cero filas.
SELECT codigo,COUNT(*) AS repeticiones FROM rg_indicadores GROUP BY codigo HAVING COUNT(*)>1;
SELECT codigo,COUNT(*) AS repeticiones FROM rg_areas GROUP BY codigo HAVING COUNT(*)>1;
SELECT pais_id,indicador_id,anio,COUNT(*) AS repeticiones FROM rg_datos_pais WHERE activo=1 GROUP BY pais_id,indicador_id,anio HAVING COUNT(*)>1;
SELECT area_id,indicador_id,periodo_id,anio_referencia,COUNT(*) AS repeticiones FROM rg_datos_area WHERE activo=1 GROUP BY area_id,indicador_id,periodo_id,anio_referencia HAVING COUNT(*)>1;

-- G. Fuentes y trazabilidad. Los datos activos sin fuente deben quedar explicados o corregidos antes de congelar.
SELECT i.codigo,COUNT(*) AS nacionales_sin_fuente FROM rg_datos_pais d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE d.activo=1 AND d.fuente_id IS NULL GROUP BY i.codigo;
SELECT i.codigo,COUNT(*) AS areas_sin_fuente FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE d.activo=1 AND d.fuente_principal_id IS NULL GROUP BY i.codigo;
SELECT f.codigo,f.nombre,f.tipo_fuente,f.url,f.activo,COUNT(DISTINCT dp.id) AS usos_pais,COUNT(DISTINCT da.id) AS usos_area
FROM rg_fuentes f LEFT JOIN rg_datos_pais dp ON dp.fuente_id=f.id AND dp.activo=1 LEFT JOIN rg_datos_area da ON da.fuente_principal_id=f.id AND da.activo=1
GROUP BY f.id,f.codigo,f.nombre,f.tipo_fuente,f.url,f.activo ORDER BY f.codigo;

-- H. Anos y dispersion temporal.
SELECT i.codigo,MIN(d.anio) AS anio_minimo,MAX(d.anio) AS anio_maximo,MAX(d.anio)-MIN(d.anio) AS dispersion,
 CASE WHEN MAX(d.anio)-MIN(d.anio)>5 THEN 'ADVERTENCIA_MAYOR_5' ELSE 'OK' END AS estado
FROM rg_datos_pais d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE d.activo=1 GROUP BY i.id,i.codigo ORDER BY dispersion DESC,i.codigo;
SELECT a.codigo AS area,i.codigo,d.anio_minimo,d.anio_maximo,d.porcentaje_cobertura,d.estado_dato
FROM rg_datos_area d JOIN rg_areas a ON a.id=d.area_id JOIN rg_indicadores i ON i.id=d.indicador_id
WHERE d.activo=1 ORDER BY i.codigo,a.codigo;

-- I. Ceros: no se corrigen automaticamente; cada fila debe estar documentada por su fuente/metodo.
SELECT p.codigo_iso3,i.codigo,d.anio,d.valor,d.fuente_id,d.observaciones
FROM rg_datos_pais d JOIN rg_paises p ON p.id=d.pais_id JOIN rg_indicadores i ON i.id=d.indicador_id
WHERE d.activo=1 AND d.valor=0 ORDER BY i.codigo,p.codigo_iso3,d.anio;
SELECT a.codigo AS area,i.codigo,d.valor,d.observaciones
FROM rg_datos_area d JOIN rg_areas a ON a.id=d.area_id JOIN rg_indicadores i ON i.id=d.indicador_id
WHERE d.activo=1 AND d.valor=0 ORDER BY i.codigo,a.codigo;

-- J. Rangos generales y extremos. Las dos primeras consultas solo deben devolver incidencias reales.
SELECT p.codigo_iso3,i.codigo,d.anio,d.valor FROM rg_datos_pais d JOIN rg_paises p ON p.id=d.pais_id JOIN rg_indicadores i ON i.id=d.indicador_id
WHERE d.activo=1 AND i.codigo IN ('TERR_PCT','POB_PCT','POB_VAR_2050','ECO_PIB_PCT','HUM_GINI','MIL_PCT','MIL_PIB','ENE_DEP','ENE_AUTO','ENE_ELEC_LC','TEC_NET') AND (d.valor<0 OR d.valor>100)
ORDER BY i.codigo,d.valor;
SELECT a.codigo AS area,i.codigo,d.valor FROM rg_datos_area d JOIN rg_areas a ON a.id=d.area_id JOIN rg_indicadores i ON i.id=d.indicador_id
WHERE d.activo=1 AND i.codigo IN ('TERR_PCT','POB_PCT','ECO_PIB_PCT','HUM_GINI','MIL_PCT','MIL_PIB','ENE_DEP','ENE_AUTO','ENE_ELEC_LC','TEC_NET') AND (d.valor<0 OR d.valor>100)
ORDER BY i.codigo,d.valor;
SELECT i.codigo,MIN(d.valor) AS minimo,MAX(d.valor) AS maximo FROM rg_datos_pais d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE d.activo=1 GROUP BY i.id,i.codigo ORDER BY i.codigo;
SELECT i.codigo,MIN(d.valor) AS minimo,MAX(d.valor) AS maximo FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE d.activo=1 GROUP BY i.id,i.codigo ORDER BY i.codigo;

-- K. Porcentajes mundiales, inventario nuclear y coherencia energetica.
SELECT i.codigo,SUM(d.valor) AS suma,CASE WHEN ABS(SUM(d.valor)-100)<0.01 THEN 'OK' ELSE 'NO_OK' END AS estado
FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id
WHERE d.activo=1 AND i.codigo IN ('TERR_PCT','POB_PCT','ECO_PIB_PCT','MIL_PCT') GROUP BY i.id,i.codigo;
SELECT SUM(d.valor) AS inventario_nuclear,COUNT(CASE WHEN d.valor>0 THEN 1 END) AS estados_nucleares,
 CASE WHEN SUM(d.valor)=12187 AND COUNT(CASE WHEN d.valor>0 THEN 1 END)=9 THEN 'OK' ELSE 'NO_OK' END AS estado
FROM rg_datos_pais d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE i.codigo='MIL_NUC' AND d.activo=1;
SELECT a.codigo,dep.valor AS dependencia,aut.valor AS autosuficiencia,
 CASE WHEN ABS(dep.valor+aut.valor-100)<0.000001 THEN 'OK' ELSE 'NO_OK' END AS estado
FROM rg_datos_area dep JOIN rg_indicadores idp ON idp.id=dep.indicador_id AND idp.codigo='ENE_DEP'
JOIN rg_datos_area aut ON aut.area_id=dep.area_id AND aut.periodo_id=dep.periodo_id AND aut.activo=1
JOIN rg_indicadores iau ON iau.id=aut.indicador_id AND iau.codigo='ENE_AUTO' JOIN rg_areas a ON a.id=dep.area_id
WHERE dep.activo=1 ORDER BY a.codigo;
SELECT codigo FROM rg_indicadores WHERE codigo IN ('ENE_FOS','TEC_ID','TEC_PESO');

-- L. Indicadores derivados recalculables en area.
SELECT a.codigo,pibpc.valor AS almacenado,pib.valor/pob.valor AS recalculado,CASE WHEN ABS(pibpc.valor-pib.valor/pob.valor)<0.01 THEN 'OK' ELSE 'NO_OK' END AS estado
FROM rg_areas a JOIN rg_datos_area pib ON pib.area_id=a.id AND pib.activo=1 JOIN rg_indicadores ipib ON ipib.id=pib.indicador_id AND ipib.codigo='ECO_PIB'
JOIN rg_datos_area pibpc ON pibpc.area_id=a.id AND pibpc.periodo_id=pib.periodo_id AND pibpc.activo=1 JOIN rg_indicadores ipc ON ipc.id=pibpc.indicador_id AND ipc.codigo='ECO_PC'
JOIN rg_datos_area pob ON pob.area_id=a.id AND pob.periodo_id=pib.periodo_id AND pob.activo=1 JOIN rg_indicadores ipo ON ipo.id=pob.indicador_id AND ipo.codigo='POB_TOTAL' ORDER BY a.codigo;
SELECT a.codigo,pc.valor AS almacenado,g.valor/p.valor AS recalculado,CASE WHEN ABS(pc.valor-g.valor/p.valor)<0.01 THEN 'OK' ELSE 'NO_OK' END AS estado
FROM rg_areas a JOIN rg_datos_area g ON g.area_id=a.id AND g.activo=1 JOIN rg_indicadores ig ON ig.id=g.indicador_id AND ig.codigo='MIL_GASTO'
JOIN rg_datos_area pc ON pc.area_id=a.id AND pc.periodo_id=g.periodo_id AND pc.activo=1 JOIN rg_indicadores ipc ON ipc.id=pc.indicador_id AND ipc.codigo='MIL_PC'
JOIN rg_datos_area p ON p.area_id=a.id AND p.periodo_id=g.periodo_id AND p.activo=1 JOIN rg_indicadores ip ON ip.id=p.indicador_id AND ip.codigo='POB_TOTAL' ORDER BY a.codigo;
SELECT a.codigo,pc.valor AS almacenado,c.valor*1000000000/p.valor AS recalculado,CASE WHEN ABS(pc.valor-c.valor*1000000000/p.valor)<0.01 THEN 'OK' ELSE 'NO_OK' END AS estado
FROM rg_areas a JOIN rg_datos_area c ON c.area_id=a.id AND c.activo=1 JOIN rg_indicadores ic ON ic.id=c.indicador_id AND ic.codigo='ENE_CONS'
JOIN rg_datos_area pc ON pc.area_id=a.id AND pc.periodo_id=c.periodo_id AND pc.activo=1 JOIN rg_indicadores ipc ON ipc.id=pc.indicador_id AND ipc.codigo='ENE_PC'
JOIN rg_datos_area p ON p.area_id=a.id AND p.periodo_id=c.periodo_id AND p.activo=1 JOIN rg_indicadores ip ON ip.id=p.indicador_id AND ip.codigo='POB_TOTAL' ORDER BY a.codigo;
SELECT a.codigo,pc.valor AS almacenado,SUM(cn.valor)/SUM(pn.valor) AS recalculado,
 CASE WHEN ABS(pc.valor-SUM(cn.valor)/SUM(pn.valor))<0.000001 THEN 'OK' ELSE 'NO_OK' END AS estado
FROM rg_areas a
JOIN rg_datos_area pc ON pc.area_id=a.id AND pc.activo=1 JOIN rg_indicadores ipc ON ipc.id=pc.indicador_id AND ipc.codigo='CLI_CO2_PC'
JOIN rg_paises rp ON rp.area_id=a.id
JOIN rg_indicadores icn ON icn.codigo='CLI_CO2' JOIN rg_datos_pais cn ON cn.pais_id=rp.id AND cn.indicador_id=icn.id AND cn.activo=1
JOIN rg_indicadores ipn ON ipn.codigo='POB_TOTAL' JOIN rg_datos_pais pn ON pn.pais_id=rp.id AND pn.indicador_id=ipn.id AND pn.anio=2025 AND pn.activo=1
GROUP BY a.id,a.codigo,pc.valor ORDER BY a.codigo;

-- M. TEC_NET recalculado desde datos nacionales y poblacion 2025.
SELECT a.codigo,d.valor AS almacenado,ROUND(SUM(n.valor*p.valor)/SUM(p.valor),6) AS recalculado,
 CASE WHEN ABS(d.valor-SUM(n.valor*p.valor)/SUM(p.valor))<0.000001 THEN 'OK' ELSE 'NO_OK' END AS estado
FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id AND i.codigo='TEC_NET' JOIN rg_areas a ON a.id=d.area_id
JOIN rg_paises rp ON rp.area_id=a.id JOIN rg_datos_pais n ON n.pais_id=rp.id AND n.indicador_id=i.id AND n.activo=1
JOIN rg_indicadores ip ON ip.codigo='POB_TOTAL' JOIN rg_datos_pais p ON p.pais_id=rp.id AND p.indicador_id=ip.id AND p.anio=2025 AND p.activo=1
WHERE d.activo=1 GROUP BY a.id,a.codigo,d.valor ORDER BY a.codigo;

-- N. Tratamientos territoriales especiales por indicador.
SELECT p.codigo_iso3,p.nombre,p.tipo_entidad,p.incluir_calculos,i.codigo,COUNT(d.id) AS filas,MIN(d.anio) AS anio_min,MAX(d.anio) AS anio_max
FROM rg_paises p CROSS JOIN rg_indicadores i LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=i.id AND d.activo=1
WHERE p.codigo_iso3 IN ('CHN','HKG','MAC','TWN','RUS','XKX','SRB','PRK') AND i.activo=1
GROUP BY p.id,p.codigo_iso3,p.nombre,p.tipo_entidad,p.incluir_calculos,i.id,i.codigo ORDER BY p.codigo_iso3,i.codigo;
SELECT tipo_entidad,incluir_calculos,COUNT(*) AS entidades FROM rg_paises WHERE activo=1 GROUP BY tipo_entidad,incluir_calculos ORDER BY tipo_entidad,incluir_calculos;
SELECT codigo_iso3,nombre,tipo_entidad FROM rg_paises WHERE activo=1 AND (CHAR_LENGTH(codigo_iso3)<>3 OR nombre REGEXP '(^World$|income|region|aggregate)');

-- O. PRK: ausencia de gasto militar y presencia nuclear.
SELECT p.codigo_iso3,i.codigo,d.anio,d.valor FROM rg_paises p JOIN rg_datos_pais d ON d.pais_id=p.id AND d.activo=1 JOIN rg_indicadores i ON i.id=d.indicador_id
WHERE p.codigo_iso3='PRK' AND i.codigo IN ('MIL_GASTO','MIL_NUC') ORDER BY i.codigo;

-- P. Estructura real, deliberadamente al final por compatibilidad con phpMyAdmin.
SELECT COLUMN_NAME,COLUMN_TYPE,IS_NULLABLE,COLUMN_DEFAULT
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA='u794456529_map_sim_Mund' AND TABLE_NAME='rg_periodos'
ORDER BY ORDINAL_POSITION;
SELECT TABLE_NAME,TABLE_TYPE
FROM information_schema.TABLES
WHERE TABLE_SCHEMA='u794456529_map_sim_Mund' AND TABLE_NAME IN ('rg_v_datos_consolidados','rg_v_primera_edicion');

-- Q. Matriz reproducible de coberturas por indicador y area.
-- Se deja al final porque la consulta P accede a information_schema en phpMyAdmin.
USE `u794456529_map_sim_Mund`;
SELECT i.codigo AS indicador,
 MAX(CASE WHEN a.codigo='AFR' THEN d.porcentaje_cobertura END) AS AFR,
 MAX(CASE WHEN a.codigo='APC' THEN d.porcentaje_cobertura END) AS APC,
 MAX(CASE WHEN a.codigo='CHN' THEN d.porcentaje_cobertura END) AS CHN,
 MAX(CASE WHEN a.codigo='EUR' THEN d.porcentaje_cobertura END) AS EUR,
 MAX(CASE WHEN a.codigo='MDE' THEN d.porcentaje_cobertura END) AS MDE,
 MAX(CASE WHEN a.codigo='NAC' THEN d.porcentaje_cobertura END) AS NAC,
 MAX(CASE WHEN a.codigo='RUE' THEN d.porcentaje_cobertura END) AS RUE,
 MAX(CASE WHEN a.codigo='SAI' THEN d.porcentaje_cobertura END) AS SAI,
 MAX(CASE WHEN a.codigo='SAM' THEN d.porcentaje_cobertura END) AS SAM,
 CASE
  WHEN MIN(d.porcentaje_cobertura)>=95 THEN 'ALTA'
  WHEN MIN(d.porcentaje_cobertura)>=90 THEN 'ACEPTABLE'
  WHEN MIN(d.porcentaje_cobertura)>=75 THEN 'CONDICIONADA'
  ELSE 'INSUFICIENTE'
 END AS clasificacion_minima
FROM rg_indicadores i JOIN rg_datos_area d ON d.indicador_id=i.id AND d.activo=1
JOIN rg_areas a ON a.id=d.area_id
WHERE i.activo=1 GROUP BY i.id,i.codigo ORDER BY i.codigo;
