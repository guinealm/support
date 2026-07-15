
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import pandas as pd
import requests


OWID_POP_URL = (
    "https://ourworldindata.org/grapher/"
    "population-with-un-projections.csv?v=1&csvType=full&useColumnShortNames=false"
)
OWID_MEDIAN_AGE_URL = (
    "https://ourworldindata.org/grapher/"
    "median-age.csv?v=1&csvType=full&useColumnShortNames=false"
)
OWID_LAND_URL = (
    "https://ourworldindata.org/grapher/"
    "land-area-hectares.csv?v=1&csvType=full&useColumnShortNames=false"
)

USER_AGENT = "Reticula Global 2025 data build/1.0"


def download(url: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(url, timeout=120, headers={"User-Agent": USER_AGENT})
    response.raise_for_status()
    path.write_bytes(response.content)


def find_value_column(df: pd.DataFrame, preferred_tokens: list[str]) -> str:
    excluded = {"Entity", "Code", "Year"}
    candidates = [c for c in df.columns if c not in excluded]
    if len(candidates) == 1:
        return candidates[0]

    # Prefer exact token column names when present (e.g., "Population").
    exact = {c.lower(): c for c in candidates}
    for token in preferred_tokens:
        if token in exact:
            return exact[token]

    lowered = {c: c.lower() for c in candidates}
    for token in preferred_tokens:
        matches = [c for c, lc in lowered.items() if token in lc]
        if len(matches) > 1:
            # If projected variants are present, keep the base metric.
            base = [c for c in matches if "projected" not in lowered[c]]
            if len(base) == 1:
                return base[0]
        if len(matches) == 1:
            return matches[0]

    raise ValueError(
        f"No se pudo identificar la columna de valor. Columnas: {list(df.columns)}"
    )


def latest_by_code(df: pd.DataFrame, value_col: str, max_year: int | None = None) -> pd.DataFrame:
    work = df.copy()
    work = work[work["Code"].notna()]
    if max_year is not None:
        work = work[work["Year"] <= max_year]
    work = work[work[value_col].notna()]
    work = work.sort_values(["Code", "Year"]).groupby("Code", as_index=False).tail(1)
    return work[["Entity", "Code", "Year", value_col]].copy()


def population_for_year(df: pd.DataFrame, year: int, value_col: str) -> pd.DataFrame:
    work = df[(df["Year"] == year) & df["Code"].notna() & df[value_col].notna()].copy()
    return work[["Entity", "Code", "Year", value_col]]


def weighted_mean(values: pd.Series, weights: pd.Series) -> float | None:
    mask = values.notna() & weights.notna() & (weights > 0)
    if not mask.any():
        return None
    return float((values[mask] * weights[mask]).sum() / weights[mask].sum())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--master", default="rg_paises_areas_operativo.csv")
    parser.add_argument("--out", default="output_1c2")
    parser.add_argument("--reuse-downloads", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    master_path = (root / args.master).resolve()
    out = (root / args.out).resolve()
    raw = out / "raw"
    out.mkdir(parents=True, exist_ok=True)
    raw.mkdir(parents=True, exist_ok=True)

    files = {
        "population": raw / "population-with-un-projections.csv",
        "median_age": raw / "median-age.csv",
        "land": raw / "land-area-hectares.csv",
    }
    urls = {
        "population": OWID_POP_URL,
        "median_age": OWID_MEDIAN_AGE_URL,
        "land": OWID_LAND_URL,
    }

    for key, path in files.items():
        if not (args.reuse_downloads and path.exists()):
            print(f"Descargando {key}...")
            download(urls[key], path)

    master = pd.read_csv(master_path, dtype={"codigo_m49": str})
    master = master[master["area_codigo"].notna() & (master["area_codigo"] != "")].copy()

    pop = pd.read_csv(files["population"])
    age = pd.read_csv(files["median_age"])
    land = pd.read_csv(files["land"])

    pop_col = find_value_column(pop, ["population (projected)", "population"])
    age_col = find_value_column(age, ["median age"])
    land_col = find_value_column(land, ["land area"])

    pop_2025 = population_for_year(pop, 2025, pop_col).rename(
        columns={"Entity": "entidad_pop", "Code": "codigo_iso3", pop_col: "poblacion_2025"}
    )
    pop_2050 = population_for_year(pop, 2050, pop_col).rename(
        columns={"Entity": "entidad_pop_2050", "Code": "codigo_iso3", pop_col: "poblacion_2050"}
    )
    age_2025 = population_for_year(age, 2025, age_col).rename(
        columns={"Entity": "entidad_edad", "Code": "codigo_iso3", age_col: "edad_mediana_2025"}
    )
    land_latest = latest_by_code(land, land_col, max_year=2023).rename(
        columns={
            "Entity": "entidad_superficie",
            "Code": "codigo_iso3",
            "Year": "anio_superficie",
            land_col: "superficie_hectareas",
        }
    )
    land_latest["superficie_km2"] = land_latest["superficie_hectareas"] / 100.0

    entity = master.merge(pop_2025[["codigo_iso3", "poblacion_2025"]], on="codigo_iso3", how="left")
    entity = entity.merge(pop_2050[["codigo_iso3", "poblacion_2050"]], on="codigo_iso3", how="left")
    entity = entity.merge(age_2025[["codigo_iso3", "edad_mediana_2025"]], on="codigo_iso3", how="left")
    entity = entity.merge(
        land_latest[["codigo_iso3", "anio_superficie", "superficie_km2"]],
        on="codigo_iso3",
        how="left",
    )

    # Kosovo auxiliary code XKX may not match OWID; keep it absent rather than guessing.
    entity["fuente_poblacion"] = "UN WPP 2024, processed by Our World in Data"
    entity["fuente_superficie"] = "FAOSTAT 2025, processed by Our World in Data"
    entity["estado_revision"] = "OK"
    missing_any = entity[
        ["poblacion_2025", "poblacion_2050", "superficie_km2"]
    ].isna().any(axis=1)
    entity.loc[missing_any, "estado_revision"] = "REVISAR"
    entity["observaciones_datos"] = ""

    entity_out = entity[
        [
            "codigo_iso3",
            "codigo_m49",
            "nombre_es",
            "area_codigo",
            "area_nombre",
            "tipo_entidad",
            "incluir_calculos",
            "superficie_km2",
            "anio_superficie",
            "poblacion_2025",
            "poblacion_2050",
            "edad_mediana_2025",
            "fuente_superficie",
            "fuente_poblacion",
            "estado_revision",
            "observaciones_datos",
        ]
    ].copy()
    entity_out.to_csv(out / "rg_territorio_poblacion_pais.csv", index=False, encoding="utf-8-sig")

    area_rows = []
    for (code, name), g in entity.groupby(["area_codigo", "area_nombre"], dropna=False):
        p25 = g["poblacion_2025"].sum(min_count=1)
        p50 = g["poblacion_2050"].sum(min_count=1)
        area_km2 = g["superficie_km2"].sum(min_count=1)
        age_mean = weighted_mean(g["edad_mediana_2025"], g["poblacion_2025"])
        area_rows.append(
            {
                "area_codigo": code,
                "area_nombre": name,
                "superficie_km2": area_km2,
                "poblacion_2025": p25,
                "densidad_2025": p25 / area_km2 if p25 and area_km2 else None,
                "edad_mediana_2025_aprox": age_mean,
                "poblacion_2050": p50,
                "variacion_2025_2050_pct": ((p50 / p25) - 1) * 100 if p25 and p50 else None,
                "entidades_totales": len(g),
                "entidades_con_poblacion": int(g["poblacion_2025"].notna().sum()),
                "entidades_con_superficie": int(g["superficie_km2"].notna().sum()),
            }
        )

    agg = pd.DataFrame(area_rows)
    world_pop = agg["poblacion_2025"].sum()
    world_land = agg["superficie_km2"].sum()
    agg["poblacion_mundial_pct"] = agg["poblacion_2025"] / world_pop * 100
    agg["superficie_mundial_pct"] = agg["superficie_km2"] / world_land * 100
    agg = agg[
        [
            "area_codigo",
            "area_nombre",
            "superficie_km2",
            "superficie_mundial_pct",
            "poblacion_2025",
            "poblacion_mundial_pct",
            "densidad_2025",
            "edad_mediana_2025_aprox",
            "poblacion_2050",
            "variacion_2025_2050_pct",
            "entidades_totales",
            "entidades_con_poblacion",
            "entidades_con_superficie",
        ]
    ].sort_values("area_codigo")
    agg.to_csv(out / "rg_agregados_territorio_poblacion.csv", index=False, encoding="utf-8-sig")

    missing = entity_out[entity_out["estado_revision"] == "REVISAR"].copy()
    missing.to_csv(out / "incidencias_territorio_poblacion.csv", index=False, encoding="utf-8-sig")

    report = f"""# Validación territorio y población — Fase 1C.2

## Resumen

- Áreas agregadas: **{len(agg)}**
- Entidades maestras: **{len(entity_out)}**
- Entidades con población 2025: **{entity_out['poblacion_2025'].notna().sum()}**
- Entidades con población 2050: **{entity_out['poblacion_2050'].notna().sum()}**
- Entidades con edad mediana 2025: **{entity_out['edad_mediana_2025'].notna().sum()}**
- Entidades con superficie: **{entity_out['superficie_km2'].notna().sum()}**
- Incidencias pendientes: **{len(missing)}**
- Población total agregada 2025: **{world_pop:,.0f}**
- Superficie terrestre agregada: **{world_land:,.0f} km²**

## Agregados

{agg.to_markdown(index=False)}

## Advertencias

1. La edad mediana del área es una media ponderada aproximada de medianas nacionales.
2. Los territorios `SEGUN_FUENTE` necesitan revisión manual si una fuente los integra en otro Estado.
3. Kosovo se mantiene sin dato cuando el proveedor no utiliza el código técnico `XKX`.
4. China, Hong Kong, Macao y Taiwán deben revisarse expresamente para descartar duplicidades.
5. La superficie procede de FAOSTAT y se convierte de hectáreas a km².
"""
    (out / "validacion-territorio-poblacion-1c2.md").write_text(report, encoding="utf-8")

    metadata = {
        "population_url": OWID_POP_URL,
        "median_age_url": OWID_MEDIAN_AGE_URL,
        "land_url": OWID_LAND_URL,
        "population_source": "United Nations World Population Prospects 2024",
        "land_source": "FAOSTAT 2025",
        "processing": "Our World in Data",
    }
    (out / "fuentes_1c2.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    print(f"Completado. Salida: {out}")
    print(agg.to_string(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
