from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import pandas as pd
import requests


WDI_INDICATOR = "NY.GDP.MKTP.CD"
WDI_API = "https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD"


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


def fetch_wdi_all() -> pd.DataFrame:
    page = 1
    rows: list[dict[str, object]] = []
    while True:
        r = requests.get(
            WDI_API,
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
                    "countryiso3code": d.get("countryiso3code"),
                    "country_name": (d.get("country") or {}).get("value"),
                    "year": int(d["date"]) if d.get("date") else None,
                    "value": d.get("value"),
                }
            )
        if page >= int(meta.get("pages", page)):
            break
        page += 1
    return pd.DataFrame(rows)


def prepare_country_gdp(master: pd.DataFrame, wb: pd.DataFrame) -> pd.DataFrame:
    wb = wb[wb["countryiso3code"].notna()].copy()
    wb = wb[wb["year"].isin([2024, 2023])].copy()
    wb["value"] = pd.to_numeric(wb["value"], errors="coerce")

    # Prefer 2024; fallback to 2023 only when 2024 missing.
    wb = wb.sort_values(["countryiso3code", "year"], ascending=[True, False])
    wb_pick = wb.dropna(subset=["value"]).groupby("countryiso3code", as_index=False).head(1)
    wb_pick = wb_pick.rename(columns={"countryiso3code": "codigo_iso3", "year": "anio_pib", "value": "pib_usd"})

    m = master.copy()
    m = m[[
        "codigo_iso3",
        "codigo_m49",
        "nombre_es",
        "area_codigo",
        "area_nombre",
        "tipo_entidad",
        "incluir_calculos",
        "tratamiento_fuente",
        "observaciones",
    ]]
    x = m.merge(wb_pick[["codigo_iso3", "anio_pib", "pib_usd"]], on="codigo_iso3", how="left")

    x["estado_revision"] = "OK"
    x["observaciones_out"] = ""
    x.loc[x["pib_usd"].isna(), "estado_revision"] = "REVISAR"
    x.loc[x["pib_usd"].isna(), "observaciones_out"] = "Sin dato comparable 2024/2023 en WDI."
    x.loc[x["anio_pib"].eq(2023), "observaciones_out"] = (
        x.loc[x["anio_pib"].eq(2023), "observaciones_out"].astype(str).str.strip().replace({"": "Fallback a 2023 por ausencia de 2024."})
    )

    # Notes for critical entities
    for iso3, note in [
        ("CHN", "WDI reporta CHN separado; revisar consistencia con HKG/MAC."),
        ("HKG", "WDI reporta HKG separado de CHN."),
        ("MAC", "WDI reporta MAC separado de CHN."),
    ]:
        mask = x["codigo_iso3"].eq(iso3)
        if mask.any():
            cur = x.loc[mask, "observaciones_out"].fillna("").astype(str).str.strip()
            x.loc[mask, "observaciones_out"] = cur.where(cur.eq(""), cur + " ") + note

    # Taiwan: keep absent if no separate value.
    mask_twn = x["codigo_iso3"].eq("TWN")
    if mask_twn.any():
        cur = x.loc[mask_twn, "observaciones_out"].fillna("").astype(str).str.strip()
        note_twn = "WDI no publica valor separado en esta extraccion; queda ausente."
        x.loc[mask_twn, "observaciones_out"] = cur.where(cur.eq(""), cur + " ") + note_twn

    # Kosovo: if present, mark as separate and warn about non-duplication with SRB.
    mask_xkx = x["codigo_iso3"].eq("XKX")
    if mask_xkx.any():
        has_val = x.loc[mask_xkx, "pib_usd"].notna()
        note_yes = "WDI publica XKX separado; mantener separado de SRB sin duplicidad."
        note_no = "WDI no publica XKX en esta extraccion; evitar duplicidad con SRB."
        cur = x.loc[mask_xkx, "observaciones_out"].fillna("").astype(str).str.strip()
        add = has_val.map(lambda v: note_yes if v else note_no)
        x.loc[mask_xkx, "observaciones_out"] = cur.where(cur.eq(""), cur + " ") + add.values

    x["fuente"] = "Banco Mundial WDI"
    x["indicador_fuente"] = WDI_INDICATOR

    out = x.rename(columns={"nombre_es": "pais"})[
        [
            "codigo_iso3",
            "codigo_m49",
            "pais",
            "area_codigo",
            "pib_usd",
            "anio_pib",
            "fuente",
            "indicador_fuente",
            "estado_revision",
            "observaciones_out",
        ]
    ].copy()
    out = out.rename(columns={"observaciones_out": "observaciones"})
    return out


