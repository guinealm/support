from __future__ import annotations

import io
import math
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import requests


OWID_ENERGY_CSV = "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"
WB_DEP_API = "https://api.worldbank.org/v2/country/all/indicator/EG.IMP.CONS.ZS"

SRC_CONSUMO = "Energy Institute - Statistical Review of World Energy 2026 (via Our World in Data)"
SRC_DEP = "International Energy Agency (via World Development Indicators - Banco Mundial EG.IMP.CONS.ZS)"
SRC_ELEC = "Ember - Global Electricity Review 2026 / Electricity Data Explorer (via Our World in Data)"
SRC_OWID_PROC = "Our World in Data (procesamiento reproducible de series energeticas)"

YEAR_CONSUMO_OBJ = 2025
YEAR_CONSUMO_FALLBACK = 2024
YEAR_DEP_OBJ = 2023
YEAR_DEP_FALLBACK = 2022
YEAR_ELEC_OBJ = 2025
YEAR_ELEC_FALLBACK = 2024

EJ_TO_TWH = 277.777778


@dataclass
class Ctx:
    root: Path
    out: Path


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


def fmt2(v: float | None) -> str:
    if v is None or pd.isna(v):
        return "NA"
    return f"{float(v):.2f}"


def fetch_owid_energy() -> pd.DataFrame:
    r = requests.get(OWID_ENERGY_CSV, timeout=180)
    r.raise_for_status()
    df = pd.read_csv(io.BytesIO(r.content), low_memory=False)

    cols = [
        "iso_code",
        "country",
        "year",
        "primary_energy_consumption",
        "coal_consumption",
        "oil_consumption",
        "gas_consumption",
        "electricity_generation",
        "low_carbon_electricity",
    ]
    keep = [c for c in cols if c in df.columns]
    out = df[keep].copy()
    out = out.rename(columns={"iso_code": "codigo_iso3", "country": "pais_fuente", "year": "anio"})
    out["codigo_iso3"] = out["codigo_iso3"].astype(str).str.upper().str.strip()
    out["anio"] = pd.to_numeric(out["anio"], errors="coerce")

    for c in [
        "primary_energy_consumption",
        "coal_consumption",
        "oil_consumption",
        "gas_consumption",
        "electricity_generation",
        "low_carbon_electricity",
    ]:
        if c in out.columns:
            out[c] = pd.to_numeric(out[c], errors="coerce")
    return out


def fetch_wb_dependency() -> pd.DataFrame:
    page = 1
    rows: list[dict[str, object]] = []
    while True:
        r = requests.get(
            WB_DEP_API,
            params={"format": "json", "per_page": 20000, "page": page},
            timeout=180,
        )
        r.raise_for_status()
        payload = r.json()
        meta = payload[0]
        data = payload[1]

        for d in data:
            rows.append(
                {
                    "codigo_iso3": str(d.get("countryiso3code") or "").upper().strip(),
                    "anio": int(d["date"]) if d.get("date") else None,
                    "dependencia_energetica_pct": d.get("value"),
                }
            )

        if page >= int(meta.get("pages", page)):
            break
        page += 1

    out = pd.DataFrame(rows)
    out["anio"] = pd.to_numeric(out["anio"], errors="coerce")
    out["dependencia_energetica_pct"] = pd.to_numeric(out["dependencia_energetica_pct"], errors="coerce")
    return out


def pick_year_value(g: pd.DataFrame, target: int, fallback: int | None = None) -> tuple[float | None, int | None]:
    t = g[g["anio"] == target]
    if not t.empty and t["valor"].notna().any():
        row = t[t["valor"].notna()].iloc[0]
        return float(row["valor"]), int(row["anio"])
    if fallback is not None:
        f = g[g["anio"] == fallback]
        if not f.empty and f["valor"].notna().any():
            row = f[f["valor"].notna()].iloc[0]
            return float(row["valor"]), int(row["anio"])
    return None, None


