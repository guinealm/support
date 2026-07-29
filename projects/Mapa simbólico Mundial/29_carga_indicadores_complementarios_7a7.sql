-- FASE 7A.7. PROPUESTA NO EJECUTADA.
-- DDL de respaldo antes de la transacción; no ejecutar sin preflight y copia verificada.
USE `u794456529_map_sim_Mund`;
SET NAMES utf8mb4;
CREATE TABLE rg_backup_datos_area_7a7_20260729 LIKE rg_datos_area;
CREATE TABLE rg_backup_indicadores_7a7_20260729 (codigo VARCHAR(40) PRIMARY KEY, existia TINYINT NOT NULL);
INSERT INTO rg_backup_indicadores_7a7_20260729
SELECT 'POB_URB', IF(COUNT(*)>0,1,0) FROM rg_indicadores WHERE codigo='POB_URB';
INSERT INTO rg_backup_datos_area_7a7_20260729
SELECT da.* FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
WHERE p.codigo='RG2025_V1' AND i.codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH');
CREATE TEMPORARY TABLE tmp_rg_area_7a7 (
 codigo_area CHAR(3) NOT NULL, codigo_indicador VARCHAR(40) NOT NULL,
 anio_referencia SMALLINT NOT NULL, valor DECIMAL(22,6) NOT NULL,
 metodo_calculo VARCHAR(120) NOT NULL, cobertura_pct DECIMAL(8,4) NOT NULL,
 observaciones TEXT, fuente_codigo VARCHAR(40) NOT NULL,
 PRIMARY KEY(codigo_area,codigo_indicador));
