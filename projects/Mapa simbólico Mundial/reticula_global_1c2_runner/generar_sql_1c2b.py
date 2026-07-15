from __future__ import annotations

import json
import unicodedata
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import pandas as pd


@dataclass
class Ctx:
    root: Path
    out: Path
    sql_out: Path


def slugify(text: str) -> str:
    norm = unicodedata.normalize("NFKD", text)
    ascii_only = "".join(ch for ch in norm if not unicodedata.combining(ch))
    out = []
    for ch in ascii_only.lower():
        if ch.isalnum():
            out.append(ch)
        else:
            out.append("-")
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


def sql_quote(value: object) -> str:
    if value is None:
        return "NULL"
    if isinstance(value, float) and pd.isna(value):
        return "NULL"
    if pd.isna(value):
        return "NULL"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value).replace("'", "''")
    return f"'{text}'"


def load_inputs(ctx: Ctx) -> dict[str, object]:
    m_op = pd.read_csv(ctx.root / "rg_paises_areas_operativo.csv", dtype=str)
    e = pd.read_csv(ctx.out / "rg_territorio_poblacion_pais.csv", dtype=str)
    a = pd.read_csv(ctx.out / "rg_agregados_territorio_poblacion.csv", dtype=str)

    corr_path = ctx.out / "correspondencias-especiales-1c2.csv"
    corr = pd.read_csv(corr_path, dtype=str) if corr_path.exists() else pd.DataFrame()

    with (ctx.out / "fuentes_1c2.json").open("r", encoding="utf-8") as fh:
        fuentes = json.load(fh)

    return {
        "master": m_op,
        "entity": e,
        "agg": a,
        "corr": corr,
        "fuentes": fuentes,
    }


def build_catalogs(agg: pd.DataFrame) -> tuple[list[dict[str, object]], dict[str, int]]:
    areas = []
    area_id_by_code: dict[str, int] = {}
    for idx, row in enumerate(agg.sort_values("area_codigo").itertuples(index=False), start=1):
        codigo = str(row.area_codigo)
        nombre = str(row.area_nombre)
        area = {
            "id": idx,
            "codigo": codigo,
            "slug": slugify(codigo),
            "nombre": nombre,
            "nombre_corto": nombre,
            "color_principal": None,
            "orden_visual": idx,
            "activo": 1,
            "fecha_revision": str(date.today()),
        }
        areas.append(area)
        area_id_by_code[codigo] = idx

    return areas, area_id_by_code


def write_01_structure(ctx: Ctx) -> None:
    sql = f"""-- 01_rg_estructura_minima.sql
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
"""
    (ctx.sql_out / "01_rg_estructura_minima.sql").write_text(sql, encoding="utf-8")


