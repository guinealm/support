-- 18_rg_datos_energia.sql
SET NAMES utf8mb4;
START TRANSACTION;

DROP TEMPORARY TABLE IF EXISTS tmp_rg_energia_pais;
CREATE TEMPORARY TABLE tmp_rg_energia_pais (
  codigo_iso3 VARCHAR(3) PRIMARY KEY,
  anio_consumo SMALLINT NULL,
  consumo_energia_twh DECIMAL(20,6) NULL,
  consumo_per_capita_kwh DECIMAL(20,6) NULL,
  anio_dependencia SMALLINT NULL,
  dependencia_energetica_pct DECIMAL(14,6) NULL,
  autosuficiencia_pct DECIMAL(14,6) NULL,
  anio_fosil SMALLINT NULL,
  energia_fosil_pct DECIMAL(14,6) NULL,
  anio_electricidad SMALLINT NULL,
  electricidad_baja_carbono_pct DECIMAL(14,6) NULL,
  observaciones TEXT NULL
) ENGINE=InnoDB;

INSERT INTO tmp_rg_energia_pais (codigo_iso3,anio_consumo,consumo_energia_twh,consumo_per_capita_kwh,anio_dependencia,dependencia_energetica_pct,autosuficiencia_pct,anio_fosil,energia_fosil_pct,anio_electricidad,electricidad_baja_carbono_pct,observaciones) VALUES
('AFG',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,86.86868686868688,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('ALB',NULL,NULL,NULL,2023.0,22.7015590200443,77.2984409799557,NULL,NULL,2024.0,100.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('DZA',2024.0,760.133,16024.623850882392,2023.0,-129.337044067666,229.337044067666,2024.0,99.74359750201609,2024.0,1.0689082606890827,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('ASM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,5.555555555555556,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('AND',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('AGO',NULL,NULL,NULL,2022.0,-353.971819384273,453.971819384273,NULL,NULL,2024.0,73.70109044259141,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('ATG',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,8.108108108108109,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('AZE',2024.0,208.152,20019.019568920547,2023.0,-255.959109290849,355.959109290849,2024.0,95.45188131749876,2025.0,12.139551441794232,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('ARG',2024.0,983.105,21441.1217599366,2023.0,0.41571453028353,99.58428546971648,2024.0,81.90478127972088,2025.0,41.60626836434867,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('AUS',2024.0,1672.114,61989.78691499644,2023.0,-214.471540281044,314.471540281044,2024.0,84.52755015507314,2025.0,38.61842564783125,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('AUT',2024.0,412.337,45244.24984347531,2023.0,63.9661980292725,36.0338019707275,2024.0,55.309370733162446,2025.0,83.5973777656378,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('BHS',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,0.8888888888888888,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('BHR',NULL,NULL,NULL,2022.0,-45.4751316679306,145.4751316679306,NULL,NULL,2024.0,0.2635046113306983,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('BGD',2024.0,529.073,3011.453830389088,2022.0,44.3070258449266,55.6929741550734,2024.0,98.83872357878782,2025.0,2.1373307543520306,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('ARM',NULL,NULL,NULL,2022.0,76.8721086405015,23.127891359498506,NULL,NULL,2025.0,65.94650205761316,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('BRB',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,9.00900900900901,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('BEL',2024.0,644.116,54778.285273902904,2023.0,89.1747801928026,10.8252198071974,2024.0,76.053226437474,2025.0,72.01262175881466,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('BMU',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,1.639344262295082,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('BTN',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,100.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('BOL',NULL,NULL,NULL,2022.0,-67.3339047798362,167.3339047798362,NULL,NULL,2025.0,36.09684519442406,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('BIH',NULL,NULL,NULL,2023.0,24.9320415177106,75.0679584822894,NULL,NULL,2025.0,43.5595567867036,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI.'),
('BWA',NULL,NULL,NULL,2022.0,23.6817784648472,76.3182215351528,NULL,NULL,2024.0,0.2915451895043732,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('BRA',2024.0,3919.054,18415.534316828358,2023.0,-13.6808969364254,113.6808969364254,2024.0,48.20497497610393,2025.0,88.71597404500821,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('BLZ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,87.2340425531915,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('IOT',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('SLB',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,9.090909090909092,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('VGB',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('BRN',NULL,NULL,NULL,2022.0,-172.552632157863,272.552632157863,NULL,NULL,2024.0,0.1798561151079137,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('BGR',2024.0,191.794,28563.913980313813,2023.0,40.9310458153299,59.0689541846701,2024.0,62.548880569777985,2025.0,71.91780821917808,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('MMR',NULL,NULL,NULL,2022.0,-19.025954239222,119.025954239222,NULL,NULL,2024.0,47.85812989405804,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('BDI',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,75.51020408163265,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('BLR',2024.0,313.657,34860.06992308283,2022.0,77.0799482437318,22.920051756268194,2024.0,86.56271022167527,2025.0,41.4276471856804,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('KHM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2025.0,40.87837837837837,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022.'),
('CMR',NULL,NULL,NULL,2022.0,-28.7126841321204,128.7126841321204,NULL,NULL,2024.0,73.14049586776859,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('CAN',2024.0,3886.195,96848.04103638852,2023.0,-89.626081306096,189.626081306096,2024.0,66.27809464012999,2025.0,76.9771933051315,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('CPV',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,30.76923076923077,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('CYM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,4.225352112676056,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('CAF',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('LKA',2024.0,111.341,4793.091741982621,2022.0,60.0395802943756,39.9604197056244,2024.0,75.6828122614311,2025.0,61.6231884057971,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('TCD',NULL,NULL,NULL,2022.0,-177.762640714933,277.762640714933,NULL,NULL,2024.0,5.405405405405405,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('CHL',2024.0,518.732,26119.54258222302,2023.0,62.2762043204213,37.7237956795787,2024.0,66.583515187033,2025.0,66.37288135593221,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('CHN',2024.0,48987.102,34593.06345250965,2023.0,23.9617588276826,76.0382411723174,2024.0,79.42350621190045,2025.0,41.65104465878511,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. CHN tratado separado de HKG/MAC.'),
('TWN',2024.0,1253.847,54249.03788148185,NULL,NULL,NULL,2024.0,90.98438645225455,2025.0,13.367315094143347,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('CXR',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('CCK',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('COL',2024.0,615.888,11527.950377523866,2023.0,-141.971675507707,241.971675507707,2024.0,72.85415530096382,2025.0,77.02523240371846,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('COM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('MYT',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('COG',NULL,NULL,NULL,2022.0,-347.419865428152,447.419865428152,NULL,NULL,2024.0,20.879120879120876,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('COD',NULL,NULL,NULL,2022.0,1.59626553466334,98.40373446533665,NULL,NULL,2024.0,100.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('COK',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,50.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('CRI',NULL,NULL,NULL,2023.0,60.4214772696159,39.5785227303841,NULL,NULL,2025.0,100.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI.'),
('HRV',2024.0,103.144,26803.431454584577,2023.0,57.2910760073134,42.7089239926866,2024.0,71.10059722329946,2025.0,76.25850340136056,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('CUB',NULL,NULL,NULL,2022.0,62.8133332274217,37.1866667725783,NULL,NULL,2024.0,4.014410705095214,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('CYP',2024.0,33.348,24328.216441462144,2022.0,117.037858353679,-17.037858353679,2024.0,88.68297948902483,2025.0,27.749576988155667,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('CZE',2024.0,392.823,37026.49416673634,2023.0,41.9751454505475,58.0248545494525,2024.0,71.18778686584034,2025.0,59.152317880794705,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('BEN',NULL,NULL,NULL,2022.0,40.9031703802238,59.0968296197762,NULL,NULL,2024.0,3.9603960396039604,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('DNK',2024.0,196.253,32695.128625251247,2023.0,43.7871947382637,56.2128052617363,2024.0,57.07785358695154,2025.0,91.17117117117117,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('DMA',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('DOM',NULL,NULL,NULL,2022.0,94.4206892076641,5.579310792335903,NULL,NULL,2025.0,23.80952380952381,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('ECU',2024.0,230.721,12614.668490770151,2022.0,-69.401314941725,169.401314941725,2024.0,73.52733387944747,2025.0,79.39890710382514,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('SLV',NULL,NULL,NULL,2022.0,59.5054447583379,40.4945552416621,NULL,NULL,2025.0,86.53250773993808,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('GNQ',NULL,NULL,NULL,2022.0,-422.769233942919,522.7692339429191,NULL,NULL,2024.0,26.845637583892618,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('ETH',NULL,NULL,NULL,2022.0,10.7924961213427,89.2075038786573,NULL,NULL,2025.0,100.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('ERI',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,11.111111111111112,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('EST',2024.0,55.764,41483.78707310324,2023.0,3.77111519842947,96.22888480157053,2024.0,81.43246538985726,2025.0,59.57446808510638,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('FRO',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('FLK',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('FJI',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,63.47826086956522,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('FIN',2024.0,334.594,59501.06413853149,2023.0,30.2718534094324,69.7281465905676,2024.0,35.94206710221941,2025.0,96.34264884568651,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('ALA',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('FRA',2024.0,2519.901,37807.5109191481,2023.0,47.1279302986198,52.8720697013802,2024.0,45.42734020106345,2025.0,94.85069651566721,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('GUF',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('PYF',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,34.72222222222222,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('DJI',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,35.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('GAB',NULL,NULL,NULL,2022.0,-187.597030037125,287.597030037125,NULL,NULL,2024.0,35.38461538461539,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('GEO',NULL,NULL,NULL,2023.0,79.9350466563312,20.064953343668805,NULL,NULL,2025.0,79.62962962962963,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI.'),
('GMB',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,0.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('PSE',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,39.3939393939394,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('DEU',2024.0,3195.441,38006.99553345626,2023.0,70.4874265375658,29.512573462434204,2024.0,75.12240094559719,2025.0,59.09245309409156,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('GHA',NULL,NULL,NULL,2022.0,-22.3656522253718,122.3656522253718,NULL,NULL,2024.0,36.21755253399258,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('GIB',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,0.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('KIR',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,25.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('GRC',2024.0,321.187,32316.324016256614,2023.0,89.2460562263153,10.753943773684696,2024.0,78.00377972956564,2025.0,49.69967393169727,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('GRL',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,83.33333333333334,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('GRD',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,0.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('GLP',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('GUM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,8.602150537634408,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('GTM',NULL,NULL,NULL,2022.0,38.364016749015,61.635983250985,NULL,NULL,2024.0,68.33438885370488,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('GIN',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,75.18610421836227,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('GUY',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,2.8985507246376816,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('HTI',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,18.6046511627907,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('VAT',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('HND',NULL,NULL,NULL,2023.0,60.5670375858002,39.4329624141998,NULL,NULL,2024.0,55.44871794871795,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('HKG',2024.0,272.932,36902.27586929554,2022.0,175.706507863695,-75.70650786369501,2024.0,98.9301364442425,2024.0,1.0416666666666667,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano. HKG/MAC solo con dato separado publicable y comparable.'),
('HUN',2024.0,260.792,27074.777472346643,2023.0,62.5098125396588,37.4901874603412,2024.0,71.54590631614468,2025.0,75.32306163021867,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('ISL',2024.0,62.817,157724.65915082733,NULL,NULL,NULL,2024.0,20.05985640829712,2024.0,100.0,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('IND',2024.0,11336.057,7743.919636683951,2023.0,36.0871843474496,63.9128156525504,2024.0,89.19669334760754,2025.0,26.653055342044578,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('IDN',2024.0,2984.731,10446.304602566635,2023.0,-89.548816280588,189.548816280588,2024.0,89.22234533028269,2024.0,18.089573128061577,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('IRN',2024.0,3589.786,38843.06384479404,2022.0,-32.4944592767049,132.4944592767049,2024.0,97.97308251801084,2025.0,5.70013643943605,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('IRQ',2024.0,736.781,15669.264340968582,2022.0,-274.87736059498,374.87736059498,2024.0,99.38014145315907,2024.0,1.6229212582648769,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('IRL',2024.0,181.792,34248.455407697955,2023.0,85.7663488731447,14.233651126855307,2024.0,76.93352842809364,2025.0,48.1421647819063,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('ISR',2024.0,277.774,29186.580649608255,2023.0,13.73424198863,86.26575801137,2024.0,89.69053979134117,2025.0,16.9305724725944,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('ITA',2024.0,1696.287,28679.529592596577,2023.0,79.59805806701,20.40194193299,2024.0,78.40229866761933,2025.0,48.775972799395554,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('CIV',NULL,NULL,NULL,2022.0,14.3786092266282,85.6213907733718,NULL,NULL,2024.0,28.915662650602414,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('JAM',NULL,NULL,NULL,2022.0,112.575323434922,-12.575323434921998,NULL,NULL,2024.0,12.601626016260163,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('JPN',2024.0,4794.816,38949.47567688582,2023.0,87.2798853157027,12.7201146842973,2024.0,82.398990910183,2025.0,32.70541627017265,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('KAZ',2024.0,862.112,41360.67977761016,2023.0,-119.1426831733,219.1426831733,2024.0,94.58388237259197,2025.0,14.859729970086505,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('JOR',NULL,NULL,NULL,2022.0,96.3523279332296,3.6476720667703972,NULL,NULL,2024.0,24.081115335868187,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('KEN',NULL,NULL,NULL,2023.0,22.3745456763117,77.6254543236883,NULL,NULL,2025.0,90.02849002849004,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI.'),
('PRK',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025. PRK se mantiene ausente cuando no hay publicacion comparable; no estimar.'),
('KOR',2024.0,3616.218,69990.81716223893,2023.0,84.6000911986392,15.399908801360795,2024.0,82.10414858838709,2025.0,39.95773700893286,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('KWT',2024.0,525.025,104460.15671460795,2022.0,-283.096624591869,383.096624591869,2024.0,99.91962287510118,2025.0,2.23807979240999,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('KGZ',NULL,NULL,NULL,2022.0,33.7815670306686,66.2184329693314,NULL,NULL,2025.0,84.72750316856781,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('LAO',NULL,NULL,NULL,2022.0,-49.0213561069782,149.0213561069782,NULL,NULL,2024.0,76.71573312942076,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('LBN',NULL,NULL,NULL,2022.0,96.923460215068,3.0765397849319953,NULL,NULL,2024.0,43.82022471910112,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('LSO',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('LVA',2024.0,38.79,20927.296661559376,2023.0,34.3077384557047,65.69226154429529,2024.0,69.21371487496778,2025.0,73.04625199362043,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('LBR',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,54.385964912280706,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('LBY',NULL,NULL,NULL,2022.0,-249.727007920872,349.727007920872,NULL,NULL,2024.0,0.028910089621277824,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('LIE',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('LTU',2024.0,73.366,25923.007614437396,2023.0,71.4559726962456,28.544027303754405,2024.0,75.7040045797781,2025.0,77.61529808773902,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('LUX',2024.0,39.742,58405.12363804166,2023.0,109.585053497428,-9.585053497428007,2024.0,85.30773489004076,2025.0,91.55844155844154,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('MAC',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,30.769230769230766,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano. HKG/MAC solo con dato separado publicable y comparable.'),
('MDG',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,42.38683127572016,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('MWI',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,95.62841530054644,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('MYS',2024.0,1381.98,38411.98444575624,2022.0,-0.578726686040022,100.57872668604003,2024.0,91.33612642729994,2025.0,20.652444179223234,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('MDV',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,7.0588235294117645,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('MLI',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,19.463087248322147,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('MLT',NULL,NULL,NULL,2023.0,403.5916298334,-303.5916298334,NULL,NULL,2025.0,15.981735159817351,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI.'),
('MTQ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('MRT',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,22.705314009661837,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('MUS',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,17.88856304985337,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('MEX',2024.0,2310.191,17508.490555863547,2023.0,21.5843559520399,78.4156440479601,2024.0,90.10674874934583,2025.0,25.93775387287447,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('MCO',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('MNG',NULL,NULL,NULL,2022.0,-226.427034086937,326.427034086937,NULL,NULL,2025.0,8.359133126934985,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('MDA',NULL,NULL,NULL,2023.0,81.1658823176762,18.834117682323793,NULL,NULL,2025.0,11.2012987012987,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI.'),
('MNE',NULL,NULL,NULL,2023.0,24.3527580071175,75.6472419928825,NULL,NULL,2025.0,75.60975609756098,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI.'),
('MSR',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,0.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('MAR',2024.0,276.349,7190.825768952767,2023.0,93.6448805073888,6.355119492611195,2024.0,90.84454801718118,2025.0,23.95505617977528,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('MOZ',NULL,NULL,NULL,2022.0,-106.352427255745,206.352427255745,NULL,NULL,2024.0,83.42597271349167,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('OMN',2024.0,446.875,81328.43018066877,2022.0,-213.629416330893,313.62941633089304,2024.0,98.81711888111889,2025.0,4.542013626040878,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('NAM',NULL,NULL,NULL,2022.0,60.4998985401718,39.5001014598282,NULL,NULL,2024.0,97.56097560975611,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('NRU',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,20.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('NPL',NULL,NULL,NULL,2022.0,27.4137248718471,72.58627512815289,NULL,NULL,2024.0,100.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('NLD',2024.0,926.465,50497.29863312029,2023.0,87.0173748946605,12.982625105339494,2024.0,80.15521363462193,2025.0,54.15678719620628,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('CUW',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('ABW',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,17.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('SXM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('BES',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('NCL',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,26.923076923076923,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('VUT',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('NZL',2024.0,233.124,44388.53237220761,2023.0,31.6329616305902,68.3670383694098,2024.0,57.81772790446287,2025.0,88.53253345639132,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('NIC',NULL,NULL,NULL,2022.0,46.4910182435548,53.5089817564452,NULL,NULL,2024.0,62.38938053097345,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('NER',NULL,NULL,NULL,2022.0,5.40557852442787,94.59442147557213,NULL,NULL,2024.0,3.1578947368421053,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('NGA',NULL,NULL,NULL,2022.0,-66.2881011856041,166.2881011856041,NULL,NULL,2025.0,31.31921039961483,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('NIU',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('NFK',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('NOR',2024.0,555.626,98811.78871201054,2023.0,-703.959305781578,803.959305781578,2024.0,27.01673427809354,2025.0,98.99881848143771,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('MNP',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('FSM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('MHL',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('PLW',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('PAK',2024.0,888.373,3480.818633179996,2022.0,39.7925509388676,60.2074490611324,2024.0,80.48038380274953,2025.0,54.904373686099575,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('PAN',NULL,NULL,NULL,2022.0,171.186492615064,-71.186492615064,NULL,NULL,2024.0,67.98212956068504,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('PNG',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,23.678646934460886,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('PRY',NULL,NULL,NULL,2023.0,-4.69402900256069,104.69402900256068,NULL,NULL,2025.0,100.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI.'),
('PER',2024.0,374.393,10827.90701118063,2022.0,12.185965103062,87.814034896938,2024.0,72.24494047698542,2025.0,63.649900727994705,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('PHL',2024.0,652.563,5587.635811395382,2022.0,54.4250767667774,45.5749232332226,2024.0,87.73344489344323,2025.0,23.31059129304743,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('PCN',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('POL',2024.0,1125.569,29510.80379224273,2023.0,48.8193550583318,51.1806449416682,2024.0,86.41895787819317,2025.0,31.50756089114626,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('PRT',2024.0,270.242,25955.28106439684,2023.0,77.2448975861994,22.7551024138006,2024.0,59.023393846996385,2025.0,80.95051828672013,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('GNB',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,0.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('TLS',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,0.0,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('PRI',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2025.0,6.3640848544647275,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('QAT',2024.0,653.95,209875.76266307133,2022.0,-396.072574936239,496.072574936239,2024.0,99.1425949996177,2025.0,4.058383766464934,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('REU',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('ROU',2024.0,355.471,18799.380495334015,2023.0,28.0603457724141,71.9396542275859,2024.0,72.44219640983371,2025.0,67.51656293916885,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('RUS',2024.0,9049.149,62842.45021019235,2022.0,-75.1375358449974,175.1375358449974,2024.0,87.75098078283384,2025.0,35.68356542224532,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. RUS asignado exclusivamente a RUE.'),
('RWA',NULL,NULL,NULL,2022.0,10.5793226381462,89.4206773618538,NULL,NULL,2024.0,49.55752212389382,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('BLM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('SHN',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('KNA',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,8.695652173913043,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('AIA',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('LCA',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,2.5,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('MAF',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('SPM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('VCT',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,13.333333333333334,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('SMR',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('STP',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('SAU',2024.0,3290.424,95191.60077378195,2022.0,-178.200448812201,278.200448812201,2024.0,99.22739440266666,2024.0,2.1599507302481085,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('SEN',NULL,NULL,NULL,2023.0,69.030995787333,30.969004212667002,NULL,NULL,2024.0,19.790301441677588,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('SRB',NULL,NULL,NULL,2023.0,42.5514943717482,57.4485056282518,NULL,NULL,2025.0,27.799016930639,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI.'),
('SYC',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,15.873015873015875,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('SLE',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,95.23809523809524,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('SGP',2024.0,1053.921,179520.70510934805,2023.0,279.622693982082,-179.622693982082,2024.0,99.43145643743696,2025.0,5.486284289276807,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('SVK',2024.0,181.077,33074.18581687907,2023.0,57.886994383722,42.113005616278,2024.0,63.26369445042715,2025.0,85.15463917525773,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('VNM',2024.0,1476.252,14530.2496010523,2022.0,33.9991947830939,66.0008052169061,2024.0,77.45222360410013,2025.0,45.41759411593922,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('SVN',2024.0,79.156,37389.41083667522,2023.0,48.9021824108035,51.0978175891965,2024.0,56.002071858102994,2025.0,78.90835579514825,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('SOM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,20.930232558139533,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('ZAF',2024.0,1362.492,21043.218793352662,2023.0,-12.5072996086864,112.5072996086864,2024.0,94.8214741811328,2025.0,17.840665678035922,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('ZWE',NULL,NULL,NULL,2022.0,16.9757127922617,83.0242872077383,NULL,NULL,2024.0,57.1150097465887,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('ESP',2024.0,1624.246,33916.2112476185,2023.0,76.9846775136602,23.015322486339798,2024.0,64.76131078666654,2025.0,74.63961929903783,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('SSD',NULL,NULL,NULL,2022.0,-859.502809253272,959.502809253272,NULL,NULL,2024.0,1.7857142857142856,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('SDN',NULL,NULL,NULL,2022.0,18.8568106273271,81.14318937267291,NULL,NULL,2024.0,79.68855788761002,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('ESH',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('SUR',NULL,NULL,NULL,2023.0,12.3045212170095,87.6954787829905,NULL,NULL,2024.0,52.87356321839081,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('SJM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('SWZ',NULL,NULL,NULL,2022.0,20.5529558411835,79.4470441588165,NULL,NULL,2024.0,96.72131147540983,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('SWE',2024.0,610.004,57241.70366708594,2023.0,27.7524049832745,72.2475950167255,2024.0,26.912282542409553,2025.0,98.78155936969128,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('CHE',2024.0,339.266,37833.20786050559,2023.0,51.7388257322457,48.2611742677543,2024.0,42.05932807885258,2025.0,97.69301753306677,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('SYR',NULL,NULL,NULL,2022.0,61.2715018609797,38.7284981390203,NULL,NULL,2024.0,3.536977491961415,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('TJK',NULL,NULL,NULL,2022.0,28.045014066896,71.954985933104,NULL,NULL,2025.0,94.36562626672071,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('THA',2024.0,1420.819,19838.336474966316,2023.0,57.5142566317877,42.4857433682123,2024.0,92.38615193068223,2025.0,16.574585635359114,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('TGO',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,29.577464788732392,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('TKL',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('TON',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,14.285714285714285,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('TTO',2024.0,159.807,105750.93107035372,2022.0,-75.4573322877313,175.4573322877313,2024.0,99.98811065848182,2024.0,0.10471204188481674,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('ARE',2024.0,1522.037,134147.38190690186,2022.0,-171.482371329992,271.482371329992,2024.0,90.70620490829066,2024.0,31.73304750084622,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('TUN',NULL,NULL,NULL,2022.0,53.1400289008402,46.8599710991598,NULL,NULL,2025.0,4.034065441506051,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('TUR',2024.0,2093.058,23870.078205811784,2023.0,71.9928600541247,28.007139945875295,2024.0,79.65579549157262,2025.0,43.25722036963771,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('TKM',2024.0,371.164,48716.52579679983,2022.0,-109.777211443604,209.77721144360402,2024.0,99.99299501029193,2024.0,0.030293850348379277,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('TCA',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,3.7037037037037033,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('TUV',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('UGA',NULL,NULL,NULL,2022.0,20.4895150227516,79.5104849772484,NULL,NULL,2024.0,97.07401032702238,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('UKR',2024.0,601.054,15419.398169027598,2023.0,23.5925758831614,76.4074241168386,2024.0,69.3911029624626,NULL,NULL,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Sin dato de electricidad baja en carbono 2025/2024 comparable.'),
('MKD',2024.0,29.569,16302.310297983451,2023.0,63.8098670871817,36.1901329128183,2024.0,83.17156481450168,2025.0,47.214076246334315,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('EGY',2024.0,1125.86,9511.684500265468,2023.0,20.2563785795628,79.7436214204372,2024.0,93.89000408576555,2025.0,13.015343290871353,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('GBR',2024.0,1936.96,27849.358000811313,2023.0,44.0436184547282,55.9563815452718,2024.0,72.77894226003635,2025.0,64.41791249016455,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('GGY',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('JEY',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('IMN',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('TZA',NULL,NULL,NULL,2022.0,12.9338562520213,87.0661437479787,NULL,NULL,2024.0,32.918552036199095,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('USA',2024.0,26528.611,76390.61032322007,2023.0,-9.00058575160831,109.00058575160831,2024.0,79.787705432448,2025.0,43.00155538199783,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.'),
('VIR',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('BFA',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,17.159763313609467,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('URY',NULL,NULL,NULL,2022.0,46.2068935643027,53.7931064356973,NULL,NULL,2025.0,97.82244556113902,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('UZB',2024.0,695.576,18772.244230682245,2022.0,1.54758954098202,98.45241045901798,2024.0,95.15150033928715,2025.0,19.377162629757784,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023.'),
('VEN',2024.0,698.546,24495.860349476978,2022.0,-73.9084713357919,173.9084713357919,2024.0,73.00549999570536,2024.0,91.1393984774741,'Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('WLF',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.'),
('WSM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,2024.0,43.75000000000001,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('YEM',NULL,NULL,NULL,2022.0,-11.0466644311721,111.0466644311721,NULL,NULL,2024.0,11.238095238095237,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('ZMB',NULL,NULL,NULL,2022.0,9.03001865064098,90.96998134935902,NULL,NULL,2024.0,87.47464503042596,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Dependencia energetica tomada en 2022 por ausencia de 2023. Electricidad baja en carbono en 2024 por ausencia de 2025.'),
('XKX',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Sin consumo de energia primaria 2025 comparable en serie OWID/EI. Sin dependencia energetica WDI en 2023/2022. Sin dato de electricidad baja en carbono 2025/2024 comparable. Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.');

SET @ind_ene_cons := (SELECT id FROM rg_indicadores WHERE codigo='ENE_CONS');
SET @ind_ene_pc := (SELECT id FROM rg_indicadores WHERE codigo='ENE_PC');
SET @ind_ene_dep := (SELECT id FROM rg_indicadores WHERE codigo='ENE_DEP');
SET @ind_ene_auto := (SELECT id FROM rg_indicadores WHERE codigo='ENE_AUTO');
SET @ind_ene_fos := (SELECT id FROM rg_indicadores WHERE codigo='ENE_FOS');
SET @ind_ene_elec_lc := (SELECT id FROM rg_indicadores WHERE codigo='ENE_ELEC_LC');

SET @src_ei := (SELECT id FROM rg_fuentes WHERE codigo='EI_SR2026');
SET @src_ember := (SELECT id FROM rg_fuentes WHERE codigo='EMBER_GER2026');
SET @src_dep := (SELECT id FROM rg_fuentes WHERE codigo='WB_IEA_ENEDEP');
SET @per := (SELECT id FROM rg_periodos WHERE codigo='RG2025_V1');

SET @next_pais_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_pais);

-- ENE_CONS
INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_ene_cons, t.anio_consumo, t.consumo_energia_twh, @src_ei,
       'FUENTE_VALIDADA', CASE WHEN t.anio_consumo=2025 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_energia_pais t
JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_ene_cons AND d.anio=t.anio_consumo
WHERE t.consumo_energia_twh IS NOT NULL AND d.id IS NULL;

-- ENE_PC
INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_ene_pc, t.anio_consumo, t.consumo_per_capita_kwh, @src_ei,
       'DERIVADO_1C6', CASE WHEN t.anio_consumo=2025 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_energia_pais t
JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_ene_pc AND d.anio=t.anio_consumo
WHERE t.consumo_per_capita_kwh IS NOT NULL AND d.id IS NULL;

-- ENE_DEP
INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_ene_dep, t.anio_dependencia, t.dependencia_energetica_pct, @src_dep,
       'FUENTE_VALIDADA', CASE WHEN t.anio_dependencia=2023 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_energia_pais t
JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_ene_dep AND d.anio=t.anio_dependencia
WHERE t.dependencia_energetica_pct IS NOT NULL AND d.id IS NULL;

-- ENE_AUTO
INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_ene_auto, t.anio_dependencia, t.autosuficiencia_pct, @src_dep,
       'DERIVADO_1C6', CASE WHEN t.anio_dependencia=2023 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_energia_pais t
JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_ene_auto AND d.anio=t.anio_dependencia
WHERE t.autosuficiencia_pct IS NOT NULL AND d.id IS NULL;

-- ENE_FOS
INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_ene_fos, t.anio_fosil, t.energia_fosil_pct, @src_ei,
       'DERIVADO_1C6', CASE WHEN t.anio_fosil=2025 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_energia_pais t
JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_ene_fos AND d.anio=t.anio_fosil
WHERE t.energia_fosil_pct IS NOT NULL AND d.id IS NULL;

-- ENE_ELEC_LC
INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_ene_elec_lc, t.anio_electricidad, t.electricidad_baja_carbono_pct, @src_ember,
       'FUENTE_VALIDADA', CASE WHEN t.anio_electricidad=2025 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_energia_pais t
JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_ene_elec_lc AND d.anio=t.anio_electricidad
WHERE t.electricidad_baja_carbono_pct IS NOT NULL AND d.id IS NULL;

DROP TEMPORARY TABLE IF EXISTS tmp_rg_energia_area;
CREATE TEMPORARY TABLE tmp_rg_energia_area (
  area_codigo VARCHAR(10) PRIMARY KEY,
  consumo_energia_twh DECIMAL(20,6) NULL,
  consumo_per_capita_kwh DECIMAL(20,6) NULL,
  dependencia_energetica_pct_aprox DECIMAL(14,6) NULL,
  autosuficiencia_pct_aprox DECIMAL(14,6) NULL,
  energia_fosil_pct DECIMAL(14,6) NULL,
  electricidad_baja_carbono_pct DECIMAL(14,6) NULL,
  entidades_totales SMALLINT NOT NULL,
  entidades_con_consumo SMALLINT NOT NULL,
  entidades_con_dependencia SMALLINT NOT NULL,
  entidades_con_fosil SMALLINT NOT NULL,
  entidades_con_electricidad SMALLINT NOT NULL,
  cobertura_consumo_poblacion_pct DECIMAL(14,6) NULL,
  cobertura_dependencia_consumo_pct DECIMAL(14,6) NULL,
  cobertura_fosil_consumo_pct DECIMAL(14,6) NULL,
  cobertura_electricidad_generacion_pct DECIMAL(14,6) NULL,
  anio_min_consumo SMALLINT NULL,
  anio_max_consumo SMALLINT NULL,
  anio_min_dependencia SMALLINT NULL,
  anio_max_dependencia SMALLINT NULL,
  anio_min_electricidad SMALLINT NULL,
  anio_max_electricidad SMALLINT NULL,
  observaciones TEXT NULL
) ENGINE=InnoDB;

INSERT INTO tmp_rg_energia_area (area_codigo,consumo_energia_twh,consumo_per_capita_kwh,dependencia_energetica_pct_aprox,autosuficiencia_pct_aprox,energia_fosil_pct,electricidad_baja_carbono_pct,entidades_totales,entidades_con_consumo,entidades_con_dependencia,entidades_con_fosil,entidades_con_electricidad,cobertura_consumo_poblacion_pct,cobertura_dependencia_consumo_pct,cobertura_fosil_consumo_pct,cobertura_electricidad_generacion_pct,anio_min_consumo,anio_max_consumo,anio_min_dependencia,anio_max_dependencia,anio_min_electricidad,anio_max_electricidad,observaciones) VALUES
('AFR',3524.834,2275.9397963762367,-18.914347599291926,118.91434759929193,95.27362139607143,27.332110465708748,59,4,4,4,51,17.367652386283233,100.0,100.0,100.0,2024,2024,2022,2023,2024,2025,'Dependencia energetica neta aproximada, ponderada por consumo energetico. Autosuficiencia energetica neta aproximada. Participacion de combustibles fosiles en el consumo de energia primaria cubierto. Porcentaje de generacion electrica baja en carbono del area cubierta.'),
('APC',20540.385000000002,21075.423877571415,29.4102929452077,70.5897070547923,85.73696646873951,31.49576716239451,43,11,10,11,29,86.97650061844332,93.89569864440223,100.0,100.0,2024,2024,2022,2023,2024,2025,'Dependencia energetica neta aproximada, ponderada por consumo energetico. Autosuficiencia energetica neta aproximada. Participacion de combustibles fosiles en el consumo de energia primaria cubierto. Porcentaje de generacion electrica baja en carbono del area cubierta. La cifra de consumo energetico del area refleja cobertura disponible, no completitud absoluta.'),
('CHN',49260.034,34587.51814454964,24.80252150039811,75.19747849960189,79.53158538217819,41.507101579990916,3,2,2,2,3,99.94930411400915,100.0,100.0,100.0,2024,2024,2022,2023,2024,2025,'Dependencia energetica neta aproximada, ponderada por consumo energetico. Autosuficiencia energetica neta aproximada. Participacion de combustibles fosiles en el consumo de energia primaria cubierto. Porcentaje de generacion electrica baja en carbono del area cubierta.'),
('EUR',19388.993000000002,32801.5049009034,38.18329048610507,61.81670951389493,65.65888697778165,71.80392685974412,51,32,31,32,38,97.07000134486388,99.67601721244624,100.0,100.0,2024,2024,2022,2023,2024,2025,'Dependencia energetica neta aproximada, ponderada por consumo energetico. Autosuficiencia energetica neta aproximada. Participacion de combustibles fosiles en el consumo de energia primaria cubierto. Porcentaje de generacion electrica baja en carbono del area cubierta.'),
('MDE',13135.71,33838.57463707289,-115.34511521002608,215.34511521002608,94.59508469660187,14.364126798260285,15,9,9,9,15,76.30078458229394,100.0,100.0,100.0,2024,2024,2022,2023,2024,2025,'Dependencia energetica neta aproximada, ponderada por consumo energetico. Autosuficiencia energetica neta aproximada. Participacion de combustibles fosiles en el consumo de energia primaria cubierto. Porcentaje de generacion electrica baja en carbono del area cubierta.'),
('NAC',32884.804000000004,53270.959949002914,-16.702915190177492,116.70291519017749,79.01428270638316,45.6985083139406,41,4,4,4,29,84.37557984250628,100.0,100.0,100.0,2024,2024,2022,2023,2024,2025,'Dependencia energetica neta aproximada, ponderada por consumo energetico. Autosuficiencia energetica neta aproximada. Participacion de combustibles fosiles en el consumo de energia primaria cubierto. Porcentaje de generacion electrica baja en carbono del area cubierta.'),
('RUE',11499.810000000001,45319.52989566567,-74.03737211194294,174.03737211194294,89.2129522139931,34.12584480918745,10,6,6,6,10,90.2105049308404,100.0,100.0,100.0,2024,2024,2022,2023,2024,2025,'Dependencia energetica neta aproximada, ponderada por consumo energetico. Autosuficiencia energetica neta aproximada. Participacion de combustibles fosiles en el consumo de energia primaria cubierto. Porcentaje de generacion electrica baja en carbono del area cubierta.'),
('SAI',12864.844000000001,6455.694552913946,36.88840102389271,63.11159897610729,88.8743695609523,28.81899845121322,8,4,4,4,8,96.24704046221989,100.0,100.0,100.0,2024,2024,2022,2023,2024,2025,'Dependencia energetica neta aproximada, ponderada por consumo energetico. Autosuficiencia energetica neta aproximada. Participacion de combustibles fosiles en el consumo de energia primaria cubierto. Porcentaje de generacion electrica baja en carbono del area cubierta.'),
('SAM',7340.439,16754.96063714492,-23.35281879791009,123.35281879791009,60.46748702632091,79.57788191190252,14,7,7,7,12,94.34551135519402,100.0,100.0,100.0,2024,2024,2022,2023,2024,2025,'Dependencia energetica neta aproximada, ponderada por consumo energetico. Autosuficiencia energetica neta aproximada. Participacion de combustibles fosiles en el consumo de energia primaria cubierto. Porcentaje de generacion electrica baja en carbono del area cubierta.');

SET @next_area_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_area);

INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)
SELECT (@next_area_id := @next_area_id + 1), a.id, x.indicador_id, @per, 2025, x.valor,
       x.metodo, t.entidades_totales, x.paises_con_dato, x.cobertura, x.anio_min, x.anio_max,
       x.fuente, 'AGREGADO_1C6', x.estado, CURDATE(), t.observaciones, 1
FROM tmp_rg_energia_area t
JOIN rg_areas a ON a.codigo=t.area_codigo
JOIN (
    SELECT area_codigo, @ind_ene_cons AS indicador_id, consumo_energia_twh AS valor,
           'Suma de consumos nacionales cubiertos' AS metodo, entidades_con_consumo AS paises_con_dato,
           cobertura_consumo_poblacion_pct AS cobertura, anio_min_consumo AS anio_min, anio_max_consumo AS anio_max,
           @src_ei AS fuente, CASE WHEN cobertura_consumo_poblacion_pct>=90 THEN 'OK' ELSE 'LIMITACION' END AS estado
    FROM tmp_rg_energia_area
    UNION ALL
    SELECT area_codigo, @ind_ene_pc, consumo_per_capita_kwh,
           'Consumo energetico agregado en kWh / poblacion 2025 del area', entidades_con_consumo,
           cobertura_consumo_poblacion_pct, anio_min_consumo, anio_max_consumo,
           @src_ei, CASE WHEN cobertura_consumo_poblacion_pct>=90 THEN 'OK' ELSE 'LIMITACION' END
    FROM tmp_rg_energia_area
    UNION ALL
    SELECT area_codigo, @ind_ene_dep, dependencia_energetica_pct_aprox,
           'Dependencia energetica neta aproximada, ponderada por consumo energetico', entidades_con_dependencia,
           cobertura_dependencia_consumo_pct, anio_min_dependencia, anio_max_dependencia,
           @src_dep, CASE WHEN cobertura_dependencia_consumo_pct>=90 THEN 'OK' ELSE 'LIMITACION' END
    FROM tmp_rg_energia_area
    UNION ALL
    SELECT area_codigo, @ind_ene_auto, autosuficiencia_pct_aprox,
           'Autosuficiencia energetica neta aproximada (100 - dependencia)', entidades_con_dependencia,
           cobertura_dependencia_consumo_pct, anio_min_dependencia, anio_max_dependencia,
           @src_dep, CASE WHEN cobertura_dependencia_consumo_pct>=90 THEN 'OK' ELSE 'LIMITACION' END
    FROM tmp_rg_energia_area
    UNION ALL
    SELECT area_codigo, @ind_ene_fos, energia_fosil_pct,
           'Participacion de combustibles fosiles en el consumo de energia primaria cubierto', entidades_con_fosil,
           cobertura_fosil_consumo_pct, anio_min_consumo, anio_max_consumo,
           @src_ei, CASE WHEN cobertura_fosil_consumo_pct>=90 THEN 'OK' ELSE 'LIMITACION' END
    FROM tmp_rg_energia_area
    UNION ALL
    SELECT area_codigo, @ind_ene_elec_lc, electricidad_baja_carbono_pct,
           'Porcentaje de generacion electrica baja en carbono del area cubierta', entidades_con_electricidad,
           cobertura_electricidad_generacion_pct, anio_min_electricidad, anio_max_electricidad,
           @src_ember, CASE WHEN cobertura_electricidad_generacion_pct>=90 THEN 'OK' ELSE 'LIMITACION' END
    FROM tmp_rg_energia_area
) x ON x.area_codigo=t.area_codigo
LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=x.indicador_id AND d.periodo_id=@per AND d.anio_referencia=2025
WHERE d.id IS NULL;

COMMIT;