INSERT INTO tmp_rg_area_7a7
(codigo_area,codigo_indicador,anio_referencia,valor,metodo_calculo,cobertura_pct,observaciones,fuente_codigo)
VALUES
('AFR','TERR_DENS',2025,51.7392812421,'Poblacion 2025 agregada / superficie terrestre 2023 agregada',100.0000,'Incluidos 58 de 59; ausentes: IOT; poblacion cubierta 1548737803 de 1548737803.','OWID'),
('APC','TERR_DENS',2025,64.5572787545,'Poblacion 2025 agregada / superficie terrestre 2023 agregada',100.0000,'Incluidos 39 de 43; ausentes: CXR, CCK, NFK, PCN; poblacion cubierta 974613138 de 974613138.','OWID'),
('CHN','TERR_DENS',2025,151.6849230288,'Poblacion 2025 agregada / superficie terrestre 2023 agregada',100.0000,'Incluidos 3 de 3; ausentes: ninguno; poblacion cubierta 1424214186 de 1424214186.','OWID'),
('EUR','TERR_DENS',2025,106.4515359952,'Poblacion 2025 agregada / superficie terrestre 2023 agregada',99.9715,'Incluidos 46 de 51; ausentes: ALA, SJM, GGY, JEY, XKX; poblacion cubierta 590932215 de 591100715.','OWID'),
('MDE','TERR_DENS',2025,62.3607420494,'Poblacion 2025 agregada / superficie terrestre 2023 agregada',100.0000,'Incluidos 15 de 15; ausentes: ninguno; poblacion cubierta 388187450 de 388187450.','OWID'),
('NAC','TERR_DENS',2025,29.3647789637,'Poblacion 2025 agregada / superficie terrestre 2023 agregada',100.0000,'Incluidos 41 de 41; ausentes: ninguno; poblacion cubierta 617312022 de 617312022.','OWID'),
('RUE','TERR_DENS',2025,12.2578028899,'Poblacion 2025 agregada / superficie terrestre 2023 agregada',100.0000,'Incluidos 10 de 10; ausentes: ninguno; poblacion cubierta 253749543 de 253749543.','OWID'),
('SAI','TERR_DENS',2025,417.7820021602,'Poblacion 2025 agregada / superficie terrestre 2023 agregada',100.0000,'Incluidos 8 de 8; ausentes: ninguno; poblacion cubierta 1992790070 de 1992790070.','OWID'),
('SAM','TERR_DENS',2025,25.0653448638,'Poblacion 2025 agregada / superficie terrestre 2023 agregada',100.0000,'Incluidos 14 de 14; ausentes: ninguno; poblacion cubierta 438105416 de 438105416.','OWID'),
('AFR','POB_URB',2023,45.4835976471,'Media de porcentajes nacionales 2023 ponderada por poblacion 2023',99.8800,'Incluidos 54 de 59; ausentes: IOT, MYT, REU, SHN, ESH; poblacion cubierta 1477914293 de 1479690254.','WB_WDI'),
('APC','POB_URB',2023,61.0707684138,'Media de porcentajes nacionales 2023 ponderada por poblacion 2023',97.5805,'Incluidos 34 de 43; ausentes: TWN, CXR, CCK, COK, NIU, NFK, PCN, TKL, WLF; poblacion cubierta 941620272 de 964967320.','WB_WDI'),
('CHN','POB_URB',2023,65.7266573572,'Media de porcentajes nacionales 2023 ponderada por poblacion 2023',100.0000,'Incluidos 3 de 3; ausentes: ninguno; poblacion cubierta 1430741584 de 1430741584.','WB_WDI'),
('EUR','POB_URB',2023,75.1259381546,'Media de porcentajes nacionales 2023 ponderada por poblacion 2023',99.9715,'Incluidos 45 de 51; ausentes: ALA, VAT, SJM, GGY, JEY, XKX; poblacion cubierta 590523665 de 590691889.','WB_WDI'),
('MDE','POB_URB',2023,76.9951151409,'Media de porcentajes nacionales 2023 ponderada por poblacion 2023',100.0000,'Incluidos 15 de 15; ausentes: ninguno; poblacion cubierta 376160100 de 376160100.','WB_WDI'),
('NAC','POB_URB',2023,77.7413796649,'Media de porcentajes nacionales 2023 ponderada por poblacion 2023',99.8705,'Incluidos 34 de 41; ausentes: GLP, MTQ, MSR, BES, BLM, AIA, SPM; poblacion cubierta 607982407 de 608770547.','WB_WDI'),
('RUE','POB_URB',2023,65.7193759157,'Media de porcentajes nacionales 2023 ponderada por poblacion 2023',100.0000,'Incluidos 10 de 10; ausentes: ninguno; poblacion cubierta 252435469 de 252435469.','WB_WDI'),
('SAI','POB_URB',2023,35.3915513787,'Media de porcentajes nacionales 2023 ponderada por poblacion 2023',100.0000,'Incluidos 8 de 8; ausentes: ninguno; poblacion cubierta 1952474474 de 1952474474.','WB_WDI'),
('SAM','POB_URB',2023,85.0426514616,'Media de porcentajes nacionales 2023 ponderada por poblacion 2023',99.9291,'Incluidos 12 de 14; ausentes: FLK, GUF; poblacion cubierta 432717317 de 433024223.','WB_WDI'),
('AFR','POB_EDAD',2023,19.4222483839,'Media aproximada de medianas nacionales 2023 ponderada por poblacion 2023',100.0000,'Aproximacion, no mediana regional publicada. Incluidos 58 de 59; ausentes: IOT; poblacion cubierta 1479690254 de 1479690254.','OWID'),
('APC','POB_EDAD',2023,34.0883791565,'Media aproximada de medianas nacionales 2023 ponderada por poblacion 2023',100.0000,'Aproximacion, no mediana regional publicada. Incluidos 39 de 43; ausentes: CXR, CCK, NFK, PCN; poblacion cubierta 964967320 de 964967320.','OWID'),
('CHN','POB_EDAD',2023,39.1024998472,'Media aproximada de medianas nacionales 2023 ponderada por poblacion 2023',100.0000,'Aproximacion, no mediana regional publicada. Incluidos 3 de 3; ausentes: ninguno; poblacion cubierta 1430741584 de 1430741584.','OWID'),
('EUR','POB_EDAD',2023,43.0168309618,'Media aproximada de medianas nacionales 2023 ponderada por poblacion 2023',100.0000,'Aproximacion, no mediana regional publicada. Incluidos 48 de 51; ausentes: ALA, SJM, XKX; poblacion cubierta 590691889 de 590691889.','OWID'),
('MDE','POB_EDAD',2023,28.0802753067,'Media aproximada de medianas nacionales 2023 ponderada por poblacion 2023',100.0000,'Aproximacion, no mediana regional publicada. Incluidos 15 de 15; ausentes: ninguno; poblacion cubierta 376160100 de 376160100.','OWID'),
('NAC','POB_EDAD',2023,34.7639368434,'Media aproximada de medianas nacionales 2023 ponderada por poblacion 2023',100.0000,'Aproximacion, no mediana regional publicada. Incluidos 41 de 41; ausentes: ninguno; poblacion cubierta 608770547 de 608770547.','OWID'),
('RUE','POB_EDAD',2023,35.0461202946,'Media aproximada de medianas nacionales 2023 ponderada por poblacion 2023',100.0000,'Aproximacion, no mediana regional publicada. Incluidos 10 de 10; ausentes: ninguno; poblacion cubierta 252435469 de 252435469.','OWID'),
('SAI','POB_EDAD',2023,26.6042206397,'Media aproximada de medianas nacionales 2023 ponderada por poblacion 2023',100.0000,'Aproximacion, no mediana regional publicada. Incluidos 8 de 8; ausentes: ninguno; poblacion cubierta 1952474474 de 1952474474.','OWID'),
('SAM','POB_EDAD',2023,32.2595807338,'Media aproximada de medianas nacionales 2023 ponderada por poblacion 2023',100.0000,'Aproximacion, no mediana regional publicada. Incluidos 14 de 14; ausentes: ninguno; poblacion cubierta 433024223 de 433024223.','OWID'),
('AFR','HUM_EV',2023,64.2045156654,'Media nacional 2023 ponderada por poblacion 2023',99.8800,'Incluidos 54 de 59; ausentes: IOT, MYT, REU, SHN, ESH; poblacion cubierta 1477914293 de 1479690254.','WB_WDI'),
('APC','HUM_EV',2023,74.5499714605,'Media nacional 2023 ponderada por poblacion 2023',97.5805,'Incluidos 34 de 43; ausentes: TWN, CXR, CCK, COK, NIU, NFK, PCN, TKL, WLF; poblacion cubierta 941620272 de 964967320.','WB_WDI'),
('CHN','HUM_EV',2023,77.9935535693,'Media nacional 2023 ponderada por poblacion 2023',100.0000,'Incluidos 3 de 3; ausentes: ninguno; poblacion cubierta 1430741584 de 1430741584.','WB_WDI'),
('EUR','HUM_EV',2023,80.7626824202,'Media nacional 2023 ponderada por poblacion 2023',99.9715,'Incluidos 45 de 51; ausentes: ALA, VAT, SJM, GGY, JEY, XKX; poblacion cubierta 590523665 de 590691889.','WB_WDI'),
('MDE','HUM_EV',2023,76.0410986325,'Media nacional 2023 ponderada por poblacion 2023',100.0000,'Incluidos 15 de 15; ausentes: ninguno; poblacion cubierta 376160100 de 376160100.','WB_WDI'),
('NAC','HUM_EV',2023,77.1547598162,'Media nacional 2023 ponderada por poblacion 2023',99.8705,'Incluidos 34 de 41; ausentes: GLP, MTQ, MSR, BES, BLM, AIA, SPM; poblacion cubierta 607982407 de 608770547.','WB_WDI'),
('RUE','HUM_EV',2023,73.1927346186,'Media nacional 2023 ponderada por poblacion 2023',100.0000,'Incluidos 10 de 10; ausentes: ninguno; poblacion cubierta 252435469 de 252435469.','WB_WDI'),
('SAI','HUM_EV',2023,71.6009692483,'Media nacional 2023 ponderada por poblacion 2023',100.0000,'Incluidos 8 de 8; ausentes: ninguno; poblacion cubierta 1952474474 de 1952474474.','WB_WDI'),
('SAM','HUM_EV',2023,76.2400545436,'Media nacional 2023 ponderada por poblacion 2023',99.9291,'Incluidos 12 de 14; ausentes: FLK, GUF; poblacion cubierta 432717317 de 433024223.','WB_WDI'),
('AFR','ECO_PC',2024,1938.6561577151,'PIB nominal 2024 agregado / poblacion cubierta 2024',98.8587,'Incluidos 52 de 59; ausentes: IOT, MYT, ERI, REU, SHN, SSD, ESH; poblacion cubierta 1496752464 de 1514032368.','WB_WDI'),
('APC','ECO_PC',2024,13751.1343374047,'PIB nominal 2024 agregado / poblacion cubierta 2024',97.2381,'Incluidos 31 de 43; ausentes: ASM, CXR, CCK, COK, GUM, PRK, NIU, NFK, MNP, PCN, TKL, WLF; poblacion cubierta 943110329 de 969897464.','WB_WDI'),
('CHN','ECO_PC',2024,13441.7439742105,'PIB nominal 2024 agregado / poblacion cubierta 2024',100.0000,'Incluidos 3 de 3; ausentes: ninguno; poblacion cubierta 1427456468 de 1427456468.','WB_WDI'),
('EUR','ECO_PC',2024,42519.1316550767,'PIB nominal 2024 agregado / poblacion cubierta 2024',99.9449,'Incluidos 42 de 51; ausentes: ALA, GIB, VAT, SMR, SJM, GGY, JEY, IMN, XKX; poblacion cubierta 590554619 de 590880428.','WB_WDI'),
('NAC','ECO_PC',2024,56842.8902189527,'PIB nominal 2024 agregado / poblacion cubierta 2024',98.0476,'Incluidos 29 de 41; ausentes: VGB, CUB, GRL, GLP, MTQ, MSR, BES, BLM, AIA, MAF, SPM, VIR; poblacion cubierta 601179114 de 613150315.','WB_WDI'),
('RUE','ECO_PC',2024,11410.1771640523,'PIB nominal 2024 agregado / poblacion cubierta 2024',100.0000,'Incluidos 10 de 10; ausentes: ninguno; poblacion cubierta 253221076 de 253221076.','WB_WDI'),
('SAI','ECO_PC',2024,2410.0424971235,'PIB nominal 2024 agregado / poblacion cubierta 2024',100.0000,'Incluidos 8 de 8; ausentes: ninguno; poblacion cubierta 1972488759 de 1972488759.','WB_WDI'),
('SAM','ECO_PC',2024,9926.7197730408,'PIB nominal 2024 agregado / poblacion cubierta 2024',99.9284,'Incluidos 12 de 14; ausentes: FLK, GUF; poblacion cubierta 435299307 de 435611337.','WB_WDI'),
('AFR','HUM_IDH',2023,0.576062797,'IDH nacional 2023 ponderado por poblacion 2023',99.8800,'IDH medio ponderado, no IDH oficial del area. Incluidos 54 de 59; ausentes: IOT, MYT, REU, SHN, ESH; poblacion cubierta 1477914293 de 1479690254.','UNDP_HDR'),
('APC','HUM_IDH',2023,0.7797007723,'IDH nacional 2023 ponderado por poblacion 2023',97.1731,'IDH medio ponderado, no IDH oficial del area. Incluidos 29 de 43; ausentes: ASM, CXR, CCK, COK, PYF, GUM, PRK, NCL, NIU, NFK, MNP, PCN, TKL, WLF; poblacion cubierta 937688985 de 964967320.','UNDP_HDR'),
('CHN','HUM_IDH',2023,0.7978223286,'IDH nacional 2023 ponderado por poblacion 2023',99.9501,'IDH medio ponderado, no IDH oficial del area. Incluidos 2 de 3; ausentes: MAC; poblacion cubierta 1430027668 de 1430741584.','UNDP_HDR'),
('EUR','HUM_IDH',2023,0.9137653314,'IDH nacional 2023 ponderado por poblacion 2023',99.9349,'IDH medio ponderado, no IDH oficial del area. Incluidos 41 de 51; ausentes: FRO, ALA, GIB, VAT, MCO, SJM, GGY, JEY, IMN, XKX; poblacion cubierta 590307273 de 590691889.','UNDP_HDR'),
('MDE','HUM_IDH',2023,0.7644397732,'IDH nacional 2023 ponderado por poblacion 2023',100.0000,'IDH medio ponderado, no IDH oficial del area. Incluidos 15 de 15; ausentes: ninguno; poblacion cubierta 376160100 de 376160100.','UNDP_HDR'),
('NAC','HUM_IDH',2023,0.8702257728,'IDH nacional 2023 ponderado por poblacion 2023',99.2183,'IDH medio ponderado, no IDH oficial del area. Incluidos 23 de 41; ausentes: BMU, VGB, CYM, GRL, GLP, MTQ, MSR, CUW, ABW, SXM, BES, PRI, BLM, AIA, MAF, SPM, TCA, VIR; poblacion cubierta 604012013 de 608770547.','UNDP_HDR'),
('RUE','HUM_IDH',2023,0.8063733675,'IDH nacional 2023 ponderado por poblacion 2023',100.0000,'IDH medio ponderado, no IDH oficial del area. Incluidos 10 de 10; ausentes: ninguno; poblacion cubierta 252435469 de 252435469.','UNDP_HDR'),
('SAI','HUM_IDH',2023,0.6632529299,'IDH nacional 2023 ponderado por poblacion 2023',100.0000,'IDH medio ponderado, no IDH oficial del area. Incluidos 8 de 8; ausentes: ninguno; poblacion cubierta 1952474474 de 1952474474.','UNDP_HDR'),
('SAM','HUM_IDH',2023,0.7924598368,'IDH nacional 2023 ponderado por poblacion 2023',99.9291,'IDH medio ponderado, no IDH oficial del area. Incluidos 12 de 14; ausentes: FLK, GUF; poblacion cubierta 432717317 de 433024223.','UNDP_HDR');

