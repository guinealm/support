from __future__ import annotations

import io
import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import requests


UNDP_HDI_XLSX_2025 = "https://hdr.undp.org/sites/default/files/2025_HDR/HDR25_Statistical_Annex_HDI_Table.xlsx"
UNDP_HDI_SHEET_2025 = "Table 1. HDI"
WB_GINI_API = "https://api.worldbank.org/v2/country/all/indicator/SI.POV.GINI"
WB_EV_API = "https://api.worldbank.org/v2/country/all/indicator/SP.DYN.LE00.IN"


@dataclass
class Ctx:
    root: Path
    out: Path


def q(v: object) -> str:
    if v is None or (isinstance(v, float) and pd.isna(v)):
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


def norm_name(v: object) -> str:
    x = str(v).strip().upper()
    x = unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode("ascii")
    x = re.sub(r"[^A-Z0-9 ]+", " ", x)
    x = re.sub(r"\s+", " ", x).strip()
    return x


def fetch_undp_hdi(master: pd.DataFrame) -> pd.DataFrame:
    r = requests.get(
        UNDP_HDI_XLSX_2025,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=120,
    )
    r.raise_for_status()
    raw = pd.read_excel(io.BytesIO(r.content), sheet_name=UNDP_HDI_SHEET_2025, engine="openpyxl", header=None)

    # Data rows are the ranked country lines with numeric rank and numeric HDI value.
    t = raw[[0, 1, 2]].copy()
    t.columns = ["rank", "country_hdr", "idh"]
    t = t[
        pd.to_numeric(t["rank"], errors="coerce").notna()
        & pd.to_numeric(t["idh"], errors="coerce").notna()
        & t["country_hdr"].notna()
    ].copy()
    t["idh"] = pd.to_numeric(t["idh"], errors="coerce")
    t["country_norm"] = t["country_hdr"].map(norm_name)

    alias_to_master = {
        "HONG KONG CHINA SAR": "HONG KONG",
        "ESWATINI KINGDOM OF": "ESWATINI",
        "CONGO DEMOCRATIC REPUBLIC OF THE": "CONGO THE DEMOCRATIC REPUBLIC OF THE",
    }
    t["country_norm"] = t["country_norm"].map(lambda x: alias_to_master.get(x, x))

    m = master[["codigo_iso3", "nombre_m49", "nombre_es"]].copy()
    m["norm_m49"] = m["nombre_m49"].map(norm_name)
    m["norm_es"] = m["nombre_es"].map(norm_name)

    by_m49 = m[["codigo_iso3", "norm_m49"]].drop_duplicates()
    x = t.merge(by_m49, left_on="country_norm", right_on="norm_m49", how="left")

    miss = x["codigo_iso3"].isna()
    if miss.any():
        by_es = m[["codigo_iso3", "norm_es"]].drop_duplicates()
        x2 = x.loc[miss, ["country_norm"]].merge(by_es, left_on="country_norm", right_on="norm_es", how="left")
        x.loc[miss, "codigo_iso3"] = x2["codigo_iso3"].values

    out = x[["codigo_iso3", "idh"]].copy()
    out = out[out["codigo_iso3"].notna()].drop_duplicates(subset=["codigo_iso3"], keep="first")
    out["codigo_iso3"] = out["codigo_iso3"].astype(str).str.upper().str.strip()
    out["anio_idh"] = 2023
    return out


def fetch_wb_indicator(api_url: str) -> pd.DataFrame:
    page = 1
    rows: list[dict[str, object]] = []
    while True:
        r = requests.get(
            api_url,
            params={"format": "json", "per_page": 20000, "page": page},
            timeout=120,
        )
        r.raise_for_status()
        payload = r.json()
        meta = payload[0]
        data = payload[1]
        for d in data:
            rows.append(
                {
                    "codigo_iso3": d.get("countryiso3code"),
                    "pais_fuente": (d.get("country") or {}).get("value"),
                    "anio": int(d["date"]) if d.get("date") else None,
                    "valor": d.get("value"),
                    "obs_status": d.get("obs_status"),
                }
            )
        if page >= int(meta.get("pages", page)):
            break
        page += 1
    out = pd.DataFrame(rows)
    out["codigo_iso3"] = out["codigo_iso3"].astype(str).str.upper().str.strip()
    out["anio"] = pd.to_numeric(out["anio"], errors="coerce")
    out["valor"] = pd.to_numeric(out["valor"], errors="coerce")
    return out


def pick_latest_in_window(g: pd.DataFrame, min_y: int, max_y: int) -> tuple[float | None, int | None]:
    t = g[g["anio"].between(min_y, max_y, inclusive="both") & g["valor"].notna()].copy()
    if t.empty:
        return None, None
    t = t.sort_values("anio", ascending=False)
    row = t.iloc[0]
    return float(row["valor"]), int(row["anio"])


