-- NO MODIFICA LA BASE. Ejecutar y copiar todos los resultados.
USE `u794456529_map_sim_Mund`;
SELECT codigo,COUNT(*) veces FROM rg_indicadores WHERE codigo IN ('TERR_DENS','POB_EDAD','ECO_PC','HUM_IDH','HUM_EV','POB_URB') GROUP BY codigo;
SELECT codigo,id,activo FROM rg_fuentes WHERE codigo IN ('OWID','WB_WDI','UNDP_HDR');
SELECT id,codigo,estado,activo FROM rg_periodos WHERE codigo='RG2025_V1';
SELECT codigo,id,activo FROM rg_areas WHERE codigo IN ('AFR','APC','CHN','EUR','MDE','NAC','RUE','SAI','SAM');
SELECT COUNT(*) filas_activas FROM rg_datos_area da JOIN rg_periodos p ON p.id=da.periodo_id WHERE p.codigo='RG2025_V1' AND da.activo=1 AND da.indicador_id IN (3,6,11,12,14);
SELECT id,area_id,indicador_id,periodo_id,anio_referencia,valor,activo FROM rg_datos_area WHERE id=95;
SELECT area_id,indicador_id,periodo_id,anio_referencia,COUNT(*) repeticiones FROM rg_datos_area da JOIN rg_periodos p ON p.id=da.periodo_id WHERE p.codigo='RG2025_V1' AND da.activo=1 GROUP BY area_id,indicador_id,periodo_id,anio_referencia HAVING COUNT(*)>1;