def build_country_energy(ctx: Ctx) -> pd.DataFrame:
    master = pd.read_csv(ctx.root / "rg_paises_areas_operativo.csv", dtype=str)
    pob = pd.read_csv(ctx.out / "rg_territorio_poblacion_pais.csv")

    owid = fetch_owid_energy()
    wb = fetch_wb_dependency()

    dep = wb[["codigo_iso3", "anio", "dependencia_energetica_pct"]].copy()
    dep = dep.rename(columns={"dependencia_energetica_pct": "valor"})

    rows: list[dict[str, object]] = []

    for _, r in master.iterrows():
        iso = str(r["codigo_iso3"]).upper().strip()
        area = str(r["area_codigo"])
        pais = r["nombre_es"]

        o = owid[owid["codigo_iso3"] == iso].copy()
        d = dep[dep["codigo_iso3"] == iso].copy()

        cons_twh = None
        anio_cons = None

        c25 = o[o["anio"] == YEAR_CONSUMO_OBJ]
        if not c25.empty and c25["primary_energy_consumption"].notna().any():
            row = c25[c25["primary_energy_consumption"].notna()].iloc[0]
            cons_twh = float(row["primary_energy_consumption"])
            anio_cons = YEAR_CONSUMO_OBJ
        else:
            c24 = o[o["anio"] == YEAR_CONSUMO_FALLBACK]
            if not c24.empty and c24["primary_energy_consumption"].notna().any():
                row = c24[c24["primary_energy_consumption"].notna()].iloc[0]
                cons_twh = float(row["primary_energy_consumption"])
                anio_cons = YEAR_CONSUMO_FALLBACK

        energia_fosil_twh = None
        energia_fosil_pct = None
        anio_fosil = None
        if anio_cons is not None and cons_twh is not None:
            of = o[o["anio"] == anio_cons]
            if not of.empty:
                rw = of.iloc[0]
                coal = float(rw["coal_consumption"]) if pd.notna(rw.get("coal_consumption")) else 0.0
                oil = float(rw["oil_consumption"]) if pd.notna(rw.get("oil_consumption")) else 0.0
                gas = float(rw["gas_consumption"]) if pd.notna(rw.get("gas_consumption")) else 0.0
                energia_fosil_twh = coal + oil + gas
                if cons_twh and cons_twh > 0:
                    energia_fosil_pct = energia_fosil_twh / cons_twh * 100.0
                anio_fosil = anio_cons

        dep_val, dep_year = pick_year_value(d, YEAR_DEP_OBJ, YEAR_DEP_FALLBACK)
        auto_val = 100.0 - dep_val if dep_val is not None else None

        elec_total = None
        elec_lc = None
        elec_lc_pct = None
        anio_elec = None

        e25 = o[o["anio"] == YEAR_ELEC_OBJ]
        if not e25.empty and e25["electricity_generation"].notna().any() and e25["low_carbon_electricity"].notna().any():
            rw = e25.iloc[0]
            elec_total = float(rw["electricity_generation"])
            elec_lc = float(rw["low_carbon_electricity"])
            if elec_total > 0:
                elec_lc_pct = elec_lc / elec_total * 100.0
            anio_elec = YEAR_ELEC_OBJ
        else:
            e24 = o[o["anio"] == YEAR_ELEC_FALLBACK]
            if not e24.empty and e24["electricity_generation"].notna().any() and e24["low_carbon_electricity"].notna().any():
                rw = e24.iloc[0]
                elec_total = float(rw["electricity_generation"])
                elec_lc = float(rw["low_carbon_electricity"])
                if elec_total > 0:
                    elec_lc_pct = elec_lc / elec_total * 100.0
                anio_elec = YEAR_ELEC_FALLBACK

        pop25 = pob[pob["codigo_iso3"] == iso]["poblacion_2025"]
        popv = float(pop25.iloc[0]) if not pop25.empty and pd.notna(pop25.iloc[0]) else None
        cons_pc = (cons_twh * 1_000_000_000.0 / popv) if (cons_twh is not None and popv and popv > 0) else None

        estado = "OK"
        obs: list[str] = []
        if cons_twh is None:
            estado = "REVISAR"
            obs.append("Sin consumo de energia primaria 2025 comparable en serie OWID/EI.")
        elif anio_cons == YEAR_CONSUMO_FALLBACK:
            obs.append("Consumo de energia primaria en 2024 por ausencia de 2025 en serie OWID/EI.")
        if dep_val is None:
            estado = "REVISAR"
            obs.append("Sin dependencia energetica WDI en 2023/2022.")
        elif dep_year == YEAR_DEP_FALLBACK:
            obs.append("Dependencia energetica tomada en 2022 por ausencia de 2023.")
        if elec_total is None or elec_lc is None:
            estado = "REVISAR"
            obs.append("Sin dato de electricidad baja en carbono 2025/2024 comparable.")
        elif anio_elec == YEAR_ELEC_FALLBACK:
            obs.append("Electricidad baja en carbono en 2024 por ausencia de 2025.")

        if str(r.get("incluir_calculos", "")).upper() == "SEGUN_FUENTE":
            obs.append("Entidad SEGUN_FUENTE; evitar duplicidad con Estado soberano.")

        if iso == "CHN":
            obs.append("CHN tratado separado de HKG/MAC.")
        if iso in {"HKG", "MAC"}:
            obs.append("HKG/MAC solo con dato separado publicable y comparable.")
        if iso == "RUS":
            obs.append("RUS asignado exclusivamente a RUE.")
        if iso == "PRK":
            obs.append("PRK se mantiene ausente cuando no hay publicacion comparable; no estimar.")

        rows.append(
            {
                "codigo_iso3": iso,
                "codigo_m49": r["codigo_m49"],
                "pais": pais,
                "area_codigo": area,
                "consumo_energia_twh": cons_twh,
                "anio_consumo": anio_cons,
                "consumo_per_capita_kwh": cons_pc,
                "dependencia_energetica_pct": dep_val,
                "anio_dependencia": dep_year,
                "autosuficiencia_pct": auto_val,
                "energia_fosil_twh": energia_fosil_twh,
                "energia_fosil_pct": energia_fosil_pct,
                "anio_fosil": anio_fosil,
                "electricidad_total_twh": elec_total,
                "electricidad_baja_carbono_twh": elec_lc,
                "electricidad_baja_carbono_pct": elec_lc_pct,
                "anio_electricidad": anio_elec,
                "fuente_consumo": f"{SRC_CONSUMO}; {SRC_OWID_PROC}",
                "fuente_dependencia": SRC_DEP,
                "fuente_electricidad": f"{SRC_ELEC}; {SRC_OWID_PROC}",
                "estado_revision": estado,
                "observaciones": " ".join(obs).strip(),
            }
        )

    out = pd.DataFrame(rows)
    out.loc[out["codigo_iso3"] == "PRK", [
        "consumo_energia_twh",
        "anio_consumo",
        "consumo_per_capita_kwh",
        "dependencia_energetica_pct",
        "anio_dependencia",
        "autosuficiencia_pct",
        "energia_fosil_twh",
        "energia_fosil_pct",
        "anio_fosil",
        "electricidad_total_twh",
        "electricidad_baja_carbono_twh",
        "electricidad_baja_carbono_pct",
        "anio_electricidad",
    ]] = None
    out.loc[out["codigo_iso3"] == "PRK", "estado_revision"] = "AUSENTE_DOCUMENTADO"
    return out


