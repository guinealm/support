-- 23_rg_catalogo_tecnologia.sql
SET NAMES utf8mb4;
START TRANSACTION;
SET @next_bloque := (SELECT COALESCE(MAX(id),0) FROM rg_bloques);
INSERT INTO rg_bloques (id,codigo,nombre,activo)
SELECT (@next_bloque := @next_bloque + 1),'TEC','Tecnologia, digitalizacion e innovacion',1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_bloques WHERE codigo='TEC');
SET @bloque_tec := (SELECT id FROM rg_bloques WHERE codigo='TEC');
SET @next_indicador := (SELECT COALESCE(MAX(id),0) FROM rg_indicadores);
INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1),'TEC_NET',@bloque_tec,'Poblacion usuaria de Internet','porcentaje_poblacion','Personas que utilizaron Internet desde cualquier lugar en los ultimos tres meses',1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='TEC_NET');
SET @next_fuente := (SELECT COALESCE(MAX(id),0) FROM rg_fuentes);
INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1),'ITU_WB_NET','UIT, World Telecommunication/ICT Indicators Database, distribuido por Banco Mundial','oficial_procesado','https://data.worldbank.org/indicator/IT.NET.USER.ZS',1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='ITU_WB_NET');
INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1),'ITU_DATAHUB','UIT DataHub, Individuals using the Internet','oficial','https://datahub.itu.int/data/?i=11624',1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='ITU_DATAHUB');
COMMIT;
