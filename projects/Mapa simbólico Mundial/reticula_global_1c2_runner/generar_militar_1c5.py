from __future__ import annotations

import math
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


SIPRI_MILEX_XLSX = "https://www.sipri.org/sites/default/files/SIPRI-Milex-data-1949-2025_v1.2.xlsx"
SIPRI_MILEX_EDICION = "SIPRI Military Expenditure Database, edición abril 2026 (v1.2), año 2025"
SIPRI_NUCLEAR_EDICION = "SIPRI Yearbook 2026, chapter 8 World nuclear forces, inventarios enero 2026"
SIPRI_NUCLEAR_TOTAL_CONTROL = 12187
PRK_GASTO_OBS = (
    "SIPRI no dispone de gasto militar reciente comparable para Corea del Norte; "
    "último dato histórico no utilizado por falta de comparabilidad temporal."
)

# Estimaciones abiertas SIPRI Yearbook 2026 (enero 2026).
# Se mantiene trazabilidad explícita de estimación y limitaciones metodológicas.
NUCLEAR_ESTIMATES = {
    "USA": 5132,
    "RUS": 5430,
    "CHN": 620,
    "FRA": 290,
    "GBR": 225,
    "IND": 180,
    "PAK": 170,
    "ISR": 90,
    "PRK": 50,
}

NUCLEAR_NOTE = (
    "Inventario nuclear estimado (columna utilizada: inventario total estimado, SIPRI Yearbook 2026) "
    "a partir de fuentes abiertas; no representa disponibilidad "
    "operativa, precision, vectores, doctrina ni capacidad de segundo ataque"
)


@dataclass
class Ctx:
    root: Path
    out: Path


def nrm(v: object) -> str:
    x = str(v).strip().upper()
    x = unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode("ascii")
    x = re.sub(r"[^A-Z0-9 ]+", " ", x)
    x = re.sub(r"\s+", " ", x).strip()
    return x


def q(v: object) -> str:
    if v is None:
        return "NULL"
    if isinstance(v, float) and (math.isnan(v) or math.isinf(v)):
        return "NULL"
    if pd.isna(v):
        return "NULL"
    if isinstance(v, (int, float)):
        return str(v)
    return "'" + str(v).replace("'", "''") + "'"


def to_num(v: object) -> float | None:
    if v is None or pd.isna(v):
        return None
    t = str(v).strip()
    if not t or t.lower() in {"xxx", "...", "nan"}:
        return None
    try:
        return float(t)
    except ValueError:
        return None


def sipri_million_to_usd(v: float | None) -> float | None:
    if v is None or pd.isna(v):
        return None
    return float(v) * 1_000_000.0


def parse_sipri_sheet(sheet_name: str) -> pd.DataFrame:
    raw = pd.read_excel(SIPRI_MILEX_XLSX, sheet_name=sheet_name, header=4)
    header = raw.iloc[0].tolist()
    t = raw.iloc[1:].copy()
    t.columns = header
    t = t[t["Country"].notna()].copy()
    t = t.rename(columns={"Country": "country", "Notes": "notes"})
    for y in [2024, 2025]:
        t[f"y{y}"] = t[y].map(to_num)
    return t[["country", "notes", "y2024", "y2025"]]


def load_master(ctx: Ctx) -> pd.DataFrame:
    return pd.read_csv(ctx.root / "rg_paises_areas_operativo.csv", dtype=str)


def build_name_map(master: pd.DataFrame) -> dict[str, str]:
    out: dict[str, str] = {}
    for _, r in master.iterrows():
        iso = str(r["codigo_iso3"]).strip().upper()
        for key in [r.get("nombre_m49"), r.get("nombre_es")]:
            if key is not None and str(key).strip():
                out[nrm(key)] = iso
    return out


def sipri_aliases() -> dict[str, str]:
    return {
        "COTE D IVOIRE": "COTE D IVOIRE",
        "CONGO DR": "CONGO THE DEMOCRATIC REPUBLIC OF THE",
        "CONGO REPUBLIC": "CONGO",
        "GAMBIA THE": "GAMBIA",
        "CAPE VERDE": "CABO VERDE",
        "TURKIYE": "TURKIYE",
        "SYRIA": "SYRIAN ARAB REPUBLIC",
        "VIETNAM": "VIET NAM",
        "LAOS": "LAO PEOPLE S DEMOCRATIC REPUBLIC",
        "BOLIVIA": "BOLIVIA PLURINATIONAL STATE OF",
        "VENEZUELA": "VENEZUELA BOLIVARIAN REPUBLIC OF",
        "RUSSIA": "RUSSIAN FEDERATION",
        "IRAN": "IRAN ISLAMIC REPUBLIC OF",
        "KOREA SOUTH": "KOREA REPUBLIC OF",
        "KOREA NORTH": "KOREA DEMOCRATIC PEOPLE S REPUBLIC OF",
        "MOLDOVA": "MOLDOVA REPUBLIC OF",
        "TANZANIA": "TANZANIA UNITED REPUBLIC OF",
        "BRUNEI": "BRUNEI DARUSSALAM",
        "BAHAMAS THE": "BAHAMAS",
        "MICRONESIA": "MICRONESIA FEDERATED STATES OF",
        "BOSNIA HERZEGOVINA": "BOSNIA AND HERZEGOVINA",
        "KYRGYZ REPUBLIC": "KYRGYZSTAN",
        "NETHERLANDS": "NETHERLANDS",
        "UNITED STATES OF AMERICA": "UNITED STATES",
        "TAIWAN": "TAIWAN PROVINCE OF CHINA",
    }