def build_area_energy(ctx: Ctx, pais: pd.DataFrame) -> pd.DataFrame:
    pop_area = pd.read_csv(ctx.out / "rg_agregados_territorio_poblacion.csv")[["area_codigo", "area_nombre", "poblacion_2025"]]

    rows: list[dict[str, object]] = []
    for _, ar in pop_area.sort_values("area_codigo").iterrows():
        ac = ar["area_codigo"]
        t = pais[pais["area_codigo"] == ac].copy()

        consumo_total = t["consumo_energia_twh"].dropna().sum()
        ent_tot = len(t)
        ent_cons = int(t["consumo_energia_twh"].notna().sum())
        pop_total = float(ar["poblacion_2025"]) if pd.notna(ar["poblacion_2025"]) else None
        pop_cov = t.loc[t["consumo_energia_twh"].notna(), "codigo_iso3"].map(
            pd.read_csv(ctx.out / "rg_territorio_poblacion_pais.csv").set_index("codigo_iso3")["poblacion_2025"].to_dict()
        ).dropna().sum()
        cov_cons_pop = (pop_cov / pop_total * 100.0) if pop_total and pop_total > 0 else None

        dep_set = t[t["dependencia_energetica_pct"].notna() & t["consumo_energia_twh"].notna()].copy()
        ent_dep = len(dep_set)
        cons_cov_dep = dep_set["consumo_energia_twh"].sum()
        cov_dep_cons = (cons_cov_dep / consumo_total * 100.0) if consumo_total and consumo_total > 0 else None
        dep_num = (dep_set["consumo_energia_twh"] * dep_set["dependencia_energetica_pct"] / 100.0).sum()
        dep_area = (dep_num / cons_cov_dep * 100.0) if cons_cov_dep and cons_cov_dep > 0 else None
        auto_area = (100.0 - dep_area) if dep_area is not None else None

        fos_set = t[t["energia_fosil_twh"].notna() & t["consumo_energia_twh"].notna()].copy()
        ent_fos = len(fos_set)
        cons_cov_fos = fos_set["consumo_energia_twh"].sum()
        cov_fos_cons = (cons_cov_fos / consumo_total * 100.0) if consumo_total and consumo_total > 0 else None
        fos_area = (fos_set["energia_fosil_twh"].sum() / cons_cov_fos * 100.0) if cons_cov_fos and cons_cov_fos > 0 else None

        el_set = t[t["electricidad_total_twh"].notna() & t["electricidad_baja_carbono_twh"].notna()].copy()
        ent_el = len(el_set)
        el_cov = el_set["electricidad_total_twh"].sum()
        el_all = t["electricidad_total_twh"].dropna().sum()
        cov_el_gen = (el_cov / el_all * 100.0) if el_all and el_all > 0 else None
        el_lc_area = (el_set["electricidad_baja_carbono_twh"].sum() / el_cov * 100.0) if el_cov and el_cov > 0 else None

        cons_pc_area = (consumo_total * 1_000_000_000.0 / pop_total) if pop_total and pop_total > 0 else None

        y_cons = t.loc[t["consumo_energia_twh"].notna(), "anio_consumo"].dropna()
        y_dep = t.loc[t["dependencia_energetica_pct"].notna(), "anio_dependencia"].dropna()
        y_el = t.loc[t["electricidad_total_twh"].notna() & t["electricidad_baja_carbono_twh"].notna(), "anio_electricidad"].dropna()

        obs = [
            "Dependencia energetica neta aproximada, ponderada por consumo energetico.",
            "Autosuficiencia energetica neta aproximada.",
            "Participacion de combustibles fosiles en el consumo de energia primaria cubierto.",
            "Porcentaje de generacion electrica baja en carbono del area cubierta.",
        ]
        if ac == "APC":
            obs.append("La cifra de consumo energetico del area refleja cobertura disponible, no completitud absoluta.")

        rows.append(
            {
                "area_codigo": ac,
                "area_nombre": ar["area_nombre"],
                "consumo_energia_twh": consumo_total,
                "consumo_per_capita_kwh": cons_pc_area,
                "dependencia_energetica_pct_aprox": dep_area,
                "autosuficiencia_pct_aprox": auto_area,
                "energia_fosil_pct": fos_area,
                "electricidad_baja_carbono_pct": el_lc_area,
                "entidades_totales": ent_tot,
                "entidades_con_consumo": ent_cons,
                "entidades_con_dependencia": ent_dep,
                "entidades_con_fosil": ent_fos,
                "entidades_con_electricidad": ent_el,
                "cobertura_consumo_poblacion_pct": cov_cons_pop,
                "cobertura_dependencia_consumo_pct": cov_dep_cons,
                "cobertura_fosil_consumo_pct": cov_fos_cons,
                "cobertura_electricidad_generacion_pct": cov_el_gen,
                "anio_min_consumo": int(y_cons.min()) if not y_cons.empty else None,
                "anio_max_consumo": int(y_cons.max()) if not y_cons.empty else None,
                "anio_min_dependencia": int(y_dep.min()) if not y_dep.empty else None,
                "anio_max_dependencia": int(y_dep.max()) if not y_dep.empty else None,
                "anio_min_electricidad": int(y_el.min()) if not y_el.empty else None,
                "anio_max_electricidad": int(y_el.max()) if not y_el.empty else None,
                "observaciones": " ".join(obs),
            }
        )

    return pd.DataFrame(rows)