def write_02_catalogs(ctx: Ctx, areas: list[dict[str, object]], fuentes_meta: dict[str, str]) -> dict[str, dict[str, int]]:
    bloques = [
        {"id": 1, "codigo": "TERR", "nombre": "Territorio", "activo": 1},
        {"id": 2, "codigo": "POB", "nombre": "Poblacion", "activo": 1},
    ]
    indicadores = [
        {"id": 1, "codigo": "TERR_SUP", "bloque_id": 1, "nombre": "Superficie", "unidad": "km2", "descripcion": "Superficie terrestre"},
        {"id": 2, "codigo": "TERR_PCT", "bloque_id": 1, "nombre": "Superficie mundial %", "unidad": "%", "descripcion": "Porcentaje de superficie mundial"},
        {"id": 3, "codigo": "TERR_DENS", "bloque_id": 1, "nombre": "Densidad", "unidad": "hab_km2", "descripcion": "Poblacion por km2"},
        {"id": 4, "codigo": "POB_TOTAL", "bloque_id": 2, "nombre": "Poblacion total", "unidad": "personas", "descripcion": "Poblacion estimada"},
        {"id": 5, "codigo": "POB_PCT", "bloque_id": 2, "nombre": "Poblacion mundial %", "unidad": "%", "descripcion": "Porcentaje de poblacion mundial"},
        {"id": 6, "codigo": "POB_EDAD", "bloque_id": 2, "nombre": "Edad mediana", "unidad": "anios", "descripcion": "Edad mediana aproximada"},
        {"id": 7, "codigo": "POB_2050", "bloque_id": 2, "nombre": "Poblacion 2050", "unidad": "personas", "descripcion": "Poblacion proyectada 2050"},
        {"id": 8, "codigo": "POB_VAR_2050", "bloque_id": 2, "nombre": "Variacion 2025-2050", "unidad": "%", "descripcion": "Variacion porcentual 2025-2050"},
    ]
    fuentes = [
        {
            "id": 1,
            "codigo": "UN_WPP_2024",
            "nombre": "ONU World Population Prospects 2024",
            "tipo_fuente": "oficial",
            "url": fuentes_meta.get("population_url"),
            "activo": 1,
        },
        {
            "id": 2,
            "codigo": "FAOSTAT_2025",
            "nombre": "FAOSTAT",
            "tipo_fuente": "oficial",
            "url": fuentes_meta.get("land_url"),
            "activo": 1,
        },
        {
            "id": 3,
            "codigo": "OWID",
            "nombre": "Our World in Data",
            "tipo_fuente": "procesador",
            "url": "https://ourworldindata.org",
            "activo": 1,
        },
    ]
    periodos = [
        {
            "id": 1,
            "codigo": "RG2025_V1",
            "nombre": "Reticula Global 2025 - Primera edicion",
            "estado": "preparacion",
            "activo": 1,
        }
    ]

    lines = [
        "-- 02_rg_catalogos_iniciales.sql",
        "SET NAMES utf8mb4;",
        "",
        "DELETE FROM rg_datos_area;",
        "DELETE FROM rg_datos_pais;",
        "DELETE FROM rg_paises;",
        "DELETE FROM rg_periodos;",
        "DELETE FROM rg_fuentes;",
        "DELETE FROM rg_indicadores;",
        "DELETE FROM rg_bloques;",
        "DELETE FROM rg_areas;",
        "",
    ]

    lines.append("INSERT INTO rg_areas (id,codigo,slug,nombre,nombre_corto,color_principal,orden_visual,activo,fecha_revision) VALUES")
    vals = []
    for r in areas:
        vals.append(
            "(" + ",".join(
                [
                    sql_quote(r["id"]),
                    sql_quote(r["codigo"]),
                    sql_quote(r["slug"]),
                    sql_quote(r["nombre"]),
                    sql_quote(r["nombre_corto"]),
                    sql_quote(r["color_principal"]),
                    sql_quote(r["orden_visual"]),
                    sql_quote(r["activo"]),
                    sql_quote(r["fecha_revision"]),
                ]
            ) + ")"
        )
    lines.append(",\n".join(vals) + ";\n")

    lines.append("INSERT INTO rg_bloques (id,codigo,nombre,activo) VALUES")
    lines.append(",\n".join([f"({b['id']},{sql_quote(b['codigo'])},{sql_quote(b['nombre'])},{b['activo']})" for b in bloques]) + ";\n")

    lines.append("INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo) VALUES")
    lines.append(",\n".join([
        f"({i['id']},{sql_quote(i['codigo'])},{i['bloque_id']},{sql_quote(i['nombre'])},{sql_quote(i['unidad'])},{sql_quote(i['descripcion'])},1)"
        for i in indicadores
    ]) + ";\n")

    lines.append("INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo) VALUES")
    lines.append(",\n".join([
        f"({f['id']},{sql_quote(f['codigo'])},{sql_quote(f['nombre'])},{sql_quote(f['tipo_fuente'])},{sql_quote(f['url'])},1)"
        for f in fuentes
    ]) + ";\n")

    lines.append("INSERT INTO rg_periodos (id,codigo,nombre,estado,activo) VALUES")
    lines.append(",\n".join([
        f"({p['id']},{sql_quote(p['codigo'])},{sql_quote(p['nombre'])},{sql_quote(p['estado'])},1)"
        for p in periodos
    ]) + ";\n")

    (ctx.sql_out / "02_rg_catalogos_iniciales.sql").write_text("\n".join(lines), encoding="utf-8")

    return {
        "bloques": {b["codigo"]: b["id"] for b in bloques},
        "indicadores": {i["codigo"]: i["id"] for i in indicadores},
        "fuentes": {f["codigo"]: f["id"] for f in fuentes},
        "periodos": {p["codigo"]: p["id"] for p in periodos},
    }