def area_aggregates(econ_pais: pd.DataFrame, pop_area: pd.DataFrame, pop_entity: pd.DataFrame) -> pd.DataFrame:
    ep = econ_pais.copy()
    ep["pib_usd"] = pd.to_numeric(ep["pib_usd"], errors="coerce")
    ep["anio_pib"] = pd.to_numeric(ep["anio_pib"], errors="coerce")

    pe = pop_entity[["codigo_iso3", "area_codigo", "poblacion_2025"]].copy()
    pe["poblacion_2025"] = pd.to_numeric(pe["poblacion_2025"], errors="coerce")

    merged = ep.merge(pe, on=["codigo_iso3", "area_codigo"], how="left")

    rows = []
    for ac, g in merged.groupby("area_codigo", dropna=False):
        total_ent = len(g)
        con_pib = int(g["pib_usd"].notna().sum())
        pib = g["pib_usd"].sum(min_count=1)
        years = g.loc[g["pib_usd"].notna(), "anio_pib"]
        anio_min = int(years.min()) if not years.empty else None
        anio_max = int(years.max()) if not years.empty else None

        g_cov = g[g["pib_usd"].notna() & g["poblacion_2025"].notna()].copy()
        cov_num = float(g_cov["poblacion_2025"].sum()) if len(g_cov) else 0.0

        pop_row = pop_area[pop_area["area_codigo"].eq(ac)].iloc[0]
        pop_area_2025 = float(pop_row["poblacion_2025"])
        cov_pct = (cov_num / pop_area_2025 * 100.0) if pop_area_2025 > 0 else None

        pib_pc = (float(pib) / pop_area_2025) if pd.notna(pib) and pop_area_2025 > 0 else None

        if cov_pct is None:
            cov_label = "insuficiente"
        elif cov_pct > 95:
            cov_label = "alta"
        elif cov_pct >= 90:
            cov_label = "aceptable"
        elif cov_pct >= 80:
            cov_label = "condicionada"
        else:
            cov_label = "insuficiente"

        obs = []
        if con_pib < total_ent:
            obs.append("Cobertura incompleta en entidades.")
        obs.append(f"Cobertura poblacional {cov_label}.")
        if years.nunique() > 1:
            obs.append("Mezcla de anios 2023/2024 por faltantes.")

        rows.append(
            {
                "area_codigo": ac,
                "area_nombre": pop_row["area_nombre"],
                "pib_usd": pib,
                "pib_mundial_pct": None,
                "poblacion_2025": pop_area_2025,
                "pib_por_habitante_usd": pib_pc,
                "entidades_totales": total_ent,
                "entidades_con_pib": con_pib,
                "poblacion_cubierta_pct": cov_pct,
                "anio_minimo": anio_min,
                "anio_maximo": anio_max,
                "observaciones": " ".join(obs),
            }
        )

    area = pd.DataFrame(rows).sort_values("area_codigo")
    total_world = area["pib_usd"].sum(min_count=1)
    area["pib_mundial_pct"] = area["pib_usd"] / total_world * 100.0
    return area


