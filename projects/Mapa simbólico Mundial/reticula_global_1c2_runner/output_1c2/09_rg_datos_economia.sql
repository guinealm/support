-- 09_rg_datos_economia.sql
SET NAMES utf8mb4;
START TRANSACTION;

DROP TEMPORARY TABLE IF EXISTS tmp_rg_economia_pais;
CREATE TEMPORARY TABLE tmp_rg_economia_pais (codigo_iso3 VARCHAR(3) NOT NULL PRIMARY KEY, anio_pib SMALLINT NOT NULL, pib_usd DECIMAL(22,2) NOT NULL, observaciones TEXT NULL) ENGINE=InnoDB;

INSERT INTO tmp_rg_economia_pais (codigo_iso3,anio_pib,pib_usd,observaciones) VALUES
('AFG',2024,17778508875.74,NULL),
('ALB',2024,27037474263.3,NULL),
('DZA',2024,269322281664.77,NULL),
('AND',2024,4044249678.66,NULL),
('AGO',2024,103080538044.06,NULL),
('ATG',2024,2162366666.67,NULL),
('AZE',2024,74426000000.0,NULL),
('ARG',2024,638365455340.04,NULL),
('AUS',2024,1757022451652.83,NULL),
('AUT',2024,534790720466.82,NULL),
('BHS',2024,15832800000.0,NULL),
('BHR',2024,47210732712.77,NULL),
('BGD',2024,450119432068.85,NULL),
('ARM',2024,25955275380.03,NULL),
('BRB',2024,7597571450.0,NULL),
('BEL',2024,670983130618.83,NULL),
('BMU',2024,9194499000.0,NULL),
('BTN',2024,3346603858.75,NULL),
('BOL',2024,54881327452.97,NULL),
('BIH',2024,29737363103.05,NULL),
('BWA',2024,19286251067.51,NULL),
('BRA',2024,2185821610689.31,NULL),
('BLZ',2024,3203631800.0,NULL),
('SLB',2024,1583964703.75,NULL),
('BRN',2024,15340808592.48,NULL),
('BGR',2024,113349149166.79,NULL),
('MMR',2024,74068349523.81,NULL),
('BDI',2024,3037579858.38,NULL),
('BLR',2024,78591839299.71,NULL),
('KHM',2024,46352647037.24,NULL),
('CMR',2024,53296694320.21,NULL),
('CAN',2024,2270076189683.46,NULL),
('CPV',2024,2713721857.39,NULL),
('CYM',2024,7765336505.34,NULL),
('CAF',2024,2751494281.07,NULL),
('LKA',2024,99616111265.76,NULL),
('TCD',2024,19906706689.76,NULL),
('CHL',2024,329260633698.73,NULL),
('CHN',2024,18729668435848.0,'WDI reporta CHN separado; revisar consistencia con HKG/MAC.'),
('COL',2024,420504033143.21,NULL),
('COM',2024,1610082688.27,NULL),
('COG',2024,15719986076.65,NULL),
('COD',2024,75716176105.07,NULL),
('CRI',2024,96715644330.66,NULL),
('HRV',2024,92981894167.97,NULL),
('CYP',2024,37634551820.74,NULL),
('CZE',2024,347082562221.38,NULL),
('BEN',2024,21482643706.42,NULL),
('DNK',2024,424524722037.05,NULL),
('DMA',2024,688881481.48,NULL),
('DOM',2024,124282245638.57,NULL),
('ECU',2024,123802374000.0,NULL),
('SLV',2024,34879730000.0,NULL),
('GNQ',2024,13254388261.13,NULL),
('ETH',2024,149740297952.38,NULL),
('EST',2024,43130419829.35,NULL),
('FRO',2024,4052937169.77,NULL),
('FJI',2024,5968125909.27,NULL),
('FIN',2024,298729432711.72,NULL),
('FRA',2024,3160442622465.08,NULL),
('PYF',2024,6323716355.05,NULL),
('DJI',2024,4152145939.98,NULL),
('GAB',2024,20895684425.68,NULL),
('GEO',2024,34189423333.14,NULL),
('GMB',2024,2404888737.55,NULL),
('PSE',2024,16016900000.0,NULL),
('DEU',2024,4685592577804.69,NULL),
('GHA',2024,83288585604.03,NULL),
('KIR',2024,343153235.08,NULL),
('GRC',2024,256238371778.12,NULL),
('GRL',2023,3326543974.39,'Fallback a 2023 por ausencia de 2024.'),
('GRD',2024,1351270370.37,NULL),
('GTM',2024,113215575150.88,NULL),
('GIN',2024,25008678293.41,NULL),
('GUY',2024,24662714628.3,NULL),
('HTI',2024,24255657481.25,NULL),
('HND',2024,36980171442.06,NULL),
('HKG',2024,408368682415.42,'WDI reporta HKG separado de CHN.'),
('HUN',2024,222848211034.37,NULL),
('ISL',2024,33186621855.01,NULL),
('IND',2024,3760813470500.86,NULL),
('IDN',2024,1396301788461.69,NULL),
('IRN',2024,475252089215.42,NULL),
('IRQ',2024,279641257615.39,NULL),
('IRL',2024,609157459747.2,NULL),
('ISR',2024,542284494490.78,NULL),
('ITA',2024,2383435562458.12,NULL),
('CIV',2024,87113179149.28,NULL),
('JAM',2024,22014429051.0,NULL),
('JPN',2024,4190008188358.57,NULL),
('KAZ',2024,291480274648.83,NULL),
('JOR',2024,58618380563.38,NULL),
('KEN',2024,120397537849.83,NULL),
('KOR',2024,1875388209406.8,NULL),
('KWT',2024,160903106639.23,NULL),
('KGZ',2024,18161630698.91,NULL),
('LAO',2024,16502933121.34,NULL),
('LBN',2024,25971643441.34,NULL),
('LSO',2024,2391282547.8,NULL),
('LVA',2024,44001275012.61,NULL),
('LBR',2024,4779300900.0,NULL),
('LBY',2024,48487151215.35,NULL),
('LIE',2024,8905764270.41,NULL),
('LTU',2024,85503938573.57,NULL),
('LUX',2024,93279851863.41,NULL),
('MAC',2024,49467258923.32,'WDI reporta MAC separado de CHN.'),
('MDG',2024,17592832696.13,NULL),
('MWI',2024,11311971400.39,NULL),
('MYS',2024,422227005428.69,NULL),
('MDV',2024,7061608267.25,NULL),
('MLI',2024,26761281076.77,NULL),
('MLT',2024,25042712191.33,NULL),
('MRT',2024,10879212033.48,NULL),
('MUS',2024,14938055690.36,NULL),
('MEX',2024,1830489311088.89,NULL),
('MCO',2024,11125788838.28,NULL),
('MNG',2024,23794540024.51,NULL),
('MDA',2024,18206842140.76,NULL),
('MNE',2024,8274290505.96,NULL),
('MAR',2024,160610994054.73,NULL),
('MOZ',2024,22752244245.47,NULL),
('OMN',2024,107137198699.61,NULL),
('NAM',2024,13641190683.46,NULL),
('NRU',2024,167833414.85,NULL),
('NPL',2024,43298911699.93,NULL),
('NLD',2024,1213936238063.28,NULL),
('CUW',2024,3561178212.29,NULL),
('ABW',2024,4167588070.29,NULL),
('SXM',2024,1797836648.04,NULL),
('NCL',2024,8548919387.13,NULL),
('VUT',2024,1297956614.78,NULL),
('NZL',2024,261497198363.91,NULL),
('NIC',2024,19696311850.33,NULL),
('NER',2024,19729786046.76,NULL),
('NGA',2024,252261880140.27,NULL),
('NOR',2024,500886328034.12,NULL),
('FSM',2024,481121300.0,NULL),
('MHL',2024,285000000.0,NULL),
('PLW',2024,321501812.5,NULL),
('PAK',2024,371747087751.31,NULL),
('PAN',2024,86523959100.0,NULL),
('PNG',2024,30803971189.41,NULL),
('PRY',2024,44738819362.33,NULL),
('PER',2024,291751523018.9,NULL),
('PHL',2024,461671157904.74,NULL),
('POL',2024,917767106146.76,NULL),
('PRT',2024,313656884870.86,NULL),
('GNB',2024,2197777209.94,NULL),
('TLS',2024,1865608515.41,NULL),
('PRI',2024,126029527033.71,NULL),
('QAT',2024,216294505494.51,NULL),
('ROU',2024,382564217988.87,NULL),
('RUS',2024,2186462268813.08,NULL),
('RWA',2024,15111064181.97,NULL),
('KNA',2024,1122388888.89,NULL),
('LCA',2024,2605148148.15,NULL),
('VCT',2024,1157207407.41,NULL),
('SMR',2023,2027243193.51,'Fallback a 2023 por ausencia de 2024.'),
('STP',2024,824992558.05,NULL),
('SAU',2024,1254140800000.0,NULL),
('SEN',2024,32169996051.85,NULL),
('SRB',2024,90088366320.41,NULL),
('SYC',2024,2228608684.3,NULL),
('SLE',2024,6971127234.07,NULL),
('SGP',2024,572877260178.43,NULL),
('SVK',2024,140934076532.38,NULL),
('VNM',2024,476324572783.81,NULL),
('SVN',2024,72972015197.39,NULL),
('SOM',2024,11967000000.0,NULL),
('ZAF',2024,401144998373.59,NULL),
('ZWE',2024,41521975830.24,NULL),
('ESP',2024,1725671652742.19,NULL),
('SDN',2024,49672435513.11,NULL),
('SUR',2024,4416775112.72,NULL),
('SWZ',2024,4858885840.77,NULL),
('SWE',2024,604827393488.58,NULL),
('CHE',2024,969919786394.88,NULL),
('TJK',2024,14425113699.79,NULL),
('THA',2024,529385520941.54,NULL),
('TGO',2024,10643440332.24,NULL),
('TON',2024,647488243.85,NULL),
('TTO',2024,25633544529.48,NULL),
('ARE',2024,552324919095.87,NULL),
('TUN',2024,51412122479.85,NULL),
('TUR',2024,1359123768774.12,NULL),
('TKM',2024,44249447717.23,NULL),
('TCA',2024,1745378000.0,NULL),
('TUV',2024,56752265.8,NULL),
('UGA',2024,53911907079.05,NULL),
('UKR',2024,190833835445.1,NULL),
('MKD',2024,16951682221.4,NULL),
('EGY',2024,389059910593.1,NULL),
('GBR',2024,3695539513534.15,NULL),
('IMN',2023,7576129932.79,'Fallback a 2023 por ausencia de 2024.'),
('TZA',2024,79235713444.98,NULL),
('USA',2024,29298013000000.0,NULL),
('BFA',2024,23136514855.76,NULL),
('URY',2024,82322859144.28,NULL),
('UZB',2024,121356065241.23,NULL),
('VEN',2024,120566112397.06,NULL),
('WSM',2024,1175749785.65,NULL),
('ZMB',2024,25303185342.25,NULL),
('XKX',2024,11203038332.34,'WDI publica XKX separado; mantener separado de SRB sin duplicidad.');

