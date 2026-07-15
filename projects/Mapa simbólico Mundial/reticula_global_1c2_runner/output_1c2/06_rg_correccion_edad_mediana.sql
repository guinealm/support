-- 06_rg_correccion_edad_mediana.sql
-- Correccion incremental 1C.2B.1: carga de edad mediana nacional y actualizacion de POB_EDAD por area
SET NAMES utf8mb4;
START TRANSACTION;

DROP TEMPORARY TABLE IF EXISTS tmp_rg_edad_mediana_2025;
CREATE TEMPORARY TABLE tmp_rg_edad_mediana_2025 (codigo_iso3 VARCHAR(3) NOT NULL PRIMARY KEY, anio SMALLINT NOT NULL, valor DECIMAL(10,4) NOT NULL) ENGINE=MEMORY;

INSERT INTO tmp_rg_edad_mediana_2025 (codigo_iso3,anio,valor) VALUES
('ABW',2023,41.0200),
('AFG',2023,16.9400),
('AGO',2023,16.4520),
('AIA',2023,38.0130),
('ALB',2023,36.2770),
('AND',2023,43.1620),
('ARE',2023,31.2320),
('ARG',2023,32.1220),
('ARM',2023,35.8320),
('ASM',2023,28.4350),
('ATG',2023,35.4860),
('AUS',2023,37.7510),
('AUT',2023,43.0860),
('AZE',2023,32.5960),
('BDI',2023,15.9020),
('BEL',2023,41.4400),
('BEN',2023,17.7720),
('BES',2023,39.6650),
('BFA',2023,17.2540),
('BGD',2023,25.3250),
('BGR',2023,44.3140),
('BHR',2023,32.8760),
('BHS',2023,34.5970),
('BIH',2023,44.9150),
('BLM',2023,38.8100),
('BLR',2023,40.5350),
('BLZ',2023,25.9460),
('BMU',2023,45.1400),
('BOL',2023,24.6640),
('BRA',2023,33.9420),
('BRB',2023,38.9050),
('BRN',2023,31.7600),
('BTN',2023,29.3880),
('BWA',2023,22.8820),
('CAF',2023,14.3200),
('CAN',2023,40.3430),
('CHE',2023,42.3310),
('CHL',2023,35.9690),
('CHN',2023,39.0660),
('CIV',2023,18.0970),
('CMR',2023,17.7520),
('COD',2023,15.7680),
('COG',2023,18.3080),
('COK',2023,35.0750),
('COL',2023,31.6060),
('COM',2023,20.3310),
('CPV',2023,27.8700),
('CRI',2023,34.0700),
('CUB',2023,41.7090),
('CUW',2023,38.2310),
('CYM',2023,37.8750),
('CYP',2023,37.7560),
('CZE',2023,42.7160),
('DEU',2023,45.1470),
('DJI',2023,24.3890),
('DMA',2023,35.6180),
('DNK',2023,41.2490),
('DOM',2023,27.6530),
('DZA',2023,28.1890),
('ECU',2023,28.4060),
('EGY',2023,24.0280),
('ERI',2023,18.6510),
('ESH',2023,32.0370),
('ESP',2023,44.9030),
('EST',2023,41.8900),
('ETH',2023,18.7330),
('FIN',2023,42.7890),
('FJI',2023,27.6660),
('FLK',2023,41.5350),
('FRA',2023,41.8170),
('FRO',2023,37.2580),
('FSM',2023,22.8500),
('GAB',2023,21.5030),
('GBR',2023,39.7820),
('GEO',2023,36.7960),
('GGY',2023,43.9780),
('GHA',2023,20.9310),
('GIB',2023,38.8820),
('GIN',2023,17.9840),
('GLP',2023,46.5740),
('GMB',2023,18.1700),
('GNB',2023,18.9430),
('GNQ',2023,20.9790),
('GRC',2023,45.7470),
('GRD',2023,33.3850),
('GRL',2023,34.2290),
('GTM',2023,22.6300),
('GUF',2023,25.2210),
('GUM',2023,31.1200),
('GUY',2023,25.6070),
('HKG',2023,46.1550),
('HND',2023,23.5460),
('HRV',2023,44.7610),
('HTI',2023,23.5110),
('HUN',2023,43.3170),
('IDN',2023,29.8310),
('IMN',2023,45.6760),
('IND',2023,28.0600),
('IRL',2023,38.4160),
('IRN',2023,32.8660),
('IRQ',2023,20.3450),
('ISL',2023,35.8080),
('ISR',2023,29.1500),
('ITA',2023,47.4610),
('JAM',2023,31.6730),
('JEY',2023,43.1010),
('JOR',2023,24.2790),
('JPN',2023,48.9580),
('KAZ',2023,29.4640),
('KEN',2023,19.5260),
('KGZ',2023,25.1270),
('KHM',2023,25.8440),
('KIR',2023,22.6860),
('KNA',2023,35.3490),
('KOR',2023,44.4860),
('KWT',2023,34.4990),
('LAO',2023,24.2840),
('LBN',2023,28.3230),
('LBR',2023,18.3580),
('LBY',2023,27.1960),
('LCA',2023,33.7450),
('LIE',2023,44.1990),
('LKA',2023,32.8120),
('LSO',2023,21.4270),
('LTU',2023,42.1190),
('LUX',2023,38.8920),
('LVA',2023,43.0780),
('MAC',2023,38.3100),
('MAF',2023,39.3630),
('MAR',2023,29.1940),
('MCO',2023,54.3560),
('MDA',2023,37.7540),
('MDG',2023,18.8770),
('MDV',2023,31.1240),
('MEX',2023,28.8860),
('MHL',2023,20.6990),
('MKD',2023,40.2600),
('MLI',2023,15.4660),
('MLT',2023,40.2810),
('MMR',2023,29.5340),
('MNE',2023,39.2910),
('MNG',2023,26.7520),
('MNP',2023,36.1360),
('MOZ',2023,16.3230),
('MRT',2023,17.1190),
('MSR',2023,41.5460),
('MTQ',2023,48.7880),
('MUS',2023,36.9330),
('MWI',2023,17.5800),
('MYS',2023,30.0580),
('MYT',2023,16.7860),
('NAM',2023,20.9570),
('NCL',2023,33.8910),
('NER',2023,15.2500),
('NGA',2023,17.7540),
('NIC',2023,25.2670),
('NIU',2023,36.5550),
('NLD',2023,41.3960),
('NOR',2023,39.5400),
('NPL',2023,24.6790),
('NRU',2023,20.4340),
('NZL',2023,37.2800),
('OMN',2023,29.2680),
('PAK',2023,20.2870),
('PAN',2023,29.6030),
('PER',2023,29.4510),
('PHL',2023,25.2870),
('PLW',2023,37.8430),
('PNG',2023,22.3440),
('POL',2023,41.3100),
('PRI',2023,45.3060),
('PRK',2023,36.0480),
('PRT',2023,46.2000),
('PRY',2023,26.3410),
('PSE',2023,19.7630),
('PYF',2023,34.7910),
('QAT',2023,33.1890),
('REU',2023,37.4300),
('ROU',2023,42.6210),
('RUS',2023,39.4540),
('RWA',2023,19.4400),
('SAU',2023,29.2470),
('SDN',2023,18.2760),
('SEN',2023,19.1290),
('SGP',2023,35.1020),
('SHN',2023,50.4500),
('SLB',2023,20.2510),
('SLE',2023,19.2700),
('SLV',2023,26.9560),
('SMR',2023,47.3930),
('SOM',2023,15.4470),
('SPM',2023,46.4030),
('SRB',2023,43.8720),
('SSD',2023,17.9700),
('STP',2023,19.0520),
('SUR',2023,28.1000),
('SVK',2023,41.3020),
('SVN',2023,43.8940),
('SWE',2023,39.9130),
('SWZ',2023,21.9950),
('SXM',2023,41.5870),
('SYC',2023,33.6530),
('SYR',2023,22.2490),
('TCA',2023,38.2980),
('TCD',2023,15.4010),
('TGO',2023,18.1440),
('THA',2023,39.6580),
('TJK',2023,21.9250),
('TKL',2023,26.6500),
('TKM',2023,26.2320),
('TLS',2023,20.9690),
('TON',2023,20.6950),
('TTO',2023,36.7180),
('TUN',2023,32.1270),
('TUR',2023,32.5200),
('TUV',2023,24.2860),
('TWN',2023,43.5380),
('TZA',2023,17.2400),
('UGA',2023,16.5140),
('UKR',2023,41.9840),
('URY',2023,35.7790),
('USA',2023,38.0230),
('UZB',2023,26.9140),
('VAT',2023,59.6250),
('VCT',2023,33.8970),
('VEN',2023,29.0250),
('VGB',2023,37.5460),
('VIR',2023,44.6670),
('VNM',2023,32.4290),
('VUT',2023,20.1430),
('WLF',2023,37.1660),
('WSM',2023,19.9040),
('YEM',2023,18.1840),
('ZAF',2023,28.2130),
('ZMB',2023,17.4900),
('ZWE',2023,17.8080);