def build_incidencias(econ_pais: pd.DataFrame, wb: pd.DataFrame) -> pd.DataFrame:
    out = []
    x = econ_pais.copy()

    miss = x[x["pib_usd"].isna()]
    for r in miss.to_dict(orient="records"):
        out.append(
            {
                "codigo_iso3": r["codigo_iso3"],
                "codigo_m49": r["codigo_m49"],
                "pais": r["pais"],
                "area_codigo": r["area_codigo"],
                "tipo_incidencia": "SIN_DATO",
                "detalle": "Sin valor WDI 2024/2023 comparable.",
                "estado": "REVISAR",
            }
        )

    fallback = x[x["anio_pib"].eq(2023)]
    for r in fallback.to_dict(orient="records"):
        out.append(
            {
                "codigo_iso3": r["codigo_iso3"],
                "codigo_m49": r["codigo_m49"],
                "pais": r["pais"],
                "area_codigo": r["area_codigo"],
                "tipo_incidencia": "FALLBACK_2023",
                "detalle": "2024 ausente, se usa 2023.",
                "estado": "OK",
            }
        )

    # Extreme values sanity check
    num = pd.to_numeric(x["pib_usd"], errors="coerce")
    if num.notna().any():
        q_hi = float(num.quantile(0.999))
        ext = x[num > q_hi]
        for r in ext.to_dict(orient="records"):
            out.append(
                {
                    "codigo_iso3": r["codigo_iso3"],
                    "codigo_m49": r["codigo_m49"],
                    "pais": r["pais"],
                    "area_codigo": r["area_codigo"],
                    "tipo_incidencia": "VALOR_EXTREMO",
                    "detalle": "Valor alto relativo, revisar unidad/fuente.",
                    "estado": "REVISAR",
                }
            )

    # Duplicated ISO in result (should be none)
    dup = x.groupby("codigo_iso3").size().reset_index(name="n")
    dup = dup[dup["n"] > 1]
    for r in dup.to_dict(orient="records"):
        out.append(
            {
                "codigo_iso3": r["codigo_iso3"],
                "codigo_m49": "",
                "pais": "",
                "area_codigo": "",
                "tipo_incidencia": "DUPLICADO_ISO3",
                "detalle": "Codigo repetido en rg_economia_pais.csv",
                "estado": "REVISAR",
            }
        )

    # Ensure no WB aggregates imported as entities
    master_iso = set(x["codigo_iso3"].astype(str))
    wb_2024_2023 = wb[wb["year"].isin([2024, 2023]) & wb["value"].notna()]
    agg_like = wb_2024_2023[~wb_2024_2023["countryiso3code"].isin(master_iso)]
    out.append(
        {
            "codigo_iso3": "",
            "codigo_m49": "",
            "pais": "",
            "area_codigo": "",
            "tipo_incidencia": "AGREGADOS_WB_NO_IMPORTADOS",
            "detalle": f"Registros WDI fuera del maestro no importados: {len(agg_like)}.",
            "estado": "OK",
        }
    )

    return pd.DataFrame(out)


def write_sql_08(ctx: Ctx) -> None:
    sql = """-- 08_rg_catalogo_economia.sql
SET NAMES utf8mb4;

START TRANSACTION;

INSERT INTO rg_bloques (id,codigo,nombre,activo)
SELECT COALESCE(MAX(id),0)+1, 'ECO', 'Economia', 1
FROM rg_bloques
WHERE NOT EXISTS (SELECT 1 FROM rg_bloques WHERE codigo='ECO');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT COALESCE(MAX(i.id),0)+1,
       'ECO_PIB',
       b.id,
       'PIB nominal',
       'USD_corrientes',
       'PIB nominal en dolares corrientes',
       1
FROM rg_indicadores i
JOIN rg_bloques b ON b.codigo='ECO'
WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ECO_PIB');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT COALESCE(MAX(i.id),0)+1,
       'ECO_PIB_PCT',
       b.id,
       'PIB mundial %',
       '%',
       'Participacion del PIB del area sobre el total agregado de las nueve areas',
       1
FROM rg_indicadores i
JOIN rg_bloques b ON b.codigo='ECO'
WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ECO_PIB_PCT');

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT COALESCE(MAX(i.id),0)+1,
       'ECO_PC',
       b.id,
       'PIB por habitante',
       'USD_corrientes_por_hab',
       'PIB total del area dividido por poblacion 2025 del area',
       1
FROM rg_indicadores i
JOIN rg_bloques b ON b.codigo='ECO'
WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='ECO_PC');

INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT COALESCE(MAX(id),0)+1,
       'WB_WDI',
       'Banco Mundial - World Development Indicators',
       'oficial',
       'https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD',
       1
FROM rg_fuentes
WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='WB_WDI');

COMMIT;
"""
    (ctx.out / "08_rg_catalogo_economia.sql").write_text(sql, encoding="utf-8")


