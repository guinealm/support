-- PROPUESTA PROVISIONAL 7A.3. NO EJECUTADA.
-- Requiere validacion definitiva en una fase posterior.
USE `u794456529_map_sim_Mund`;
SET NAMES utf8mb4;

-- La tabla de respaldo permite ejecutar 94_reversion_indicadores_complementarios_7a3.sql.
-- Confirmar antes que no exista una copia de una ejecucion anterior.
CREATE TABLE rg_backup_datos_area_7a3 LIKE rg_datos_area;
INSERT INTO rg_backup_datos_area_7a3
SELECT da.*
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
WHERE p.codigo='RG2025_V1'
  AND i.codigo IN ('TERR_DENS','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH');

CREATE TEMPORARY TABLE tmp_rg_area_7a3 (
  codigo_area CHAR(3) NOT NULL,
  codigo_indicador VARCHAR(40) NOT NULL,
  anio_referencia SMALLINT NOT NULL,
  valor DECIMAL(22,10) NOT NULL,
  metodo_calculo VARCHAR(255) NOT NULL,
  paises_totales SMALLINT UNSIGNED NOT NULL,
  paises_con_dato SMALLINT UNSIGNED NOT NULL,
  cobertura_pct DECIMAL(8,4) NOT NULL,
  observaciones TEXT NULL,
  PRIMARY KEY (codigo_area,codigo_indicador)
);

