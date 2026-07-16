-- 14_rg_catalogo_militar.sql
SET NAMES utf8mb4;
START TRANSACTION;

SET @next_bloque := (SELECT COALESCE(MAX(id),0) FROM rg_bloques);

INSERT INTO rg_bloques (id,codigo,nombre,activo)
SELECT (@next_bloque := @next_bloque + 1), 'MIL', 'Fuerza militar y capacidad estrategica', 1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_bloques WHERE codigo='MIL');

SET @bloque_mil := (SELECT id FROM rg_bloques WHERE codigo='MIL' LIMIT 1);
SET @next_indicador := (SELECT COALESCE(MAX(id),0) FROM rg_indicadores);

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'MIL_GASTO', @bloque_mil, 'Gasto militar', 'usd_corrientes', 'Gasto militar nacional o agregado en dolares corrientes', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='MIL_GASTO');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'MIL_PCT', @bloque_mil, 'Porcentaje del gasto militar mundial', 'porcentaje', 'Participacion del area en el gasto militar mundial agregado', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='MIL_PCT');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'MIL_PIB', @bloque_mil, 'Gasto militar respecto al PIB', 'porcentaje', 'Relacion entre gasto militar agregado y PIB agregado comparable cubierto', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='MIL_PIB');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'MIL_PC', @bloque_mil, 'Gasto militar por habitante', 'usd_por_habitante', 'Gasto militar agregado dividido por poblacion 2025 del area', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='MIL_PC');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'MIL_NUC', @bloque_mil, 'Inventario nuclear estimado', 'ojivas', 'Total estimado de ojivas nucleares por Estado o area (fuentes abiertas)', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='MIL_NUC');

SET @next_fuente := (SELECT COALESCE(MAX(id),0) FROM rg_fuentes);

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1), 'SIPRI_MILEX_2026', 'SIPRI Military Expenditure Database 2025 (edicion 2026)', 'oficial', 'https://www.sipri.org/databases/milex', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='SIPRI_MILEX_2026');

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1), 'SIPRI_YB26_NUC', 'SIPRI Yearbook 2026 - World nuclear forces', 'oficial', 'https://www.sipri.org/yearbook/2026/08', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='SIPRI_YB26_NUC');

COMMIT;