def write_sql_09(ctx: Ctx, econ_pais: pd.DataFrame, econ_area: pd.DataFrame) -> dict[str, int]:
    ep = econ_pais.copy()
    ep["pib_usd"] = pd.to_numeric(ep["pib_usd"], errors="coerce")
    ep["anio_pib"] = pd.to_numeric(ep["anio_pib"], errors="coerce")
    ep_ok = ep[ep["pib_usd"].notna()].copy()

    ea = econ_area.copy()

    lines = [
        "-- 09_rg_datos_economia.sql",
        "SET NAMES utf8mb4;",
        "START TRANSACTION;",
        "",
        "DROP TEMPORARY TABLE IF EXISTS tmp_rg_economia_pais;",
        "CREATE TEMPORARY TABLE tmp_rg_economia_pais (codigo_iso3 VARCHAR(3) NOT NULL PRIMARY KEY, anio_pib SMALLINT NOT NULL, pib_usd DECIMAL(22,2) NOT NULL, observaciones TEXT NULL) ENGINE=InnoDB;",
        "",
        "INSERT INTO tmp_rg_economia_pais (codigo_iso3,anio_pib,pib_usd,observaciones) VALUES",
    ]
    vals = []
    for r in ep_ok.to_dict(orient="records"):
        vals.append(
            "(" + ",".join([
                q(r["codigo_iso3"]),
                q(int(float(r["anio_pib"]))),
                q(round(float(r["pib_usd"]), 2)),
                q(str(r.get("observaciones", "")).strip() or None),
            ]) + ")"
        )
    lines.append(",\n".join(vals) + ";\n")

    lines.append("SET @ind_eco_pib := (SELECT id FROM rg_indicadores WHERE codigo='ECO_PIB');")
    lines.append("SET @src_wb := (SELECT id FROM rg_fuentes WHERE codigo='WB_WDI');")
    lines.append("SET @next_pais_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_pais);")
    lines.append(
        "INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)\n"
        "SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_eco_pib, t.anio_pib, t.pib_usd, @src_wb,\n"
        "       'FUENTE_VALIDADA', 'OK', CURDATE(), t.observaciones, 1\n"
        "FROM tmp_rg_economia_pais t\n"
        "JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1\n"
        "LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_eco_pib AND d.anio=t.anio_pib\n"
        "WHERE d.id IS NULL;"
    )
    lines.append("")
    lines.append(
        "UPDATE rg_datos_pais d\n"
        "JOIN rg_paises p ON p.id=d.pais_id\n"
        "JOIN tmp_rg_economia_pais t ON t.codigo_iso3=p.codigo_iso3 AND t.anio_pib=d.anio\n"
        "SET d.valor=t.pib_usd,\n"
        "    d.fuente_id=@src_wb,\n"
        "    d.tipo_procedencia='FUENTE_VALIDADA',\n"
        "    d.estado_dato='OK',\n"
        "    d.fecha_carga=CURDATE(),\n"
        "    d.observaciones=t.observaciones,\n"
        "    d.activo=1\n"
        "WHERE d.indicador_id=@ind_eco_pib;"
    )

    lines.extend([
        "",
        "DROP TEMPORARY TABLE IF EXISTS tmp_rg_economia_area;",
        "CREATE TEMPORARY TABLE tmp_rg_economia_area (area_codigo VARCHAR(10) PRIMARY KEY, anio_ref SMALLINT NOT NULL, pib_usd DECIMAL(22,2) NULL, pib_mundial_pct DECIMAL(12,8) NULL, pib_pc DECIMAL(22,8) NULL, entidades_totales SMALLINT NULL, entidades_con_pib SMALLINT NULL, cobertura_pct DECIMAL(8,4) NULL, anio_minimo SMALLINT NULL, anio_maximo SMALLINT NULL, observaciones TEXT NULL) ENGINE=InnoDB;",
        "",
        "INSERT INTO tmp_rg_economia_area (area_codigo,anio_ref,pib_usd,pib_mundial_pct,pib_pc,entidades_totales,entidades_con_pib,cobertura_pct,anio_minimo,anio_maximo,observaciones) VALUES",
    ])
    avals = []
    for r in ea.to_dict(orient="records"):
        avals.append(
            "(" + ",".join([
                q(r["area_codigo"]),
                q(2024),
                q(round(float(r["pib_usd"]), 2) if pd.notna(r["pib_usd"]) else None),
                q(round(float(r["pib_mundial_pct"]), 8) if pd.notna(r["pib_mundial_pct"]) else None),
                q(round(float(r["pib_por_habitante_usd"]), 8) if pd.notna(r["pib_por_habitante_usd"]) else None),
                q(int(r["entidades_totales"])),
                q(int(r["entidades_con_pib"])),
                q(round(float(r["poblacion_cubierta_pct"]), 4) if pd.notna(r["poblacion_cubierta_pct"]) else None),
                q(int(r["anio_minimo"]) if pd.notna(r["anio_minimo"]) else None),
                q(int(r["anio_maximo"]) if pd.notna(r["anio_maximo"]) else None),
                q(r["observaciones"]),
            ]) + ")"
        )
    lines.append(",\n".join(avals) + ";\n")

    lines.extend([
        "SET @per := (SELECT id FROM rg_periodos WHERE codigo='RG2025_V1');",
        "SET @ind_area_pib := (SELECT id FROM rg_indicadores WHERE codigo='ECO_PIB');",
        "SET @ind_area_pct := (SELECT id FROM rg_indicadores WHERE codigo='ECO_PIB_PCT');",
        "SET @ind_area_pc := (SELECT id FROM rg_indicadores WHERE codigo='ECO_PC');",
        "SET @next_area_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_area);",
        "",
        "INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)",
        "SELECT (@next_area_id := @next_area_id + 1), a.id, @ind_area_pib, @per, t.anio_ref, t.pib_usd,",
        "       'Suma PIB nacional incluido', t.entidades_totales, t.entidades_con_pib, t.cobertura_pct, t.anio_minimo, t.anio_maximo, @src_wb,",
        "       'AGREGADO_1C3', CASE WHEN t.cobertura_pct >= 90 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1",
        "FROM tmp_rg_economia_area t",
        "JOIN rg_areas a ON a.codigo=t.area_codigo",
        "LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=@ind_area_pib AND d.periodo_id=@per AND d.anio_referencia=t.anio_ref",
        "WHERE d.id IS NULL;",
        "",
        "INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)",
        "SELECT (@next_area_id := @next_area_id + 1), a.id, @ind_area_pct, @per, t.anio_ref, t.pib_mundial_pct,",
        "       'PIB area / PIB total nueve areas * 100', t.entidades_totales, t.entidades_con_pib, t.cobertura_pct, t.anio_minimo, t.anio_maximo, @src_wb,",
        "       'AGREGADO_1C3', CASE WHEN t.cobertura_pct >= 90 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1",
        "FROM tmp_rg_economia_area t",
        "JOIN rg_areas a ON a.codigo=t.area_codigo",
        "LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=@ind_area_pct AND d.periodo_id=@per AND d.anio_referencia=t.anio_ref",
        "WHERE d.id IS NULL;",
        "",
        "INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)",
        "SELECT (@next_area_id := @next_area_id + 1), a.id, @ind_area_pc, @per, t.anio_ref, t.pib_pc,",
        "       'PIB area / poblacion 2025 area', t.entidades_totales, t.entidades_con_pib, t.cobertura_pct, t.anio_minimo, t.anio_maximo, @src_wb,",
        "       'AGREGADO_1C3', CASE WHEN t.cobertura_pct >= 90 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1",
        "FROM tmp_rg_economia_area t",
        "JOIN rg_areas a ON a.codigo=t.area_codigo",
        "LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=@ind_area_pc AND d.periodo_id=@per AND d.anio_referencia=t.anio_ref",
        "WHERE d.id IS NULL;",
        "",
        "-- Actualizacion idempotente de los 27 registros economicos",
        "UPDATE rg_datos_area d",
        "JOIN rg_areas a ON a.id=d.area_id",
        "JOIN tmp_rg_economia_area t ON t.area_codigo=a.codigo",
        "SET d.valor=CASE",
        "      WHEN d.indicador_id=@ind_area_pib THEN t.pib_usd",
        "      WHEN d.indicador_id=@ind_area_pct THEN t.pib_mundial_pct",
        "      WHEN d.indicador_id=@ind_area_pc THEN t.pib_pc",
        "      ELSE d.valor END,",
        "    d.metodo_calculo=CASE",
        "      WHEN d.indicador_id=@ind_area_pib THEN 'Suma PIB nacional incluido'",
        "      WHEN d.indicador_id=@ind_area_pct THEN 'PIB area / PIB total nueve areas * 100'",
        "      WHEN d.indicador_id=@ind_area_pc THEN 'PIB area / poblacion 2025 area'",
        "      ELSE d.metodo_calculo END,",
        "    d.paises_totales=t.entidades_totales,",
        "    d.paises_con_dato=t.entidades_con_pib,",
        "    d.porcentaje_cobertura=t.cobertura_pct,",
        "    d.anio_minimo=t.anio_minimo,",
        "    d.anio_maximo=t.anio_maximo,",
        "    d.fuente_principal_id=@src_wb,",
        "    d.tipo_procedencia='AGREGADO_1C3',",
        "    d.estado_dato=CASE WHEN t.cobertura_pct >= 90 THEN 'OK' ELSE 'LIMITACION' END,",
        "    d.fecha_calculo=CURDATE(),",
        "    d.observaciones=t.observaciones,",
        "    d.activo=1",
        "WHERE d.periodo_id=@per AND d.anio_referencia=2024 AND d.indicador_id IN (@ind_area_pib,@ind_area_pct,@ind_area_pc);",
        "",
        "COMMIT;",
    ])

    (ctx.out / "09_rg_datos_economia.sql").write_text("\n".join(lines), encoding="utf-8")
    return {"n_pais": len(ep_ok), "n_area": 27}


