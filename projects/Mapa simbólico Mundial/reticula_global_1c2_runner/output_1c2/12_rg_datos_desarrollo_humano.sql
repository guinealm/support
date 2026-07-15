-- 12_rg_datos_desarrollo_humano.sql
SET NAMES utf8mb4;
START TRANSACTION;

DROP TEMPORARY TABLE IF EXISTS tmp_rg_humano_pais;
CREATE TEMPORARY TABLE tmp_rg_humano_pais (codigo_iso3 VARCHAR(3) PRIMARY KEY, anio_idh SMALLINT NULL, idh DECIMAL(10,6) NULL, anio_gini SMALLINT NULL, gini DECIMAL(10,6) NULL, anio_ev SMALLINT NULL, ev DECIMAL(10,6) NULL, observaciones TEXT NULL) ENGINE=InnoDB;

INSERT INTO tmp_rg_humano_pais (codigo_iso3,anio_idh,idh,anio_gini,gini,anio_ev,ev,observaciones) VALUES
('AFG',2023,0.496,NULL,NULL,2023,66.035,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('ALB',2023,0.81,2020,29.4,2023,79.602,NULL),
('DZA',2023,0.763,NULL,NULL,2023,76.261,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('ASM',NULL,NULL,NULL,NULL,2023,72.852,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('AND',2023,0.913,NULL,NULL,2023,84.041,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('AGO',2023,0.616,2018,51.3,2023,64.617,'Gini seleccionado en 2015-2018 (antiguo).'),
('ATG',2023,0.851,NULL,NULL,2023,77.598,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('AZE',2023,0.789,NULL,NULL,2023,74.429,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('ARG',2023,0.865,2024,42.4,2023,77.395,NULL),
('AUS',2023,0.958,2020,33.8,2023,83.05122,NULL),
('AUT',2023,0.93,2023,31.2,2023,81.792683,NULL),
('BHS',2023,0.82,NULL,NULL,2023,74.552,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('BHR',2023,0.899,NULL,NULL,2023,81.284,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('BGD',2023,0.685,2022,30.9,2023,74.672,NULL),
('ARM',2023,0.811,2024,27.4,2023,77.465854,NULL),
('BRB',2023,0.811,2016,34.1,2023,76.178,'Gini seleccionado en 2015-2018 (antiguo).'),
('BEL',2023,0.951,2023,26.8,2023,82.4,NULL),
('BMU',NULL,NULL,NULL,NULL,2023,82.309,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('BTN',2023,0.698,2022,28.5,2023,72.975,NULL),
('BOL',2023,0.733,2024,40.9,2023,68.581,NULL),
('BIH',2023,0.804,2021,30.3,2023,77.85,NULL),
('BWA',2023,0.731,2015,54.9,2023,69.163,'Gini seleccionado en 2015-2018 (antiguo).'),
('BRA',2023,0.786,2024,50.3,2023,75.848,NULL),
('BLZ',2023,0.721,2018,39.9,2023,73.566,'Gini seleccionado en 2015-2018 (antiguo).'),
('IOT',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('SLB',2023,0.584,NULL,NULL,2023,70.528,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('VGB',NULL,NULL,NULL,NULL,2023,77.276,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('BRN',2023,0.837,NULL,NULL,2023,75.327,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('BGR',2023,0.845,2023,39.5,2023,75.756098,NULL),
('MMR',2023,0.609,2017,30.7,2023,66.889,'Gini seleccionado en 2015-2018 (antiguo).'),
('BDI',2023,0.439,2020,37.5,2023,63.651,NULL),
('BLR',2023,0.824,2020,24.4,2023,74.18378,NULL),
('KHM',2023,0.606,NULL,NULL,2023,70.668,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('CMR',2023,0.588,2021,42.2,2023,63.7,NULL),
('CAN',2023,0.939,2022,31.5,2023,81.626341,NULL),
('CPV',2023,0.668,2015,42.4,2023,76.059,'Gini seleccionado en 2015-2018 (antiguo).'),
('CYM',NULL,NULL,NULL,NULL,2023,80.358,'Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('CAF',2023,0.414,2021,43.0,2023,57.408,NULL),
('LKA',2023,0.776,2019,37.7,2023,77.483,NULL),
('TCD',2023,0.416,2022,37.4,2023,55.069,NULL),
('CHL',2023,0.878,2024,43.0,2023,81.167,NULL),
('CHN',2023,0.797,2022,36.0,2023,77.953,'CHN tratado separado de HKG y MAC.'),
('TWN',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI. TWN revisado expresamente; mantener criterio SEGUN_FUENTE sin duplicidad.'),
('CXR',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('CCK',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('COL',2023,0.788,2024,54.4,2023,77.725,NULL),
('COM',2023,0.603,2024,30.3,2023,66.777,NULL),
('MYT',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('COG',2023,0.649,NULL,NULL,2023,65.772,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('COD',2023,0.522,2020,44.7,2023,61.895,NULL),
('COK',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('CRI',2023,0.833,2024,45.8,2023,80.799,NULL),
('HRV',2023,0.889,2023,30.1,2023,78.473171,NULL),
('CUB',2023,0.762,NULL,NULL,2023,78.085,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('CYP',2023,0.913,2023,31.8,2023,81.648,NULL),
('CZE',2023,0.915,2023,25.7,2023,79.826829,NULL),
('BEN',2023,0.515,2021,34.4,2023,60.774,NULL),
('DNK',2023,0.962,2023,29.9,2023,81.753659,NULL),
('DMA',2023,0.761,NULL,NULL,2023,71.132,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('DOM',2023,0.776,2024,39.0,2023,73.72,NULL),
('ECU',2023,0.777,2024,45.2,2023,77.392,NULL),
('SLV',2023,0.678,2023,39.8,2023,72.099,NULL),
('GNQ',2023,0.674,2022,38.5,2023,63.707,NULL),
('ETH',2023,0.497,2021,31.1,2023,67.315,NULL),
('ERI',2023,0.503,NULL,NULL,2023,68.624,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('EST',2023,0.905,2023,30.7,2023,78.792683,NULL),
('FRO',NULL,NULL,NULL,NULL,2023,82.95212,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('FLK',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('FJI',2023,0.731,2019,30.7,2023,67.316,NULL),
('FIN',2023,0.948,2023,27.4,2023,81.585366,NULL),
('ALA',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('FRA',2023,0.92,2023,31.8,2023,82.831707,NULL),
('GUF',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('PYF',NULL,NULL,NULL,NULL,2023,84.07,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('DJI',2023,0.513,2017,41.6,2023,65.987,'Gini seleccionado en 2015-2018 (antiguo).'),
('GAB',2023,0.733,2017,38.0,2023,68.337,'Gini seleccionado en 2015-2018 (antiguo).'),
('GEO',2023,0.844,2024,33.9,2023,74.496,NULL),
('GMB',2023,0.524,2020,38.8,2023,65.86,NULL),
('PSE',2023,0.674,2023,36.4,2023,65.17,NULL),
('DEU',2023,0.959,2022,33.7,2023,81.041463,NULL),
('GHA',2023,0.628,2016,43.5,2023,65.498,'Gini seleccionado en 2015-2018 (antiguo).'),
('GIB',NULL,NULL,NULL,NULL,2023,83.553,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('KIR',2023,0.644,2023,24.7,2023,66.473,NULL),
('GRC',2023,0.908,2023,33.4,2023,81.736585,NULL),
('GRL',NULL,NULL,NULL,NULL,2023,70.972439,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('GRD',2023,0.791,2018,43.8,2023,75.205,'Gini seleccionado en 2015-2018 (antiguo).'),
('GLP',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('GUM',NULL,NULL,NULL,NULL,2023,77.209,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('GTM',2023,0.662,2023,45.2,2023,72.602,NULL),
('GIN',2023,0.5,2018,29.6,2023,60.74,'Gini seleccionado en 2015-2018 (antiguo).'),
('GUY',2023,0.776,NULL,NULL,2023,70.18,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('HTI',2023,0.554,NULL,NULL,2023,64.936,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('VAT',NULL,NULL,NULL,NULL,NULL,NULL,'Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('HND',2023,0.645,2024,45.7,2023,72.884,NULL),
('HKG',2023,0.955,NULL,NULL,2023,85.247317,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin Gini 2015-2024 usable en WDI/PIP. HKG tratado separado de CHN.'),
('HUN',2023,0.87,2017,30.6,2023,76.570732,'Gini seleccionado en 2015-2018 (antiguo).'),
('ISL',2023,0.972,2019,26.8,2023,82.456098,NULL),
('IND',2023,0.685,2022,25.5,2023,72.003,NULL),
('IDN',2023,0.728,2024,34.9,2023,71.146,NULL),
('IRN',2023,0.799,2023,35.9,2023,77.654,NULL),
('IRQ',2023,0.695,2023,29.8,2023,72.324,NULL),
('IRL',2023,0.949,2023,29.0,2023,82.807317,NULL),
('ISR',2023,0.919,2022,38.3,2023,83.195122,NULL),
('ITA',2023,0.915,2023,34.3,2023,83.35122,NULL),
('CIV',2023,0.582,2021,35.3,2023,61.944,NULL),
('JAM',2023,0.72,2021,39.9,2023,71.479,NULL),
('JPN',2023,0.925,2020,32.3,2023,84.04122,NULL),
('KAZ',2023,0.837,2021,29.2,2023,74.402,NULL),
('JOR',2023,0.754,NULL,NULL,2023,77.814,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('KEN',2023,0.628,2022,38.5,2023,63.646,NULL),
('PRK',NULL,NULL,NULL,NULL,2023,73.642,'Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('KOR',2023,0.937,2021,32.9,2023,83.429268,NULL),
('KWT',2023,0.852,NULL,NULL,2023,83.187805,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('KGZ',2023,0.72,2024,27.5,2023,72.24878,NULL),
('LAO',2023,0.617,2024,34.7,2023,68.964,NULL),
('LBN',2023,0.752,2022,35.5,2023,77.817,NULL),
('LSO',2023,0.55,2017,44.9,2023,57.375,'Gini seleccionado en 2015-2018 (antiguo).'),
('LVA',2023,0.889,2023,34.0,2023,75.426829,NULL),
('LBR',2023,0.51,2016,35.3,2023,62.163,'Gini seleccionado en 2015-2018 (antiguo).'),
('LBY',2023,0.721,NULL,NULL,2023,69.339,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('LIE',2023,0.938,NULL,NULL,2023,84.595122,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('LTU',2023,0.895,2023,36.0,2023,77.290244,NULL),
('LUX',2023,0.922,2023,33.6,2023,83.309756,NULL),
('MAC',NULL,NULL,NULL,NULL,2023,83.180488,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. MAC tratado separado de CHN.'),
('MDG',2023,0.487,2021,36.8,2023,63.632,NULL),
('MWI',2023,0.517,2019,38.5,2023,67.353,NULL),
('MYS',2023,0.819,2021,40.7,2023,76.657,NULL),
('MDV',2023,0.766,2019,29.3,2023,81.041,NULL),
('MLI',2023,0.419,2021,35.7,2023,60.439,NULL),
('MLT',2023,0.924,2023,31.8,2023,83.356098,NULL),
('MTQ',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('MRT',2023,0.563,2019,32.0,2023,68.484,NULL),
('MUS',2023,0.806,2017,36.8,2023,73.412195,'Gini seleccionado en 2015-2018 (antiguo).'),
('MEX',2023,0.789,2024,42.6,2023,75.069,NULL),
('MCO',NULL,NULL,NULL,NULL,2023,86.372,'Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('MNG',2023,0.747,2022,31.4,2023,72.122439,NULL),
('MDA',2023,0.785,2023,26.8,2023,71.198,NULL),
('MNE',2023,0.862,2021,34.3,2023,77.587805,NULL),
('MSR',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('MAR',2023,0.71,NULL,NULL,2023,75.313,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('MOZ',2023,0.493,2022,49.6,2023,63.611,NULL),
('OMN',2023,0.858,NULL,NULL,2023,80.031,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('NAM',2023,0.665,2015,59.1,2023,67.385,'Gini seleccionado en 2015-2018 (antiguo).'),
('NRU',2023,0.703,NULL,NULL,2023,62.109,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('NPL',2023,0.622,2022,30.0,2023,70.354,NULL),
('NLD',2023,0.955,2021,25.7,2023,81.863415,NULL),
('CUW',NULL,NULL,NULL,NULL,2023,76.8,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('ABW',NULL,NULL,NULL,NULL,2023,76.353,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('SXM',NULL,NULL,NULL,NULL,2023,76.371,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('BES',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('NCL',NULL,NULL,NULL,NULL,2023,78.766,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('VUT',2023,0.621,2019,32.3,2023,71.477,NULL),
('NZL',2023,0.938,NULL,NULL,2023,81.758537,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('NIC',2023,0.706,NULL,NULL,2023,74.947,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('NER',2023,0.419,2021,32.9,2023,61.183,NULL),
('NGA',2023,0.56,2022,33.9,2023,54.462,NULL),
('NIU',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('NFK',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('NOR',2023,0.97,2023,26.5,2023,83.012195,NULL),
('MNP',NULL,NULL,NULL,NULL,2023,78.808,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('FSM',2023,0.615,NULL,NULL,2023,67.198,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('MHL',2023,0.733,2019,35.5,2023,66.945,NULL),
('PLW',2023,0.786,NULL,NULL,2023,69.269,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('PAK',2023,0.544,2024,33.5,2023,67.649,NULL),
('PAN',2023,0.839,2024,49.7,2023,79.594,NULL),
('PNG',2023,0.576,NULL,NULL,2023,66.134,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('PRY',2023,0.756,2024,44.2,2023,73.844,NULL),
('PER',2023,0.794,2024,40.1,2023,77.74,NULL),
('PHL',2023,0.72,2023,39.3,2023,69.833,NULL),
('PCN',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('POL',2023,0.906,2023,28.5,2023,78.258537,NULL),
('PRT',2023,0.89,2023,33.9,2023,82.329268,NULL),
('GNB',2023,0.514,2021,33.4,2023,64.085,NULL),
('TLS',2023,0.634,NULL,NULL,2023,67.689,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('PRI',NULL,NULL,NULL,NULL,2023,81.69,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('QAT',2023,0.886,2017,35.1,2023,82.368,'Gini seleccionado en 2015-2018 (antiguo).'),
('REU',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('ROU',2023,0.845,2023,29.8,2023,76.404878,NULL),
('RUS',2023,0.832,2023,33.0,2023,73.254634,NULL),
('RWA',2023,0.578,2023,39.4,2023,67.785,NULL),
('BLM',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('SHN',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('KNA',2023,0.84,NULL,NULL,2023,72.145,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('AIA',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('LCA',2023,0.748,2015,43.7,2023,72.697,'Gini seleccionado en 2015-2018 (antiguo).'),
('MAF',NULL,NULL,NULL,NULL,2023,80.224,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('SPM',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('VCT',2023,0.798,NULL,NULL,2023,71.23,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('SMR',2023,0.915,NULL,NULL,2023,85.706,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('STP',2023,0.637,2017,40.7,2023,69.718,'Gini seleccionado en 2015-2018 (antiguo).'),
('SAU',2023,0.9,NULL,NULL,2023,78.732,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('SEN',2023,0.53,2021,36.2,2023,68.683,NULL),
('SRB',2023,0.833,2023,32.8,2023,76.141463,'SRB revisado expresamente junto con XKX.'),
('SYC',2023,0.848,2018,32.1,2023,75.419512,'Gini seleccionado en 2015-2018 (antiguo).'),
('SLE',2023,0.467,2018,35.7,2023,61.786,'Gini seleccionado en 2015-2018 (antiguo).'),
('SGP',2023,0.946,NULL,NULL,2023,83.097561,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('SVK',2023,0.88,2023,23.8,2023,78.119512,NULL),
('VNM',2023,0.766,2022,36.1,2023,74.588,NULL),
('SVN',2023,0.931,2023,24.7,2023,81.929268,NULL),
('SOM',2023,0.404,NULL,NULL,2023,58.816,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('ZAF',2023,0.741,2022,54.1,2023,66.139,NULL),
('ZWE',2023,0.598,2019,50.3,2023,62.775,NULL),
('ESP',2023,0.918,2023,33.4,2023,83.934146,NULL),
('SSD',2023,0.388,2016,44.0,2023,57.617,'Gini seleccionado en 2015-2018 (antiguo).'),
('SDN',2023,0.511,NULL,NULL,2023,66.331,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('ESH',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('SUR',2023,0.722,2022,39.2,2023,73.631,NULL),
('SJM',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('SWZ',2023,0.695,2016,54.6,2023,64.123,'Gini seleccionado en 2015-2018 (antiguo).'),
('SWE',2023,0.959,2023,29.3,2023,83.309756,NULL),
('CHE',2023,0.97,2022,33.8,2023,84.156098,NULL),
('SYR',2023,0.564,2022,26.4,2023,72.12,NULL),
('TJK',2023,0.691,2024,36.1,2023,71.79,NULL),
('THA',2023,0.798,2024,33.3,2023,76.412,NULL),
('TGO',2023,0.571,2021,37.9,2023,62.74,NULL),
('TKL',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('TON',2023,0.769,2021,27.1,2023,72.895,NULL),
('TTO',2023,0.807,NULL,NULL,2023,73.49,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('ARE',2023,0.94,2018,26.4,2023,82.909,'Gini seleccionado en 2015-2018 (antiguo).'),
('TUN',2023,0.746,2021,33.7,2023,76.508,NULL),
('TUR',2023,0.853,2023,43.7,2023,77.156,NULL),
('TKM',2023,0.764,NULL,NULL,2023,70.073,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('TCA',NULL,NULL,NULL,NULL,2023,78.008,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('TUV',2023,0.689,NULL,NULL,2023,67.105,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('UGA',2023,0.582,2019,42.7,2023,68.252,NULL),
('UKR',2023,0.779,2020,25.6,2023,73.422,NULL),
('MKD',2023,0.815,2019,33.5,2023,75.316098,NULL),
('EGY',2023,0.754,2021,28.5,2023,71.633,NULL),
('GBR',2023,0.946,2021,32.4,2023,81.238098,NULL),
('GGY',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('JEY',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('IMN',NULL,NULL,NULL,NULL,2023,80.999,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('TZA',2023,0.555,2018,40.5,2023,66.995,'Gini seleccionado en 2015-2018 (antiguo).'),
('USA',2023,0.938,2024,41.8,2023,78.385366,NULL),
('VIR',NULL,NULL,NULL,NULL,2023,80.519512,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP.'),
('BFA',2023,0.459,2021,37.4,2023,61.092,NULL),
('URY',2023,0.862,2024,40.0,2023,78.138,NULL),
('UZB',2023,0.74,2024,34.6,2023,72.388,NULL),
('VEN',2023,0.709,NULL,NULL,2023,72.514,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('WLF',NULL,NULL,NULL,NULL,NULL,NULL,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. Sin Gini 2015-2024 usable en WDI/PIP. Sin esperanza de vida 2023/2022 usable en WDI.'),
('WSM',2023,0.708,NULL,NULL,2023,71.698,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('YEM',2023,0.47,NULL,NULL,2023,69.295,'Sin Gini 2015-2024 usable en WDI/PIP.'),
('ZMB',2023,0.595,2022,51.5,2023,66.349,NULL),
('XKX',NULL,NULL,2022,38.3,2023,78.033,'Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado. Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad. XKX revisado expresamente; mantener separado de SRB sin duplicidad.');

SET @ind_hum_idh := (SELECT id FROM rg_indicadores WHERE codigo='HUM_IDH');
SET @ind_hum_gini := (SELECT id FROM rg_indicadores WHERE codigo='HUM_GINI');
SET @ind_hum_ev := (SELECT id FROM rg_indicadores WHERE codigo='HUM_EV');
SET @src_undp := (SELECT id FROM rg_fuentes WHERE codigo='UNDP_HDR');
SET @src_pip := (SELECT id FROM rg_fuentes WHERE codigo='WB_PIP');
SET @src_wdi := (SELECT id FROM rg_fuentes WHERE codigo='WB_WDI');
SET @next_pais_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_pais);

INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_hum_idh, t.anio_idh, t.idh, @src_undp,
       'FUENTE_VALIDADA', 'OK', CURDATE(), t.observaciones, 1
FROM tmp_rg_humano_pais t
JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_hum_idh AND d.anio=t.anio_idh
WHERE t.idh IS NOT NULL AND d.id IS NULL;

INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_hum_gini, t.anio_gini, t.gini, @src_pip,
       'FUENTE_VALIDADA', CASE WHEN t.anio_gini < 2019 THEN 'LIMITACION' ELSE 'OK' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_humano_pais t
JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_hum_gini AND d.anio=t.anio_gini
WHERE t.gini IS NOT NULL AND d.id IS NULL;

INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_hum_ev, t.anio_ev, t.ev, @src_wdi,
       'FUENTE_VALIDADA', CASE WHEN t.anio_ev = 2022 THEN 'LIMITACION' ELSE 'OK' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_humano_pais t
JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_hum_ev AND d.anio=t.anio_ev
WHERE t.ev IS NOT NULL AND d.id IS NULL;

UPDATE rg_datos_pais d
JOIN rg_paises p ON p.id=d.pais_id
JOIN tmp_rg_humano_pais t ON t.codigo_iso3=p.codigo_iso3
SET d.valor=t.idh, d.fuente_id=@src_undp, d.tipo_procedencia='FUENTE_VALIDADA', d.estado_dato='OK', d.fecha_carga=CURDATE(), d.observaciones=t.observaciones, d.activo=1
WHERE d.indicador_id=@ind_hum_idh AND t.idh IS NOT NULL AND d.anio=t.anio_idh;

UPDATE rg_datos_pais d
JOIN rg_paises p ON p.id=d.pais_id
JOIN tmp_rg_humano_pais t ON t.codigo_iso3=p.codigo_iso3
SET d.valor=t.gini, d.fuente_id=@src_pip, d.tipo_procedencia='FUENTE_VALIDADA', d.estado_dato=CASE WHEN t.anio_gini < 2019 THEN 'LIMITACION' ELSE 'OK' END, d.fecha_carga=CURDATE(), d.observaciones=t.observaciones, d.activo=1
WHERE d.indicador_id=@ind_hum_gini AND t.gini IS NOT NULL AND d.anio=t.anio_gini;

UPDATE rg_datos_pais d
JOIN rg_paises p ON p.id=d.pais_id
JOIN tmp_rg_humano_pais t ON t.codigo_iso3=p.codigo_iso3
SET d.valor=t.ev, d.fuente_id=@src_wdi, d.tipo_procedencia='FUENTE_VALIDADA', d.estado_dato=CASE WHEN t.anio_ev = 2022 THEN 'LIMITACION' ELSE 'OK' END, d.fecha_carga=CURDATE(), d.observaciones=t.observaciones, d.activo=1
WHERE d.indicador_id=@ind_hum_ev AND t.ev IS NOT NULL AND d.anio=t.anio_ev;

DROP TEMPORARY TABLE IF EXISTS tmp_rg_humano_area;
CREATE TEMPORARY TABLE tmp_rg_humano_area (area_codigo VARCHAR(10) PRIMARY KEY, idh_aprox DECIMAL(12,8) NULL, gini_aprox DECIMAL(12,8) NULL, ev_aprox DECIMAL(12,8) NULL, entidades_totales SMALLINT NULL, entidades_con_idh SMALLINT NULL, entidades_con_gini SMALLINT NULL, entidades_con_ev SMALLINT NULL, cobertura_idh DECIMAL(8,4) NULL, cobertura_gini DECIMAL(8,4) NULL, cobertura_ev DECIMAL(8,4) NULL, anio_min_idh SMALLINT NULL, anio_max_idh SMALLINT NULL, anio_min_gini SMALLINT NULL, anio_max_gini SMALLINT NULL, anio_min_ev SMALLINT NULL, anio_max_ev SMALLINT NULL, observaciones TEXT NULL) ENGINE=InnoDB;

INSERT INTO tmp_rg_humano_area (area_codigo,idh_aprox,gini_aprox,ev_aprox,entidades_totales,entidades_con_idh,entidades_con_gini,entidades_con_ev,cobertura_idh,cobertura_gini,cobertura_ev,anio_min_idh,anio_max_idh,anio_min_gini,anio_max_gini,anio_min_ev,anio_max_ev,observaciones) VALUES
('AFR',0.57508765,38.39213085,64.1741359,59,54,47,54,99.8821,88.5998,99.8821,2023,2023,2015,2024,2023,2023,'Cobertura IDH alta. Cobertura Gini condicionada. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 17 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada.'),
('APC',0.77501233,34.92900269,74.50584026,43,28,16,34,94.8134,90.4189,97.6255,2023,2023,2017,2024,2023,2023,'Cobertura IDH aceptable. Cobertura Gini aceptable. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 1 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada.'),
('CHN',0.79782092,36.0,77.99353018,3,2,1,3,99.9493,99.43,100.0,2023,2023,2022,2022,2023,2023,'Cobertura IDH alta. Cobertura Gini alta. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area.'),
('EUR',0.91365599,31.29447637,80.75758653,51,41,39,46,99.9344,99.9079,99.9714,2023,2023,2017,2023,2023,2023,'Cobertura IDH alta. Cobertura Gini alta. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 1 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada.'),
('MDE',0.7625419,36.13161283,76.00249357,15,15,9,15,100.0,74.2328,100.0,2023,2023,2017,2023,2023,2023,'Cobertura IDH alta. Cobertura Gini insuficiente. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 2 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada.'),
('NAC',0.86989018,41.46004158,77.14717063,41,23,14,34,99.2311,94.0357,99.8734,2023,2023,2015,2024,2023,2023,'Cobertura IDH alta. Cobertura Gini aceptable. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini incluye 4 datos previos a 2019. Gini con dispersion temporal relevante; comparabilidad condicionada.'),
('RUE',0.80561117,32.50328899,73.18431353,10,10,8,10,100.0,92.8999,100.0,2023,2023,2020,2024,2023,2023,'Cobertura IDH alta. Cobertura Gini aceptable. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini con dispersion temporal relevante; comparabilidad condicionada.'),
('SAI',0.66293481,27.25045887,71.59153647,8,8,7,8,100.0,97.7999,100.0,2023,2023,2019,2024,2023,2023,'Cobertura IDH alta. Cobertura Gini alta. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area. Gini con dispersion temporal relevante; comparabilidad condicionada.'),
('SAM',0.79240291,48.00555466,76.23982799,14,12,10,12,99.9276,93.2276,99.9276,2023,2023,2022,2024,2023,2023,'Cobertura IDH alta. Cobertura Gini aceptable. Cobertura EV alta. IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos. Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area.');

SET @per := (SELECT id FROM rg_periodos WHERE codigo='RG2025_V1');
SET @next_area_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_area);

INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)
SELECT (@next_area_id := @next_area_id + 1), a.id, @ind_hum_idh, @per, 2023, t.idh_aprox,
       'Media nacional de IDH 2023 ponderada por poblacion 2025; no es un IDH oficial del area', t.entidades_totales, t.entidades_con_idh, t.cobertura_idh, t.anio_min_idh, t.anio_max_idh, @src_undp,
       'AGREGADO_1C4', CASE WHEN t.cobertura_idh >= 90 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_humano_area t
JOIN rg_areas a ON a.codigo=t.area_codigo
LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=@ind_hum_idh AND d.periodo_id=@per AND d.anio_referencia=2023
WHERE d.id IS NULL;

INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)
SELECT (@next_area_id := @next_area_id + 1), a.id, @ind_hum_gini, @per, 2024, t.gini_aprox,
       'Media ponderada de indices nacionales; no representa la desigualdad conjunta entre todos los habitantes del area', t.entidades_totales, t.entidades_con_gini, t.cobertura_gini, t.anio_min_gini, t.anio_max_gini, @src_pip,
       'AGREGADO_1C4', CASE WHEN t.cobertura_gini >= 90 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_humano_area t
JOIN rg_areas a ON a.codigo=t.area_codigo
LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=@ind_hum_gini AND d.periodo_id=@per AND d.anio_referencia=2024
WHERE d.id IS NULL;

INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)
SELECT (@next_area_id := @next_area_id + 1), a.id, @ind_hum_ev, @per, 2023, t.ev_aprox,
       'Media nacional ponderada por poblacion 2025', t.entidades_totales, t.entidades_con_ev, t.cobertura_ev, t.anio_min_ev, t.anio_max_ev, @src_wdi,
       'AGREGADO_1C4', CASE WHEN t.cobertura_ev >= 90 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_humano_area t
JOIN rg_areas a ON a.codigo=t.area_codigo
LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=@ind_hum_ev AND d.periodo_id=@per AND d.anio_referencia=2023
WHERE d.id IS NULL;

-- Actualizacion idempotente de los 27 registros HUM
UPDATE rg_datos_area d
JOIN rg_areas a ON a.id=d.area_id
JOIN tmp_rg_humano_area t ON t.area_codigo=a.codigo
SET d.valor=CASE
      WHEN d.indicador_id=@ind_hum_idh THEN t.idh_aprox
      WHEN d.indicador_id=@ind_hum_gini THEN t.gini_aprox
      WHEN d.indicador_id=@ind_hum_ev THEN t.ev_aprox
      ELSE d.valor END,
    d.metodo_calculo=CASE
      WHEN d.indicador_id=@ind_hum_idh THEN 'Media nacional de IDH 2023 ponderada por poblacion 2025; no es un IDH oficial del area'
      WHEN d.indicador_id=@ind_hum_gini THEN 'Media ponderada de indices nacionales; no representa la desigualdad conjunta entre todos los habitantes del area'
      WHEN d.indicador_id=@ind_hum_ev THEN 'Media nacional ponderada por poblacion 2025'
      ELSE d.metodo_calculo END,
    d.paises_totales=t.entidades_totales,
    d.paises_con_dato=CASE
      WHEN d.indicador_id=@ind_hum_idh THEN t.entidades_con_idh
      WHEN d.indicador_id=@ind_hum_gini THEN t.entidades_con_gini
      WHEN d.indicador_id=@ind_hum_ev THEN t.entidades_con_ev
      ELSE d.paises_con_dato END,
    d.porcentaje_cobertura=CASE
      WHEN d.indicador_id=@ind_hum_idh THEN t.cobertura_idh
      WHEN d.indicador_id=@ind_hum_gini THEN t.cobertura_gini
      WHEN d.indicador_id=@ind_hum_ev THEN t.cobertura_ev
      ELSE d.porcentaje_cobertura END,
    d.anio_minimo=CASE
      WHEN d.indicador_id=@ind_hum_idh THEN t.anio_min_idh
      WHEN d.indicador_id=@ind_hum_gini THEN t.anio_min_gini
      WHEN d.indicador_id=@ind_hum_ev THEN t.anio_min_ev
      ELSE d.anio_minimo END,
    d.anio_maximo=CASE
      WHEN d.indicador_id=@ind_hum_idh THEN t.anio_max_idh
      WHEN d.indicador_id=@ind_hum_gini THEN t.anio_max_gini
      WHEN d.indicador_id=@ind_hum_ev THEN t.anio_max_ev
      ELSE d.anio_maximo END,
    d.fuente_principal_id=CASE
      WHEN d.indicador_id=@ind_hum_idh THEN @src_undp
      WHEN d.indicador_id=@ind_hum_gini THEN @src_pip
      WHEN d.indicador_id=@ind_hum_ev THEN @src_wdi
      ELSE d.fuente_principal_id END,
    d.tipo_procedencia='AGREGADO_1C4',
    d.estado_dato=CASE
      WHEN d.indicador_id=@ind_hum_idh AND t.cobertura_idh >= 90 THEN 'OK'
      WHEN d.indicador_id=@ind_hum_gini AND t.cobertura_gini >= 90 THEN 'OK'
      WHEN d.indicador_id=@ind_hum_ev AND t.cobertura_ev >= 90 THEN 'OK'
      ELSE 'LIMITACION' END,
    d.fecha_calculo=CURDATE(),
    d.observaciones=t.observaciones,
    d.activo=1
WHERE d.periodo_id=@per AND ((d.indicador_id=@ind_hum_idh AND d.anio_referencia=2023) OR (d.indicador_id=@ind_hum_gini AND d.anio_referencia=2024) OR (d.indicador_id=@ind_hum_ev AND d.anio_referencia=2023));

COMMIT;