def write_03_paises(
    ctx: Ctx,
    master: pd.DataFrame,
    corr: pd.DataFrame,
    area_id_by_code: dict[str, int],
) -> dict[str, int]:
    corr_map: dict[str, dict[str, str]] = {}
    if not corr.empty:
        for r in corr.to_dict(orient="records"):
            corr_map[str(r["ISO maestro"])] = r

    rows = []
    pais_id_by_iso3: dict[str, int] = {}
    for idx, r in enumerate(master.itertuples(index=False), start=1):
        iso3 = str(r.codigo_iso3)
        area_id = area_id_by_code[str(r.area_codigo)]

        nota = r.motivo_excepcion if pd.notna(r.motivo_excepcion) and str(r.motivo_excepcion).strip() else r.observaciones
        base_trat = r.tratamiento_fuente if pd.notna(r.tratamiento_fuente) else None
        if iso3 in corr_map:
            c = corr_map[iso3]
            extra = f"1C.2A={c.get('Tratamiento','')}; nota={c.get('Nota','')}"
            if base_trat:
                base_trat = f"{base_trat} | {extra}"
            else:
                base_trat = extra

        rows.append(
            {
                "id": idx,
                "codigo_m49": r.codigo_m49,
                "codigo_iso2": r.codigo_iso2,
                "codigo_iso3": iso3,
                "nombre": r.nombre_es,
                "nombre_m49": r.nombre_m49,
                "region_m49": r.region_m49,
                "subregion_m49": r.subregion_m49,
                "area_id": area_id,
                "tipo_entidad": r.tipo_entidad,
                "es_excepcion": 1 if str(r.es_excepcion_m49).upper() == "SI" else 0,
                "nota_asignacion": nota,
                "incluir_mapa": r.incluir_mapa if pd.notna(r.incluir_mapa) else "SI",
                "incluir_calculos": r.incluir_calculos if pd.notna(r.incluir_calculos) else "SI",
                "tratamiento_fuente": base_trat,
                "activo": 1,
            }
        )
        pais_id_by_iso3[iso3] = idx

    lines = [
        "-- 03_rg_paises.sql",
        "SET NAMES utf8mb4;",
        "",
        "INSERT INTO rg_paises (id,codigo_m49,codigo_iso2,codigo_iso3,nombre,nombre_m49,region_m49,subregion_m49,area_id,tipo_entidad,es_excepcion,nota_asignacion,incluir_mapa,incluir_calculos,tratamiento_fuente,activo) VALUES",
    ]
    vals = []
    for r in rows:
        vals.append(
            "(" + ",".join(
                [
                    sql_quote(r["id"]),
                    sql_quote(r["codigo_m49"]),
                    sql_quote(r["codigo_iso2"]),
                    sql_quote(r["codigo_iso3"]),
                    sql_quote(r["nombre"]),
                    sql_quote(r["nombre_m49"]),
                    sql_quote(r["region_m49"]),
                    sql_quote(r["subregion_m49"]),
                    sql_quote(r["area_id"]),
                    sql_quote(r["tipo_entidad"]),
                    sql_quote(r["es_excepcion"]),
                    sql_quote(r["nota_asignacion"]),
                    sql_quote(r["incluir_mapa"]),
                    sql_quote(r["incluir_calculos"]),
                    sql_quote(r["tratamiento_fuente"]),
                    sql_quote(r["activo"]),
                ]
            ) + ")"
        )
    lines.append(",\n".join(vals) + ";")
    (ctx.sql_out / "03_rg_paises.sql").write_text("\n".join(lines), encoding="utf-8")
    return pais_id_by_iso3


