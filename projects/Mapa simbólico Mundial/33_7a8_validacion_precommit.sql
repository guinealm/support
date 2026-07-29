-- NO MODIFICA LA BASE. Ejecutar dentro de la transacción y copiar resultados.
USE `u794456529_map_sim_Mund`;
SELECT i.codigo,COUNT(*) activos,COUNT(DISTINCT a.codigo) areas,SUM(da.valor IS NULL) nulos,SUM(da.valor=0) ceros FROM rg_datos_area da JOIN rg_indicadores i ON i.id=da.indicador_id JOIN rg_areas a ON a.id=da.area_id JOIN rg_periodos p ON p.id=da.periodo_id WHERE p.codigo='RG2025_V1' AND da.activo=1 GROUP BY i.codigo;
SELECT COUNT(*) total_activos FROM rg_datos_area da JOIN rg_periodos p ON p.id=da.periodo_id WHERE p.codigo='RG2025_V1' AND da.activo=1 AND da.indicador_id IN (SELECT id FROM rg_indicadores WHERE codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH'));
SELECT COUNT(*) eco_pc_mde_activos FROM rg_datos_area da JOIN rg_areas a ON a.id=da.area_id JOIN rg_indicadores i ON i.id=da.indicador_id JOIN rg_periodos p ON p.id=da.periodo_id WHERE p.codigo='RG2025_V1' AND a.codigo='MDE' AND i.codigo='ECO_PC' AND da.activo=1;
SELECT codigo,COUNT(*) FROM rg_indicadores WHERE codigo='POB_URB' GROUP BY codigo;
SELECT a.codigo,i.codigo,da.anio_referencia,da.porcentaje_cobertura,da.fuente_principal_id,da.observaciones FROM rg_datos_area da JOIN rg_areas a ON a.id=da.area_id JOIN rg_indicadores i ON i.id=da.indicador_id JOIN rg_periodos p ON p.id=da.periodo_id WHERE p.codigo='RG2025_V1' AND da.activo=1;