def write_sql_10(ctx: Ctx) -> None:
    sql = """-- 10_rg_comprobaciones_economia.sql
SET NAMES utf8mb4;

-- Bloque economico y tres indicadores
SELECT COUNT(*) AS bloques_eco FROM rg_bloques WHERE codigo='ECO' AND activo=1;
SELECT COUNT(*) AS indicadores_eco FROM rg_indicadores WHERE codigo IN ('ECO_PIB','ECO_PIB_PCT','ECO_PC') AND activo=1;

-- Numero de datos nacionales de PIB
SELECT COUNT(*) AS datos_nacionales_eco_pib
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
WHERE i.codigo='ECO_PIB' AND dp.activo=1;

-- 27 nuevos registros de area y 99 total esperado
SELECT COUNT(*) AS datos_area_eco
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo IN ('ECO_PIB','ECO_PIB_PCT','ECO_PC') AND da.activo=1;

SELECT COUNT(*) AS total_datos_area_activos FROM rg_datos_area WHERE activo=1;

-- Conservacion de 72 registros anteriores (no ECO)
SELECT COUNT(*) AS datos_area_no_eco
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo NOT IN ('ECO_PIB','ECO_PIB_PCT','ECO_PC') AND da.activo=1;

-- Porcentajes ECO al ~100
SELECT SUM(da.valor) AS suma_eco_pib_pct
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo='ECO_PIB_PCT' AND da.activo=1;

-- PIB mundial agregado y PIB por habitante por area
SELECT SUM(da.valor) AS pib_mundial_agregado
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
WHERE i.codigo='ECO_PIB' AND da.activo=1;

SELECT a.codigo AS area, da.valor AS pib_por_habitante
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo='ECO_PC' AND da.activo=1
ORDER BY a.codigo;

-- Cobertura por area
SELECT a.codigo AS area, da.paises_totales, da.paises_con_dato, da.porcentaje_cobertura
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_areas a ON a.id=da.area_id
WHERE i.codigo='ECO_PIB' AND da.activo=1
ORDER BY a.codigo;

-- Duplicidades pais+indicador+anio en ECO_PIB
SELECT p.codigo_iso3, dp.anio, COUNT(*) AS repeticiones
FROM rg_datos_pais dp
JOIN rg_indicadores i ON i.id=dp.indicador_id
JOIN rg_paises p ON p.id=dp.pais_id
WHERE i.codigo='ECO_PIB' AND dp.activo=1
GROUP BY p.codigo_iso3, dp.anio
HAVING COUNT(*) > 1;
"""
    (ctx.out / "10_rg_comprobaciones_economia.sql").write_text(sql, encoding="utf-8")