def write_04_datos(
    ctx: Ctx,
    entity: pd.DataFrame,
    agg: pd.DataFrame,
    ids: dict[str, dict[str, int]],
    area_id_by_code: dict[str, int],
    pais_id_by_iso3: dict[str, int],
) -> dict[str, int]:
    ind = ids["indicadores"]
    src = ids["fuentes"]
    periodo_id = ids["periodos"]["RG2025_V1"]

    def fnum(v: object) -> float | None:
        if v is None or pd.isna(v):
            return None
        s = str(v).strip()
        if not s:
            return None
        return float(s)

    pais_rows: list[dict[str, object]] = []
    pid = 1
    today = str(date.today())

    edad_cobertura_por_area: dict[str, int] = (
        entity.assign(_edad_ok=entity["edad_mediana_2025"].notna())
        .groupby("area_codigo")["_edad_ok"]
        .sum()
        .astype(int)
        .to_dict()
    )

    for r in entity.to_dict(orient="records"):
        iso3 = str(r["codigo_iso3"])
        if iso3 not in pais_id_by_iso3:
            continue
        pais_id = pais_id_by_iso3[iso3]
        estado_src = str(r.get("estado_revision") or "OK")
        estado_dato = "LIMITACION_ACEPTADA" if estado_src == "LIMITACION_DOCUMENTADA" else "OK"
        obs = r.get("observaciones_datos")

        p25 = fnum(r.get("poblacion_2025"))
        p50 = fnum(r.get("poblacion_2050"))
        edad = fnum(r.get("edad_mediana_2025"))
        sup = fnum(r.get("superficie_km2"))
        anio_sup = int(float(r.get("anio_superficie"))) if fnum(r.get("anio_superficie")) is not None else None

        if sup is not None:
            pais_rows.append(
                {
                    "id": pid,
                    "pais_id": pais_id,
                    "indicador_id": ind["TERR_SUP"],
                    "anio": anio_sup,
                    "valor": sup,
                    "fuente_id": src["FAOSTAT_2025"],
                    "tipo_procedencia": "FUENTE_VALIDADA",
                    "estado_dato": estado_dato,
                    "fecha_carga": today,
                    "observaciones": obs,
                    "activo": 1,
                }
            )
            pid += 1

        if p25 is not None:
            pais_rows.append(
                {
                    "id": pid,
                    "pais_id": pais_id,
                    "indicador_id": ind["POB_TOTAL"],
                    "anio": 2025,
                    "valor": p25,
                    "fuente_id": src["UN_WPP_2024"],
                    "tipo_procedencia": "FUENTE_VALIDADA",
                    "estado_dato": estado_dato,
                    "fecha_carga": today,
                    "observaciones": obs,
                    "activo": 1,
                }
            )
            pid += 1

        if p50 is not None:
            pais_rows.append(
                {
                    "id": pid,
                    "pais_id": pais_id,
                    "indicador_id": ind["POB_2050"],
                    "anio": 2050,
                    "valor": p50,
                    "fuente_id": src["UN_WPP_2024"],
                    "tipo_procedencia": "FUENTE_VALIDADA",
                    "estado_dato": estado_dato,
                    "fecha_carga": today,
                    "observaciones": obs,
                    "activo": 1,
                }
            )
            pid += 1

        if edad is not None:
            pais_rows.append(
                {
                    "id": pid,
                    "pais_id": pais_id,
                    "indicador_id": ind["POB_EDAD"],
                    "anio": 2025,
                    "valor": edad,
                    "fuente_id": src["OWID"],
                    "tipo_procedencia": "FUENTE_VALIDADA",
                    "estado_dato": estado_dato,
                    "fecha_carga": today,
                    "observaciones": obs,
                    "activo": 1,
                }
            )
            pid += 1

        if p25 is not None and sup is not None and sup > 0:
            pais_rows.append(
                {
                    "id": pid,
                    "pais_id": pais_id,
                    "indicador_id": ind["TERR_DENS"],
                    "anio": 2025,
                    "valor": p25 / sup,
                    "fuente_id": src["OWID"],
                    "tipo_procedencia": "CALCULADO_1C2B",
                    "estado_dato": estado_dato,
                    "fecha_carga": today,
                    "observaciones": "Densidad calculada = poblacion_2025 / superficie_km2",
                    "activo": 1,
                }
            )
            pid += 1

        if p25 is not None and p50 is not None and p25 > 0:
            pais_rows.append(
                {
                    "id": pid,
                    "pais_id": pais_id,
                    "indicador_id": ind["POB_VAR_2050"],
                    "anio": 2050,
                    "valor": ((p50 / p25) - 1.0) * 100.0,
                    "fuente_id": src["OWID"],
                    "tipo_procedencia": "CALCULADO_1C2B",
                    "estado_dato": estado_dato,
                    "fecha_carga": today,
                    "observaciones": "Variacion porcentual 2025-2050",
                    "activo": 1,
                }
            )
            pid += 1

    area_rows: list[dict[str, object]] = []
    aid = 1
    for r in agg.to_dict(orient="records"):
        code = str(r["area_codigo"])
        area_id = area_id_by_code[code]
        total = int(float(r["entidades_totales"]))
        con_pob = int(float(r["entidades_con_poblacion"]))
        con_sup = int(float(r["entidades_con_superficie"]))
        con_dens = min(con_pob, con_sup)

        def add_area(
            ind_code: str,
            anio: int,
            valor: object,
            metodo: str,
            con_dato: int,
            anio_min: int,
            anio_max: int,
            fuente_id: int,
            keep_when_null: bool = False,
        ) -> None:
            nonlocal aid
            valor_num = fnum(valor)
            if valor_num is None and not keep_when_null:
                return
            cov = (con_dato / total * 100.0) if total > 0 else None
            estado = "OK" if cov is not None and cov >= 90 and valor_num is not None else "LIMITACION"
            area_rows.append(
                {
                    "id": aid,
                    "area_id": area_id,
                    "indicador_id": ind[ind_code],
                    "periodo_id": periodo_id,
                    "anio_referencia": anio,
                    "valor": valor_num,
                    "metodo_calculo": metodo,
                    "paises_totales": total,
                    "paises_con_dato": con_dato,
                    "porcentaje_cobertura": cov,
                    "anio_minimo": anio_min,
                    "anio_maximo": anio_max,
                    "fuente_principal_id": fuente_id,
                    "tipo_procedencia": "AGREGADO_1C2A",
                    "estado_dato": estado,
                    "fecha_calculo": today,
                    "observaciones": "Con limitaciones documentadas en 1C.2A" if cov is not None and cov < 100 else None,
                    "activo": 1,
                }
            )
            aid += 1

        add_area("TERR_SUP", 2023, r.get("superficie_km2"), "Suma superficies validadas", con_sup, 2023, 2023, src["FAOSTAT_2025"])
        add_area("TERR_PCT", 2023, r.get("superficie_mundial_pct"), "Participacion sobre superficie mundial", con_sup, 2023, 2023, src["FAOSTAT_2025"])
        add_area("POB_TOTAL", 2025, r.get("poblacion_2025"), "Suma poblacion 2025", con_pob, 2025, 2025, src["UN_WPP_2024"])
        add_area("POB_PCT", 2025, r.get("poblacion_mundial_pct"), "Participacion sobre poblacion mundial", con_pob, 2025, 2025, src["UN_WPP_2024"])
        add_area("TERR_DENS", 2025, r.get("densidad_2025"), "Poblacion area / superficie area", con_dens, 2025, 2025, src["OWID"])
        con_edad = int(edad_cobertura_por_area.get(code, 0))
        add_area(
            "POB_EDAD",
            2025,
            r.get("edad_mediana_2025_aprox"),
            "Media ponderada de medianas",
            con_edad,
            2025,
            2025,
            src["OWID"],
            keep_when_null=True,
        )
        add_area("POB_2050", 2050, r.get("poblacion_2050"), "Suma poblacion 2050", con_pob, 2050, 2050, src["UN_WPP_2024"])
        add_area("POB_VAR_2050", 2050, r.get("variacion_2025_2050_pct"), "Variacion porcentual 2025-2050", con_pob, 2025, 2050, src["OWID"])

    lines = ["-- 04_rg_datos_territorio_poblacion.sql", "SET NAMES utf8mb4;", ""]

    lines.append("INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo) VALUES")
    vals = []
    for r in pais_rows:
        vals.append(
            "(" + ",".join([
                sql_quote(r["id"]),
                sql_quote(r["pais_id"]),
                sql_quote(r["indicador_id"]),
                sql_quote(r["anio"]),
                sql_quote(round(float(r["valor"]), 6) if r["valor"] is not None else None),
                sql_quote(r["fuente_id"]),
                sql_quote(r["tipo_procedencia"]),
                sql_quote(r["estado_dato"]),
                sql_quote(r["fecha_carga"]),
                sql_quote(r["observaciones"]),
                sql_quote(r["activo"]),
            ]) + ")"
        )
    lines.append(",\n".join(vals) + ";\n")

    lines.append("INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo) VALUES")
    avals = []
    for r in area_rows:
        avals.append(
            "(" + ",".join([
                sql_quote(r["id"]),
                sql_quote(r["area_id"]),
                sql_quote(r["indicador_id"]),
                sql_quote(r["periodo_id"]),
                sql_quote(r["anio_referencia"]),
                sql_quote(round(float(r["valor"]), 6) if r["valor"] is not None else None),
                sql_quote(r["metodo_calculo"]),
                sql_quote(r["paises_totales"]),
                sql_quote(r["paises_con_dato"]),
                sql_quote(round(float(r["porcentaje_cobertura"]), 4) if r["porcentaje_cobertura"] is not None else None),
                sql_quote(r["anio_minimo"]),
                sql_quote(r["anio_maximo"]),
                sql_quote(r["fuente_principal_id"]),
                sql_quote(r["tipo_procedencia"]),
                sql_quote(r["estado_dato"]),
                sql_quote(r["fecha_calculo"]),
                sql_quote(r["observaciones"]),
                sql_quote(r["activo"]),
            ]) + ")"
        )
    lines.append(",\n".join(avals) + ";\n")

    (ctx.sql_out / "04_rg_datos_territorio_poblacion.sql").write_text("\n".join(lines), encoding="utf-8")

    return {
        "rg_datos_pais": len(pais_rows),
        "rg_datos_area": len(area_rows),
    }