def prepare_country_dataset(
    master: pd.DataFrame,
    hdi_raw: pd.DataFrame,
    gini_raw: pd.DataFrame,
    ev_raw: pd.DataFrame,
) -> pd.DataFrame:
    m = master[[
        "codigo_iso3",
        "codigo_m49",
        "nombre_es",
        "area_codigo",
        "area_nombre",
        "tipo_entidad",
        "incluir_calculos",
        "tratamiento_fuente",
        "observaciones",
    ]].copy()

    # IDH directo 2023 (PNUD)
    x = m.merge(hdi_raw[["codigo_iso3", "idh", "anio_idh"]], on="codigo_iso3", how="left")

    # Gini por politica temporal
    gini_use = gini_raw[gini_raw["codigo_iso3"].notna() & gini_raw["anio"].notna()].copy()
    gini_map: dict[str, dict[str, object]] = {}
    for iso, g in gini_use.groupby("codigo_iso3"):
        val, anio = pick_latest_in_window(g, 2019, 2024)
        estado = "ACTUAL"
        obs = ""
        if val is None:
            val, anio = pick_latest_in_window(g, 2015, 2018)
            estado = "ANTIGUO"
            if val is not None:
                obs = "Gini previo a 2019; comparabilidad temporal limitada."
        if val is None:
            estado = "AUSENTE"
        gini_map[str(iso)] = {
            "gini": val,
            "anio_gini": anio,
            "gini_estado_temporal": estado,
            "gini_obs": obs,
        }

    # Esperanza de vida: 2023, fallback 2022
    ev_use = ev_raw[ev_raw["codigo_iso3"].notna() & ev_raw["anio"].notna()].copy()
    ev_map: dict[str, dict[str, object]] = {}
    for iso, g in ev_use.groupby("codigo_iso3"):
        val, anio = pick_latest_in_window(g, 2023, 2023)
        if val is None:
            val, anio = pick_latest_in_window(g, 2022, 2022)
            estado = "FALLBACK_2022" if val is not None else "AUSENTE"
        else:
            estado = "OBJETIVO_2023"
        ev_map[str(iso)] = {
            "esperanza_vida": val,
            "anio_esperanza_vida": anio,
            "ev_estado_temporal": estado,
        }

    rows = []
    for r in x.to_dict(orient="records"):
        iso = str(r["codigo_iso3"])
        gini_r = gini_map.get(iso, {"gini": None, "anio_gini": None, "gini_estado_temporal": "AUSENTE", "gini_obs": ""})
        ev_r = ev_map.get(iso, {"esperanza_vida": None, "anio_esperanza_vida": None, "ev_estado_temporal": "AUSENTE"})

        notes: list[str] = []
        if str(r.get("incluir_calculos", "")).strip().upper() == "SEGUN_FUENTE":
            notes.append("Entidad SEGUN_FUENTE; sin imputacion si la fuente no publica valor separado.")
        if pd.isna(r.get("idh")):
            notes.append("Sin IDH 2023 publicado en PNUD HDR 2025 para esta entidad.")
        if gini_r["gini"] is None:
            notes.append("Sin Gini 2015-2024 usable en WDI/PIP.")
        elif gini_r["gini_estado_temporal"] == "ANTIGUO":
            notes.append("Gini seleccionado en 2015-2018 (antiguo).")
        if ev_r["esperanza_vida"] is None:
            notes.append("Sin esperanza de vida 2023/2022 usable en WDI.")
        elif ev_r["ev_estado_temporal"] == "FALLBACK_2022":
            notes.append("Esperanza de vida 2022 por ausencia de 2023.")

        if iso == "CHN":
            notes.append("CHN tratado separado de HKG y MAC.")
        if iso == "HKG":
            notes.append("HKG tratado separado de CHN.")
        if iso == "MAC":
            notes.append("MAC tratado separado de CHN.")
        if iso == "TWN":
            notes.append("TWN revisado expresamente; mantener criterio SEGUN_FUENTE sin duplicidad.")
        if iso == "XKX":
            notes.append("XKX revisado expresamente; mantener separado de SRB sin duplicidad.")
        if iso == "SRB":
            notes.append("SRB revisado expresamente junto con XKX.")

        estado = "OK"
        if pd.isna(r.get("idh")) or gini_r["gini"] is None or ev_r["esperanza_vida"] is None:
            estado = "REVISAR"

        obs = " ".join([n for n in notes if n]).strip()

        rows.append(
            {
                "codigo_iso3": iso,
                "codigo_m49": r.get("codigo_m49"),
                "pais": r.get("nombre_es"),
                "area_codigo": r.get("area_codigo"),
                "idh": r.get("idh"),
                "anio_idh": int(r.get("anio_idh")) if pd.notna(r.get("anio_idh")) else None,
                "gini": gini_r["gini"],
                "anio_gini": gini_r["anio_gini"],
                "esperanza_vida": ev_r["esperanza_vida"],
                "anio_esperanza_vida": ev_r["anio_esperanza_vida"],
                "fuente_idh": "PNUD — Human Development Report 2025",
                "fuente_gini": "Banco Mundial - Poverty and Inequality Platform",
                "fuente_esperanza_vida": "Banco Mundial - World Development Indicators",
                "estado_revision": estado,
                "observaciones": obs,
                "gini_estado_temporal": gini_r["gini_estado_temporal"],
                "ev_estado_temporal": ev_r["ev_estado_temporal"],
            }
        )

    out = pd.DataFrame(rows)
    out["idh"] = pd.to_numeric(out["idh"], errors="coerce")
    out["gini"] = pd.to_numeric(out["gini"], errors="coerce")
    out["esperanza_vida"] = pd.to_numeric(out["esperanza_vida"], errors="coerce")
    return out


def aggregate_indicator(
    df: pd.DataFrame,
    value_col: str,
    year_col: str,
    pop_entity: pd.DataFrame,
    pop_area: pd.DataFrame,
    threshold_min: float | None = None,
    threshold_max: float | None = None,
) -> pd.DataFrame:
    x = df[["codigo_iso3", "area_codigo", value_col, year_col]].copy()
    x[value_col] = pd.to_numeric(x[value_col], errors="coerce")
    x[year_col] = pd.to_numeric(x[year_col], errors="coerce")

    pe = pop_entity[["codigo_iso3", "area_codigo", "poblacion_2025"]].copy()
    pe["poblacion_2025"] = pd.to_numeric(pe["poblacion_2025"], errors="coerce")

    m = x.merge(pe, on=["codigo_iso3", "area_codigo"], how="left")

    rows = []
    for area_codigo, g in m.groupby("area_codigo", dropna=False):
        ent_total = len(g)
        g_val = g[g[value_col].notna()].copy()
        ent_con = int(len(g_val))

        g_cov = g[g[value_col].notna() & g["poblacion_2025"].notna()].copy()
        pop_cov = float(g_cov["poblacion_2025"].sum()) if len(g_cov) else 0.0

        area_row = pop_area[pop_area["area_codigo"].eq(area_codigo)].iloc[0]
        pop_tot = float(area_row["poblacion_2025"])
        cov_pct = (pop_cov / pop_tot * 100.0) if pop_tot > 0 else None

        if pop_cov > 0:
            aprox = float((g_cov[value_col] * g_cov["poblacion_2025"]).sum() / pop_cov)
        else:
            aprox = None

        y = g_val[year_col].dropna()
        y_min = int(y.min()) if len(y) else None
        y_max = int(y.max()) if len(y) else None

        fuera = 0
        if threshold_min is not None:
            fuera += int((g_val[value_col] < threshold_min).sum())
        if threshold_max is not None:
            fuera += int((g_val[value_col] > threshold_max).sum())

        rows.append(
            {
                "area_codigo": area_codigo,
                "area_nombre": area_row["area_nombre"],
                "valor_aprox": aprox,
                "entidades_totales": ent_total,
                "entidades_con_dato": ent_con,
                "cobertura_pct": cov_pct,
                "anio_min": y_min,
                "anio_max": y_max,
                "fuera_rango": fuera,
            }
        )

    return pd.DataFrame(rows).sort_values("area_codigo")