INSERT INTO tmp_rg_area_7a3
(codigo_area,codigo_indicador,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,cobertura_pct,observaciones)
VALUES
('AFR','TERR_DENS',2025,51.7392812421,'Poblacion 2025 / superficie terrestre 2023',59,58,100.000000,'Cociente de totales; superficie estructural 2023 y poblacion 2025. Incluidos 58 de 59; poblacion cubierta 1548737803 de 1548737803.'),
('APC','TERR_DENS',2025,64.5572787545,'Poblacion 2025 / superficie terrestre 2023',43,39,100.000000,'Cociente de totales; superficie estructural 2023 y poblacion 2025. Incluidos 39 de 43; poblacion cubierta 974613138 de 974613138.'),
('CHN','TERR_DENS',2025,151.6849230288,'Poblacion 2025 / superficie terrestre 2023',3,3,100.000000,'Cociente de totales; superficie estructural 2023 y poblacion 2025. Incluidos 3 de 3; poblacion cubierta 1424214186 de 1424214186.'),
('EUR','TERR_DENS',2025,106.4515359952,'Poblacion 2025 / superficie terrestre 2023',51,46,99.971494,'Cociente de totales; superficie estructural 2023 y poblacion 2025. Incluidos 46 de 51; poblacion cubierta 590932215 de 591100715.'),
('MDE','TERR_DENS',2025,62.3607420494,'Poblacion 2025 / superficie terrestre 2023',15,15,100.000000,'Cociente de totales; superficie estructural 2023 y poblacion 2025. Incluidos 15 de 15; poblacion cubierta 388187450 de 388187450.'),
('NAC','TERR_DENS',2025,29.3647789637,'Poblacion 2025 / superficie terrestre 2023',41,41,100.000000,'Cociente de totales; superficie estructural 2023 y poblacion 2025. Incluidos 41 de 41; poblacion cubierta 617312022 de 617312022.'),
('RUE','TERR_DENS',2025,12.2578028899,'Poblacion 2025 / superficie terrestre 2023',10,10,100.000000,'Cociente de totales; superficie estructural 2023 y poblacion 2025. Incluidos 10 de 10; poblacion cubierta 253749543 de 253749543.'),
('SAI','TERR_DENS',2025,417.7820021602,'Poblacion 2025 / superficie terrestre 2023',8,8,100.000000,'Cociente de totales; superficie estructural 2023 y poblacion 2025. Incluidos 8 de 8; poblacion cubierta 1992790070 de 1992790070.'),
('SAM','TERR_DENS',2025,25.0653448638,'Poblacion 2025 / superficie terrestre 2023',14,14,100.000000,'Cociente de totales; superficie estructural 2023 y poblacion 2025. Incluidos 14 de 14; poblacion cubierta 438105416 de 438105416.'),
('AFR','POB_EDAD',2023,19.4222483839,'Media ponderada aproximada de medianas nacionales 2023',59,58,100.000000,'Aproximacion: media ponderada de medianas, no mediana regional publicada. Incluidos 58 de 59; poblacion cubierta 1479690254 de 1479690254.'),
('APC','POB_EDAD',2023,34.0883791565,'Media ponderada aproximada de medianas nacionales 2023',43,39,100.000000,'Aproximacion: media ponderada de medianas, no mediana regional publicada. Incluidos 39 de 43; poblacion cubierta 964967320 de 964967320.'),
('CHN','POB_EDAD',2023,39.1024998472,'Media ponderada aproximada de medianas nacionales 2023',3,3,100.000000,'Aproximacion: media ponderada de medianas, no mediana regional publicada. Incluidos 3 de 3; poblacion cubierta 1430741584 de 1430741584.'),
('EUR','POB_EDAD',2023,43.0168309618,'Media ponderada aproximada de medianas nacionales 2023',51,48,100.000000,'Aproximacion: media ponderada de medianas, no mediana regional publicada. Incluidos 48 de 51; poblacion cubierta 590691889 de 590691889.'),
('MDE','POB_EDAD',2023,28.0802753067,'Media ponderada aproximada de medianas nacionales 2023',15,15,100.000000,'Aproximacion: media ponderada de medianas, no mediana regional publicada. Incluidos 15 de 15; poblacion cubierta 376160100 de 376160100.'),
('NAC','POB_EDAD',2023,34.7639368434,'Media ponderada aproximada de medianas nacionales 2023',41,41,100.000000,'Aproximacion: media ponderada de medianas, no mediana regional publicada. Incluidos 41 de 41; poblacion cubierta 608770547 de 608770547.'),
('RUE','POB_EDAD',2023,35.0461202946,'Media ponderada aproximada de medianas nacionales 2023',10,10,100.000000,'Aproximacion: media ponderada de medianas, no mediana regional publicada. Incluidos 10 de 10; poblacion cubierta 252435469 de 252435469.'),
('SAI','POB_EDAD',2023,26.6042206397,'Media ponderada aproximada de medianas nacionales 2023',8,8,100.000000,'Aproximacion: media ponderada de medianas, no mediana regional publicada. Incluidos 8 de 8; poblacion cubierta 1952474474 de 1952474474.'),
('SAM','POB_EDAD',2023,32.2595807338,'Media ponderada aproximada de medianas nacionales 2023',14,14,100.000000,'Aproximacion: media ponderada de medianas, no mediana regional publicada. Incluidos 14 de 14; poblacion cubierta 433024223 de 433024223.'),
('AFR','HUM_EV',2023,64.2045156654,'Media nacional 2023 ponderada por poblacion 2023',59,54,99.879978,'Media nacional ponderada; no es una tabla de mortalidad regional. Incluidos 54 de 59; poblacion cubierta 1477914293 de 1479690254.'),
('APC','HUM_EV',2023,74.5499714605,'Media nacional 2023 ponderada por poblacion 2023',43,34,97.580535,'Media nacional ponderada; no es una tabla de mortalidad regional. Incluidos 34 de 43; poblacion cubierta 941620272 de 964967320.'),
('CHN','HUM_EV',2023,77.9935535693,'Media nacional 2023 ponderada por poblacion 2023',3,3,100.000000,'Media nacional ponderada; no es una tabla de mortalidad regional. Incluidos 3 de 3; poblacion cubierta 1430741584 de 1430741584.'),
('EUR','HUM_EV',2023,80.7626824202,'Media nacional 2023 ponderada por poblacion 2023',51,45,99.971521,'Media nacional ponderada; no es una tabla de mortalidad regional. Incluidos 45 de 51; poblacion cubierta 590523665 de 590691889.'),
('MDE','HUM_EV',2023,76.0410986325,'Media nacional 2023 ponderada por poblacion 2023',15,15,100.000000,'Media nacional ponderada; no es una tabla de mortalidad regional. Incluidos 15 de 15; poblacion cubierta 376160100 de 376160100.'),
('NAC','HUM_EV',2023,77.1547598162,'Media nacional 2023 ponderada por poblacion 2023',41,34,99.870536,'Media nacional ponderada; no es una tabla de mortalidad regional. Incluidos 34 de 41; poblacion cubierta 607982407 de 608770547.'),
('RUE','HUM_EV',2023,73.1927346186,'Media nacional 2023 ponderada por poblacion 2023',10,10,100.000000,'Media nacional ponderada; no es una tabla de mortalidad regional. Incluidos 10 de 10; poblacion cubierta 252435469 de 252435469.'),
('SAI','HUM_EV',2023,71.6009692483,'Media nacional 2023 ponderada por poblacion 2023',8,8,100.000000,'Media nacional ponderada; no es una tabla de mortalidad regional. Incluidos 8 de 8; poblacion cubierta 1952474474 de 1952474474.'),
('SAM','HUM_EV',2023,76.2400545436,'Media nacional 2023 ponderada por poblacion 2023',14,12,99.929125,'Media nacional ponderada; no es una tabla de mortalidad regional. Incluidos 12 de 14; poblacion cubierta 432717317 de 433024223.'),
('AFR','ECO_PC',2024,1938.6561577151,'PIB nominal 2024 / poblacion cubierta 2024',59,52,98.858683,'Solo PIB nominal y poblacion de 2024 para las mismas entidades. Incluidos 52 de 59; poblacion cubierta 1496752464 de 1514032368.'),
('CHN','ECO_PC',2024,13441.7439742105,'PIB nominal 2024 / poblacion cubierta 2024',3,3,100.000000,'Solo PIB nominal y poblacion de 2024 para las mismas entidades. Incluidos 3 de 3; poblacion cubierta 1427456468 de 1427456468.'),
('EUR','ECO_PC',2024,42519.1316550767,'PIB nominal 2024 / poblacion cubierta 2024',51,42,99.944860,'Solo PIB nominal y poblacion de 2024 para las mismas entidades. Incluidos 42 de 51; poblacion cubierta 590554619 de 590880428.'),
('NAC','ECO_PC',2024,56842.8902189527,'PIB nominal 2024 / poblacion cubierta 2024',41,29,98.047591,'Solo PIB nominal y poblacion de 2024 para las mismas entidades. Incluidos 29 de 41; poblacion cubierta 601179114 de 613150315.'),
('RUE','ECO_PC',2024,11410.1771640523,'PIB nominal 2024 / poblacion cubierta 2024',10,10,100.000000,'Solo PIB nominal y poblacion de 2024 para las mismas entidades. Incluidos 10 de 10; poblacion cubierta 253221076 de 253221076.'),
('SAI','ECO_PC',2024,2410.0424971235,'PIB nominal 2024 / poblacion cubierta 2024',8,8,100.000000,'Solo PIB nominal y poblacion de 2024 para las mismas entidades. Incluidos 8 de 8; poblacion cubierta 1972488759 de 1972488759.'),
('SAM','ECO_PC',2024,9926.7197730408,'PIB nominal 2024 / poblacion cubierta 2024',14,12,99.928370,'Solo PIB nominal y poblacion de 2024 para las mismas entidades. Incluidos 12 de 14; poblacion cubierta 435299307 de 435611337.'),
('AFR','HUM_IDH',2023,0.5760627970,'IDH nacional 2023 ponderado por poblacion 2023',59,54,99.879978,'IDH medio ponderado; no es un IDH oficial del area. Incluidos 54 de 59; poblacion cubierta 1477914293 de 1479690254.'),
('CHN','HUM_IDH',2023,0.7978223286,'IDH nacional 2023 ponderado por poblacion 2023',3,2,99.950102,'IDH medio ponderado; no es un IDH oficial del area. Incluidos 2 de 3; poblacion cubierta 1430027668 de 1430741584.'),
('EUR','HUM_IDH',2023,0.9137653314,'IDH nacional 2023 ponderado por poblacion 2023',51,41,99.934887,'IDH medio ponderado; no es un IDH oficial del area. Incluidos 41 de 51; poblacion cubierta 590307273 de 590691889.'),
('MDE','HUM_IDH',2023,0.7644397732,'IDH nacional 2023 ponderado por poblacion 2023',15,15,100.000000,'IDH medio ponderado; no es un IDH oficial del area. Incluidos 15 de 15; poblacion cubierta 376160100 de 376160100.'),
('NAC','HUM_IDH',2023,0.8702257728,'IDH nacional 2023 ponderado por poblacion 2023',41,23,99.218337,'IDH medio ponderado; no es un IDH oficial del area. Incluidos 23 de 41; poblacion cubierta 604012013 de 608770547.'),
('RUE','HUM_IDH',2023,0.8063733675,'IDH nacional 2023 ponderado por poblacion 2023',10,10,100.000000,'IDH medio ponderado; no es un IDH oficial del area. Incluidos 10 de 10; poblacion cubierta 252435469 de 252435469.'),
('SAI','HUM_IDH',2023,0.6632529299,'IDH nacional 2023 ponderado por poblacion 2023',8,8,100.000000,'IDH medio ponderado; no es un IDH oficial del area. Incluidos 8 de 8; poblacion cubierta 1952474474 de 1952474474.'),
('SAM','HUM_IDH',2023,0.7924598368,'IDH nacional 2023 ponderado por poblacion 2023',14,12,99.929125,'IDH medio ponderado; no es un IDH oficial del area. Incluidos 12 de 14; poblacion cubierta 432717317 de 433024223.');