START TRANSACTION;
-- POB_URB es el código aprobado en el diccionario; se crea solo si está ausente.
INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (SELECT COALESCE(MAX(id),0)+1 FROM rg_indicadores),'POB_URB',b.id,
       'Población urbana','porcentaje_poblacion','Población urbana como porcentaje de la población total',1
FROM rg_bloques b WHERE b.codigo='POB'
  AND NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='POB_URB');
SET @per_7a7 := (SELECT id FROM rg_periodos WHERE codigo='RG2025_V1' AND activo=1);
SET @next_7a7 := (SELECT COALESCE(MAX(id),0) FROM rg_datos_area);
-- Inserta únicamente las nueve filas nuevas de POB_URB; el preflight exige que no existan.
INSERT INTO rg_datos_area
(id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)
SELECT (@next_7a7:=@next_7a7+1),a.id,i.id,@per_7a7,t.anio_referencia,t.valor,t.metodo_calculo,NULL,NULL,t.cobertura_pct,t.anio_referencia,t.anio_referencia,f.id,'CALCULO_7A7','OK',CURDATE(),t.observaciones,1
FROM tmp_rg_area_7a7 t JOIN rg_areas a ON a.codigo=t.codigo_area JOIN rg_indicadores i ON i.codigo=t.codigo_indicador JOIN rg_fuentes f ON f.codigo=t.fuente_codigo
WHERE t.codigo_indicador='POB_URB';
-- Actualiza los 44 registros existentes publicables de los otros cinco indicadores.
UPDATE rg_datos_area da JOIN rg_areas a ON a.id=da.area_id JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id JOIN tmp_rg_area_7a7 t ON t.codigo_area=a.codigo AND t.codigo_indicador=i.codigo
JOIN rg_fuentes f ON f.codigo=t.fuente_codigo
SET da.anio_referencia=t.anio_referencia,da.valor=t.valor,da.metodo_calculo=t.metodo_calculo,
 da.porcentaje_cobertura=t.cobertura_pct,da.anio_minimo=t.anio_referencia,da.anio_maximo=t.anio_referencia,
 da.fuente_principal_id=f.id,da.tipo_procedencia='CALCULO_7A7',da.estado_dato='OK',da.fecha_calculo=CURDATE(),da.observaciones=t.observaciones,da.activo=1
