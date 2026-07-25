"""Genera datos-indicadores.json desde los agregados congelados RG2025_V1.

No consulta MySQL ni la API. Los valores naturales proceden exclusivamente de
los CSV validados de output_1c2; los metadatos reproducen los catálogos SQL de
esa misma edición congelada.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


BASE = Path(__file__).resolve().parent
OUTPUT = BASE.parent / "reticula_global_1c2_runner" / "output_1c2"
AREA_ORDER = ["AFR", "APC", "CHN", "EUR", "MDE", "NAC", "RUE", "SAI", "SAM"]

SOURCES = {
    "POB_TOTAL": {
        "anio": 2025,
        "unidad": "personas",
        "fuente_codigo": "UN_WPP_2024",
        "fuente": "ONU World Population Prospects 2024",
    },
    "TERR_SUP": {
        "anio": 2023,
        "unidad": "km2",
        "fuente_codigo": "FAOSTAT_2025",
        "fuente": "FAOSTAT",
    },
    "ECO_PIB": {
        "anio": 2024,
        "unidad": "USD_corrientes",
        "fuente_codigo": "WB_WDI",
        "fuente": "Banco Mundial — World Development Indicators",
    },
    "MIL_GASTO": {
        "anio": 2025,
        "unidad": "usd_corrientes",
        "fuente_codigo": "SIPRI_MILEX_2026",
        "fuente": "SIPRI Military Expenditure Database 2025 (edición 2026)",
    },
    "MIL_NUC": {
        "anio": 2026,
        "unidad": "ojivas",
        "fuente_codigo": "SIPRI_YB26_NUC",
        "fuente": "SIPRI Yearbook 2026 — World nuclear forces",
    },
}


def read_indexed_csv(filename: str) -> dict[str, dict[str, str]]:
    with (OUTPUT / filename).open(encoding="utf-8-sig", newline="") as source:
        rows = list(csv.DictReader(source))
    indexed = {row["area_codigo"]: row for row in rows}
    if len(rows) != 9 or len(indexed) != 9 or set(indexed) != set(AREA_ORDER):
        raise ValueError(f"{filename}: se esperaban las nueve áreas exactas y sin duplicados")
    return indexed


territory = read_indexed_csv("rg_agregados_territorio_poblacion.csv")
economy = read_indexed_csv("rg_agregados_economia.csv")
military = read_indexed_csv("rg_agregados_militar.csv")

area_document = json.loads((BASE / "areas.json").read_text(encoding="utf-8"))
display_names = {area["codigo"]: area["nombre"] for area in area_document["areas"]}

areas = []
for code in AREA_ORDER:
    economy_note = economy[code]["observaciones"].strip()
    military_note = military[code]["observaciones"].strip()
    areas.append(
        {
            "codigo": code,
            "nombre": display_names[code],
            "indicadores": {
                "POB_TOTAL": {
                    **SOURCES["POB_TOTAL"],
                    "valor": float(territory[code]["poblacion_2025"]),
                    "observaciones": "",
                },
                "TERR_SUP": {
                    **SOURCES["TERR_SUP"],
                    "valor": float(territory[code]["superficie_km2"]),
                    "observaciones": "",
                },
                "ECO_PIB": {
                    **SOURCES["ECO_PIB"],
                    "valor": float(economy[code]["pib_usd"]),
                    "anio_minimo": int(economy[code]["anio_minimo"]),
                    "anio_maximo": int(economy[code]["anio_maximo"]),
                    "observaciones": economy_note,
                },
                "MIL_GASTO": {
                    **SOURCES["MIL_GASTO"],
                    "valor": float(military[code]["gasto_militar_usd"]),
                    "anio_minimo": int(military[code]["anio_min_gasto"]),
                    "anio_maximo": int(military[code]["anio_max_gasto"]),
                    "observaciones": military_note,
                },
                "MIL_NUC": {
                    **SOURCES["MIL_NUC"],
                    "valor": int(military[code]["ojivas_nucleares_estimadas"]),
                    "observaciones": military_note,
                },
            },
        }
    )

document = {
    "edicion": {
        "codigo": "RG2025_V1",
        "estado": "congelado",
    },
    "generado_desde": [
        "../reticula_global_1c2_runner/output_1c2/rg_agregados_territorio_poblacion.csv",
        "../reticula_global_1c2_runner/output_1c2/rg_agregados_economia.csv",
        "../reticula_global_1c2_runner/output_1c2/rg_agregados_militar.csv",
    ],
    "indicadores": SOURCES,
    "areas": areas,
}

(BASE / "datos-indicadores.json").write_text(
    json.dumps(document, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
print(f"Generado datos-indicadores.json: {len(areas)} áreas × {len(SOURCES)} indicadores")