-- Inserta POB_EDAD solo para paises sin registro previo en (pais_id, indicador_id, anio)
SET @next_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_pais);
INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_id := @next_id + 1) AS id, p.id, i.id, t.anio, t.valor, f.id, 'FUENTE_VALIDADA', 'OK', CURDATE(),
       'Edad mediana aproximada: ultimo dato disponible <= 2025 (OWID).', 1
FROM tmp_rg_edad_mediana_2025 t
JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
JOIN rg_indicadores i ON i.codigo='POB_EDAD'
JOIN rg_fuentes f ON f.codigo='OWID'
LEFT JOIN rg_datos_pais dp ON dp.pais_id=p.id AND dp.indicador_id=i.id AND dp.anio=t.anio
WHERE dp.id IS NULL;

-- Si ya existian filas de POB_EDAD, actualiza valor y metadatos en lugar de duplicar
UPDATE rg_datos_pais dp
JOIN rg_paises p ON p.id=dp.pais_id
JOIN rg_indicadores i ON i.id=dp.indicador_id AND i.codigo='POB_EDAD'
JOIN rg_fuentes f ON f.codigo='OWID'
JOIN tmp_rg_edad_mediana_2025 t ON t.codigo_iso3=p.codigo_iso3 AND t.anio=dp.anio
SET dp.valor=t.valor,
    dp.fuente_id=f.id,
    dp.tipo_procedencia='FUENTE_VALIDADA',
    dp.estado_dato='OK',
    dp.fecha_carga=CURDATE(),
    dp.observaciones='Edad mediana aproximada: ultimo dato disponible <= 2025 (OWID).',
    dp.activo=1;