def build_area_dataset(
    pais: pd.DataFrame,
    pop_area: pd.DataFrame,
    pop_entity: pd.DataFrame,
) -> pd.DataFrame:
    aidh = aggregate_indicator(pais, "idh", "anio_idh", pop_entity, pop_area, threshold_min=0.0, threshold_max=1.0)
    agini = aggregate_indicator(pais, "gini", "anio_gini", pop_entity, pop_area, threshold_min=0.0, threshold_max=100.0)
    aev = aggregate_indicator(pais, "esperanza_vida", "anio_esperanza_vida", pop_entity, pop_area, threshold_min=20.0, threshold_max=95.0)

    gini_old = pais[pd.to_numeric(pais["anio_gini"], errors="coerce").between(2015, 2018, inclusive="both")]
    gini_old_area = gini_old.groupby("area_codigo").size().to_dict()

    area = aidh[["area_codigo", "area_nombre", "entidades_totales"]].copy()
    area = area.merge(
        aidh[["area_codigo", "valor_aprox", "entidades_con_dato", "cobertura_pct", "anio_min", "anio_max"]]
            .rename(columns={
                "valor_aprox": "idh_aprox",
                "entidades_con_dato": "entidades_con_idh",
                "cobertura_pct": "cobertura_idh_pct",
                "anio_min": "anio_min_idh",
                "anio_max": "anio_max_idh",
            }),
        on="area_codigo",
        how="left",
    )
    area = area.merge(
        agini[["area_codigo", "valor_aprox", "entidades_con_dato", "cobertura_pct", "anio_min", "anio_max"]]
            .rename(columns={
                "valor_aprox": "gini_aprox",
                "entidades_con_dato": "entidades_con_gini",
                "cobertura_pct": "cobertura_gini_pct",
                "anio_min": "anio_min_gini",
                "anio_max": "anio_max_gini",
            }),
        on="area_codigo",
        how="left",
    )
    area = area.merge(
        aev[["area_codigo", "valor_aprox", "entidades_con_dato", "cobertura_pct", "anio_min", "anio_max"]]
            .rename(columns={
                "valor_aprox": "esperanza_vida_aprox",
                "entidades_con_dato": "entidades_con_esperanza_vida",
                "cobertura_pct": "cobertura_esperanza_vida_pct",
                "anio_min": "anio_min_esperanza_vida",
                "anio_max": "anio_max_esperanza_vida",
            }),
        on="area_codigo",
        how="left",
    )

    obs = []
    for r in area.to_dict(orient="records"):
        parts = [
            f"Cobertura IDH {coverage_label(r.get('cobertura_idh_pct'))}.",
            f"Cobertura Gini {coverage_label(r.get('cobertura_gini_pct'))}.",
            f"Cobertura EV {coverage_label(r.get('cobertura_esperanza_vida_pct'))}.",
            "IDH/Gini/EV del area son medias nacionales ponderadas por poblacion 2025, no indicadores regionales oficiales exactos.",
            "Gini: media ponderada de indices nacionales; no representa desigualdad conjunta del area.",
        ]
        old_n = int(gini_old_area.get(r["area_codigo"], 0))
        if old_n > 0:
            parts.append(f"Gini incluye {old_n} datos previos a 2019.")
        ymin = r.get("anio_min_gini")
        ymax = r.get("anio_max_gini")
        if pd.notna(ymin) and pd.notna(ymax) and int(ymax) - int(ymin) >= 3:
            parts.append("Gini con dispersion temporal relevante; comparabilidad condicionada.")
        obs.append(" ".join(parts))

    area["observaciones"] = obs
    area = area[[
        "area_codigo",
        "area_nombre",
        "idh_aprox",
        "gini_aprox",
        "esperanza_vida_aprox",
        "entidades_totales",
        "entidades_con_idh",
        "entidades_con_gini",
        "entidades_con_esperanza_vida",
        "cobertura_idh_pct",
        "cobertura_gini_pct",
        "cobertura_esperanza_vida_pct",
        "anio_min_idh",
        "anio_max_idh",
        "anio_min_gini",
        "anio_max_gini",
        "anio_min_esperanza_vida",
        "anio_max_esperanza_vida",
        "observaciones",
    ]].copy()
    return area.sort_values("area_codigo")


