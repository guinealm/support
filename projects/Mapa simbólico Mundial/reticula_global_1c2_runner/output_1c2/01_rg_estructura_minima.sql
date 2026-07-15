-- 01_rg_estructura_minima.sql
-- Fase 1C.2B - estructura minima de prueba para Reticula Global

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE IF NOT EXISTS rg_areas (
  id INT UNSIGNED NOT NULL,
  codigo VARCHAR(10) NOT NULL,
  slug VARCHAR(64) NOT NULL,
  nombre VARCHAR(120) NOT NULL,
  nombre_corto VARCHAR(80) NOT NULL,
  color_principal VARCHAR(16) NULL,
  orden_visual SMALLINT UNSIGNED NOT NULL,
  activo TINYINT(1) NOT NULL DEFAULT 1,
  fecha_revision DATE NULL,
  PRIMARY KEY (id),
  UNIQUE KEY uq_rg_areas_codigo (codigo),
  UNIQUE KEY uq_rg_areas_slug (slug),
  KEY idx_rg_areas_activo (activo)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS rg_paises (
  id INT UNSIGNED NOT NULL,
  codigo_m49 VARCHAR(3) NULL,
  codigo_iso2 VARCHAR(2) NULL,
  codigo_iso3 VARCHAR(3) NOT NULL,
  nombre VARCHAR(160) NOT NULL,
  nombre_m49 VARCHAR(160) NULL,
  region_m49 VARCHAR(120) NULL,
  subregion_m49 VARCHAR(120) NULL,
  area_id INT UNSIGNED NOT NULL,
  tipo_entidad VARCHAR(40) NOT NULL,
  es_excepcion TINYINT(1) NOT NULL DEFAULT 0,
  nota_asignacion TEXT NULL,
  incluir_mapa ENUM('SI','NO') NOT NULL DEFAULT 'SI',
  incluir_calculos ENUM('SI','NO','SEGUN_FUENTE') NOT NULL DEFAULT 'SI',
  tratamiento_fuente TEXT NULL,
  activo TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (id),
  UNIQUE KEY uq_rg_paises_iso3 (codigo_iso3),
  UNIQUE KEY uq_rg_paises_m49 (codigo_m49),
  KEY idx_rg_paises_area (area_id),
  KEY idx_rg_paises_tipo (tipo_entidad),
  KEY idx_rg_paises_activo (activo),
  CONSTRAINT fk_rg_paises_area FOREIGN KEY (area_id) REFERENCES rg_areas(id)
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS rg_bloques (
  id INT UNSIGNED NOT NULL,
  codigo VARCHAR(20) NOT NULL,
  nombre VARCHAR(80) NOT NULL,
  activo TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (id),
  UNIQUE KEY uq_rg_bloques_codigo (codigo)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS rg_indicadores (
  id INT UNSIGNED NOT NULL,
  codigo VARCHAR(30) NOT NULL,
  bloque_id INT UNSIGNED NOT NULL,
  nombre VARCHAR(120) NOT NULL,
  unidad VARCHAR(30) NULL,
  descripcion VARCHAR(255) NULL,
  activo TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (id),
  UNIQUE KEY uq_rg_indicadores_codigo (codigo),
  KEY idx_rg_indicadores_bloque (bloque_id),
  CONSTRAINT fk_rg_indicadores_bloque FOREIGN KEY (bloque_id) REFERENCES rg_bloques(id)
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS rg_fuentes (
  id INT UNSIGNED NOT NULL,
  codigo VARCHAR(30) NOT NULL,
  nombre VARCHAR(180) NOT NULL,
  tipo_fuente VARCHAR(40) NOT NULL,
  url TEXT NULL,
  activo TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (id),
  UNIQUE KEY uq_rg_fuentes_codigo (codigo)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS rg_periodos (
  id INT UNSIGNED NOT NULL,
  codigo VARCHAR(30) NOT NULL,
  nombre VARCHAR(180) NOT NULL,
  estado VARCHAR(30) NOT NULL,
  activo TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (id),
  UNIQUE KEY uq_rg_periodos_codigo (codigo)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS rg_datos_pais (
  id BIGINT UNSIGNED NOT NULL,
  pais_id INT UNSIGNED NOT NULL,
  indicador_id INT UNSIGNED NOT NULL,
  anio SMALLINT NULL,
  valor DECIMAL(22,6) NULL,
  fuente_id INT UNSIGNED NULL,
  tipo_procedencia VARCHAR(40) NOT NULL,
  estado_dato VARCHAR(40) NOT NULL,
  fecha_carga DATE NOT NULL,
  observaciones TEXT NULL,
  activo TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (id),
  UNIQUE KEY uq_rg_datos_pais (pais_id, indicador_id, anio),
  KEY idx_rg_datos_pais_indicador (indicador_id),
  KEY idx_rg_datos_pais_anio (anio),
  KEY idx_rg_datos_pais_fuente (fuente_id),
  CONSTRAINT fk_rg_datos_pais_pais FOREIGN KEY (pais_id) REFERENCES rg_paises(id)
    ON UPDATE CASCADE,
  CONSTRAINT fk_rg_datos_pais_indicador FOREIGN KEY (indicador_id) REFERENCES rg_indicadores(id)
    ON UPDATE CASCADE,
  CONSTRAINT fk_rg_datos_pais_fuente FOREIGN KEY (fuente_id) REFERENCES rg_fuentes(id)
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS rg_datos_area (
  id BIGINT UNSIGNED NOT NULL,
  area_id INT UNSIGNED NOT NULL,
  indicador_id INT UNSIGNED NOT NULL,
  periodo_id INT UNSIGNED NOT NULL,
  anio_referencia SMALLINT NULL,
  valor DECIMAL(22,6) NULL,
  metodo_calculo VARCHAR(120) NOT NULL,
  paises_totales SMALLINT UNSIGNED NULL,
  paises_con_dato SMALLINT UNSIGNED NULL,
  porcentaje_cobertura DECIMAL(8,4) NULL,
  anio_minimo SMALLINT NULL,
  anio_maximo SMALLINT NULL,
  fuente_principal_id INT UNSIGNED NULL,
  tipo_procedencia VARCHAR(40) NOT NULL,
  estado_dato VARCHAR(40) NOT NULL,
  fecha_calculo DATE NOT NULL,
  observaciones TEXT NULL,
  activo TINYINT(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (id),
  UNIQUE KEY uq_rg_datos_area (area_id, indicador_id, periodo_id, anio_referencia),
  KEY idx_rg_datos_area_indicador (indicador_id),
  KEY idx_rg_datos_area_periodo (periodo_id),
  KEY idx_rg_datos_area_fuente (fuente_principal_id),
  CONSTRAINT fk_rg_datos_area_area FOREIGN KEY (area_id) REFERENCES rg_areas(id)
    ON UPDATE CASCADE,
  CONSTRAINT fk_rg_datos_area_indicador FOREIGN KEY (indicador_id) REFERENCES rg_indicadores(id)
    ON UPDATE CASCADE,
  CONSTRAINT fk_rg_datos_area_periodo FOREIGN KEY (periodo_id) REFERENCES rg_periodos(id)
    ON UPDATE CASCADE,
  CONSTRAINT fk_rg_datos_area_fuente FOREIGN KEY (fuente_principal_id) REFERENCES rg_fuentes(id)
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;

CREATE OR REPLACE VIEW rg_v_datos_consolidados AS
SELECT
  a.codigo AS codigo_area,
  a.nombre AS nombre_area,
  i.codigo AS codigo_indicador,
  i.nombre AS indicador,
  da.valor,
  i.unidad,
  da.anio_referencia AS anio,
  da.metodo_calculo AS metodo,
  da.porcentaje_cobertura AS cobertura,
  da.observaciones
FROM rg_datos_area da
JOIN rg_areas a ON a.id = da.area_id
JOIN rg_indicadores i ON i.id = da.indicador_id
WHERE da.activo = 1;

CREATE OR REPLACE VIEW rg_v_portada_territorio_poblacion AS
SELECT
  a.codigo AS codigo_area,
  a.nombre AS nombre_area,
  MAX(CASE WHEN i.codigo = 'POB_TOTAL' THEN da.valor END) AS poblacion_2025,
  MAX(CASE WHEN i.codigo = 'POB_PCT' THEN da.valor END) AS poblacion_pct_mundial,
  MAX(CASE WHEN i.codigo = 'TERR_SUP' THEN da.valor END) AS superficie_km2,
  MAX(CASE WHEN i.codigo = 'TERR_PCT' THEN da.valor END) AS superficie_pct_mundial,
  MAX(CASE WHEN i.codigo = 'TERR_DENS' THEN da.valor END) AS densidad,
  MAX(CASE WHEN i.codigo = 'POB_EDAD' THEN da.valor END) AS edad_mediana,
  MAX(CASE WHEN i.codigo = 'POB_2050' THEN da.valor END) AS poblacion_2050,
  MAX(CASE WHEN i.codigo = 'POB_VAR_2050' THEN da.valor END) AS variacion_2025_2050
FROM rg_areas a
LEFT JOIN rg_datos_area da ON da.area_id = a.id AND da.activo = 1
LEFT JOIN rg_indicadores i ON i.id = da.indicador_id
GROUP BY a.codigo, a.nombre;
