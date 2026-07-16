-- 15_rg_datos_militar.sql
SET NAMES utf8mb4;
START TRANSACTION;

DROP TEMPORARY TABLE IF EXISTS tmp_rg_militar_pais;
CREATE TEMPORARY TABLE tmp_rg_militar_pais (
  codigo_iso3 VARCHAR(3) PRIMARY KEY,
  anio_gasto SMALLINT NULL,
  gasto_militar_usd DECIMAL(20,6) NULL,
  gasto_militar_pct_pib DECIMAL(12,6) NULL,
  observaciones TEXT NULL
) ENGINE=InnoDB;

INSERT INTO tmp_rg_militar_pais (codigo_iso3,anio_gasto,gasto_militar_usd,gasto_militar_pct_pib,observaciones) VALUES
('AFG',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('ALB',2025.0,623614024.5729697,0.020325031435452803,''),
('DZA',2025.0,25438789692.334564,0.0883062559516761,''),
('ASM',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('AND',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('AGO',2025.0,1459150446.303329,0.013968300022016407,''),
('ATG',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('AZE',2025.0,4939000000.0,0.06465505956276998,''),
('ARG',2025.0,3875750072.354246,0.005631741127021983,''),
('AUS',2025.0,35326559811.29522,0.01917873083691095,''),
('AUT',2025.0,6353360557.723981,0.011006335138112954,''),
('BHS',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('BHR',2025.0,1468151595.744681,0.031054670025549735,''),
('BGD',2025.0,3826632299.58464,0.008105876769470378,''),
('ARM',2025.0,1725213042.6808634,0.06093545985205533,''),
('BRB',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('BEL',2025.0,14531958576.811136,0.02008893871208229,''),
('BMU',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('BTN',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('BOL',2025.0,688306801.7366136,0.01214532355175434,''),
('BIH',2025.0,231395167.75581536,0.007283302900341615,''),
('BWA',2025.0,614353516.2293174,0.031078158759045633,''),
('BRA',2025.0,23949869705.559586,0.010544932096497133,''),
('BLZ',2025.0,33317349.999999996,0.009956591792927613,''),
('IOT',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('SLB',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('VGB',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('BRN',2024.0,560266733.7424988,0.03652133760216016,'SIPRI no publica 2025 para esta entidad; se conserva 2024 separado.'),
('BGR',2025.0,2589155424.306569,0.02006374577483869,''),
('MMR',2024.0,5011272415.126733,0.06604805119117459,'SIPRI no publica 2025 para esta entidad; se conserva 2024 separado.'),
('BDI',2025.0,226615473.53087303,0.03242394814929607,''),
('BLR',2025.0,1938589500.4900749,0.023973873975455792,''),
('KHM',2025.0,738950217.7180358,0.014501226624683072,''),
('CMR',2025.0,627467840.6823967,0.010582867226575213,''),
('CAN',2025.0,37494244642.3716,0.01627447396350995,''),
('CPV',2025.0,20076627.568532564,0.006575158855219908,''),
('CYM',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('CAF',2025.0,74185526.58732888,0.023321331656720103,''),
('LKA',2025.0,1390730987.1518633,0.013111912838068854,''),
('TCD',2025.0,648809933.2737154,0.031851802790340174,''),
('CHL',2025.0,5327885653.379976,0.015202086436351594,''),
('CHN',2025.0,335524155624.44,0.01724723316575711,'CHN separado de HKG y MAC.'),
('TWN',2025.0,18187723316.285767,0.02098535636731983,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. TWN revisado expresamente; mantener separado si la fuente no publica serie comparable.'),
('CXR',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('CCK',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('COL',2025.0,14502706852.6697,0.03202105085963565,''),
('COM',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('MYT',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('COG',2025.0,204916764.11914426,0.013092720148724422,''),
('COD',2025.0,1225252134.1519628,0.013751452231075286,''),
('COK',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('CRI',2025.0,0.0,0.0,''),
('HRV',2025.0,2101617670.2840512,0.02018558343673175,''),
('CUB',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('CYP',2025.0,663312501.4101031,0.01605310961570736,''),
('CZE',2025.0,7051481133.0233755,0.01835646969402079,''),
('BEN',2025.0,216913737.3598404,0.008900779239346037,''),
('DNK',2025.0,14948790190.933384,0.03252852051205041,''),
('DMA',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('DOM',2025.0,1037253440.08817,0.008023020922876148,''),
('ECU',2025.0,2735600000.0,0.020957782267652623,''),
('SLV',2025.0,490000000.0,0.013392735124497773,''),
('GNQ',2025.0,120731065.55685492,0.0089763643005565,''),
('ETH',2025.0,528111206.3192609,0.004937391634111991,''),
('ERI',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('EST',2025.0,1575931232.0916905,0.03374417800792759,''),
('FRO',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('FLK',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('FJI',2025.0,81159432.22357386,0.013300334824945277,''),
('FIN',2025.0,8081582925.343501,0.02571170162367027,''),
('ALA',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('FRA',2025.0,68007580714.301834,0.020266296920856373,''),
('GUF',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('PYF',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('DJI',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('GAB',2025.0,356111990.0942423,0.016619472806552956,''),
('GEO',2025.0,657878727.0171082,0.01745828116359766,''),
('GMB',2025.0,14738181.34045069,0.00569750931440142,''),
('PSE',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('DEU',2025.0,113585948604.56197,0.02268510925145227,''),
('GHA',2025.0,506651717.200633,0.004768161807193156,''),
('GIB',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('KIR',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('GRC',2025.0,8388421361.369943,0.029888142525625296,''),
('GRL',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('GRD',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('GLP',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('GUM',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('GTM',2025.0,632872273.9811586,0.005231496438573953,''),
('GIN',2025.0,600539642.4306408,0.02027963292300796,''),
('GUY',2025.0,247643803.40654925,0.009913924529825313,''),
('HTI',2025.0,39144696.97650407,0.0012116192286238739,''),
('VAT',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('HND',2025.0,580246011.6353736,0.014634721943738289,''),
('HKG',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('HUN',2025.0,5001983632.200585,0.02036801022463418,''),
('ISL',2025.0,0.0,0.0,''),
('IND',2025.0,92057013588.1601,0.022951791793515173,''),
('IDN',2025.0,15025416115.28609,0.010446886384200042,''),
('IRN',2025.0,7396057109.81132,0.020915792291092736,''),
('IRQ',2025.0,6447958100.793245,0.024473493526667365,''),
('IRL',2025.0,1551113417.4130812,0.0021912979177091934,''),
('ISR',2025.0,48281256782.26126,0.07809064087959404,''),
('ITA',2025.0,48143627462.04002,0.018887272002891593,''),
('CIV',2025.0,759441425.3284721,0.007748750663545787,''),
('JAM',2025.0,286646045.6699049,0.013682967070821951,''),
('JPN',2025.0,62158093812.44194,0.014116699864430388,''),
('KAZ',2025.0,1308552096.598493,0.004303384155314186,''),
('JOR',2025.0,2555352112.6760564,0.045568102032700626,''),
('KEN',2025.0,1469684195.8712654,0.010677992140784137,''),
('PRK',NULL,NULL,NULL,'SIPRI no dispone de gasto militar reciente comparable para Corea del Norte; último dato histórico no utilizado por falta de comparabilidad temporal.'),
('KOR',2025.0,47770908937.46307,0.02601468951273027,''),
('KWT',2025.0,8088284947.007522,0.04687972209290038,''),
('KGZ',2025.0,601125601.9789898,0.029171251904690748,''),
('LAO',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('LBN',2025.0,828299104.1556169,0.025096134166182504,''),
('LSO',2025.0,39909364.883225515,0.016290959098571717,''),
('LVA',2025.0,1731606615.0756943,0.03607721000298902,''),
('LBR',2025.0,44210000.0,0.00853145503666538,''),
('LBY',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('LIE',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('LTU',2025.0,2952191864.2691154,0.03079753664717059,''),
('LUX',2025.0,855409155.5174514,0.008510505050505051,''),
('MAC',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('MDG',2025.0,119676668.15152624,0.006188718289447978,''),
('MWI',2025.0,162819193.4042492,0.011454969663418304,''),
('MYS',2025.0,4933177367.160248,0.010360232333830478,''),
('MDV',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('MLI',2025.0,952899497.8331155,0.038741279168859825,''),
('MLT',2025.0,124657626.96568373,0.004488288390428941,''),
('MTQ',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('MRT',2025.0,321759024.9932787,0.027484162249529907,''),
('MUS',2025.0,23839838.912924312,0.0014553642153844236,''),
('MEX',2025.0,13647711360.169912,0.007368094923746284,''),
('MCO',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('MNG',2025.0,221316703.29112354,0.008826504651376375,''),
('MDA',2025.0,113287334.34316091,0.005603007679420097,''),
('MNE',2025.0,176544908.96374342,0.01889984443151503,''),
('MSR',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('MAR',2025.0,6330727244.328332,0.035431055025931676,''),
('MOZ',2025.0,468062039.7932007,0.018654788323732446,''),
('OMN',2025.0,5988296488.946684,0.05682376091700867,''),
('NAM',2025.0,410522284.1614994,0.027663322168259792,''),
('NRU',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('NPL',2025.0,428290814.1303412,0.009657444785825284,''),
('NLD',2025.0,28944340410.17079,0.021945445152637934,''),
('CUW',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('ABW',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('SXM',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('BES',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('NCL',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('VUT',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('NZL',2025.0,2855732604.4604692,0.011022496023962065,''),
('NIC',2025.0,116367344.16423084,0.0056480290286382824,''),
('NER',2025.0,488890417.555204,0.021357835044651524,''),
('NGA',2025.0,2101677527.9642794,0.009094449270720074,''),
('NIU',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('NFK',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('NOR',2025.0,17033643852.490572,0.032784814370343564,''),
('MNP',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('FSM',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('MHL',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('PLW',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('PAK',2025.0,11871380866.105368,0.029136125148539926,''),
('PAN',2025.0,0.0,0.0,''),
('PNG',2025.0,106480682.7655668,0.0035026033136118665,''),
('PRY',2025.0,421095331.4693742,0.008755943179888046,''),
('PER',2025.0,2596241408.393085,0.008124447472562586,''),
('PHL',2025.0,6378758229.620545,0.01295336952280744,''),
('PCN',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('POL',2025.0,46760133894.597916,0.044969375748071326,''),
('PRT',2025.0,5861290977.596282,0.017112082110627345,''),
('GNB',2025.0,22360184.357157595,0.008870465553036184,''),
('TLS',2025.0,47916000.0,0.02254870588235294,''),
('PRI',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('QAT',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('REU',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('ROU',2025.0,9725350362.953861,0.02281166438721189,''),
('RUS',2025.0,190416640325.2106,0.07501484654936362,'RUS asignado exclusivamente a RUE.'),
('RWA',2025.0,191192499.02185458,0.012862046757969887,''),
('BLM',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('SHN',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('KNA',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('AIA',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('LCA',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('MAF',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('SPM',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('VCT',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('SMR',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('STP',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('SAU',2025.0,83181333333.33333,0.06482319949446061,''),
('SEN',2025.0,566873602.7515048,0.015554365077066411,''),
('SRB',2025.0,2781295696.285387,0.027553912788627778,''),
('SYC',2025.0,28380338.884222656,0.012443069628920844,''),
('SLE',2025.0,32182766.10896686,0.0037026571772029063,''),
('SGP',2025.0,17438486492.276382,0.030462464248483066,''),
('SVK',2025.0,3118330513.254371,0.020319797041979115,''),
('VNM',2025.0,10487302148.867115,0.02153801933360168,''),
('SVN',2025.0,1221658206.42978,0.015441648249803949,''),
('SOM',2025.0,199468000.0,0.015410074165636589,''),
('ZAF',2025.0,3173874329.7418494,0.007373520085170768,''),
('ZWE',2025.0,159639292.7063351,0.005646127356810411,''),
('ESP',2025.0,40211754089.114494,0.02128921138284213,''),
('SSD',2025.0,178422465.6947426,0.03424746568970281,''),
('SDN',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('ESH',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('SUR',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('SJM',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('SWZ',2025.0,93361425.00097848,0.016021843061389714,''),
('SWE',2025.0,16473477206.496712,0.024711848495400413,''),
('CHE',2025.0,7591405901.0693865,0.007569245382939775,''),
('SYR',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('TJK',2025.0,246931888.3215365,0.014735834768823543,''),
('THA',2025.0,5983978404.684055,0.010376759596338476,''),
('TGO',2025.0,204947549.4411006,0.01873993929415102,''),
('TKL',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('TON',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('TTO',2025.0,229899160.50605452,0.009393365273659585,''),
('ARE',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('TUN',2025.0,1484859113.7612534,0.024949611547812552,''),
('TUR',2025.0,29986711540.60079,0.0190825227714357,''),
('TKM',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('TCA',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('TUV',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('UGA',2025.0,1296994464.2173004,0.019571287799143737,''),
('UKR',2025.0,84109045741.85442,0.39561018358008804,''),
('MKD',2025.0,374751246.9719014,0.019664112754277915,''),
('EGY',2025.0,2501747815.2309613,0.006055802166128685,''),
('GBR',2025.0,88977496940.39256,0.02353264154125178,''),
('GGY',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('JEY',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('IMN',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('TZA',2025.0,1030461758.3207084,0.011567162118438742,''),
('USA',2025.0,954387000000.0,0.031173079810605936,'USA asignado exclusivamente a NAC.'),
('VIR',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('BFA',2025.0,891556029.4421132,0.03300299356452818,''),
('URY',2025.0,1954316864.68679,0.02284444197592897,''),
('UZB',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('VEN',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('WLF',NULL,NULL,NULL,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('WSM',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('YEM',NULL,NULL,NULL,'Sin dato SIPRI usable para 2025/2024 en esta entidad.'),
('ZMB',2025.0,405858785.2056163,0.012601679088743102,''),
('XKX',2025.0,234500146.6507231,0.01852817265223786,'Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado. XKX revisado expresamente; mantener sin duplicidad con SRB.');

DROP TEMPORARY TABLE IF EXISTS tmp_rg_militar_nuclear;
CREATE TEMPORARY TABLE tmp_rg_militar_nuclear (
  codigo_iso3 VARCHAR(3) PRIMARY KEY,
  anio_referencia SMALLINT NOT NULL,
  ojivas_totales_estimadas INT NOT NULL,
  observaciones TEXT NULL
) ENGINE=InnoDB;

INSERT INTO tmp_rg_militar_nuclear (codigo_iso3,anio_referencia,ojivas_totales_estimadas,observaciones) VALUES
('USA',2026,5132,'Inventario nuclear estimado (columna utilizada: inventario total estimado, SIPRI Yearbook 2026) a partir de fuentes abiertas; no representa disponibilidad operativa, precision, vectores, doctrina ni capacidad de segundo ataque'),
('RUS',2026,5430,'Inventario nuclear estimado (columna utilizada: inventario total estimado, SIPRI Yearbook 2026) a partir de fuentes abiertas; no representa disponibilidad operativa, precision, vectores, doctrina ni capacidad de segundo ataque'),
('CHN',2026,620,'Inventario nuclear estimado (columna utilizada: inventario total estimado, SIPRI Yearbook 2026) a partir de fuentes abiertas; no representa disponibilidad operativa, precision, vectores, doctrina ni capacidad de segundo ataque'),
('FRA',2026,290,'Inventario nuclear estimado (columna utilizada: inventario total estimado, SIPRI Yearbook 2026) a partir de fuentes abiertas; no representa disponibilidad operativa, precision, vectores, doctrina ni capacidad de segundo ataque'),
('GBR',2026,225,'Inventario nuclear estimado (columna utilizada: inventario total estimado, SIPRI Yearbook 2026) a partir de fuentes abiertas; no representa disponibilidad operativa, precision, vectores, doctrina ni capacidad de segundo ataque'),
('IND',2026,180,'Inventario nuclear estimado (columna utilizada: inventario total estimado, SIPRI Yearbook 2026) a partir de fuentes abiertas; no representa disponibilidad operativa, precision, vectores, doctrina ni capacidad de segundo ataque'),
('PAK',2026,170,'Inventario nuclear estimado (columna utilizada: inventario total estimado, SIPRI Yearbook 2026) a partir de fuentes abiertas; no representa disponibilidad operativa, precision, vectores, doctrina ni capacidad de segundo ataque'),
('ISR',2026,90,'Inventario nuclear estimado (columna utilizada: inventario total estimado, SIPRI Yearbook 2026) a partir de fuentes abiertas; no representa disponibilidad operativa, precision, vectores, doctrina ni capacidad de segundo ataque'),
('PRK',2026,50,'Inventario nuclear estimado (columna utilizada: inventario total estimado, SIPRI Yearbook 2026) a partir de fuentes abiertas; no representa disponibilidad operativa, precision, vectores, doctrina ni capacidad de segundo ataque');

SET @ind_mil_gasto := (SELECT id FROM rg_indicadores WHERE codigo='MIL_GASTO');
SET @ind_mil_pct := (SELECT id FROM rg_indicadores WHERE codigo='MIL_PCT');
SET @ind_mil_pib := (SELECT id FROM rg_indicadores WHERE codigo='MIL_PIB');
SET @ind_mil_pc := (SELECT id FROM rg_indicadores WHERE codigo='MIL_PC');
SET @ind_mil_nuc := (SELECT id FROM rg_indicadores WHERE codigo='MIL_NUC');
SET @src_milex := (SELECT id FROM rg_fuentes WHERE codigo='SIPRI_MILEX_2026');
SET @src_nuc := (SELECT id FROM rg_fuentes WHERE codigo='SIPRI_YB26_NUC');
SET @per := (SELECT id FROM rg_periodos WHERE codigo='RG2025_V1');

SET @next_pais_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_pais);

INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_mil_gasto, t.anio_gasto, t.gasto_militar_usd, @src_milex,
       'FUENTE_VALIDADA', CASE WHEN t.anio_gasto = 2025 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_militar_pais t
JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_mil_gasto AND d.anio=t.anio_gasto
WHERE t.gasto_militar_usd IS NOT NULL AND d.id IS NULL;

INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_mil_pib, t.anio_gasto, t.gasto_militar_pct_pib, @src_milex,
       'FUENTE_VALIDADA', CASE WHEN t.anio_gasto = 2025 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_militar_pais t
JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_mil_pib AND d.anio=t.anio_gasto
WHERE t.gasto_militar_pct_pib IS NOT NULL AND d.id IS NULL;

INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_mil_nuc, n.anio_referencia, n.ojivas_totales_estimadas, @src_nuc,
       'FUENTE_VALIDADA', 'LIMITACION', CURDATE(), n.observaciones, 1
FROM tmp_rg_militar_nuclear n
JOIN rg_paises p ON p.codigo_iso3=n.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_mil_nuc AND d.anio=n.anio_referencia
WHERE d.id IS NULL;

UPDATE rg_datos_pais d
JOIN rg_paises p ON p.id=d.pais_id
JOIN tmp_rg_militar_pais t ON t.codigo_iso3=p.codigo_iso3
SET d.valor=t.gasto_militar_usd, d.fuente_id=@src_milex, d.tipo_procedencia='FUENTE_VALIDADA',
    d.estado_dato=CASE WHEN t.anio_gasto=2025 THEN 'OK' ELSE 'LIMITACION' END, d.fecha_carga=CURDATE(),
    d.observaciones=t.observaciones, d.activo=1
WHERE d.indicador_id=@ind_mil_gasto AND t.gasto_militar_usd IS NOT NULL AND d.anio=t.anio_gasto;

UPDATE rg_datos_pais d
JOIN rg_paises p ON p.id=d.pais_id
JOIN tmp_rg_militar_pais t ON t.codigo_iso3=p.codigo_iso3
SET d.valor=t.gasto_militar_pct_pib, d.fuente_id=@src_milex, d.tipo_procedencia='FUENTE_VALIDADA',
    d.estado_dato=CASE WHEN t.anio_gasto=2025 THEN 'OK' ELSE 'LIMITACION' END, d.fecha_carga=CURDATE(),
    d.observaciones=t.observaciones, d.activo=1
WHERE d.indicador_id=@ind_mil_pib AND t.gasto_militar_pct_pib IS NOT NULL AND d.anio=t.anio_gasto;

UPDATE rg_datos_pais d
JOIN rg_paises p ON p.id=d.pais_id
JOIN tmp_rg_militar_nuclear n ON n.codigo_iso3=p.codigo_iso3
SET d.valor=n.ojivas_totales_estimadas, d.fuente_id=@src_nuc, d.tipo_procedencia='FUENTE_VALIDADA',
    d.estado_dato='LIMITACION', d.fecha_carga=CURDATE(), d.observaciones=n.observaciones, d.activo=1
WHERE d.indicador_id=@ind_mil_nuc AND d.anio=n.anio_referencia;

DROP TEMPORARY TABLE IF EXISTS tmp_rg_militar_area;
CREATE TEMPORARY TABLE tmp_rg_militar_area (
  area_codigo VARCHAR(10) PRIMARY KEY,
  anio_gasto SMALLINT NOT NULL,
  gasto_militar_usd DECIMAL(20,6) NOT NULL,
  gasto_militar_mundial_pct DECIMAL(12,8) NOT NULL,
  gasto_militar_pct_pib_aprox DECIMAL(12,8) NULL,
  gasto_militar_por_habitante DECIMAL(20,8) NULL,
  anio_nuclear SMALLINT NOT NULL,
  ojivas_nucleares_estimadas INT NOT NULL,
  entidades_totales SMALLINT NOT NULL,
  entidades_con_gasto SMALLINT NOT NULL,
  cobertura_poblacion_pct DECIMAL(12,8) NULL,
  cobertura_pib_pct DECIMAL(12,8) NULL,
  anio_min_gasto SMALLINT NULL,
  anio_max_gasto SMALLINT NULL,
  observaciones TEXT NULL
) ENGINE=InnoDB;

INSERT INTO tmp_rg_militar_area (area_codigo,anio_gasto,gasto_militar_usd,gasto_militar_mundial_pct,gasto_militar_pct_pib_aprox,gasto_militar_por_habitante,anio_nuclear,ojivas_nucleares_estimadas,entidades_totales,entidades_con_gasto,cobertura_poblacion_pct,cobertura_pib_pct,anio_min_gasto,anio_max_gasto,observaciones) VALUES
('AFR',2025,59039714638.15033,2.0631828444780567,2.1108669272253655,38.121181341210104,2026,0,59,48,95.68290611422495,96.39014276640059,2025,2025,'MIL_PIB calculado como gasto agregado / PIB agregado comparable cubierto. No se usa media simple de porcentajes nacionales. Area sin Estado con arsenal nuclear identificado por SIPRI (cero real).'),
('APC',2025,233313499424.70847,8.153298374635916,1.9217154354882446,239.39088272859755,2026,50,43,18,96.19006038886376,99.69014511967401,2024,2025,'MIL_PIB calculado como gasto agregado / PIB agregado comparable cubierto. No se usa media simple de porcentajes nacionales. Incluye entidades con ultimo dato 2024 separado y marcado. Gasto militar conocido y comparable de los paises cubiertos por SIPRI.'),
('CHN',2025,335524155624.44,11.725119032757199,1.7914046731455067,235.58546103713644,2026,620,3,1,99.42999493476468,97.61388488915165,2025,2025,'MIL_PIB calculado como gasto agregado / PIB agregado comparable cubierto. No se usa media simple de porcentajes nacionales.'),
('EUR',2025,662803047287.608,23.162101727841502,2.641392138403282,1121.303071486909,2026,515,51,39,99.9079074028865,99.84985635454431,2025,2025,'MIL_PIB calculado como gasto agregado / PIB agregado comparable cubierto. No se usa media simple de porcentajes nacionales.'),
('MDE',2025,194221701115.33054,6.787208986737891,4.506007606463988,500.32967607615996,2026,90,15,10,77.47329827381076,84.5996334409021,2025,2025,'MIL_PIB calculado como gasto agregado / PIB agregado comparable cubierto. No se usa media simple de porcentajes nacionales. Cobertura PIB condicionada para el calculo aproximado.'),
('NAC',2025,1008974702325.5629,35.25930484435813,2.9687968983219095,1634.4646894396021,2026,5132,41,14,97.2503449803218,99.44374692921869,2025,2025,'MIL_PIB calculado como gasto agregado / PIB agregado comparable cubierto. No se usa media simple de porcentajes nacionales.'),
('RUE',2025,201833931182.29767,7.053223525911124,7.410307189124442,795.4060874202153,2026,5430,10,8,82.3951288850203,94.26831185794782,2025,2025,'MIL_PIB calculado como gasto agregado / PIB agregado comparable cubierto. No se usa media simple de porcentajes nacionales.'),
('SAI',2025,109574048555.13231,3.829139394804453,2.318735487214809,54.98524415827318,2026,350,8,5,97.7333043916663,99.40706741333038,2025,2025,'MIL_PIB calculado como gasto agregado / PIB agregado comparable cubierto. No se usa media simple de porcentajes nacionales.'),
('SAM',2025,56299416493.655914,1.9674212684757466,1.3417045400199334,128.50655216199362,2026,0,14,10,93.2724141442707,97.10761023420808,2025,2025,'MIL_PIB calculado como gasto agregado / PIB agregado comparable cubierto. No se usa media simple de porcentajes nacionales. Area sin Estado con arsenal nuclear identificado por SIPRI (cero real).');

SET @next_area_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_area);

INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)
SELECT (@next_area_id := @next_area_id + 1), a.id, x.indicador_id, @per, x.anio_referencia, x.valor,
       x.metodo_calculo, t.entidades_totales, x.paises_con_dato, x.cobertura, x.anio_minimo, x.anio_maximo,
       x.fuente_id, 'AGREGADO_1C5', x.estado_dato, CURDATE(), t.observaciones, 1
FROM tmp_rg_militar_area t
JOIN rg_areas a ON a.codigo=t.area_codigo
JOIN (
    SELECT area_codigo, @ind_mil_gasto AS indicador_id, anio_gasto AS anio_referencia, gasto_militar_usd AS valor,
           'Suma del gasto militar nacional incluido (SIPRI)' AS metodo_calculo, entidades_con_gasto AS paises_con_dato,
           cobertura_poblacion_pct AS cobertura, anio_min_gasto AS anio_minimo, anio_max_gasto AS anio_maximo,
           @src_milex AS fuente_id, CASE WHEN cobertura_poblacion_pct >= 90 THEN 'OK' ELSE 'LIMITACION' END AS estado_dato
    FROM tmp_rg_militar_area
    UNION ALL
    SELECT area_codigo, @ind_mil_pct, anio_gasto, gasto_militar_mundial_pct,
           'Gasto militar del area / gasto militar de las nueve areas x 100', entidades_con_gasto,
           cobertura_poblacion_pct, anio_min_gasto, anio_max_gasto,
           @src_milex, CASE WHEN cobertura_poblacion_pct >= 90 THEN 'OK' ELSE 'LIMITACION' END
    FROM tmp_rg_militar_area
    UNION ALL
    SELECT area_codigo, @ind_mil_pib, anio_gasto, gasto_militar_pct_pib_aprox,
           'Gasto militar agregado / PIB agregado comparable cubierto x 100', entidades_con_gasto,
           cobertura_pib_pct, anio_min_gasto, anio_max_gasto,
           @src_milex, CASE WHEN cobertura_pib_pct >= 90 THEN 'OK' ELSE 'LIMITACION' END
    FROM tmp_rg_militar_area
    UNION ALL
    SELECT area_codigo, @ind_mil_pc, anio_gasto, gasto_militar_por_habitante,
           'Gasto militar agregado / poblacion 2025 del area', entidades_con_gasto,
           cobertura_poblacion_pct, anio_min_gasto, anio_max_gasto,
           @src_milex, CASE WHEN cobertura_poblacion_pct >= 90 THEN 'OK' ELSE 'LIMITACION' END
    FROM tmp_rg_militar_area
    UNION ALL
    SELECT area_codigo, @ind_mil_nuc, anio_nuclear, ojivas_nucleares_estimadas,
           'Suma de ojivas estimadas de los Estados nucleares del area', entidades_totales,
           100.0, anio_nuclear, anio_nuclear,
           @src_nuc, 'LIMITACION'
    FROM tmp_rg_militar_area
) x ON x.area_codigo=t.area_codigo
LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=x.indicador_id AND d.periodo_id=@per AND d.anio_referencia=x.anio_referencia
WHERE d.id IS NULL;

UPDATE rg_datos_area d
JOIN rg_areas a ON a.id=d.area_id
JOIN tmp_rg_militar_area t ON t.area_codigo=a.codigo
SET d.valor = CASE
        WHEN d.indicador_id=@ind_mil_gasto THEN t.gasto_militar_usd
        WHEN d.indicador_id=@ind_mil_pct THEN t.gasto_militar_mundial_pct
        WHEN d.indicador_id=@ind_mil_pib THEN t.gasto_militar_pct_pib_aprox
        WHEN d.indicador_id=@ind_mil_pc THEN t.gasto_militar_por_habitante
        WHEN d.indicador_id=@ind_mil_nuc THEN t.ojivas_nucleares_estimadas
        ELSE d.valor END,
    d.paises_totales=t.entidades_totales,
    d.paises_con_dato=CASE WHEN d.indicador_id=@ind_mil_nuc THEN t.entidades_totales ELSE t.entidades_con_gasto END,
    d.porcentaje_cobertura=CASE WHEN d.indicador_id=@ind_mil_pib THEN t.cobertura_pib_pct WHEN d.indicador_id=@ind_mil_nuc THEN 100.0 ELSE t.cobertura_poblacion_pct END,
    d.anio_minimo=CASE WHEN d.indicador_id=@ind_mil_nuc THEN t.anio_nuclear ELSE t.anio_min_gasto END,
    d.anio_maximo=CASE WHEN d.indicador_id=@ind_mil_nuc THEN t.anio_nuclear ELSE t.anio_max_gasto END,
    d.fuente_principal_id=CASE WHEN d.indicador_id=@ind_mil_nuc THEN @src_nuc ELSE @src_milex END,
    d.tipo_procedencia='AGREGADO_1C5',
    d.estado_dato=CASE
        WHEN d.indicador_id=@ind_mil_nuc THEN 'LIMITACION'
        WHEN d.indicador_id=@ind_mil_pib AND t.cobertura_pib_pct >= 90 THEN 'OK'
        WHEN d.indicador_id<>@ind_mil_pib AND t.cobertura_poblacion_pct >= 90 THEN 'OK'
        ELSE 'LIMITACION' END,
    d.fecha_calculo=CURDATE(),
    d.observaciones=t.observaciones,
    d.activo=1
WHERE d.periodo_id=@per
  AND (
      (d.indicador_id IN (@ind_mil_gasto,@ind_mil_pct,@ind_mil_pib,@ind_mil_pc) AND d.anio_referencia=2025)
      OR (d.indicador_id=@ind_mil_nuc AND d.anio_referencia=2026)
  );

COMMIT;
