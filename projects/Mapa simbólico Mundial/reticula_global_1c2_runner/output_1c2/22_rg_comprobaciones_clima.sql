-- 22_rg_comprobaciones_clima.sql
SET NAMES utf8mb4;
SELECT CASE WHEN COUNT(*)=7 THEN 'OK' ELSE 'NO_OK' END AS bloques_esperados_7 FROM rg_bloques WHERE activo=1;
SELECT CASE WHEN COUNT(*)=26 THEN 'OK' ELSE 'NO_OK' END AS indicadores_esperados_26 FROM rg_indicadores WHERE activo=1;
SELECT i.codigo,COUNT(*) AS registros FROM rg_datos_pais d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE i.codigo IN ('CLI_CO2','CLI_CO2_PC') AND d.activo=1 GROUP BY i.codigo;
SELECT e.codigo,e.esperados,COUNT(d.id) AS cargados,CASE WHEN COUNT(d.id)=e.esperados THEN 'OK' ELSE 'NO_OK' END AS estado
FROM (SELECT 'CLI_CO2' AS codigo,214 AS esperados UNION ALL SELECT 'CLI_CO2_PC',213) e
LEFT JOIN rg_indicadores i ON i.codigo=e.codigo AND i.activo=1
LEFT JOIN rg_datos_pais d ON d.indicador_id=i.id AND d.activo=1
GROUP BY e.codigo,e.esperados ORDER BY e.codigo;
SELECT CASE WHEN COUNT(*)=18 THEN 'OK' ELSE 'NO_OK' END AS datos_area_cli_esperados_18 FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE i.codigo IN ('CLI_CO2','CLI_CO2_PC') AND d.activo=1;
SELECT CASE WHEN COUNT(*)=234 THEN 'OK' ELSE 'NO_OK' END AS datos_area_totales_esperados_234 FROM rg_datos_area WHERE activo=1;
SELECT CASE WHEN COUNT(*)=216 THEN 'OK' ELSE 'NO_OK' END AS datos_area_anteriores_esperados_216 FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE i.codigo NOT IN ('CLI_CO2','CLI_CO2_PC') AND d.activo=1;
SELECT i.codigo,COUNT(*) AS filas_por_indicador FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE i.codigo IN ('CLI_CO2','CLI_CO2_PC') AND d.activo=1 GROUP BY i.codigo;
SELECT p.codigo_iso3,i.codigo,d.valor FROM rg_datos_pais d JOIN rg_indicadores i ON i.id=d.indicador_id JOIN rg_paises p ON p.id=d.pais_id WHERE i.codigo IN ('CLI_CO2','CLI_CO2_PC') AND d.activo=1 AND d.valor<0;
SELECT p.codigo_iso3,i.codigo,d.anio,COUNT(*) AS repeticiones FROM rg_datos_pais d JOIN rg_indicadores i ON i.id=d.indicador_id JOIN rg_paises p ON p.id=d.pais_id WHERE i.codigo IN ('CLI_CO2','CLI_CO2_PC') AND d.activo=1 GROUP BY p.codigo_iso3,i.codigo,d.anio HAVING COUNT(*)>1;
SELECT a.codigo,i.codigo,d.porcentaje_cobertura,d.anio_minimo,d.anio_maximo FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id JOIN rg_areas a ON a.id=d.area_id WHERE i.codigo IN ('CLI_CO2','CLI_CO2_PC') AND d.activo=1 ORDER BY i.codigo,a.codigo;
SELECT a.codigo,tot.valor AS co2_t,pc.valor AS co2_pc FROM rg_datos_area tot JOIN rg_datos_area pc ON pc.area_id=tot.area_id AND pc.periodo_id=tot.periodo_id JOIN rg_indicadores it ON it.id=tot.indicador_id JOIN rg_indicadores ip ON ip.id=pc.indicador_id JOIN rg_areas a ON a.id=tot.area_id WHERE it.codigo='CLI_CO2' AND ip.codigo='CLI_CO2_PC' AND tot.activo=1 AND pc.activo=1 ORDER BY a.codigo;