START TRANSACTION;
UPDATE rg_datos_area da
JOIN rg_areas a ON a.id=da.area_id
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
JOIN tmp_rg_area_7a3 t ON t.codigo_area=a.codigo AND t.codigo_indicador=i.codigo
SET da.anio_referencia=t.anio_referencia,
    da.valor=t.valor,
    da.metodo_calculo=t.metodo_calculo,
    da.paises_totales=t.paises_totales,
    da.paises_con_dato=t.paises_con_dato,
    da.porcentaje_cobertura=t.cobertura_pct,
    da.anio_minimo=t.anio_referencia,
    da.anio_maximo=t.anio_referencia,
    da.tipo_procedencia='CALCULO_7A3',
    da.estado_dato=CASE WHEN t.cobertura_pct>=95 THEN 'OK' ELSE 'LIMITACION' END,
    da.fecha_calculo=CURDATE(),
    da.observaciones=t.observaciones
WHERE p.codigo='RG2025_V1';

SELECT ROW_COUNT() AS filas_actualizadas;
SELECT i.codigo,COUNT(*) AS filas
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
WHERE p.codigo='RG2025_V1'
  AND i.codigo IN ('TERR_DENS','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH')
GROUP BY i.codigo;
COMMIT;

-- POB_URB se excluye: no existen datos nacionales comparables incorporados.