def write_05_checks(ctx: Ctx) -> None:
    sql = """-- 05_rg_comprobaciones.sql
SET NAMES utf8mb4;

-- Nueve areas
SELECT COUNT(*) AS total_areas FROM rg_areas WHERE activo = 1;

-- Numero de paises y territorios
SELECT COUNT(*) AS total_paises FROM rg_paises WHERE activo = 1;

-- Numero de indicadores y fuentes
SELECT COUNT(*) AS total_indicadores FROM rg_indicadores WHERE activo = 1;
SELECT COUNT(*) AS total_fuentes FROM rg_fuentes WHERE activo = 1;

-- Datos por indicador (pais)
SELECT i.codigo, COUNT(*) AS registros
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id = dp.indicador_id
WHERE dp.activo = 1
GROUP BY i.codigo
ORDER BY i.codigo;

-- Agregados por area
SELECT a.codigo AS area, i.codigo AS indicador, da.valor
FROM rg_datos_area da
JOIN rg_areas a ON a.id = da.area_id
JOIN rg_indicadores i ON i.id = da.indicador_id
WHERE da.activo = 1
ORDER BY a.codigo, i.codigo;

-- Registros ausentes en fuente de entidad
SELECT
  COUNT(*) AS paises_sin_poblacion_2025
FROM rg_paises p
LEFT JOIN rg_datos_pais dp ON dp.pais_id = p.id
  AND dp.indicador_id = (SELECT id FROM rg_indicadores WHERE codigo='POB_TOTAL')
WHERE p.activo = 1 AND dp.id IS NULL;

SELECT
  COUNT(*) AS paises_sin_superficie
FROM rg_paises p
LEFT JOIN rg_datos_pais dp ON dp.pais_id = p.id
  AND dp.indicador_id = (SELECT id FROM rg_indicadores WHERE codigo='TERR_SUP')
WHERE p.activo = 1 AND dp.id IS NULL;

-- Duplicidades ISO3
SELECT codigo_iso3, COUNT(*) AS repeticiones
FROM rg_paises
GROUP BY codigo_iso3
HAVING COUNT(*) > 1;

-- Porcentajes mundiales por area
SELECT
  SUM(CASE WHEN i.codigo='POB_PCT' THEN da.valor ELSE 0 END) AS suma_pob_pct,
  SUM(CASE WHEN i.codigo='TERR_PCT' THEN da.valor ELSE 0 END) AS suma_terr_pct
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id = da.indicador_id
WHERE da.activo = 1;

-- Poblacion total mundial 2025 y 2050
SELECT
  SUM(CASE WHEN i.codigo='POB_TOTAL' THEN da.valor ELSE 0 END) AS poblacion_2025,
  SUM(CASE WHEN i.codigo='POB_2050' THEN da.valor ELSE 0 END) AS poblacion_2050
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id = da.indicador_id
WHERE da.activo = 1;
"""
    (ctx.sql_out / "05_rg_comprobaciones.sql").write_text(sql, encoding="utf-8")