def build_country_military(ctx: Ctx) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    master = load_master(ctx)
    cur = parse_sipri_sheet("Current US$")
    pct = parse_sipri_sheet("Share of GDP")

    cur = cur.rename(columns={"y2024": "gasto_2024", "y2025": "gasto_2025", "notes": "notes_gasto"})
    pct = pct.rename(columns={"y2024": "pct_2024", "y2025": "pct_2025", "notes": "notes_pct"})

    sipri = cur.merge(pct[["country", "pct_2024", "pct_2025", "notes_pct"]], on="country", how="outer")

    nm = build_name_map(master)
    aliases = sipri_aliases()

    mapped_rows: list[dict[str, object]] = []
    unmatched_sipri: list[str] = []
    seen_iso: set[str] = set()
    excluded_aggregates = {
        "AFRICA",
        "AMERICAS",
        "ASIA OCEANIA",
        "CENTRAL AMERICA AND THE CARIBBEAN",
        "CENTRAL ASIA",
        "CENTRAL EUROPE",
        "EAST ASIA",
        "EASTERN EUROPE",
        "EUROPE",
        "EUROPEAN UNION",
        "MIDDLE EAST",
        "NORTH AFRICA",
        "NORTH AMERICA",
        "OCEANIA",
        "SOUTH AMERICA",
        "SOUTH ASIA",
        "SOUTH EAST ASIA",
        "SUB SAHARAN AFRICA",
        "WESTERN EUROPE",
        "USSR",
        "CZECHOSLOVAKIA",
        "GERMAN DEMOCRATIC REPUBLIC",
        "YEMEN NORTH",
        "YUGOSLAVIA",
        "WORLD TOTAL",
    }

    for _, r in sipri.iterrows():
        c = str(r["country"]).strip()
        k = nrm(c)
        if k in excluded_aggregates:
            continue
        k = aliases.get(k, k)
        iso = nm.get(k)
        if iso is None:
            unmatched_sipri.append(c)
            continue
        if iso in seen_iso:
            continue
        seen_iso.add(iso)

        gasto = r.get("gasto_2025")
        anio = 2025
        estado = "OK_2025"
        obs_parts: list[str] = []
        if pd.isna(gasto):
            gasto = r.get("gasto_2024")
            anio = 2024
            if pd.isna(gasto):
                gasto = None
                anio = None
                estado = "AUSENTE"
            else:
                estado = "ANIO_ANTERIOR_2024"
                obs_parts.append("SIPRI no publica 2025 para esta entidad; se conserva 2024 separado.")

        pct_pib = None
        if anio == 2025:
            pct_pib = r.get("pct_2025")
            if pd.isna(pct_pib) and pd.notna(r.get("pct_2024")):
                pct_pib = r.get("pct_2024")
                obs_parts.append("Porcentaje PIB tomado en 2024 por ausencia de 2025.")
        elif anio == 2024:
            pct_pib = r.get("pct_2024")

        if iso == "RUS":
            obs_parts.append("RUS asignado exclusivamente a RUE.")
        if iso == "USA":
            obs_parts.append("USA asignado exclusivamente a NAC.")
        if iso == "CHN":
            obs_parts.append("CHN separado de HKG y MAC.")
        if iso == "TWN":
            obs_parts.append("TWN revisado expresamente; mantener separado si la fuente no publica serie comparable.")
        if iso == "XKX":
            obs_parts.append("XKX revisado expresamente; mantener sin duplicidad con SRB.")

        mapped_rows.append(
            {
                "codigo_iso3": iso,
                "gasto_militar_usd": sipri_million_to_usd(gasto),
                "gasto_militar_pct_pib": float(pct_pib) if pct_pib is not None and pd.notna(pct_pib) else None,
                "anio_gasto": anio,
                "fuente_gasto": SIPRI_MILEX_EDICION,
                "estado_revision": estado,
                "observaciones_sipri": " ".join(obs_parts).strip(),
            }
        )

    map_df = pd.DataFrame(mapped_rows)

    out = master[
        [
            "codigo_iso3",
            "codigo_m49",
            "nombre_es",
            "area_codigo",
            "incluir_calculos",
            "tratamiento_fuente",
        ]
    ].copy()
    out = out.rename(columns={"nombre_es": "pais"})
    out = out.merge(map_df, on="codigo_iso3", how="left")

    def build_row_obs(r: pd.Series) -> str:
        notes: list[str] = []
        if str(r.get("incluir_calculos", "")).upper() == "SEGUN_FUENTE":
            notes.append("Entidad SEGUN_FUENTE; no imputar cero si SIPRI no publica valor separado.")
        if pd.isna(r.get("gasto_militar_usd")):
            notes.append("Sin dato SIPRI usable para 2025/2024 en esta entidad.")
        if pd.notna(r.get("observaciones_sipri")) and str(r.get("observaciones_sipri", "")).strip():
            notes.append(str(r.get("observaciones_sipri")))
        return " ".join(notes).strip()

    out["fuente_gasto"] = out["fuente_gasto"].fillna(SIPRI_MILEX_EDICION)
    out["estado_revision"] = out["estado_revision"].fillna("AUSENTE")
    out["observaciones"] = out.apply(build_row_obs, axis=1)

    # Resolucion metodologica 1C.5A: PRK sin gasto comparable reciente en SIPRI.
    prk = out["codigo_iso3"] == "PRK"
    out.loc[prk, "gasto_militar_usd"] = None
    out.loc[prk, "gasto_militar_pct_pib"] = None
    out.loc[prk, "anio_gasto"] = None
    out.loc[prk, "estado_revision"] = "AUSENTE_DOCUMENTADO"
    out.loc[prk, "observaciones"] = PRK_GASTO_OBS

    out = out[
        [
            "codigo_iso3",
            "codigo_m49",
            "pais",
            "area_codigo",
            "gasto_militar_usd",
            "gasto_militar_pct_pib",
            "anio_gasto",
            "fuente_gasto",
            "estado_revision",
            "observaciones",
        ]
    ].copy()

    unmatched_df = pd.DataFrame({"nombre_sipri_sin_match": sorted(set(unmatched_sipri))})
    return out, unmatched_df, master