SET @ind_eco_pib := (SELECT id FROM rg_indicadores WHERE codigo='ECO_PIB');
SET @src_wb := (SELECT id FROM rg_fuentes WHERE codigo='WB_WDI');
SET @next_pais_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_pais);
INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_eco_pib, t.anio_pib, t.pib_usd, @src_wb,
       'FUENTE_VALIDADA', 'OK', CURDATE(), t.observaciones, 1
FROM tmp_rg_economia_pais t
JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_eco_pib AND d.anio=t.anio_pib
WHERE d.id IS NULL;

UPDATE rg_datos_pais d
JOIN rg_paises p ON p.id=d.pais_id
JOIN tmp_rg_economia_pais t ON t.codigo_iso3=p.codigo_iso3 AND t.anio_pib=d.anio
SET d.valor=t.pib_usd,
    d.fuente_id=@src_wb,
    d.tipo_procedencia='FUENTE_VALIDADA',
    d.estado_dato='OK',
    d.fecha_carga=CURDATE(),
    d.observaciones=t.observaciones,
    d.activo=1
WHERE d.indicador_id=@ind_eco_pib;

DROP TEMPORARY TABLE IF EXISTS tmp_rg_economia_area;
CREATE TEMPORARY TABLE tmp_rg_economia_area (area_codigo VARCHAR(10) PRIMARY KEY, anio_ref SMALLINT NOT NULL, pib_usd DECIMAL(22,2) NULL, pib_mundial_pct DECIMAL(12,8) NULL, pib_pc DECIMAL(22,8) NULL, entidades_totales SMALLINT NULL, entidades_con_pib SMALLINT NULL, cobertura_pct DECIMAL(8,4) NULL, anio_minimo SMALLINT NULL, anio_maximo SMALLINT NULL, observaciones TEXT NULL) ENGINE=InnoDB;