def write_99_revert(ctx: Ctx) -> None:
    sql = """-- 99_rg_reversion_prueba.sql
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
"""
    (ctx.sql_out / "99_rg_reversion_prueba.sql").write_text(sql, encoding="utf-8")


def write_implant_doc(ctx: Ctx, counts: dict[str, int], input_files: list[str]) -> None:
    content = f"""# Implantacion MySQL minima - Reticula Global 1C.2B

## Alcance

Prueba tecnica minima para territorio y poblacion (sin datos economicos y sin tocar la web publica).

## Tablas creadas

- `rg_areas`
- `rg_paises`
- `rg_bloques`
- `rg_indicadores`
- `rg_fuentes`
- `rg_periodos`
- `rg_datos_pais`
- `rg_datos_area`

## Vistas creadas

- `rg_v_datos_consolidados`
- `rg_v_portada_territorio_poblacion`

## Relaciones principales

- `rg_paises.area_id` -> `rg_areas.id`
- `rg_indicadores.bloque_id` -> `rg_bloques.id`
- `rg_datos_pais.pais_id` -> `rg_paises.id`
- `rg_datos_pais.indicador_id` -> `rg_indicadores.id`
- `rg_datos_pais.fuente_id` -> `rg_fuentes.id`
- `rg_datos_area.area_id` -> `rg_areas.id`
- `rg_datos_area.indicador_id` -> `rg_indicadores.id`
- `rg_datos_area.periodo_id` -> `rg_periodos.id`
- `rg_datos_area.fuente_principal_id` -> `rg_fuentes.id`

## Archivos de entrada usados

{chr(10).join([f"- `{f}`" for f in input_files])}

## Transformacion aplicada

- Carga de catalogos minimos (areas, bloques, indicadores, fuentes, periodo).
- Carga de paises y territorios desde maestro operativo final.
- Carga de datos de entidad desde `rg_territorio_poblacion_pais.csv`.
- Carga de agregados por area desde `rg_agregados_territorio_poblacion.csv`.
- Conservacion de ausencias como `NULL`.
- Indicadores calculados: `TERR_DENS` y `POB_VAR_2050` cuando existen insumos.

## Numero de registros previstos

- `rg_areas`: **{counts['rg_areas']}**
- `rg_paises`: **{counts['rg_paises']}**
- `rg_bloques`: **{counts['rg_bloques']}**
- `rg_indicadores`: **{counts['rg_indicadores']}**
- `rg_fuentes`: **{counts['rg_fuentes']}**
- `rg_periodos`: **{counts['rg_periodos']}**
- `rg_datos_pais`: **{counts['rg_datos_pais']}**
- `rg_datos_area`: **{counts['rg_datos_area']}**

## Ausencias conservadas

- No se convierten faltantes a cero.
- Las limitaciones 1C.2A se preservan como `NULL` y notas en observaciones.

## Orden de ejecucion en phpMyAdmin

1. `01_rg_estructura_minima.sql`
2. `02_rg_catalogos_iniciales.sql`
3. `03_rg_paises.sql`
4. `04_rg_datos_territorio_poblacion.sql`
5. `05_rg_comprobaciones.sql`

## Reversion

- Ejecutar `99_rg_reversion_prueba.sql` para eliminar solo vistas/tablas `rg_` de esta prueba.

## Riesgos

- Si existen tablas `rg_` previas no compatibles, revisar antes de ejecutar.
- `rg_datos_pais` no carga indicadores de porcentaje por entidad (no estan en fuentes base).
- Cualquier ajuste semantico adicional debe hacerse en una fase posterior, no en esta prueba minima.

## Decision tecnica para ejecucion manual en phpMyAdmin

**GO** para entorno de prueba, con ejecucion manual y validacion con `05_rg_comprobaciones.sql`.
"""
    (ctx.sql_out / "implantacion-mysql-minima-reticula-global-1c2b.md").write_text(content, encoding="utf-8")