WHERE p.codigo='RG2025_V1' AND t.codigo_indicador<>'POB_URB' AND NOT (i.codigo='ECO_PC' AND a.codigo='MDE');
-- Retira el dato antiguo parcial, sin sustituirlo por cero o NULL.
UPDATE rg_datos_area da JOIN rg_areas a ON a.id=da.area_id JOIN rg_indicadores i ON i.id=da.indicador_id JOIN rg_periodos p ON p.id=da.periodo_id
SET da.activo=0,da.estado_dato='NO_PUBLICABLE',da.observaciones='Retirado de publicación en Fase 7A.7: cobertura 93.5486%; Siria sin PIB nominal comparable.'
WHERE p.codigo='RG2025_V1' AND i.codigo='ECO_PC' AND a.codigo='MDE' AND da.activo=1;
-- Validaciones dentro de la transacción: si alguna devuelve discrepancias, hacer ROLLBACK manual.
SELECT i.codigo,COUNT(*) AS activos,COUNT(DISTINCT a.codigo) AS areas,SUM(da.valor IS NULL) AS nulos
FROM rg_datos_area da JOIN rg_indicadores i ON i.id=da.indicador_id JOIN rg_areas a ON a.id=da.area_id JOIN rg_periodos p ON p.id=da.periodo_id
WHERE da.activo=1 AND p.codigo='RG2025_V1' AND i.codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH') GROUP BY i.codigo;
-- El operador debe confirmar los resultados esperados.
-- NO HAY COMMIT AUTOMATICO: detenerse aquí, revisar los SELECT y confirmar manualmente solo tras autorización.