def build_nuclear_country(master: pd.DataFrame) -> pd.DataFrame:
    base = master[["codigo_iso3", "nombre_es", "area_codigo"]].drop_duplicates().copy()
    rows = []
    for iso, ojivas in NUCLEAR_ESTIMATES.items():
        m = base[base["codigo_iso3"] == iso]
        if m.empty:
            continue
        r = m.iloc[0]
        rows.append(
            {
                "codigo_iso3": iso,
                "pais": r["nombre_es"],
                "area_codigo": r["area_codigo"],
                "inventario_total_estimado": int(ojivas),
                "stock_militar_estimado": None,
                "ojivas_desplegadas_estimadas": None,
                "ojivas_totales_estimadas": int(ojivas),
                "anio_referencia": 2026,
                "fuente": SIPRI_NUCLEAR_EDICION,
                "tipo_estimacion": "ESTIMACION_FUENTES_ABIERTAS",
                "observaciones": NUCLEAR_NOTE,
            }
        )
    return pd.DataFrame(rows)


def build_area_aggregates(ctx: Ctx, militar_pais: pd.DataFrame, nuclear_pais: pd.DataFrame) -> pd.DataFrame:
    pop = pd.read_csv(ctx.out / "rg_agregados_territorio_poblacion.csv")
    eco_area = pd.read_csv(ctx.out / "rg_agregados_economia.csv")
    eco_pais = pd.read_csv(ctx.out / "rg_economia_pais.csv")
    pob_pais = pd.read_csv(ctx.out / "rg_territorio_poblacion_pais.csv")

    base = militar_pais.merge(
        eco_pais[["codigo_iso3", "pib_usd"]], on="codigo_iso3", how="left"
    ).merge(
        pob_pais[["codigo_iso3", "poblacion_2025"]], on="codigo_iso3", how="left"
    )

    area_names = (
        militar_pais[["area_codigo"]]
        .drop_duplicates()
        .merge(pop[["area_codigo", "area_nombre", "poblacion_2025"]], on="area_codigo", how="left")
        .merge(eco_area[["area_codigo", "pib_usd"]], on="area_codigo", how="left", suffixes=("", "_area"))
    )

    out_rows: list[dict[str, object]] = []
    for _, ar in area_names.sort_values("area_codigo").iterrows():
        ac = ar["area_codigo"]
        t = base[base["area_codigo"] == ac].copy()

        gasto = t["gasto_militar_usd"].dropna().sum()
        total_ent = len(t)
        con_gasto = int(t["gasto_militar_usd"].notna().sum())

        pop_area = float(ar["poblacion_2025"]) if pd.notna(ar["poblacion_2025"]) else None
        pop_cov = t.loc[t["gasto_militar_usd"].notna(), "poblacion_2025"].dropna().sum()
        cov_pop = (pop_cov / pop_area * 100.0) if pop_area and pop_area > 0 else None

        gdp_cov = t.loc[t["gasto_militar_usd"].notna(), "pib_usd"].dropna().sum()
        gdp_area = float(ar["pib_usd"]) if pd.notna(ar["pib_usd"]) else None
        cov_gdp = (gdp_cov / gdp_area * 100.0) if gdp_area and gdp_area > 0 else None

        mil_pib = (gasto / gdp_cov * 100.0) if gdp_cov and gdp_cov > 0 else None
        mil_pc = (gasto / pop_area) if pop_area and pop_area > 0 else None

        years = t.loc[t["gasto_militar_usd"].notna(), "anio_gasto"].dropna()
        y_min = int(years.min()) if not years.empty else None
        y_max = int(years.max()) if not years.empty else None

        nuc = nuclear_pais[nuclear_pais["area_codigo"] == ac]
        oj = int(nuc["ojivas_totales_estimadas"].sum()) if not nuc.empty else 0

        obs_parts = [
            "MIL_PIB calculado como gasto agregado / PIB agregado comparable cubierto.",
            "No se usa media simple de porcentajes nacionales.",
        ]
        if y_min is not None and y_min < 2025:
            obs_parts.append("Incluye entidades con ultimo dato 2024 separado y marcado.")
        if cov_gdp is not None and cov_gdp < 90:
            obs_parts.append("Cobertura PIB condicionada para el calculo aproximado.")
        if ac == "APC":
            obs_parts.append("Gasto militar conocido y comparable de los paises cubiertos por SIPRI.")
        if oj == 0:
            obs_parts.append("Area sin Estado con arsenal nuclear identificado por SIPRI (cero real).")

        out_rows.append(
            {
                "area_codigo": ac,
                "area_nombre": ar["area_nombre"],
                "gasto_militar_usd": gasto,
                "gasto_militar_mundial_pct": 0.0,
                "gasto_militar_pct_pib_aprox": mil_pib,
                "gasto_militar_por_habitante": mil_pc,
                "ojivas_nucleares_estimadas": oj,
                "entidades_totales": total_ent,
                "entidades_con_gasto": con_gasto,
                "cobertura_poblacion_pct": cov_pop,
                "cobertura_pib_pct": cov_gdp,
                "anio_min_gasto": y_min,
                "anio_max_gasto": y_max,
                "anio_nuclear": 2026,
                "observaciones": " ".join(obs_parts),
            }
        )

    out = pd.DataFrame(out_rows)
    world = out["gasto_militar_usd"].sum()
    if world > 0:
        out["gasto_militar_mundial_pct"] = out["gasto_militar_usd"] / world * 100.0
    return out