def main() -> int:
    root = Path(__file__).resolve().parent
    out = root / "output_1c2"
    ctx = Ctx(root=root, out=out, sql_out=out)

    data = load_inputs(ctx)
    master = data["master"]
    entity = data["entity"]
    agg = data["agg"]
    corr = data["corr"]
    fuentes = data["fuentes"]

    areas, area_id_by_code = build_catalogs(agg)
    write_01_structure(ctx)
    ids = write_02_catalogs(ctx, areas, fuentes)
    pais_id_by_iso3 = write_03_paises(ctx, master, corr, area_id_by_code)
    fact_counts = write_04_datos(ctx, entity, agg, ids, area_id_by_code, pais_id_by_iso3)
    write_05_checks(ctx)
    write_99_revert(ctx)

    counts = {
        "rg_areas": len(areas),
        "rg_paises": len(master),
        "rg_bloques": 2,
        "rg_indicadores": 8,
        "rg_fuentes": 3,
        "rg_periodos": 1,
        **fact_counts,
    }

    input_files = [
        str((root / "rg_paises_areas.csv").relative_to(root)),
        str((root / "rg_paises_areas_operativo.csv").relative_to(root)),
        str((out / "rg_territorio_poblacion_pais.csv").relative_to(root)),
        str((out / "rg_agregados_territorio_poblacion.csv").relative_to(root)),
        str((out / "fuentes_1c2.json").relative_to(root)),
        str((out / "validacion-territorio-poblacion-1c2.md").relative_to(root)),
        str((out / "resolucion-incidencias-territorio-poblacion-1c2a.md").relative_to(root)),
    ]
    if (out / "correspondencias-especiales-1c2.csv").exists():
        input_files.append(str((out / "correspondencias-especiales-1c2.csv").relative_to(root)))

    write_implant_doc(ctx, counts, input_files)

    print(json.dumps(counts, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