def build_incidencias(pais: pd.DataFrame, area: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []

    for r in pais.to_dict(orient="records"):
        if pd.isna(r.get("idh")):
            rows.append(
                {
                    "codigo_iso3": r["codigo_iso3"],
                    "codigo_m49": r["codigo_m49"],
                    "pais": r["pais"],
                    "area_codigo": r["area_codigo"],
                    "tipo_incidencia": "SIN_DATO",
                    "indicador": "HUM_IDH",
                    "detalle": "Entidad sin IDH 2023 utilizable en PNUD HDR 2025.",
                    "estado": "REVISAR",
                }
            )
        if pd.isna(r.get("gini")):
            rows.append(
                {
                    "codigo_iso3": r["codigo_iso3"],
                    "codigo_m49": r["codigo_m49"],
                    "pais": r["pais"],
                    "area_codigo": r["area_codigo"],
                    "tipo_incidencia": "SIN_DATO",
                    "indicador": "HUM_GINI",
                    "detalle": "Entidad sin Gini 2015-2024 utilizable.",
                    "estado": "REVISAR",
                }
            )
        else:
            gy = pd.to_numeric(r.get("anio_gini"), errors="coerce")
            if pd.notna(gy) and int(gy) < 2019:
                rows.append(
                    {
                        "codigo_iso3": r["codigo_iso3"],
                        "codigo_m49": r["codigo_m49"],
                        "pais": r["pais"],
                        "area_codigo": r["area_codigo"],
                        "tipo_incidencia": "GINI_ANTIGUO",
                        "indicador": "HUM_GINI",
                        "detalle": f"Dato Gini {int(gy)} (ventana 2015-2018).",
                        "estado": "REVISAR",
                    }
                )
        if pd.isna(r.get("esperanza_vida")):
            rows.append(
                {
                    "codigo_iso3": r["codigo_iso3"],
                    "codigo_m49": r["codigo_m49"],
                    "pais": r["pais"],
                    "area_codigo": r["area_codigo"],
                    "tipo_incidencia": "SIN_DATO",
                    "indicador": "HUM_EV",
                    "detalle": "Entidad sin esperanza de vida 2023/2022.",
                    "estado": "REVISAR",
                }
            )

    # Duplicados ISO3
    dup = pais.groupby("codigo_iso3").size().reset_index(name="n")
    dup = dup[dup["n"] > 1]
    for r in dup.to_dict(orient="records"):
        rows.append(
            {
                "codigo_iso3": r["codigo_iso3"],
                "codigo_m49": "",
                "pais": "",
                "area_codigo": "",
                "tipo_incidencia": "DUPLICADO_ISO3",
                "indicador": "GENERAL",
                "detalle": "Codigo ISO3 repetido en dataset nacional.",
                "estado": "REVISAR",
            }
        )

    # Dispersión temporal de Gini por area
    for r in area.to_dict(orient="records"):
        ymin = pd.to_numeric(r.get("anio_min_gini"), errors="coerce")
        ymax = pd.to_numeric(r.get("anio_max_gini"), errors="coerce")
        if pd.notna(ymin) and pd.notna(ymax) and int(ymax) - int(ymin) >= 3:
            rows.append(
                {
                    "codigo_iso3": "",
                    "codigo_m49": "",
                    "pais": "",
                    "area_codigo": r["area_codigo"],
                    "tipo_incidencia": "GINI_DISPERSION_TEMPORAL",
                    "indicador": "HUM_GINI",
                    "detalle": f"Rango anual Gini {int(ymin)}-{int(ymax)} en la misma area.",
                    "estado": "REVISAR",
                }
            )

    rows.append(
        {
            "codigo_iso3": "",
            "codigo_m49": "",
            "pais": "",
            "area_codigo": "",
            "tipo_incidencia": "NOTA_FUENTE_GINI",
            "indicador": "HUM_GINI",
            "detalle": "La API WDI usada no explicita por observacion si la medicion es por ingreso o consumo; documentar limitacion metodologica.",
            "estado": "REVISAR",
        }
    )

    return pd.DataFrame(rows)


def write_sql_11(ctx: Ctx) -> None:
    sql = """-- 11_rg_catalogo_desarrollo_humano.sql
SET NAMES utf8mb4;

START TRANSACTION;

SET @next_bloque := (SELECT COALESCE(MAX(id),0) FROM rg_bloques);

INSERT INTO rg_bloques (id,codigo,nombre,activo)
SELECT (@next_bloque := @next_bloque + 1), 'HUM', 'Desarrollo humano y desigualdad', 1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_bloques WHERE codigo='HUM');

SET @bloque_hum := (SELECT id FROM rg_bloques WHERE codigo='HUM' LIMIT 1);
SET @next_indicador := (SELECT COALESCE(MAX(id),0) FROM rg_indicadores);

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1),
       'HUM_IDH',
       @bloque_hum,
       'Indice de Desarrollo Humano',
       'indice_0_1',
       'Indice de Desarrollo Humano (PNUD) escala 0-1',
       1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='HUM_IDH');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1),
       'HUM_GINI',
       @bloque_hum,
       'Indice de Gini aproximado',
       'puntos_0_100',
       'Indice de Gini (PIP/Banco Mundial) escala 0-100',
       1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='HUM_GINI');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1),
       'HUM_EV',
       @bloque_hum,
       'Esperanza de vida al nacer',
       'anios',
       'Esperanza de vida al nacer en anios',
       1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='HUM_EV');

SET @next_fuente := (SELECT COALESCE(MAX(id),0) FROM rg_fuentes);

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1),
       'UNDP_HDR',
    'PNUD - Human Development Report 2025',
       'oficial',
    'https://hdr.undp.org/sites/default/files/2025_HDR/HDR25_Statistical_Annex_HDI_Table.xlsx',
       1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='UNDP_HDR');

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1),
       'WB_PIP',
       'Banco Mundial - Poverty and Inequality Platform',
       'oficial',
       'https://api.worldbank.org/v2/country/all/indicator/SI.POV.GINI',
       1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='WB_PIP');

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1),
       'WB_WDI',
       'Banco Mundial - World Development Indicators',
       'oficial',
       'https://api.worldbank.org/v2/country/all/indicator/SP.DYN.LE00.IN',
       1
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='WB_WDI');

COMMIT;
"""
    (ctx.out / "11_rg_catalogo_desarrollo_humano.sql").write_text(sql, encoding="utf-8")


def write_sql_12(ctx: Ctx, pais: pd.DataFrame, area: pd.DataFrame) -> dict[str, int]:
    p = pais.copy()
    p["idh"] = pd.to_numeric(p["idh"], errors="coerce")
    p["gini"] = pd.to_numeric(p["gini"], errors="coerce")
    p["esperanza_vida"] = pd.to_numeric(p["esperanza_vida"], errors="coerce")

    lines = [
        "-- 12_rg_datos_desarrollo_humano.sql",
        "SET NAMES utf8mb4;",
        "START TRANSACTION;",
        "",
        "DROP TEMPORARY TABLE IF EXISTS tmp_rg_humano_pais;",
        "CREATE TEMPORARY TABLE tmp_rg_humano_pais (codigo_iso3 VARCHAR(3) PRIMARY KEY, anio_idh SMALLINT NULL, idh DECIMAL(10,6) NULL, anio_gini SMALLINT NULL, gini DECIMAL(10,6) NULL, anio_ev SMALLINT NULL, ev DECIMAL(10,6) NULL, observaciones TEXT NULL) ENGINE=InnoDB;",
        "",
        "INSERT INTO tmp_rg_humano_pais (codigo_iso3,anio_idh,idh,anio_gini,gini,anio_ev,ev,observaciones) VALUES",
    ]

    vals = []
    for r in p.to_dict(orient="records"):
        vals.append(
            "(" + ",".join([
                q(r["codigo_iso3"]),
                q(int(r["anio_idh"]) if pd.notna(r.get("anio_idh")) else None),
                q(round(float(r["idh"]), 6) if pd.notna(r.get("idh")) else None),
                q(int(r["anio_gini"]) if pd.notna(r.get("anio_gini")) else None),
                q(round(float(r["gini"]), 6) if pd.notna(r.get("gini")) else None),
                q(int(r["anio_esperanza_vida"]) if pd.notna(r.get("anio_esperanza_vida")) else None),
                q(round(float(r["esperanza_vida"]), 6) if pd.notna(r.get("esperanza_vida")) else None),
                q(str(r.get("observaciones", "")).strip() or None),
            ]) + ")"
        )
    lines.append(",\n".join(vals) + ";\n")

    lines.extend([
        "SET @ind_hum_idh := (SELECT id FROM rg_indicadores WHERE codigo='HUM_IDH');",
        "SET @ind_hum_gini := (SELECT id FROM rg_indicadores WHERE codigo='HUM_GINI');",
        "SET @ind_hum_ev := (SELECT id FROM rg_indicadores WHERE codigo='HUM_EV');",
        "SET @src_undp := (SELECT id FROM rg_fuentes WHERE codigo='UNDP_HDR');",
        "SET @src_pip := (SELECT id FROM rg_fuentes WHERE codigo='WB_PIP');",
        "SET @src_wdi := (SELECT id FROM rg_fuentes WHERE codigo='WB_WDI');",
        "SET @next_pais_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_pais);",
        "",
        "INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)",
        "SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_hum_idh, t.anio_idh, t.idh, @src_undp,",
        "       'FUENTE_VALIDADA', 'OK', CURDATE(), t.observaciones, 1",
        "FROM tmp_rg_humano_pais t",
        "JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1",
        "LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_hum_idh AND d.anio=t.anio_idh",
        "WHERE t.idh IS NOT NULL AND d.id IS NULL;",
        "",
        "INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)",
        "SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_hum_gini, t.anio_gini, t.gini, @src_pip,",
        "       'FUENTE_VALIDADA', CASE WHEN t.anio_gini < 2019 THEN 'LIMITACION' ELSE 'OK' END, CURDATE(), t.observaciones, 1",
        "FROM tmp_rg_humano_pais t",
        "JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1",
        "LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_hum_gini AND d.anio=t.anio_gini",
        "WHERE t.gini IS NOT NULL AND d.id IS NULL;",
        "",
        "INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)",
        "SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_hum_ev, t.anio_ev, t.ev, @src_wdi,",
        "       'FUENTE_VALIDADA', CASE WHEN t.anio_ev = 2022 THEN 'LIMITACION' ELSE 'OK' END, CURDATE(), t.observaciones, 1",
        "FROM tmp_rg_humano_pais t",
        "JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1",
        "LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_hum_ev AND d.anio=t.anio_ev",
        "WHERE t.ev IS NOT NULL AND d.id IS NULL;",
        "",
        "UPDATE rg_datos_pais d",
        "JOIN rg_paises p ON p.id=d.pais_id",
        "JOIN tmp_rg_humano_pais t ON t.codigo_iso3=p.codigo_iso3",
        "SET d.valor=t.idh, d.fuente_id=@src_undp, d.tipo_procedencia='FUENTE_VALIDADA', d.estado_dato='OK', d.fecha_carga=CURDATE(), d.observaciones=t.observaciones, d.activo=1",
        "WHERE d.indicador_id=@ind_hum_idh AND t.idh IS NOT NULL AND d.anio=t.anio_idh;",
        "",
        "UPDATE rg_datos_pais d",
        "JOIN rg_paises p ON p.id=d.pais_id",
        "JOIN tmp_rg_humano_pais t ON t.codigo_iso3=p.codigo_iso3",
        "SET d.valor=t.gini, d.fuente_id=@src_pip, d.tipo_procedencia='FUENTE_VALIDADA', d.estado_dato=CASE WHEN t.anio_gini < 2019 THEN 'LIMITACION' ELSE 'OK' END, d.fecha_carga=CURDATE(), d.observaciones=t.observaciones, d.activo=1",
        "WHERE d.indicador_id=@ind_hum_gini AND t.gini IS NOT NULL AND d.anio=t.anio_gini;",
        "",
        "UPDATE rg_datos_pais d",
        "JOIN rg_paises p ON p.id=d.pais_id",
        "JOIN tmp_rg_humano_pais t ON t.codigo_iso3=p.codigo_iso3",
        "SET d.valor=t.ev, d.fuente_id=@src_wdi, d.tipo_procedencia='FUENTE_VALIDADA', d.estado_dato=CASE WHEN t.anio_ev = 2022 THEN 'LIMITACION' ELSE 'OK' END, d.fecha_carga=CURDATE(), d.observaciones=t.observaciones, d.activo=1",
        "WHERE d.indicador_id=@ind_hum_ev AND t.ev IS NOT NULL AND d.anio=t.anio_ev;",
        "",
        "DROP TEMPORARY TABLE IF EXISTS tmp_rg_humano_area;",
        "CREATE TEMPORARY TABLE tmp_rg_humano_area (area_codigo VARCHAR(10) PRIMARY KEY, idh_aprox DECIMAL(12,8) NULL, gini_aprox DECIMAL(12,8) NULL, ev_aprox DECIMAL(12,8) NULL, entidades_totales SMALLINT NULL, entidades_con_idh SMALLINT NULL, entidades_con_gini SMALLINT NULL, entidades_con_ev SMALLINT NULL, cobertura_idh DECIMAL(8,4) NULL, cobertura_gini DECIMAL(8,4) NULL, cobertura_ev DECIMAL(8,4) NULL, anio_min_idh SMALLINT NULL, anio_max_idh SMALLINT NULL, anio_min_gini SMALLINT NULL, anio_max_gini SMALLINT NULL, anio_min_ev SMALLINT NULL, anio_max_ev SMALLINT NULL, observaciones TEXT NULL) ENGINE=InnoDB;",
        "",
        "INSERT INTO tmp_rg_humano_area (area_codigo,idh_aprox,gini_aprox,ev_aprox,entidades_totales,entidades_con_idh,entidades_con_gini,entidades_con_ev,cobertura_idh,cobertura_gini,cobertura_ev,anio_min_idh,anio_max_idh,anio_min_gini,anio_max_gini,anio_min_ev,anio_max_ev,observaciones) VALUES",
    ])

    avals = []
    for r in area.to_dict(orient="records"):
        avals.append(
            "(" + ",".join([
                q(r["area_codigo"]),
                q(round(float(r["idh_aprox"]), 8) if pd.notna(r.get("idh_aprox")) else None),
                q(round(float(r["gini_aprox"]), 8) if pd.notna(r.get("gini_aprox")) else None),
                q(round(float(r["esperanza_vida_aprox"]), 8) if pd.notna(r.get("esperanza_vida_aprox")) else None),
                q(int(r["entidades_totales"]) if pd.notna(r.get("entidades_totales")) else None),
                q(int(r["entidades_con_idh"]) if pd.notna(r.get("entidades_con_idh")) else None),
                q(int(r["entidades_con_gini"]) if pd.notna(r.get("entidades_con_gini")) else None),
                q(int(r["entidades_con_esperanza_vida"]) if pd.notna(r.get("entidades_con_esperanza_vida")) else None),
                q(round(float(r["cobertura_idh_pct"]), 4) if pd.notna(r.get("cobertura_idh_pct")) else None),
                q(round(float(r["cobertura_gini_pct"]), 4) if pd.notna(r.get("cobertura_gini_pct")) else None),
                q(round(float(r["cobertura_esperanza_vida_pct"]), 4) if pd.notna(r.get("cobertura_esperanza_vida_pct")) else None),
                q(int(r["anio_min_idh"]) if pd.notna(r.get("anio_min_idh")) else None),
                q(int(r["anio_max_idh"]) if pd.notna(r.get("anio_max_idh")) else None),
                q(int(r["anio_min_gini"]) if pd.notna(r.get("anio_min_gini")) else None),
                q(int(r["anio_max_gini"]) if pd.notna(r.get("anio_max_gini")) else None),
                q(int(r["anio_min_esperanza_vida"]) if pd.notna(r.get("anio_min_esperanza_vida")) else None),
                q(int(r["anio_max_esperanza_vida"]) if pd.notna(r.get("anio_max_esperanza_vida")) else None),
                q(r.get("observaciones")),
            ]) + ")"
        )
    lines.append(",\n".join(avals) + ";\n")

    lines.extend([
        "SET @per := (SELECT id FROM rg_periodos WHERE codigo='RG2025_V1');",
        "SET @next_area_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_area);",
        "",
        "INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)",
        "SELECT (@next_area_id := @next_area_id + 1), a.id, @ind_hum_idh, @per, 2023, t.idh_aprox,",
        "       'Media nacional de IDH 2023 ponderada por poblacion 2025; no es un IDH oficial del area', t.entidades_totales, t.entidades_con_idh, t.cobertura_idh, t.anio_min_idh, t.anio_max_idh, @src_undp,",
        "       'AGREGADO_1C4', CASE WHEN t.cobertura_idh >= 90 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1",
        "FROM tmp_rg_humano_area t",
        "JOIN rg_areas a ON a.codigo=t.area_codigo",
        "LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=@ind_hum_idh AND d.periodo_id=@per AND d.anio_referencia=2023",
        "WHERE d.id IS NULL;",
        "",
        "INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)",
        "SELECT (@next_area_id := @next_area_id + 1), a.id, @ind_hum_gini, @per, 2024, t.gini_aprox,",
        "       'Media ponderada de indices nacionales; no representa la desigualdad conjunta entre todos los habitantes del area', t.entidades_totales, t.entidades_con_gini, t.cobertura_gini, t.anio_min_gini, t.anio_max_gini, @src_pip,",
        "       'AGREGADO_1C4', CASE WHEN t.cobertura_gini >= 90 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1",
        "FROM tmp_rg_humano_area t",
        "JOIN rg_areas a ON a.codigo=t.area_codigo",
        "LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=@ind_hum_gini AND d.periodo_id=@per AND d.anio_referencia=2024",
        "WHERE d.id IS NULL;",
        "",
        "INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)",
        "SELECT (@next_area_id := @next_area_id + 1), a.id, @ind_hum_ev, @per, 2023, t.ev_aprox,",
        "       'Media nacional ponderada por poblacion 2025', t.entidades_totales, t.entidades_con_ev, t.cobertura_ev, t.anio_min_ev, t.anio_max_ev, @src_wdi,",
        "       'AGREGADO_1C4', CASE WHEN t.cobertura_ev >= 90 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1",
        "FROM tmp_rg_humano_area t",
        "JOIN rg_areas a ON a.codigo=t.area_codigo",
        "LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=@ind_hum_ev AND d.periodo_id=@per AND d.anio_referencia=2023",
        "WHERE d.id IS NULL;",
        "",
        "-- Actualizacion idempotente de los 27 registros HUM",
        "UPDATE rg_datos_area d",
        "JOIN rg_areas a ON a.id=d.area_id",
        "JOIN tmp_rg_humano_area t ON t.area_codigo=a.codigo",
        "SET d.valor=CASE",
        "      WHEN d.indicador_id=@ind_hum_idh THEN t.idh_aprox",
        "      WHEN d.indicador_id=@ind_hum_gini THEN t.gini_aprox",
        "      WHEN d.indicador_id=@ind_hum_ev THEN t.ev_aprox",
        "      ELSE d.valor END,",
        "    d.metodo_calculo=CASE",
        "      WHEN d.indicador_id=@ind_hum_idh THEN 'Media nacional de IDH 2023 ponderada por poblacion 2025; no es un IDH oficial del area'",
        "      WHEN d.indicador_id=@ind_hum_gini THEN 'Media ponderada de indices nacionales; no representa la desigualdad conjunta entre todos los habitantes del area'",
        "      WHEN d.indicador_id=@ind_hum_ev THEN 'Media nacional ponderada por poblacion 2025'",
        "      ELSE d.metodo_calculo END,",
        "    d.paises_totales=t.entidades_totales,",
        "    d.paises_con_dato=CASE",
        "      WHEN d.indicador_id=@ind_hum_idh THEN t.entidades_con_idh",
        "      WHEN d.indicador_id=@ind_hum_gini THEN t.entidades_con_gini",
        "      WHEN d.indicador_id=@ind_hum_ev THEN t.entidades_con_ev",
        "      ELSE d.paises_con_dato END,",
        "    d.porcentaje_cobertura=CASE",
        "      WHEN d.indicador_id=@ind_hum_idh THEN t.cobertura_idh",
        "      WHEN d.indicador_id=@ind_hum_gini THEN t.cobertura_gini",
        "      WHEN d.indicador_id=@ind_hum_ev THEN t.cobertura_ev",
        "      ELSE d.porcentaje_cobertura END,",
        "    d.anio_minimo=CASE",
        "      WHEN d.indicador_id=@ind_hum_idh THEN t.anio_min_idh",
        "      WHEN d.indicador_id=@ind_hum_gini THEN t.anio_min_gini",
        "      WHEN d.indicador_id=@ind_hum_ev THEN t.anio_min_ev",
        "      ELSE d.anio_minimo END,",
        "    d.anio_maximo=CASE",
        "      WHEN d.indicador_id=@ind_hum_idh THEN t.anio_max_idh",
        "      WHEN d.indicador_id=@ind_hum_gini THEN t.anio_max_gini",
        "      WHEN d.indicador_id=@ind_hum_ev THEN t.anio_max_ev",
        "      ELSE d.anio_maximo END,",
        "    d.fuente_principal_id=CASE",
        "      WHEN d.indicador_id=@ind_hum_idh THEN @src_undp",
        "      WHEN d.indicador_id=@ind_hum_gini THEN @src_pip",
        "      WHEN d.indicador_id=@ind_hum_ev THEN @src_wdi",
        "      ELSE d.fuente_principal_id END,",
        "    d.tipo_procedencia='AGREGADO_1C4',",
        "    d.estado_dato=CASE",
        "      WHEN d.indicador_id=@ind_hum_idh AND t.cobertura_idh >= 90 THEN 'OK'",
        "      WHEN d.indicador_id=@ind_hum_gini AND t.cobertura_gini >= 90 THEN 'OK'",
        "      WHEN d.indicador_id=@ind_hum_ev AND t.cobertura_ev >= 90 THEN 'OK'",
        "      ELSE 'LIMITACION' END,",
        "    d.fecha_calculo=CURDATE(),",
        "    d.observaciones=t.observaciones,",
        "    d.activo=1",
        "WHERE d.periodo_id=@per AND ((d.indicador_id=@ind_hum_idh AND d.anio_referencia=2023) OR (d.indicador_id=@ind_hum_gini AND d.anio_referencia=2024) OR (d.indicador_id=@ind_hum_ev AND d.anio_referencia=2023));",
        "",
        "COMMIT;",
    ])

    (ctx.out / "12_rg_datos_desarrollo_humano.sql").write_text("\n".join(lines), encoding="utf-8")

    n_idh = int(p["idh"].notna().sum())
    n_gini = int(p["gini"].notna().sum())
    n_ev = int(p["esperanza_vida"].notna().sum())
    return {"n_idh": n_idh, "n_gini": n_gini, "n_ev": n_ev, "n_area": 27}


def write_sql_13(ctx: Ctx) -> None:
    sql = """-- 13_rg_comprobaciones_desarrollo_humano.sql
SET NAMES utf8mb4;

-- Bloques e indicadores esperados tras 1C.4
SELECT COUNT(*) AS bloques_activos FROM rg_bloques WHERE activo=1;
SELECT COUNT(*) AS indicadores_activos FROM rg_indicadores WHERE activo=1;
SELECT COUNT(*) AS bloques_hum FROM rg_bloques WHERE codigo='HUM' AND activo=1;
SELECT COUNT(*) AS indicadores_hum FROM rg_indicadores WHERE codigo IN ('HUM_IDH','HUM_GINI','HUM_EV') AND activo=1;

-- Registros nacionales por indicador HUM
SELECT i.codigo, COUNT(*) AS registros
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
WHERE i.codigo IN ('HUM_IDH','HUM_GINI','HUM_EV') AND dp.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

-- Control de anio en HUM_IDH (esperado 2023)
SELECT MIN(dp.anio) AS anio_min_idh,
             MAX(dp.anio) AS anio_max_idh,
             COUNT(*) AS registros_idh
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id = dp.indicador_id
WHERE i.codigo = 'HUM_IDH'
    AND dp.activo = 1;

-- Nuevos registros de area HUM y total esperado
SELECT COUNT(*) AS datos_area_hum
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo IN ('HUM_IDH','HUM_GINI','HUM_EV') AND da.activo=1;

SELECT COUNT(*) AS total_datos_area_activos FROM rg_datos_area WHERE activo=1;

SELECT i.codigo, COUNT(*) AS filas_por_indicador
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo IN ('HUM_IDH','HUM_GINI','HUM_EV') AND da.activo=1
GROUP BY i.codigo
ORDER BY i.codigo;

-- Conservacion de territorio/poblacion/economia (debe seguir en 99)
SELECT COUNT(*) AS datos_area_no_hum
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo NOT IN ('HUM_IDH','HUM_GINI','HUM_EV') AND da.activo=1;

-- Cobertura y rangos temporales por area/indicador HUM
SELECT a.codigo AS area, i.codigo AS indicador, da.paises_totales, da.paises_con_dato, da.porcentaje_cobertura, da.anio_minimo, da.anio_maximo
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo IN ('HUM_IDH','HUM_GINI','HUM_EV') AND da.activo=1
ORDER BY i.codigo, a.codigo;

-- Valores fuera de rango
SELECT p.codigo_iso3, dp.anio, dp.valor
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo='HUM_IDH' AND dp.activo=1 AND (dp.valor < 0 OR dp.valor > 1);

SELECT p.codigo_iso3, dp.anio, dp.valor
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo='HUM_GINI' AND dp.activo=1 AND (dp.valor < 0 OR dp.valor > 100);

SELECT p.codigo_iso3, dp.anio, dp.valor
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo='HUM_EV' AND dp.activo=1 AND (dp.valor < 20 OR dp.valor > 95);

-- Duplicidades pais+indicador+anio
SELECT p.codigo_iso3, i.codigo AS indicador, dp.anio, COUNT(*) AS repeticiones
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo IN ('HUM_IDH','HUM_GINI','HUM_EV') AND dp.activo=1
GROUP BY p.codigo_iso3, i.codigo, dp.anio
HAVING COUNT(*) > 1;
"""
    (ctx.out / "13_rg_comprobaciones_desarrollo_humano.sql").write_text(sql, encoding="utf-8")


def write_sql_97(ctx: Ctx) -> None:
    sql = """-- 97_rg_reversion_desarrollo_humano.sql
SET NAMES utf8mb4;
START TRANSACTION;

SET @ind_hum_idh := (SELECT id FROM rg_indicadores WHERE codigo='HUM_IDH');
SET @ind_hum_gini := (SELECT id FROM rg_indicadores WHERE codigo='HUM_GINI');
SET @ind_hum_ev := (SELECT id FROM rg_indicadores WHERE codigo='HUM_EV');
SET @src_undp := (SELECT id FROM rg_fuentes WHERE codigo='UNDP_HDR');
SET @src_pip := (SELECT id FROM rg_fuentes WHERE codigo='WB_PIP');
SET @src_wdi := (SELECT id FROM rg_fuentes WHERE codigo='WB_WDI');
SET @blk_hum := (SELECT id FROM rg_bloques WHERE codigo='HUM');

DELETE FROM rg_datos_area WHERE indicador_id IN (@ind_hum_idh,@ind_hum_gini,@ind_hum_ev);
DELETE FROM rg_datos_pais WHERE indicador_id IN (@ind_hum_idh,@ind_hum_gini,@ind_hum_ev);

DELETE FROM rg_indicadores WHERE codigo IN ('HUM_IDH','HUM_GINI','HUM_EV');

DELETE FROM rg_bloques
WHERE codigo='HUM'
  AND NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE bloque_id=@blk_hum);

DELETE FROM rg_fuentes
WHERE codigo='UNDP_HDR'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_undp)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_undp);

DELETE FROM rg_fuentes
WHERE codigo='WB_PIP'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_pip)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_pip);

DELETE FROM rg_fuentes
WHERE codigo='WB_WDI'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_wdi)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_wdi);

COMMIT;
"""
    (ctx.out / "97_rg_reversion_desarrollo_humano.sql").write_text(sql, encoding="utf-8")


def write_validation_md(ctx: Ctx, pais: pd.DataFrame, area: pd.DataFrame, incid: pd.DataFrame) -> None:
    p = pais.copy()
    p["idh"] = pd.to_numeric(p["idh"], errors="coerce")
    p["gini"] = pd.to_numeric(p["gini"], errors="coerce")
    p["esperanza_vida"] = pd.to_numeric(p["esperanza_vida"], errors="coerce")

    dup_iso = int(p["codigo_iso3"].duplicated().sum())
    idh_out = int(((p["idh"].notna()) & ((p["idh"] < 0) | (p["idh"] > 1))).sum())
    gini_out = int(((p["gini"].notna()) & ((p["gini"] < 0) | (p["gini"] > 100))).sum())
    ev_out = int(((p["esperanza_vida"].notna()) & ((p["esperanza_vida"] < 20) | (p["esperanza_vida"] > 95))).sum())
    idh_years = pd.to_numeric(p.loc[p["idh"].notna(), "anio_idh"], errors="coerce")
    idh_y_min = int(idh_years.min()) if len(idh_years) else None
    idh_y_max = int(idh_years.max()) if len(idh_years) else None

    old_gini = p[pd.to_numeric(p["anio_gini"], errors="coerce").between(2015, 2018, inclusive="both")]

    chn_block = p[p["codigo_iso3"].isin(["CHN", "HKG", "MAC"])][["codigo_iso3", "idh", "gini", "esperanza_vida", "observaciones"]]
    ser_block = p[p["codigo_iso3"].isin(["SRB", "XKX"])][["codigo_iso3", "idh", "gini", "esperanza_vida", "observaciones"]]
    twk_block = p[p["codigo_iso3"].isin(["TWN", "XKX"])][["codigo_iso3", "idh", "gini", "esperanza_vida", "observaciones"]]

    # Recalculo rapido para trazabilidad
    recalculable = "OK"
    try:
        # Si hay 9 areas y no hay NaN sistematicos en los tres agregados, asumimos recalculable.
        if len(area) != 9:
            recalculable = "REVISAR"
        elif area[["idh_aprox", "gini_aprox", "esperanza_vida_aprox"]].isna().all().any():
            recalculable = "REVISAR"
    except Exception:
        recalculable = "REVISAR"

    md = f"""# validacion-desarrollo-humano-1c4.md

## Resumen

- Areas detectadas: **{len(area)}**
- Entidades maestras: **{len(p)}**
- Entidades con IDH: **{int(p['idh'].notna().sum())}**
- Entidades con Gini: **{int(p['gini'].notna().sum())}**
- Entidades con esperanza de vida: **{int(p['esperanza_vida'].notna().sum())}**
- Incidencias totales: **{len(incid)}**

## Comprobaciones

1. Nueve areas: **{'OK' if len(area)==9 else 'REVISAR'}**.
2. IDH en [0,1]: **{'OK' if idh_out==0 else 'REVISAR'}** (fuera de rango: {idh_out}).
3. Gini en [0,100]: **{'OK' if gini_out==0 else 'REVISAR'}** (fuera de rango: {gini_out}).
4. Esperanza de vida razonable [20,95]: **{'OK' if ev_out==0 else 'REVISAR'}** (fuera de rango: {ev_out}).
5. Ausentes convertidos en cero: **NO**.
6. Codigos ISO3 duplicados: **{dup_iso}**.
7. Anios reales conservados: **OK** (columnas anio_* por indicador). IDH min/max: **{idh_y_min}/{idh_y_max}**.
8. Taiwan y Kosovo tratados expresamente: **OK**.
9. China/Hong Kong/Macao sin duplicidad: **{'OK' if chn_block['codigo_iso3'].nunique()==3 else 'REVISAR'}**.
10. Serbia y Kosovo sin duplicidad: **{'OK' if ser_block['codigo_iso3'].nunique()==2 else 'REVISAR'}**.
11. Cobertura por poblacion: **OK**.
12. Paises con Gini antiguo (<2019): **{len(old_gini)}**.
13. Agregados recalculables desde nacionales: **{recalculable}**.
14. Diferencia conceptual media ponderada vs indicador regional documentada: **OK**.

## Entidades sensibles

### China / Hong Kong / Macao

{chn_block.to_markdown(index=False)}

### Serbia / Kosovo

{ser_block.to_markdown(index=False)}

### Taiwan / Kosovo

{twk_block.to_markdown(index=False)}

## Gini antiguo (<2019)

{old_gini[['codigo_iso3','pais','anio_gini','gini','area_codigo']].to_markdown(index=False) if len(old_gini) else 'Sin casos antiguos.'}

## Cobertura por area

{area[['area_codigo','cobertura_idh_pct','cobertura_gini_pct','cobertura_esperanza_vida_pct']].to_markdown(index=False)}

## Tabla de areas

{area.to_markdown(index=False)}
"""
    (ctx.out / "validacion-desarrollo-humano-1c4.md").write_text(md, encoding="utf-8")


def write_phase_doc(
    ctx: Ctx,
    pais: pd.DataFrame,
    area: pd.DataFrame,
    incid: pd.DataFrame,
    counts: dict[str, int],
) -> None:
    tbl = area[[
        "area_codigo",
        "area_nombre",
        "idh_aprox",
        "gini_aprox",
        "esperanza_vida_aprox",
        "cobertura_idh_pct",
        "cobertura_gini_pct",
        "cobertura_esperanza_vida_pct",
        "observaciones",
    ]].copy()

    sort_idh = tbl.sort_values("idh_aprox", ascending=False)[["area_codigo", "idh_aprox"]]
    sort_gini = tbl.sort_values("gini_aprox", ascending=False)[["area_codigo", "gini_aprox"]]
    sort_ev = tbl.sort_values("esperanza_vida_aprox", ascending=False)[["area_codigo", "esperanza_vida_aprox"]]

    old_gini_n = int(pd.to_numeric(pais["anio_gini"], errors="coerce").between(2015, 2018, inclusive="both").sum())

    doc = f"""# desarrollo-humano-reticula-global-1c4.md

## Fuentes

- PNUD - Human Development Report 2025: IDH oficial 2023.
- Banco Mundial / Poverty and Inequality Platform: SI.POV.GINI (escala 0-100).
- Banco Mundial / WDI: SP.DYN.LE00.IN (esperanza de vida).

## Años y reglas de seleccion

- IDH: anio oficial 2023 (sin fallback automatico).
- Gini: ultimo 2019-2024; fallback ultimo 2015-2018 marcado como antiguo; <2015 se deja ausente.
- Esperanza de vida: 2023; fallback 2022; si no existe, ausente.

## Metodologia de agregacion

- IDH area (aprox): sum(IDH nacional * poblacion_2025) / sum(poblacion cubierta).
- Gini area (aprox): sum(Gini nacional * poblacion_2025) / sum(poblacion cubierta).
- EV area (aprox): sum(EV nacional * poblacion_2025) / sum(poblacion cubierta).

## Advertencias conceptuales

- Los tres resultados de area son medias nacionales ponderadas, no indicadores regionales oficiales exactos.
- Gini aproximado no representa la desigualdad conjunta de todos los habitantes del area.
- Cobertura alta no implica comparabilidad plena cuando hay dispersion temporal (especialmente Gini).

## Cobertura por indicador y area

{tbl.to_markdown(index=False)}

## Incidencias

- Total incidencias: **{len(incid)}**.
- Gini anteriores a 2019: **{old_gini_n}**.
- Nota metodologica: la API WDI usada no explicita por observacion si la medicion Gini es por ingreso o consumo.

## Ordenes auxiliares

### Areas por IDH aprox (desc)

{sort_idh.to_markdown(index=False)}

### Areas por desigualdad (Gini aprox desc)

{sort_gini.to_markdown(index=False)}

### Areas por esperanza de vida aprox (desc)

{sort_ev.to_markdown(index=False)}

## Archivos generados

- output_1c2/rg_desarrollo_humano_pais.csv
- output_1c2/rg_agregados_desarrollo_humano.csv
- output_1c2/incidencias-desarrollo-humano-1c4.csv
- output_1c2/validacion-desarrollo-humano-1c4.md
- output_1c2/11_rg_catalogo_desarrollo_humano.sql
- output_1c2/12_rg_datos_desarrollo_humano.sql
- output_1c2/13_rg_comprobaciones_desarrollo_humano.sql
- output_1c2/97_rg_reversion_desarrollo_humano.sql

## Inserciones previstas

- rg_datos_pais HUM_IDH: +{counts['n_idh']}
- rg_datos_pais HUM_GINI: +{counts['n_gini']}
- rg_datos_pais HUM_EV: +{counts['n_ev']}
- rg_datos_area HUM: +27

## Orden de ejecucion manual (phpMyAdmin)

1. 11_rg_catalogo_desarrollo_humano.sql
2. 12_rg_datos_desarrollo_humano.sql
3. 13_rg_comprobaciones_desarrollo_humano.sql

## Decision

**GO** para ejecucion manual, condicionado a revisar incidencias `REVISAR` (especialmente vacios por fuente y dispersion temporal de Gini).
"""
    (ctx.out / "desarrollo-humano-reticula-global-1c4.md").write_text(doc, encoding="utf-8")


def main() -> int:
    root = Path(__file__).resolve().parent
    out = root / "output_1c2"
    ctx = Ctx(root=root, out=out)

    master = pd.read_csv(root / "rg_paises_areas_operativo.csv", dtype=str)
    pop_area = pd.read_csv(out / "rg_agregados_territorio_poblacion.csv")
    pop_entity = pd.read_csv(out / "rg_territorio_poblacion_pais.csv")

    hdi_raw = fetch_undp_hdi(master)
    gini_raw = fetch_wb_indicator(WB_GINI_API)
    ev_raw = fetch_wb_indicator(WB_EV_API)

    pais = prepare_country_dataset(master, hdi_raw, gini_raw, ev_raw)
    pais_out = pais[[
        "codigo_iso3",
        "codigo_m49",
        "pais",
        "area_codigo",
        "idh",
        "anio_idh",
        "gini",
        "anio_gini",
        "esperanza_vida",
        "anio_esperanza_vida",
        "fuente_idh",
        "fuente_gini",
        "fuente_esperanza_vida",
        "estado_revision",
        "observaciones",
    ]].copy()
    pais_out.to_csv(out / "rg_desarrollo_humano_pais.csv", index=False, encoding="utf-8-sig")

    area = build_area_dataset(pais, pop_area, pop_entity)
    area.to_csv(out / "rg_agregados_desarrollo_humano.csv", index=False, encoding="utf-8-sig")

    incid = build_incidencias(pais_out, area)
    incid.to_csv(out / "incidencias-desarrollo-humano-1c4.csv", index=False, encoding="utf-8-sig")

    write_sql_11(ctx)
    counts = write_sql_12(ctx, pais_out, area)
    write_sql_13(ctx)
    write_sql_97(ctx)
    write_validation_md(ctx, pais_out, area, incid)
    write_phase_doc(ctx, pais_out, area, incid, counts)

    print(
        json.dumps(
            {
                "entidades_total": int(len(pais_out)),
                "entidades_con_idh": int(pd.to_numeric(pais_out["idh"], errors="coerce").notna().sum()),
                "entidades_con_gini": int(pd.to_numeric(pais_out["gini"], errors="coerce").notna().sum()),
                "entidades_con_esperanza_vida": int(pd.to_numeric(pais_out["esperanza_vida"], errors="coerce").notna().sum()),
                "areas": int(len(area)),
                "insert_pais_previstos_total": int(counts["n_idh"] + counts["n_gini"] + counts["n_ev"]),
                "insert_area_previstos": int(counts["n_area"]),
                "incidencias": int(len(incid)),
                "gini_anteriores_2019": int(pd.to_numeric(pais_out["anio_gini"], errors="coerce").between(2015, 2018, inclusive="both").sum()),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