-- Cobertura y agregacion ponderada por area (sin media simple)
DROP TEMPORARY TABLE IF EXISTS tmp_rg_area_edad_cobertura;
CREATE TEMPORARY TABLE tmp_rg_area_edad_cobertura AS
SELECT a.id AS area_id,
       COUNT(p.id) AS paises_totales,
       SUM(CASE WHEN de.valor IS NOT NULL AND dp.valor IS NOT NULL AND dp.valor>0 THEN 1 ELSE 0 END) AS paises_con_dato
FROM rg_areas a
LEFT JOIN rg_paises p ON p.area_id=a.id AND p.activo=1
LEFT JOIN rg_indicadores ie ON ie.codigo='POB_EDAD'
LEFT JOIN rg_indicadores ip ON ip.codigo='POB_TOTAL'
LEFT JOIN rg_datos_pais de ON de.pais_id=p.id AND de.indicador_id=ie.id AND de.anio=2023 AND de.activo=1
LEFT JOIN rg_datos_pais dp ON dp.pais_id=p.id AND dp.indicador_id=ip.id AND dp.anio=2025 AND dp.activo=1
GROUP BY a.id;

DROP TEMPORARY TABLE IF EXISTS tmp_rg_area_edad_valor;
CREATE TEMPORARY TABLE tmp_rg_area_edad_valor AS
SELECT p.area_id,
       SUM(de.valor * dp.valor) / NULLIF(SUM(dp.valor),0) AS valor_edad
FROM rg_paises p
JOIN rg_indicadores ie ON ie.codigo='POB_EDAD'
JOIN rg_indicadores ip ON ip.codigo='POB_TOTAL'
JOIN rg_datos_pais de ON de.pais_id=p.id AND de.indicador_id=ie.id AND de.anio=2023 AND de.activo=1 AND de.valor IS NOT NULL
JOIN rg_datos_pais dp ON dp.pais_id=p.id AND dp.indicador_id=ip.id AND dp.anio=2025 AND dp.activo=1 AND dp.valor IS NOT NULL AND dp.valor>0
WHERE p.activo=1
GROUP BY p.area_id;

-- Actualiza solo POB_EDAD en rg_datos_area (9 filas existentes)
UPDATE rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id AND i.codigo='POB_EDAD'
JOIN rg_areas a ON a.id=da.area_id
LEFT JOIN tmp_rg_area_edad_valor v ON v.area_id=a.id
LEFT JOIN tmp_rg_area_edad_cobertura c ON c.area_id=a.id
JOIN rg_fuentes f ON f.codigo='OWID'
SET da.valor=v.valor_edad,
    da.metodo_calculo='Media ponderada aproximada por poblacion 2025 (edad 2023 OWID)',
    da.paises_totales=c.paises_totales,
    da.paises_con_dato=c.paises_con_dato,
    da.porcentaje_cobertura=CASE WHEN c.paises_totales>0 THEN ROUND((c.paises_con_dato*100.0)/c.paises_totales,4) ELSE NULL END,
    da.anio_minimo=2023,
    da.anio_maximo=2023,
    da.fuente_principal_id=f.id,
    da.tipo_procedencia='AGREGADO_1C2B_CORRECCION',
    da.estado_dato=CASE WHEN v.valor_edad IS NULL THEN 'LIMITACION'
                        WHEN c.paises_totales>0 AND ((c.paises_con_dato*100.0)/c.paises_totales)>=90 THEN 'OK'
                        ELSE 'LIMITACION' END,
    da.fecha_calculo=CURDATE(),
    da.observaciones='Edad mediana aproximada; ultimo dato disponible <=2025 (actualmente 2023), ponderado por poblacion 2025.'
WHERE da.activo=1;

COMMIT;