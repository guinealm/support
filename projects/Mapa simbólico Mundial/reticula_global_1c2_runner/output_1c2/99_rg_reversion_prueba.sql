-- 99_rg_reversion_prueba.sql
-- Reversion de la implantacion minima 1C.2B.
-- Elimina solo objetos prefijados con rg_ creados para esta prueba.

SET FOREIGN_KEY_CHECKS = 0;

DROP VIEW IF EXISTS rg_v_portada_territorio_poblacion;
DROP VIEW IF EXISTS rg_v_datos_consolidados;

DROP TABLE IF EXISTS rg_datos_area;
DROP TABLE IF EXISTS rg_datos_pais;
DROP TABLE IF EXISTS rg_periodos;
DROP TABLE IF EXISTS rg_fuentes;
DROP TABLE IF EXISTS rg_indicadores;
DROP TABLE IF EXISTS rg_bloques;
DROP TABLE IF EXISTS rg_paises;
DROP TABLE IF EXISTS rg_areas;

SET FOREIGN_KEY_CHECKS = 1;
