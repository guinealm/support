-- 02_rg_catalogos_iniciales.sql
SET NAMES utf8mb4;

DELETE FROM rg_datos_area;
DELETE FROM rg_datos_pais;
DELETE FROM rg_paises;
DELETE FROM rg_periodos;
DELETE FROM rg_fuentes;
DELETE FROM rg_indicadores;
DELETE FROM rg_bloques;
DELETE FROM rg_areas;

INSERT INTO rg_areas (id,codigo,slug,nombre,nombre_corto,color_principal,orden_visual,activo,fecha_revision) VALUES
(1,'AFR','afr','África','África',NULL,1,1,'2026-07-15'),
(2,'APC','apc','Asia-Pacífico','Asia-Pacífico',NULL,2,1,'2026-07-15'),
(3,'CHN','chn','China','China',NULL,3,1,'2026-07-15'),
(4,'EUR','eur','Europa','Europa',NULL,4,1,'2026-07-15'),
(5,'MDE','mde','Oriente Medio','Oriente Medio',NULL,5,1,'2026-07-15'),
(6,'NAC','nac','Norteamérica y Caribe','Norteamérica y Caribe',NULL,6,1,'2026-07-15'),
(7,'RUE','rue','Rusia y Eurasia postsoviética','Rusia y Eurasia postsoviética',NULL,7,1,'2026-07-15'),
(8,'SAI','sai','Subcontinente indio','Subcontinente indio',NULL,8,1,'2026-07-15'),
(9,'SAM','sam','Sudamérica','Sudamérica',NULL,9,1,'2026-07-15');

INSERT INTO rg_bloques (id,codigo,nombre,activo) VALUES
(1,'TERR','Territorio',1),
(2,'POB','Poblacion',1);

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo) VALUES
(1,'TERR_SUP',1,'Superficie','km2','Superficie terrestre',1),
(2,'TERR_PCT',1,'Superficie mundial %','%','Porcentaje de superficie mundial',1),
(3,'TERR_DENS',1,'Densidad','hab_km2','Poblacion por km2',1),
(4,'POB_TOTAL',2,'Poblacion total','personas','Poblacion estimada',1),
(5,'POB_PCT',2,'Poblacion mundial %','%','Porcentaje de poblacion mundial',1),
(6,'POB_EDAD',2,'Edad mediana','anios','Edad mediana aproximada',1),
(7,'POB_2050',2,'Poblacion 2050','personas','Poblacion proyectada 2050',1),
(8,'POB_VAR_2050',2,'Variacion 2025-2050','%','Variacion porcentual 2025-2050',1);

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo) VALUES
(1,'UN_WPP_2024','ONU World Population Prospects 2024','oficial','https://ourworldindata.org/grapher/population-with-un-projections.csv?v=1&csvType=full&useColumnShortNames=false',1),
(2,'FAOSTAT_2025','FAOSTAT','oficial','https://ourworldindata.org/grapher/land-area-hectares.csv?v=1&csvType=full&useColumnShortNames=false',1),
(3,'OWID','Our World in Data','procesador','https://ourworldindata.org',1);

INSERT INTO rg_periodos (id,codigo,nombre,estado,activo) VALUES
(1,'RG2025_V1','Reticula Global 2025 - Primera edicion','preparacion',1);