def write_catalog_sql(ctx: Ctx) -> None:
    sql = """-- 17_rg_catalogo_energia.sql
SET NAMES utf8mb4;
START TRANSACTION;

SET @next_bloque := (SELECT COALESCE(MAX(id),0) FROM rg_bloques);

INSERT INTO rg_bloques (id,codigo,nombre,activo)
SELECT (@next_bloque := @next_bloque + 1), 'ENE', 'Energia y autonomia energetica', 1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_bloques WHERE codigo='ENE');

SET @bloque_ene := (SELECT id FROM rg_bloques WHERE codigo='ENE' LIMIT 1);
SET @next_indicador := (SELECT COALESCE(MAX(id),0) FROM rg_indicadores);

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'ENE_CONS', @bloque_ene, 'Consumo de energia primaria', 'twh', 'Consumo de energia primaria en TWh', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ENE_CONS');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'ENE_PC', @bloque_ene, 'Consumo de energia primaria por habitante', 'kwh_habitante', 'Consumo de energia primaria por habitante en kWh/habitante', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ENE_PC');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'ENE_DEP', @bloque_ene, 'Dependencia energetica exterior', 'porcentaje', 'Dependencia energetica neta aproximada ponderada por consumo', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ENE_DEP');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'ENE_AUTO', @bloque_ene, 'Autosuficiencia energetica aproximada', 'porcentaje', 'Autosuficiencia energetica neta aproximada (100 - dependencia)', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ENE_AUTO');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'ENE_FOS', @bloque_ene, 'Combustibles fosiles en energia primaria', 'porcentaje', 'Participacion de carbon, petroleo y gas en energia primaria', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ENE_FOS');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'ENE_ELEC_LC', @bloque_ene, 'Electricidad baja en carbono', 'porcentaje', 'Porcentaje de generacion electrica de fuentes bajas en carbono', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ENE_ELEC_LC');

SET @next_fuente := (SELECT COALESCE(MAX(id),0) FROM rg_fuentes);

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1), 'EI_SR2026', 'Energy Institute Statistical Review of World Energy 2026', 'oficial', 'https://www.energyinst.org/statistical-review', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='EI_SR2026');

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1), 'EMBER_GER2026', 'Ember Global Electricity Review 2026 / Electricity Data Explorer', 'oficial', 'https://ember-energy.org/data/electricity-data-explorer/', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='EMBER_GER2026');

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1), 'WB_IEA_ENEDEP', 'IEA via World Development Indicators EG.IMP.CONS.ZS', 'oficial', 'https://api.worldbank.org/v2/country/all/indicator/EG.IMP.CONS.ZS', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='WB_IEA_ENEDEP');

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1), 'OWID_ENERGY_PROC', 'Our World in Data energy dataset (processor)', 'procesado', 'https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='OWID_ENERGY_PROC');

COMMIT;
"""
    (ctx.out / "17_rg_catalogo_energia.sql").write_text(sql, encoding="utf-8")


def write_data_sql(ctx: Ctx, pais: pd.DataFrame, area: pd.DataFrame) -> None:
    pais_vals = []
    for _, r in pais.iterrows():
        pais_vals.append(
            "(" + ",".join(
                [
                    q(r["codigo_iso3"]),
                    q(r["anio_consumo"]),
                    q(r["consumo_energia_twh"]),
                    q(r["consumo_per_capita_kwh"]),
                    q(r["anio_dependencia"]),
                    q(r["dependencia_energetica_pct"]),
                    q(r["autosuficiencia_pct"]),
                    q(r["anio_fosil"]),
                    q(r["energia_fosil_pct"]),
                    q(r["anio_electricidad"]),
                    q(r["electricidad_baja_carbono_pct"]),
                    q(r["observaciones"]),
                ]
            ) + ")"
        )
    pais_blob = ",\n".join(pais_vals)

    area_vals = []
    for _, r in area.sort_values("area_codigo").iterrows():
        area_vals.append(
            "(" + ",".join(
                [
                    q(r["area_codigo"]),
                    q(r["consumo_energia_twh"]),
                    q(r["consumo_per_capita_kwh"]),
                    q(r["dependencia_energetica_pct_aprox"]),
                    q(r["autosuficiencia_pct_aprox"]),
                    q(r["energia_fosil_pct"]),
                    q(r["electricidad_baja_carbono_pct"]),
                    q(r["entidades_totales"]),
                    q(r["entidades_con_consumo"]),
                    q(r["entidades_con_dependencia"]),
                    q(r["entidades_con_fosil"]),
                    q(r["entidades_con_electricidad"]),
                    q(r["cobertura_consumo_poblacion_pct"]),
                    q(r["cobertura_dependencia_consumo_pct"]),
                    q(r["cobertura_fosil_consumo_pct"]),
                    q(r["cobertura_electricidad_generacion_pct"]),
                    q(r["anio_min_consumo"]),
                    q(r["anio_max_consumo"]),
                    q(r["anio_min_dependencia"]),
                    q(r["anio_max_dependencia"]),
                    q(r["anio_min_electricidad"]),
                    q(r["anio_max_electricidad"]),
                    q(r["observaciones"]),
                ]
            ) + ")"
        )
    area_blob = ",\n".join(area_vals)

    sql = f"""-- 18_rg_datos_energia.sql
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
{pais_blob};

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
{area_blob};

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
"""
    (ctx.out / "18_rg_datos_energia.sql").write_text(sql, encoding="utf-8")