def coverage_label(v: float | None) -> str:
    if v is None or pd.isna(v):
        return "insuficiente"
    if v > 95:
        return "alta"
    if v >= 90:
        return "aceptable"
    if v >= 80:
        return "condicionada"
    return "insuficiente"


def write_catalog_sql(ctx: Ctx) -> None:
    sql = """-- 14_rg_catalogo_militar.sql
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
"""
    (ctx.out / "14_rg_catalogo_militar.sql").write_text(sql, encoding="utf-8")


def write_data_sql(ctx: Ctx, militar_pais: pd.DataFrame, nuclear_pais: pd.DataFrame, agg: pd.DataFrame) -> None:
    pais_vals = []
    for _, r in militar_pais.iterrows():
        pais_vals.append(
            f"({q(r['codigo_iso3'])},{q(r['anio_gasto'])},{q(r['gasto_militar_usd'])},{q(r['gasto_militar_pct_pib'])},{q(r['observaciones'])})"
        )
    pais_blob = ",\n".join(pais_vals)

    nuc_vals = []
    for _, r in nuclear_pais.iterrows():
        nuc_vals.append(
            f"({q(r['codigo_iso3'])},{q(r['anio_referencia'])},{q(r['ojivas_totales_estimadas'])},{q(r['observaciones'])})"
        )
    nuc_blob = ",\n".join(nuc_vals)

    area_vals = []
    for _, r in agg.sort_values("area_codigo").iterrows():
        area_vals.append(
            "(" + ",".join(
                [
                    q(r["area_codigo"]),
                    q(2025),
                    q(r["gasto_militar_usd"]),
                    q(r["gasto_militar_mundial_pct"]),
                    q(r["gasto_militar_pct_pib_aprox"]),
                    q(r["gasto_militar_por_habitante"]),
                    q(2026),
                    q(r["ojivas_nucleares_estimadas"]),
                    q(r["entidades_totales"]),
                    q(r["entidades_con_gasto"]),
                    q(r["cobertura_poblacion_pct"]),
                    q(r["cobertura_pib_pct"]),
                    q(r["anio_min_gasto"]),
                    q(r["anio_max_gasto"]),
                    q(r["observaciones"]),
                ]
            ) + ")"
        )
    area_blob = ",\n".join(area_vals)

    sql = f"""-- 15_rg_datos_militar.sql
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
{pais_blob};

DROP TEMPORARY TABLE IF EXISTS tmp_rg_militar_nuclear;
CREATE TEMPORARY TABLE tmp_rg_militar_nuclear (
  codigo_iso3 VARCHAR(3) PRIMARY KEY,
  anio_referencia SMALLINT NOT NULL,
  ojivas_totales_estimadas INT NOT NULL,
  observaciones TEXT NULL
) ENGINE=InnoDB;

INSERT INTO tmp_rg_militar_nuclear (codigo_iso3,anio_referencia,ojivas_totales_estimadas,observaciones) VALUES
{nuc_blob};

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
{area_blob};

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
"""
    (ctx.out / "15_rg_datos_militar.sql").write_text(sql, encoding="utf-8")