INSERT INTO tmp_rg_economia_area (area_codigo,anio_ref,pib_usd,pib_mundial_pct,pib_pc,entidades_totales,entidades_con_pib,cobertura_pct,anio_minimo,anio_maximo,observaciones) VALUES
('AFR',2024,2901688380908.9,2.62278935,1873.58271703,59,52,98.8622,2024,2024,'Cobertura incompleta en entidades. Cobertura poblacional alta.'),
('APC',2024,12178633494512.9,11.00807047,12495.86427647,43,30,94.8727,2024,2024,'Cobertura incompleta en entidades. Cobertura poblacional aceptable.'),
('CHN',2024,19187504377186.75,17.34327587,13472.3446556,3,3,100.0,2024,2024,'Cobertura poblacional alta.'),
('EUR',2024,25130676006233.32,22.71521289,42515.04924374,51,45,99.9646,2023,2024,'Cobertura incompleta en entidades. Cobertura poblacional alta. Mezcla de anios 2023/2024 por faltantes.'),
('MDE',2024,5094919796742.41,4.60521587,13124.89570887,15,13,82.6387,2024,2024,'Cobertura incompleta en entidades. Cobertura poblacional condicionada.'),
('NAC',2024,34176084923003.62,30.89121218,55362.73991924,41,30,98.0775,2023,2024,'Cobertura incompleta en entidades. Cobertura poblacional alta. Mezcla de anios 2023/2024 por faltantes.'),
('RUE',2024,2889297338831.94,2.61158928,11386.41396029,10,10,100.0,2024,2024,'Cobertura poblacional alta.'),
('SAI',2024,4753781734288.45,4.29686667,2385.49047682,8,8,100.0,2024,2024,'Cobertura poblacional alta.'),
('SAM',2024,4321094237987.85,3.90576742,9863.13814022,14,12,99.9276,2024,2024,'Cobertura incompleta en entidades. Cobertura poblacional alta.');