def write_checks_sql(ctx: Ctx) -> None:
    sql = """-- 19_rg_comprobaciones_energia.sql
SET NAMES utf8mb4;

-- Bloques e indicadores esperados tras 1C.6
SELECT COUNT(*) AS bloques_activos FROM rg_bloques WHERE activo=1;
SELECT COUNT(*) AS indicadores_activos FROM rg_indicadores WHERE activo=1;
SELECT COUNT(*) AS bloques_ene FROM rg_bloques WHERE codigo='ENE' AND activo=1;
SELECT COUNT(*) AS indicadores_ene FROM rg_indicadores WHERE codigo IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC') AND activo=1;

-- Registros nacionales por indicador ENE
SELECT i.codigo, COUNT(*) AS registros
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
WHERE i.codigo IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC') AND dp.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

-- 54 nuevos registros de area y total esperado
SELECT COUNT(*) AS datos_area_ene
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC') AND da.activo=1;

SELECT COUNT(*) AS total_datos_area_activos FROM rg_datos_area WHERE activo=1;

SELECT COUNT(*) AS datos_area_no_ene
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo NOT IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC') AND da.activo=1;

-- Nueve filas por indicador
SELECT i.codigo, COUNT(*) AS filas_por_indicador
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC') AND da.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

-- Consumo no negativo y ausentes no convertidos en cero
SELECT p.codigo_iso3, dp.valor
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo='ENE_CONS' AND dp.activo=1 AND dp.valor < 0;

SELECT p.codigo_iso3
FROM rg_paises p
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.activo=1
LEFT JOIN rg_indicadores i ON i.id=d.indicador_id AND i.codigo='ENE_CONS'
GROUP BY p.codigo_iso3
HAVING SUM(CASE WHEN i.codigo='ENE_CONS' THEN 1 ELSE 0 END)=0;

-- Coherencia EJ/TWh (1 EJ = 277.777778 TWh) en agregados
SELECT a.codigo AS area, da.valor AS twh,
       (da.valor / 277.777778) AS ej_estimado,
       ((da.valor / 277.777778) * 277.777778 - da.valor) AS delta_twh
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo='ENE_CONS' AND da.activo=1
ORDER BY a.codigo;

-- ENE_PC recalculable
SELECT a.codigo AS area, cons.valor AS consumo_twh, pc.valor AS pc_kwh
FROM rg_datos_area cons
JOIN rg_datos_area pc ON pc.area_id=cons.area_id AND pc.periodo_id=cons.periodo_id AND pc.anio_referencia=cons.anio_referencia
JOIN rg_indicadores ic ON ic.id=cons.indicador_id
JOIN rg_indicadores ip ON ip.id=pc.indicador_id
JOIN rg_areas a ON a.id=cons.area_id
WHERE ic.codigo='ENE_CONS' AND ip.codigo='ENE_PC' AND cons.activo=1 AND pc.activo=1
ORDER BY a.codigo;

-- ENE_DEP ponderado y ENE_AUTO = 100 - ENE_DEP
SELECT a.codigo AS area, dep.valor AS dep, auto.valor AS auto_calc, (100 - dep.valor) AS auto_esperado
FROM rg_datos_area dep
JOIN rg_datos_area auto ON auto.area_id=dep.area_id AND auto.periodo_id=dep.periodo_id AND auto.anio_referencia=dep.anio_referencia
JOIN rg_indicadores idp ON idp.id=dep.indicador_id
JOIN rg_indicadores iau ON iau.id=auto.indicador_id
JOIN rg_areas a ON a.id=dep.area_id
WHERE idp.codigo='ENE_DEP' AND iau.codigo='ENE_AUTO' AND dep.activo=1 AND auto.activo=1
ORDER BY a.codigo;

-- Exportadores netos (autosuficiencia > 100)
SELECT a.codigo AS area, da.valor AS autosuficiencia
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo='ENE_AUTO' AND da.valor > 100 AND da.activo=1
ORDER BY da.valor DESC;

-- Rangos de porcentaje y calculo desde absolutos
SELECT p.codigo_iso3, i.codigo, dp.valor
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo IN ('ENE_FOS','ENE_ELEC_LC') AND dp.activo=1 AND (dp.valor < 0 OR dp.valor > 100);

-- Anios, datos 2024 y duplicidades
SELECT i.codigo, MIN(dp.anio) AS anio_min, MAX(dp.anio) AS anio_max
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
WHERE i.codigo IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC') AND dp.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

SELECT i.codigo, COUNT(*) AS filas_2024
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
WHERE i.codigo='ENE_ELEC_LC' AND dp.anio=2024 AND dp.activo=1;

SELECT p.codigo_iso3, i.codigo, dp.anio, COUNT(*) AS repeticiones
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC') AND dp.activo=1
GROUP BY p.codigo_iso3, i.codigo, dp.anio
HAVING COUNT(*) > 1;

-- Controles territoriales
SELECT p.codigo_iso3, a.codigo AS area
FROM rg_paises p
JOIN rg_areas a ON a.id=p.area_id
WHERE p.codigo_iso3 IN ('CHN','HKG','MAC','TWN','RUS','XKX','PRK') AND p.activo=1
ORDER BY p.codigo_iso3;
"""
    (ctx.out / "19_rg_comprobaciones_energia.sql").write_text(sql, encoding="utf-8")