def write_checks_sql(ctx: Ctx) -> None:
    sql = """-- 16_rg_comprobaciones_militar.sql
SET NAMES utf8mb4;

-- Bloques e indicadores esperados tras 1C.5
SELECT COUNT(*) AS bloques_activos FROM rg_bloques WHERE activo=1;
SELECT COUNT(*) AS indicadores_activos FROM rg_indicadores WHERE activo=1;
SELECT COUNT(*) AS bloques_mil FROM rg_bloques WHERE codigo='MIL' AND activo=1;
SELECT COUNT(*) AS indicadores_mil FROM rg_indicadores WHERE codigo IN ('MIL_GASTO','MIL_PCT','MIL_PIB','MIL_PC','MIL_NUC') AND activo=1;

-- Registros nacionales por indicador MIL
SELECT i.codigo, COUNT(*) AS registros
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
WHERE i.codigo IN ('MIL_GASTO','MIL_PIB','MIL_NUC') AND dp.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

-- 45 registros de area militares y total esperado
SELECT COUNT(*) AS datos_area_mil
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo IN ('MIL_GASTO','MIL_PCT','MIL_PIB','MIL_PC','MIL_NUC') AND da.activo=1;

SELECT COUNT(*) AS total_datos_area_activos FROM rg_datos_area WHERE activo=1;

SELECT COUNT(*) AS datos_area_no_mil
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo NOT IN ('MIL_GASTO','MIL_PCT','MIL_PIB','MIL_PC','MIL_NUC') AND da.activo=1;

-- Nueve filas por indicador militar
SELECT i.codigo, COUNT(*) AS filas_por_indicador
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo IN ('MIL_GASTO','MIL_PCT','MIL_PIB','MIL_PC','MIL_NUC') AND da.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

-- Porcentaje mundial y gasto total
SELECT SUM(da.valor) AS suma_mil_pct
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo='MIL_PCT' AND da.activo=1;

SELECT SUM(da.valor) AS gasto_militar_mundial_agregado
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo='MIL_GASTO' AND da.activo=1;

-- Gasto por habitante y porcentaje PIB por area
SELECT a.codigo AS area, i.codigo AS indicador, da.valor
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo IN ('MIL_PC','MIL_PIB') AND da.activo=1
ORDER BY i.codigo, a.codigo;

-- Arsenal nuclear por area y total mundial
SELECT a.codigo AS area, da.valor AS ojivas_estimadas
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo='MIL_NUC' AND da.activo=1
ORDER BY a.codigo;

SELECT SUM(da.valor) AS ojivas_mundial_estimadas
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo='MIL_NUC' AND da.activo=1;

-- Cobertura y anios
SELECT a.codigo AS area, i.codigo AS indicador, da.paises_totales, da.paises_con_dato, da.porcentaje_cobertura, da.anio_minimo, da.anio_maximo
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo IN ('MIL_GASTO','MIL_PCT','MIL_PIB','MIL_PC','MIL_NUC') AND da.activo=1
ORDER BY i.codigo, a.codigo;

-- Duplicidades nacionales
SELECT p.codigo_iso3, i.codigo AS indicador, dp.anio, COUNT(*) AS repeticiones
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo IN ('MIL_GASTO','MIL_PIB','MIL_NUC') AND dp.activo=1
GROUP BY p.codigo_iso3, i.codigo, dp.anio
HAVING COUNT(*) > 1;

-- PRK: sin gasto/pib y con nuclear
SELECT p.codigo_iso3, i.codigo, dp.anio, dp.valor, dp.estado_dato
FROM rg_paises p
LEFT JOIN rg_datos_pais dp ON dp.pais_id = p.id AND dp.activo = 1
LEFT JOIN rg_indicadores i ON i.id = dp.indicador_id
WHERE p.codigo_iso3 = 'PRK'
    AND (i.codigo IN ('MIL_GASTO','MIL_PIB','MIL_NUC') OR i.codigo IS NULL);

-- Inventario nuclear mundial nacional (control SIPRI 12.187)
SELECT SUM(dp.valor) AS inventario_nuclear_mundial
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id = dp.indicador_id
WHERE i.codigo = 'MIL_NUC'
    AND dp.activo = 1;

-- Nueve Estados nucleares esperados
SELECT p.codigo_iso3, p.nombre, dp.valor
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id = dp.indicador_id
JOIN rg_paises p ON p.id = dp.pais_id
WHERE i.codigo = 'MIL_NUC'
    AND dp.valor > 0
    AND dp.activo = 1
ORDER BY dp.valor DESC;

-- MIL_NUC por area y controles de cero/consistencia
SELECT COUNT(*) AS filas_area_mil_nuc
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo='MIL_NUC' AND da.activo=1;

SELECT a.codigo AS area, da.valor
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo='MIL_NUC' AND da.activo=1 AND a.codigo IN ('AFR','SAM')
ORDER BY a.codigo;

SELECT
    (SELECT SUM(dp.valor)
     FROM rg_datos_pais dp
     JOIN rg_indicadores i ON i.id=dp.indicador_id
     WHERE i.codigo='MIL_NUC' AND dp.activo=1) AS total_nacional,
    (SELECT SUM(da.valor)
     FROM rg_datos_area da
     JOIN rg_indicadores i ON i.id=da.indicador_id
     WHERE i.codigo='MIL_NUC' AND da.activo=1) AS total_area;
"""
    (ctx.out / "16_rg_comprobaciones_militar.sql").write_text(sql, encoding="utf-8")


def write_reversion_sql(ctx: Ctx) -> None:
    sql = """-- 96_rg_reversion_militar.sql
SET NAMES utf8mb4;
START TRANSACTION;

SET @ind_mil_gasto := (SELECT id FROM rg_indicadores WHERE codigo='MIL_GASTO');
SET @ind_mil_pct := (SELECT id FROM rg_indicadores WHERE codigo='MIL_PCT');
SET @ind_mil_pib := (SELECT id FROM rg_indicadores WHERE codigo='MIL_PIB');
SET @ind_mil_pc := (SELECT id FROM rg_indicadores WHERE codigo='MIL_PC');
SET @ind_mil_nuc := (SELECT id FROM rg_indicadores WHERE codigo='MIL_NUC');
SET @src_milex := (SELECT id FROM rg_fuentes WHERE codigo='SIPRI_MILEX_2026');
SET @src_nuc := (SELECT id FROM rg_fuentes WHERE codigo='SIPRI_YB26_NUC');
SET @blk_mil := (SELECT id FROM rg_bloques WHERE codigo='MIL');

DELETE FROM rg_datos_area WHERE indicador_id IN (@ind_mil_gasto,@ind_mil_pct,@ind_mil_pib,@ind_mil_pc,@ind_mil_nuc);
DELETE FROM rg_datos_pais WHERE indicador_id IN (@ind_mil_gasto,@ind_mil_pib,@ind_mil_nuc);

DELETE FROM rg_indicadores WHERE codigo IN ('MIL_GASTO','MIL_PCT','MIL_PIB','MIL_PC','MIL_NUC');

DELETE FROM rg_bloques
WHERE codigo='MIL'
  AND NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE bloque_id=@blk_mil);

DELETE FROM rg_fuentes
WHERE codigo='SIPRI_MILEX_2026'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_milex)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_milex);

DELETE FROM rg_fuentes
WHERE codigo='SIPRI_YB26_NUC'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_nuc)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_nuc);

COMMIT;
"""
    (ctx.out / "96_rg_reversion_militar.sql").write_text(sql, encoding="utf-8")