def write_sql_98(ctx: Ctx) -> None:
    sql = """-- 98_rg_reversion_economia.sql
SET NAMES utf8mb4;
START TRANSACTION;

SET @eco_pib := (SELECT id FROM rg_indicadores WHERE codigo='ECO_PIB');
SET @eco_pct := (SELECT id FROM rg_indicadores WHERE codigo='ECO_PIB_PCT');
SET @eco_pc := (SELECT id FROM rg_indicadores WHERE codigo='ECO_PC');
SET @src_wb := (SELECT id FROM rg_fuentes WHERE codigo='WB_WDI');
SET @blk_eco := (SELECT id FROM rg_bloques WHERE codigo='ECO');

DELETE FROM rg_datos_area WHERE indicador_id IN (@eco_pib,@eco_pct,@eco_pc);
DELETE FROM rg_datos_pais WHERE indicador_id=@eco_pib;

DELETE FROM rg_indicadores WHERE codigo IN ('ECO_PIB','ECO_PIB_PCT','ECO_PC');

DELETE FROM rg_bloques
WHERE codigo='ECO'
  AND NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE bloque_id=@blk_eco);

DELETE FROM rg_fuentes
WHERE codigo='WB_WDI'
  AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_wb)
  AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_wb);

COMMIT;
"""
    (ctx.out / "98_rg_reversion_economia.sql").write_text(sql, encoding="utf-8")