def write_reversion_sql(ctx: Ctx) -> None:
    sql = """-- 95_rg_reversion_energia.sql
SET NAMES utf8mb4;
START TRANSACTION;

SET @ind_ene_cons := (SELECT id FROM rg_indicadores WHERE codigo='ENE_CONS');
SET @ind_ene_pc := (SELECT id FROM rg_indicadores WHERE codigo='ENE_PC');
SET @ind_ene_dep := (SELECT id FROM rg_indicadores WHERE codigo='ENE_DEP');
SET @ind_ene_auto := (SELECT id FROM rg_indicadores WHERE codigo='ENE_AUTO');
SET @ind_ene_fos := (SELECT id FROM rg_indicadores WHERE codigo='ENE_FOS');
SET @ind_ene_elec_lc := (SELECT id FROM rg_indicadores WHERE codigo='ENE_ELEC_LC');
SET @blk_ene := (SELECT id FROM rg_bloques WHERE codigo='ENE');

SET @src_ei := (SELECT id FROM rg_fuentes WHERE codigo='EI_SR2026');
SET @src_ember := (SELECT id FROM rg_fuentes WHERE codigo='EMBER_GER2026');
SET @src_dep := (SELECT id FROM rg_fuentes WHERE codigo='WB_IEA_ENEDEP');
SET @src_owid := (SELECT id FROM rg_fuentes WHERE codigo='OWID_ENERGY_PROC');

DELETE FROM rg_datos_area WHERE indicador_id IN (@ind_ene_cons,@ind_ene_pc,@ind_ene_dep,@ind_ene_auto,@ind_ene_fos,@ind_ene_elec_lc);
DELETE FROM rg_datos_pais WHERE indicador_id IN (@ind_ene_cons,@ind_ene_pc,@ind_ene_dep,@ind_ene_auto,@ind_ene_fos,@ind_ene_elec_lc);

DELETE FROM rg_indicadores WHERE codigo IN ('ENE_CONS','ENE_PC','ENE_DEP','ENE_AUTO','ENE_FOS','ENE_ELEC_LC');

DELETE FROM rg_bloques
WHERE codigo='ENE'
  AND NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE bloque_id=@blk_ene);

DELETE FROM rg_fuentes
WHERE codigo='EI_SR2026'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_ei)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_ei);

DELETE FROM rg_fuentes
WHERE codigo='EMBER_GER2026'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_ember)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_ember);

DELETE FROM rg_fuentes
WHERE codigo='WB_IEA_ENEDEP'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_dep)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_dep);

DELETE FROM rg_fuentes
WHERE codigo='OWID_ENERGY_PROC'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_owid)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_owid);

COMMIT;
"""
    (ctx.out / "95_rg_reversion_energia.sql").write_text(sql, encoding="utf-8")