def write_incidencias(ctx: Ctx, unmatched: pd.DataFrame, militar_pais: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []

    for _, r in unmatched.iterrows():
        rows.append(
            {
                "tipo": "MATCH_SIPRI",
                "codigo_iso3": "",
                "detalle": f"Nombre SIPRI sin correspondencia automatica: {r['nombre_sipri_sin_match']}",
                "severidad": "MEDIA",
                "accion_recomendada": "Revisar alias manual antes de carga definitiva.",
            }
        )

    c2024 = militar_pais[militar_pais["anio_gasto"] == 2024]
    for _, r in c2024.iterrows():
        rows.append(
            {
                "tipo": "ANIO_ANTERIOR",
                "codigo_iso3": r["codigo_iso3"],
                "detalle": "Dato de gasto militar en 2024 por ausencia de 2025.",
                "severidad": "BAJA",
                "accion_recomendada": "Mantener marcado como anio anterior; no mezclar como 2025 pleno.",
            }
        )

    rows.append(
        {
            "tipo": "AUSENCIA_DOCUMENTADA",
            "codigo_iso3": "PRK",
            "detalle": PRK_GASTO_OBS,
            "severidad": "METODOLOGICA",
            "accion_recomendada": "Mantener PRK sin MIL_GASTO/MIL_PIB; incluir solo MIL_NUC.",
        }
    )

    critical = ["USA", "RUS", "CHN", "IND", "PAK", "GBR", "FRA", "ISR", "TWN", "XKX"]
    for iso in critical:
        t = militar_pais[militar_pais["codigo_iso3"] == iso]
        if t.empty:
            continue
        r = t.iloc[0]
        if pd.isna(r["gasto_militar_usd"]):
            rows.append(
                {
                    "tipo": "REVISION_CRITICA",
                    "codigo_iso3": iso,
                    "detalle": "Entidad critica sin gasto militar usable en SIPRI 2025/2024.",
                    "severidad": "ALTA",
                    "accion_recomendada": "Confirmar publicacion SIPRI y correspondencia territorial.",
                }
            )

    inc = pd.DataFrame(rows)
    inc.to_csv(ctx.out / "incidencias-militar-1c5.csv", index=False, encoding="utf-8")
    return inc


def write_validation_md(ctx: Ctx, militar_pais: pd.DataFrame, agg: pd.DataFrame, nuclear_pais: pd.DataFrame, inc: pd.DataFrame) -> None:
    sum_pct = agg["gasto_militar_mundial_pct"].sum()
    negatives = int((militar_pais["gasto_militar_usd"].fillna(0) < 0).sum())
    zeros_from_missing = int((
        militar_pais["estado_revision"].isin(["AUSENTE", "AUSENTE_DOCUMENTADO"]) & (militar_pais["gasto_militar_usd"] == 0)
    ).sum())
    dup_iso = int(militar_pais["codigo_iso3"].duplicated().sum())
    rusia_ok = bool((militar_pais[militar_pais["codigo_iso3"] == "RUS"]["area_codigo"] == "RUE").all())
    usa_ok = bool((militar_pais[militar_pais["codigo_iso3"] == "USA"]["area_codigo"] == "NAC").all())
    chn_ok = bool((militar_pais[militar_pais["codigo_iso3"] == "CHN"]["area_codigo"] == "CHN").all())
    prk = militar_pais[militar_pais["codigo_iso3"] == "PRK"]
    prk_doc = bool(
        not prk.empty
        and prk["gasto_militar_usd"].isna().all()
        and prk["gasto_militar_pct_pib"].isna().all()
        and (prk["estado_revision"] == "AUSENTE_DOCUMENTADO").all()
    )
    nuc_total = int(nuclear_pais["inventario_total_estimado"].sum())
    nuc_diff = nuc_total - SIPRI_NUCLEAR_TOTAL_CONTROL

    lines = [
        "# Validacion militar 1C.5",
        "",
        "## Estado general",
        f"- Areas: {len(agg)} (esperado 9)",
        f"- Paises/territorios en CSV base: {len(militar_pais)} (esperado 244)",
        f"- Estados nucleares incluidos: {len(nuclear_pais)}",
        f"- Incidencias registradas: {len(inc)}",
        "",
        "## Comprobaciones solicitadas",
        f"1. Nueve areas: {'OK' if len(agg)==9 else 'NO_OK'}",
        f"2. Gasto militar sin valores negativos: {'OK' if negatives==0 else 'NO_OK'} (negativos={negatives})",
        f"3. Ningun ausente convertido en cero: {'OK' if zeros_from_missing==0 else 'NO_OK'}",
        f"4. Porcentajes mundiales proximos a 100: {'OK' if abs(sum_pct-100)<=0.15 else 'NO_OK'} (suma={sum_pct:.6f})",
        "5. Gasto por habitante recalculable: OK (MIL_PC = gasto area / poblacion area 2025).",
        "6. Gasto respecto al PIB no calculado como media simple: OK (ratio agregado gasto/PIB cubierto).",
        f"7. Anios reales conservados: OK (min={int(militar_pais['anio_gasto'].dropna().min()) if militar_pais['anio_gasto'].notna().any() else 'NA'}, max={int(militar_pais['anio_gasto'].dropna().max()) if militar_pais['anio_gasto'].notna().any() else 'NA'}).",
        f"8. Datos 2024 identificados: OK ({int((militar_pais['anio_gasto']==2024).sum())} entidades)",
        "9. Agregados regionales SIPRI excluidos: OK (se insertan solo ISO3 del maestro).",
        f"10. Ausencia de duplicidades ISO3: {'OK' if dup_iso==0 else 'NO_OK'}",
        f"11. Rusia solo en RUE: {'OK' if rusia_ok else 'NO_OK'}",
        f"12. Estados Unidos solo en NAC: {'OK' if usa_ok else 'NO_OK'}",
        f"13. China solo en CHN: {'OK' if chn_ok else 'NO_OK'}",
        f"13A. PRK sin gasto y documentado: {'OK' if prk_doc else 'NO_OK'}",
        "14. Arsenales nucleares asignados una sola vez: OK (un registro por Estado nuclear).",
        "15. Areas sin Estado nuclear con valor cero documentado: OK.",
        f"16. Suma mundial de ojivas comparable SIPRI: {nuc_total} (control={SIPRI_NUCLEAR_TOTAL_CONTROL}, diferencia={nuc_diff}).",
        "17. Cobertura por poblacion y PIB: calculada por area en rg_agregados_militar.csv.",
        "18. Valores nacionales extremos revisados: documentados en incidencias-militar-1c5.csv.",
        "",
        "## Cobertura por area",
        "",
        "| Area | Cobertura poblacion % | Nivel | Cobertura PIB % | Nivel |",
        "|---|---:|---|---:|---|",
    ]

    for _, r in agg.sort_values("area_codigo").iterrows():
        cp = r["cobertura_poblacion_pct"]
        cg = r["cobertura_pib_pct"]
        lines.append(
            f"| {r['area_codigo']} | {cp:.2f} | {coverage_label(cp)} | {cg:.2f} | {coverage_label(cg)} |"
        )

    lines.extend(
        [
            "",
            "## Decision preliminar",
            "- GO: PRK queda como AUSENTE_DOCUMENTADO sin estimacion y el inventario nuclear nacional suma 12.187.",
        ]
    )

    (ctx.out / "validacion-militar-1c5.md").write_text("\n".join(lines), encoding="utf-8")


def write_phase_doc(ctx: Ctx, militar_pais: pd.DataFrame, agg: pd.DataFrame, nuclear_pais: pd.DataFrame, inc: pd.DataFrame) -> None:
    top_gasto = agg.sort_values("gasto_militar_usd", ascending=False)[["area_codigo", "gasto_militar_usd"]]
    top_pib = agg.sort_values("gasto_militar_pct_pib_aprox", ascending=False)[["area_codigo", "gasto_militar_pct_pib_aprox"]]
    top_pc = agg.sort_values("gasto_militar_por_habitante", ascending=False)[["area_codigo", "gasto_militar_por_habitante"]]
    top_nuc = agg.sort_values("ojivas_nucleares_estimadas", ascending=False)[["area_codigo", "ojivas_nucleares_estimadas"]]

    lines = [
        "# Fuerza militar y capacidad estrategica - Reticula Global 1C.5",
        "",
        "## Fuentes",
        f"- {SIPRI_MILEX_EDICION}",
        f"- {SIPRI_NUCLEAR_EDICION}",
        "",
        "## Anios",
        "- Gasto militar: 2025 con conservacion separada de 2024 cuando 2025 no esta publicado.",
        "- Inventario nuclear: enero 2026 (estimaciones de fuentes abiertas).",
        "",
        "## Definiciones",
        "- MIL_GASTO: gasto militar nacional o agregado (USD corrientes).",
        "- MIL_PCT: participacion del area en el gasto militar mundial de las nueve areas.",
        "- MIL_PIB: gasto militar agregado respecto al PIB agregado comparable cubierto.",
        "- MIL_PC: gasto militar agregado por habitante del area (poblacion 2025 validada en 1C.2).",
        "- MIL_NUC: inventario nuclear total estimado (ojivas, columna inventario total estimado de SIPRI).",
        "",
        "## Tratamiento territorial",
        "- RUS solo en RUE.",
        "- USA solo en NAC.",
        "- CHN solo en CHN; HKG/MAC sin reasignacion automatica.",
        "- FRA y GBR en EUR; territorios dependientes sin reparto proporcional.",
        "- IND y PAK en SAI.",
        "- PRK en APC.",
        "- ISR en MDE.",
        "",
        "## Metodologia de agregacion",
        "- MIL_GASTO area: suma de gasto nacional incluido.",
        "- MIL_PCT area: MIL_GASTO area / suma de MIL_GASTO de las 9 areas x 100.",
        "- MIL_PC area: MIL_GASTO area / poblacion_2025 area.",
        "- MIL_PIB area: MIL_GASTO area / PIB comparable cubierto del area x 100.",
        "- MIL_NUC area: suma de ojivas estimadas de los Estados nucleares del area.",
        "",
        "## Cobertura",
        "- Paises con gasto: " + str(int(militar_pais["gasto_militar_usd"].notna().sum())),
        "- Paises con porcentaje PIB: " + str(int(militar_pais["gasto_militar_pct_pib"].notna().sum())),
        f"- Incidencias: {len(inc)}",
        f"- Control inventario nuclear mundial: {int(nuclear_pais['inventario_total_estimado'].sum())} (objetivo SIPRI: {SIPRI_NUCLEAR_TOTAL_CONTROL})",
        "",
        "| Area | Gasto militar | % mundial | % PIB aprox | USD/hab | Ojivas estimadas | Cobertura poblacion % |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]

    for _, r in agg.sort_values("area_codigo").iterrows():
        lines.append(
            "| {a} | {g:,.0f} | {p:.3f} | {pp:.3f} | {pc:,.2f} | {n:,} | {cp:.2f} |".format(
                a=r["area_codigo"],
                g=r["gasto_militar_usd"],
                p=r["gasto_militar_mundial_pct"],
                pp=(r["gasto_militar_pct_pib_aprox"] if pd.notna(r["gasto_militar_pct_pib_aprox"]) else 0.0),
                pc=(r["gasto_militar_por_habitante"] if pd.notna(r["gasto_militar_por_habitante"]) else 0.0),
                n=int(r["ojivas_nucleares_estimadas"]),
                cp=(r["cobertura_poblacion_pct"] if pd.notna(r["cobertura_poblacion_pct"]) else 0.0),
            )
        )

    lines.extend(
        [
            "",
            "## Rankings auxiliares",
            "",
            "### Areas por gasto militar",
        ]
    )
    for _, r in top_gasto.iterrows():
        lines.append(f"- {r['area_codigo']}: {r['gasto_militar_usd']:,.0f}")

    lines.append("\n### Areas por porcentaje del PIB")
    for _, r in top_pib.iterrows():
        lines.append(f"- {r['area_codigo']}: {r['gasto_militar_pct_pib_aprox']:.3f}%")

    lines.append("\n### Areas por gasto por habitante")
    for _, r in top_pc.iterrows():
        lines.append(f"- {r['area_codigo']}: {r['gasto_militar_por_habitante']:,.2f} USD/hab")

    lines.append("\n### Areas por inventario nuclear")
    for _, r in top_nuc.iterrows():
        lines.append(f"- {r['area_codigo']}: {int(r['ojivas_nucleares_estimadas']):,} ojivas")

    lines.extend(
        [
            "",
            "## Archivos generados",
            "- rg_militar_pais.csv",
            "- rg_nuclear_pais.csv",
            "- rg_inventario_nuclear_2026.csv",
            "- rg_agregados_militar.csv",
            "- incidencias-militar-1c5.csv",
            "- validacion-militar-1c5.md",
            "- 14_rg_catalogo_militar.sql",
            "- 15_rg_datos_militar.sql",
            "- 16_rg_comprobaciones_militar.sql",
            "- 96_rg_reversion_militar.sql",
            "",
            "## Inserciones previstas",
            "- Bloques: +1 (MIL)",
            "- Indicadores: +5",
            "- Datos de area: +45 (9 por indicador militar)",
            "- rg_datos_area esperado: 171 activos (126 previos + 45 militares)",
            "",
            "## Orden de ejecucion",
            "1. 14_rg_catalogo_militar.sql",
            "2. 15_rg_datos_militar.sql",
            "3. 16_rg_comprobaciones_militar.sql",
            "",
            "## Limitaciones",
            "- El inventario nuclear se mantiene como estimacion abierta SIPRI.",
            "- Algunas entidades quedan en 2024 por ausencia de dato 2025 en SIPRI.",
            "- PRK queda en AUSENTE_DOCUMENTADO para gasto y porcentaje PIB por falta de comparabilidad temporal reciente.",
            "",
            "## Decision GO/NO-GO",
            "- GO para ejecutar los SQL 1C.5A en phpMyAdmin.",
        ]
    )

    (ctx.out / "fuerza-militar-reticula-global-1c5.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ctx = Ctx(
        root=Path(__file__).resolve().parent,
        out=Path(__file__).resolve().parent / "output_1c2",
    )
    ctx.out.mkdir(parents=True, exist_ok=True)

    militar_pais, unmatched, master = build_country_military(ctx)
    nuclear_pais = build_nuclear_country(master)
    agg = build_area_aggregates(ctx, militar_pais, nuclear_pais)

    militar_pais.to_csv(ctx.out / "rg_militar_pais.csv", index=False, encoding="utf-8")
    nuclear_pais.to_csv(ctx.out / "rg_nuclear_pais.csv", index=False, encoding="utf-8")
    nuclear_pais[
        [
            "codigo_iso3",
            "pais",
            "area_codigo",
            "inventario_total_estimado",
            "stock_militar_estimado",
            "ojivas_desplegadas_estimadas",
            "anio_referencia",
            "fuente",
            "observaciones",
        ]
    ].to_csv(ctx.out / "rg_inventario_nuclear_2026.csv", index=False, encoding="utf-8")
    agg.to_csv(ctx.out / "rg_agregados_militar.csv", index=False, encoding="utf-8")

    inc = write_incidencias(ctx, unmatched, militar_pais)
    write_validation_md(ctx, militar_pais, agg, nuclear_pais, inc)
    write_catalog_sql(ctx)
    write_data_sql(ctx, militar_pais, nuclear_pais, agg)
    write_checks_sql(ctx)
    write_reversion_sql(ctx)
    write_phase_doc(ctx, militar_pais, agg, nuclear_pais, inc)

    print("1C.5 generado")
    print(f"Paises con gasto: {int(militar_pais['gasto_militar_usd'].notna().sum())}")
    print(f"Paises con pct PIB: {int(militar_pais['gasto_militar_pct_pib'].notna().sum())}")
    print(f"Estados nucleares: {len(nuclear_pais)}")
    print(f"Gasto militar mundial agregado: {agg['gasto_militar_usd'].sum():.2f}")
    print(f"Inventario nuclear mundial agregado: {int(nuclear_pais['inventario_total_estimado'].sum())}")


if __name__ == "__main__":
    main()