def write_validation_md(ctx: Ctx, econ_pais: pd.DataFrame, econ_area: pd.DataFrame, incid: pd.DataFrame, pib_world: float) -> None:
    x = econ_pais.copy()
    x["pib_usd"] = pd.to_numeric(x["pib_usd"], errors="coerce")

    dup_iso = x["codigo_iso3"].duplicated().sum()
    missing_as_zero = int(((x["pib_usd"] == 0) & x["estado_revision"].eq("REVISAR")).sum())
    sum_pct = float(pd.to_numeric(econ_area["pib_mundial_pct"], errors="coerce").sum())

    chn = x[x["codigo_iso3"].isin(["CHN", "HKG", "MAC"])][["codigo_iso3", "pib_usd", "anio_pib", "observaciones"]]
    ser_kos = x[x["codigo_iso3"].isin(["SRB", "XKX"])][["codigo_iso3", "pib_usd", "anio_pib", "observaciones"]]
    sin_dato = x[x["pib_usd"].isna()][["codigo_iso3", "pais", "area_codigo"]]

    md = f"""# validacion-economia-1c3.md

## Resumen

- Areas detectadas: **{len(econ_area)}**
- Entidades maestras: **{len(x)}**
- Entidades con PIB: **{int(x['pib_usd'].notna().sum())}**
- Entidades sin PIB: **{int(x['pib_usd'].isna().sum())}**
- Suma PIB mundial agregado (nueve areas): **{pib_world:,.2f}**
- Suma porcentajes PIB: **{sum_pct:.6f}**

## Comprobaciones

1. Nueve areas: **{'OK' if len(econ_area)==9 else 'REVISAR'}**.
2. Ausentes convertidos a cero: **{'NO' if missing_as_zero==0 else 'SI'}**.
3. Porcentajes suman ~100: **{'OK' if abs(sum_pct-100) < 0.01 else 'REVISAR'}**.
4. PIB por habitante derivado de totales: **OK** (calculado como PIB area / poblacion 2025 area).
5. Codigos duplicados en salida nacional: **{dup_iso}**.
6. Agregados WDI como paises: **NO** (se cruza solo contra maestro ISO3).
7. China/Hong Kong/Macao (revision duplicidad):

{chn.to_markdown(index=False)}

8. Serbia/Kosovo (revision duplicidad):

{ser_kos.to_markdown(index=False)}

9. Datos con anio 2023 (fallback): **{int(pd.to_numeric(x['anio_pib'], errors='coerce').eq(2023).sum())}**.
10. Cobertura por area: ver tabla de agregados economicos.
11. Entidades sin dato listadas abajo.
12. Valores extremos/unidades: registrados en incidencias.

## Entidades sin dato

{sin_dato.to_markdown(index=False) if len(sin_dato) else 'Sin entidades sin dato.'}

## Tabla de areas

{econ_area.to_markdown(index=False)}

## Incidencias

Total incidencias registradas: **{len(incid)}**.
"""
    (ctx.out / "validacion-economia-1c3.md").write_text(md, encoding="utf-8")