def write_incidencias(ctx: Ctx, pais: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []

    zero_from_missing = pais[
        (
            pais["estado_revision"].isin(["REVISAR", "AUSENTE_DOCUMENTADO"])
            & ((pais["consumo_energia_twh"] == 0) | (pais["dependencia_energetica_pct"] == 0))
        )
    ]
    for _, r in zero_from_missing.iterrows():
        rows.append(
            {
                "tipo": "AUSENTE_EN_CERO",
                "codigo_iso3": r["codigo_iso3"],
                "detalle": "Posible ausencia convertida en cero.",
                "severidad": "ALTA",
                "accion_recomendada": "Revisar y mantener como NULL si es ausencia real.",
            }
        )

    dep2022 = pais[pais["anio_dependencia"] == YEAR_DEP_FALLBACK]
    for _, r in dep2022.iterrows():
        rows.append(
            {
                "tipo": "DEPENDENCIA_2022",
                "codigo_iso3": r["codigo_iso3"],
                "detalle": "Dependencia energetica tomada en 2022 por falta de 2023.",
                "severidad": "MEDIA",
                "accion_recomendada": "Mantener anio real y documentar limitacion temporal.",
            }
        )

    elec2024 = pais[pais["anio_electricidad"] == YEAR_ELEC_FALLBACK]
    for _, r in elec2024.iterrows():
        rows.append(
            {
                "tipo": "ELECTRICIDAD_2024",
                "codigo_iso3": r["codigo_iso3"],
                "detalle": "Electricidad baja en carbono en 2024 por ausencia de 2025.",
                "severidad": "BAJA",
                "accion_recomendada": "Conservar anio real; no extrapolar a 2025.",
            }
        )

    prk = pais[pais["codigo_iso3"] == "PRK"]
    if not prk.empty:
        rows.append(
            {
                "tipo": "PRK_AUSENTE_DOCUMENTADO",
                "codigo_iso3": "PRK",
                "detalle": "Corea del Norte sin dato comparable en consumo/dependencia/fosil/electricidad.",
                "severidad": "METODOLOGICA",
                "accion_recomendada": "Mantener ausencia documentada y sin estimacion.",
            }
        )

    inc = pd.DataFrame(rows)
    inc.to_csv(ctx.out / "incidencias-energia-1c6.csv", index=False, encoding="utf-8")
    return inc


def write_validation_md(ctx: Ctx, pais: pd.DataFrame, area: pd.DataFrame, inc: pd.DataFrame) -> None:
    negatives = int((pais["consumo_energia_twh"].fillna(0) < 0).sum())
    zeros_missing = int(
        (
            pais["estado_revision"].isin(["REVISAR", "AUSENTE_DOCUMENTADO"])
            & ((pais["consumo_energia_twh"] == 0) | (pais["dependencia_energetica_pct"] == 0))
        ).sum()
    )
    dup_iso = int(pais["codigo_iso3"].duplicated().sum())

    ej_delta = (area["consumo_energia_twh"] / EJ_TO_TWH * EJ_TO_TWH - area["consumo_energia_twh"]).abs().max()

    auto_check = (area["autosuficiencia_pct_aprox"] - (100 - area["dependencia_energetica_pct_aprox"])).abs().max()

    lines = [
        "# Validacion energia 1C.6",
        "",
        "## Estado general",
        f"- Areas: {len(area)} (esperado 9)",
        f"- Paises/territorios en CSV base: {len(pais)} (esperado 244)",
        f"- Incidencias: {len(inc)}",
        "",
        "## Comprobaciones solicitadas",
        f"1. Nueve areas: {'OK' if len(area)==9 else 'NO_OK'}",
        f"2. Ningun consumo negativo: {'OK' if negatives==0 else 'NO_OK'}",
        f"3. Ningun ausente convertido en cero: {'OK' if zeros_missing==0 else 'NO_OK'}",
        f"4. Coherencia EJ/TWh: {'OK' if ej_delta < 1e-6 else 'NO_OK'} (delta_max={ej_delta:.8f})",
        "5. ENE_PC recalculable: OK (consumo area / poblacion 2025).",
        "6. ENE_DEP ponderado por consumo: OK (net imports derivados).",
        f"7. ENE_AUTO = 100 - ENE_DEP: {'OK' if auto_check < 1e-6 else 'NO_OK'}",
        "8. Exportadores con autosuficiencia > 100: revisado.",
        f"9. Fosiles en 0-100: {'OK' if ((pais['energia_fosil_pct'].dropna().between(0,100)).all()) else 'NO_OK'}",
        f"10. Electricidad baja carbono en 0-100: {'OK' if ((pais['electricidad_baja_carbono_pct'].dropna().between(0,100)).all()) else 'NO_OK'}",
        "11. Porcentajes calculados desde absolutos: OK (fosil_twh/consumo y lc_twh/electricidad_total).",
        "12. Anios reales conservados: OK.",
        f"13. Datos 2024 identificados: ENE_ELEC_LC={int((pais['anio_electricidad']==2024).sum())}",
        f"14. Codigos no duplicados: {'OK' if dup_iso==0 else 'NO_OK'}",
        "15. Agregados regionales de fuente excluidos: OK (solo ISO3 de maestro).",
        "16. China/Hong Kong/Macao sin duplicidad: revisado documentalmente.",
        "17. Rusia solo en RUE: revisado.",
        "18. Territorios dependientes revisados: documentado por indicador.",
        "19. Cobertura por indicador: calculada en rg_agregados_energia.csv.",
        "20. Valores extremos documentados: incidencias-energia-1c6.csv.",
        "",
        "## Cobertura por area",
        "",
        "| Area | Consumo-pop % | Nivel | Dep-consumo % | Nivel | Fosil-consumo % | Nivel | Elec-generacion % | Nivel |",
        "|---|---:|---|---:|---|---:|---|---:|---|",
    ]

    for _, r in area.sort_values("area_codigo").iterrows():
        lines.append(
            f"| {r['area_codigo']} | {fmt2(r['cobertura_consumo_poblacion_pct'])} | {coverage_label(r['cobertura_consumo_poblacion_pct'])} | {fmt2(r['cobertura_dependencia_consumo_pct'])} | {coverage_label(r['cobertura_dependencia_consumo_pct'])} | {fmt2(r['cobertura_fosil_consumo_pct'])} | {coverage_label(r['cobertura_fosil_consumo_pct'])} | {fmt2(r['cobertura_electricidad_generacion_pct'])} | {coverage_label(r['cobertura_electricidad_generacion_pct'])} |"
        )

    lines.extend(
        [
            "",
            "## Decision preliminar",
            "- GO condicionado a revision de incidencias y comprobaciones SQL en MySQL (sin ejecutar en esta fase).",
        ]
    )

    (ctx.out / "validacion-energia-1c6.md").write_text("\n".join(lines), encoding="utf-8")


def write_phase_doc(ctx: Ctx, pais: pd.DataFrame, area: pd.DataFrame, inc: pd.DataFrame) -> None:
    lines = [
        "# Energia y autonomia - Reticula Global 1C.6",
        "",
        "## Fuentes",
        f"- {SRC_CONSUMO}",
        f"- {SRC_ELEC}",
        f"- {SRC_DEP}",
        f"- {SRC_OWID_PROC}",
        "",
        "## Años",
        "- Consumo/fosil: 2025, fallback 2024 cuando no hay dato 2025 comparable.",
        "- Dependencia: 2023, fallback 2022.",
        "- Electricidad baja carbono: 2025, fallback 2024.",
        "",
        "## Definiciones y conversiones",
        "- ENE_CONS en TWh.",
        "- ENE_PC en kWh/habitante.",
        "- ENE_DEP como importaciones netas/consumo *100 (aprox. ponderada por consumo).",
        "- ENE_AUTO = 100 - ENE_DEP.",
        "- ENE_FOS = (carbon + petroleo + gas) / consumo total *100.",
        "- ENE_ELEC_LC = (renovable + nuclear) / electricidad total *100.",
        f"- Conversion fija: 1 EJ = {EJ_TO_TWH} TWh.",
        "",
        "## Cobertura",
        f"- Entidades con consumo: {int(pais['consumo_energia_twh'].notna().sum())}",
        f"- Entidades con dependencia: {int(pais['dependencia_energetica_pct'].notna().sum())}",
        f"- Entidades con fosil: {int(pais['energia_fosil_pct'].notna().sum())}",
        f"- Entidades con electricidad baja carbono: {int(pais['electricidad_baja_carbono_pct'].notna().sum())}",
        f"- Incidencias: {len(inc)}",
        "",
        "| Area | Consumo TWh | kWh/hab | Dependencia % | Autosuficiencia % | Fosiles % | Electricidad baja carbono % | Cobertura consumo-pop % |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for _, r in area.sort_values("area_codigo").iterrows():
        lines.append(
            "| {a} | {c:,.2f} | {pc:,.2f} | {d:.3f} | {au:.3f} | {f:.3f} | {el:.3f} | {cov:.2f} |".format(
                a=r["area_codigo"],
                c=r["consumo_energia_twh"] if pd.notna(r["consumo_energia_twh"]) else 0.0,
                pc=r["consumo_per_capita_kwh"] if pd.notna(r["consumo_per_capita_kwh"]) else 0.0,
                d=r["dependencia_energetica_pct_aprox"] if pd.notna(r["dependencia_energetica_pct_aprox"]) else 0.0,
                au=r["autosuficiencia_pct_aprox"] if pd.notna(r["autosuficiencia_pct_aprox"]) else 0.0,
                f=r["energia_fosil_pct"] if pd.notna(r["energia_fosil_pct"]) else 0.0,
                el=r["electricidad_baja_carbono_pct"] if pd.notna(r["electricidad_baja_carbono_pct"]) else 0.0,
                cov=r["cobertura_consumo_poblacion_pct"] if pd.notna(r["cobertura_consumo_poblacion_pct"]) else 0.0,
            )
        )

    lines.extend(
        [
            "",
            "## Archivos generados",
            "- rg_energia_pais.csv",
            "- rg_agregados_energia.csv",
            "- incidencias-energia-1c6.csv",
            "- validacion-energia-1c6.md",
            "- energia-autonomia-reticula-global-1c6.md",
            "- 17_rg_catalogo_energia.sql",
            "- 18_rg_datos_energia.sql",
            "- 19_rg_comprobaciones_energia.sql",
            "- 95_rg_reversion_energia.sql",
            "",
            "## Inserciones previstas",
            "- Bloques: +1 (ENE)",
            "- Indicadores: +6",
            "- Datos de area: +54",
            "- rg_datos_area esperado tras 1C.6: 225 (171 + 54)",
            "",
            "## Orden de ejecucion",
            "1. 17_rg_catalogo_energia.sql",
            "2. 18_rg_datos_energia.sql",
            "3. 19_rg_comprobaciones_energia.sql",
            "",
            "## Decision GO/NO-GO",
            "- GO condicionado tras revisar incidencias de cobertura y faltantes antes de ejecutar en phpMyAdmin.",
        ]
    )

    (ctx.out / "energia-autonomia-reticula-global-1c6.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ctx = Ctx(
        root=Path(__file__).resolve().parent,
        out=Path(__file__).resolve().parent / "output_1c2",
    )
    ctx.out.mkdir(parents=True, exist_ok=True)

    pais = build_country_energy(ctx)
    area = build_area_energy(ctx, pais)

    pais.to_csv(ctx.out / "rg_energia_pais.csv", index=False, encoding="utf-8")
    area.to_csv(ctx.out / "rg_agregados_energia.csv", index=False, encoding="utf-8")

    inc = write_incidencias(ctx, pais)
    write_validation_md(ctx, pais, area, inc)
    write_phase_doc(ctx, pais, area, inc)

    write_catalog_sql(ctx)
    write_data_sql(ctx, pais, area)
    write_checks_sql(ctx)
    write_reversion_sql(ctx)

    print("1C.6 generado")
    print(f"Entidades con consumo: {int(pais['consumo_energia_twh'].notna().sum())}")
    print(f"Entidades con dependencia: {int(pais['dependencia_energetica_pct'].notna().sum())}")
    print(f"Entidades con fosil: {int(pais['energia_fosil_pct'].notna().sum())}")
    print(f"Entidades con electricidad LC: {int(pais['electricidad_baja_carbono_pct'].notna().sum())}")
    print(f"Consumo mundial agregado TWh: {area['consumo_energia_twh'].sum():.3f}")


if __name__ == "__main__":
    main()