SET @per := (SELECT id FROM rg_periodos WHERE codigo='RG2025_V1');
SET @ind_area_pib := (SELECT id FROM rg_indicadores WHERE codigo='ECO_PIB');
SET @ind_area_pct := (SELECT id FROM rg_indicadores WHERE codigo='ECO_PIB_PCT');
SET @ind_area_pc := (SELECT id FROM rg_indicadores WHERE codigo='ECO_PC');
SET @next_area_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_area);

INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)
SELECT (@next_area_id := @next_area_id + 1), a.id, @ind_area_pib, @per, t.anio_ref, t.pib_usd,
       'Suma PIB nacional incluido', t.entidades_totales, t.entidades_con_pib, t.cobertura_pct, t.anio_minimo, t.anio_maximo, @src_wb,
       'AGREGADO_1C3', CASE WHEN t.cobertura_pct >= 90 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_economia_area t
JOIN rg_areas a ON a.codigo=t.area_codigo
LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=@ind_area_pib AND d.periodo_id=@per AND d.anio_referencia=t.anio_ref
WHERE d.id IS NULL;

INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)
SELECT (@next_area_id := @next_area_id + 1), a.id, @ind_area_pct, @per, t.anio_ref, t.pib_mundial_pct,
       'PIB area / PIB total nueve areas * 100', t.entidades_totales, t.entidades_con_pib, t.cobertura_pct, t.anio_minimo, t.anio_maximo, @src_wb,
       'AGREGADO_1C3', CASE WHEN t.cobertura_pct >= 90 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_economia_area t
JOIN rg_areas a ON a.codigo=t.area_codigo
LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=@ind_area_pct AND d.periodo_id=@per AND d.anio_referencia=t.anio_ref
WHERE d.id IS NULL;

INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)
SELECT (@next_area_id := @next_area_id + 1), a.id, @ind_area_pc, @per, t.anio_ref, t.pib_pc,
       'PIB area / poblacion 2025 area', t.entidades_totales, t.entidades_con_pib, t.cobertura_pct, t.anio_minimo, t.anio_maximo, @src_wb,
       'AGREGADO_1C3', CASE WHEN t.cobertura_pct >= 90 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_economia_area t
JOIN rg_areas a ON a.codigo=t.area_codigo
LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=@ind_area_pc AND d.periodo_id=@per AND d.anio_referencia=t.anio_ref
WHERE d.id IS NULL;

-- Actualizacion idempotente de los 27 registros economicos
UPDATE rg_datos_area d
JOIN rg_areas a ON a.id=d.area_id
JOIN tmp_rg_economia_area t ON t.area_codigo=a.codigo
SET d.valor=CASE
      WHEN d.indicador_id=@ind_area_pib THEN t.pib_usd
      WHEN d.indicador_id=@ind_area_pct THEN t.pib_mundial_pct
      WHEN d.indicador_id=@ind_area_pc THEN t.pib_pc
      ELSE d.valor END,
    d.metodo_calculo=CASE
      WHEN d.indicador_id=@ind_area_pib THEN 'Suma PIB nacional incluido'
      WHEN d.indicador_id=@ind_area_pct THEN 'PIB area / PIB total nueve areas * 100'
      WHEN d.indicador_id=@ind_area_pc THEN 'PIB area / poblacion 2025 area'
      ELSE d.metodo_calculo END,
    d.paises_totales=t.entidades_totales,
    d.paises_con_dato=t.entidades_con_pib,
    d.porcentaje_cobertura=t.cobertura_pct,
    d.anio_minimo=t.anio_minimo,
    d.anio_maximo=t.anio_maximo,
    d.fuente_principal_id=@src_wb,
    d.tipo_procedencia='AGREGADO_1C3',
    d.estado_dato=CASE WHEN t.cobertura_pct >= 90 THEN 'OK' ELSE 'LIMITACION' END,
    d.fecha_calculo=CURDATE(),
    d.observaciones=t.observaciones,
    d.activo=1
WHERE d.periodo_id=@per AND d.anio_referencia=2024 AND d.indicador_id IN (@ind_area_pib,@ind_area_pct,@ind_area_pc);

COMMIT;