def write_phase_doc(
    ctx: Ctx,
    econ_pais: pd.DataFrame,
    econ_area: pd.DataFrame,
    incid: pd.DataFrame,
    pib_world: float,
    n_insert_pais: int,
) -> None:
    table_small = econ_area[[
        "area_codigo",
        "area_nombre",
        "pib_usd",
        "pib_mundial_pct",
        "pib_por_habitante_usd",
        "poblacion_cubierta_pct",
        "anio_minimo",
        "anio_maximo",
        "observaciones",
    ]].copy()

    doc = f"""# economia-reticula-global-1c3.md

## Fuente y anio

- Fuente principal: Banco Mundial WDI (API oficial)
- Indicador: NY.GDP.MKTP.CD (GDP current US$)
- Politica temporal: 2024 preferente, 2023 fallback, ausente si no comparable

## Tratamiento territorial

- Maestro usado: rg_paises_areas_operativo.csv
- China/Hong Kong/Macao: se cargan por codigo separado (CHN/HKG/MAC) segun WDI; sin cargar agregados regionales WDI.
- Taiwan: sin valor separado en esta extraccion WDI, se mantiene ausente.
- Kosovo: se usa codigo separado de WDI cuando existe; se mantiene separado de Serbia para evitar duplicidad.
- Territorios SEGUN_FUENTE: se respetan ausencias, sin imputacion.

## Cobertura y calculos

- Entidades con PIB: **{int(pd.to_numeric(econ_pais['pib_usd'], errors='coerce').notna().sum())}** de **{len(econ_pais)}**.
- PIB mundial agregado (nueve areas): **{pib_world:,.2f}**.
- PIB area: suma nacional incluida.
- PIB % mundial: PIB area / PIB total nueve areas * 100.
- PIB por habitante: PIB area / poblacion_2025 area.

## Tabla de nueve areas

{table_small.to_markdown(index=False)}

## Incidencias

- Total registradas: **{len(incid)}** (ver incidencias-economia-1c3.csv).

## Archivos generados

- output_1c2/rg_economia_pais.csv
- output_1c2/rg_agregados_economia.csv
- output_1c2/incidencias-economia-1c3.csv
- output_1c2/validacion-economia-1c3.md
- output_1c2/08_rg_catalogo_economia.sql
- output_1c2/09_rg_datos_economia.sql
- output_1c2/10_rg_comprobaciones_economia.sql
- output_1c2/98_rg_reversion_economia.sql

## Inserciones previstas

- rg_bloques: +1 (si ECO no existe)
- rg_indicadores: +3 (si no existen)
- rg_fuentes: +1 (si WB_WDI no existe)
- rg_datos_pais: +{n_insert_pais} (ECO_PIB)
- rg_datos_area: +27 (ECO_PIB, ECO_PIB_PCT, ECO_PC)

## Orden de ejecucion manual

1. 08_rg_catalogo_economia.sql
2. 09_rg_datos_economia.sql
3. 10_rg_comprobaciones_economia.sql

## Decision

**GO** para ejecucion manual en phpMyAdmin, condicionado a revisar incidencias REVISAR.
"""
    (ctx.out / "economia-reticula-global-1c3.md").write_text(doc, encoding="utf-8")


def main() -> int:
    root = Path(__file__).resolve().parent
    out = root / "output_1c2"
    ctx = Ctx(root=root, out=out)

    master = pd.read_csv(root / "rg_paises_areas_operativo.csv", dtype=str)
    pop_area = pd.read_csv(out / "rg_agregados_territorio_poblacion.csv")
    pop_entity = pd.read_csv(out / "rg_territorio_poblacion_pais.csv")

    wb = fetch_wdi_all()

    econ_pais = prepare_country_gdp(master, wb)
    econ_pais.to_csv(out / "rg_economia_pais.csv", index=False, encoding="utf-8-sig")

    econ_area = area_aggregates(econ_pais, pop_area, pop_entity)
    econ_area.to_csv(out / "rg_agregados_economia.csv", index=False, encoding="utf-8-sig")

    incid = build_incidencias(econ_pais, wb)
    incid.to_csv(out / "incidencias-economia-1c3.csv", index=False, encoding="utf-8-sig")

    pib_world = float(pd.to_numeric(econ_area["pib_usd"], errors="coerce").sum())

    write_validation_md(ctx, econ_pais, econ_area, incid, pib_world)
    write_sql_08(ctx)
    counts = write_sql_09(ctx, econ_pais, econ_area)
    write_sql_10(ctx)
    write_sql_98(ctx)
    write_phase_doc(ctx, econ_pais, econ_area, incid, pib_world, counts["n_pais"])

    print(
        json.dumps(
            {
                "entidades_total": int(len(econ_pais)),
                "entidades_con_pib": int(pd.to_numeric(econ_pais["pib_usd"], errors="coerce").notna().sum()),
                "areas": int(len(econ_area)),
                "pib_mundial_agregado": pib_world,
                "insert_pais_previstos": counts["n_pais"],
                "insert_area_previstos": counts["n_area"],
                "incidencias": int(len(incid)),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
