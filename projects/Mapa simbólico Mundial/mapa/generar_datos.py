"""Genera areas.json, world.geojson e informe-correspondencias.json.

Fuente territorial única:
../reticula_global_1c2_runner/rg_paises_areas_operativo.csv

Fuente geométrica:
../natural-earth-source/ne_10m_admin_0_countries.shp
Natural Earth, Admin 0 Countries 1:10m, dominio público.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import shapefile


BASE = Path(__file__).resolve().parent
PROJECT = BASE.parent
CSV_PATH = PROJECT / "reticula_global_1c2_runner" / "rg_paises_areas_operativo.csv"
SHP_PATH = PROJECT / "natural-earth-source" / "ne_10m_admin_0_countries.shp"

AREA_ORDER = ["AFR", "APC", "CHN", "EUR", "MDE", "NAC", "RUE", "SAI", "SAM"]
AREA_DISPLAY_NAMES = {
    "AFR": "África",
    "APC": "Asia-Pacífico",
    "CHN": "China",
    "EUR": "Europa",
    "MDE": "Oriente Medio",
    "NAC": "Norteamérica, Centroamérica y Caribe",
    "RUE": "Rusia-Eurasia",
    "SAI": "Subcontinente indio",
    "SAM": "Sudamérica",
}
SIMPLIFICATION_TOLERANCE = 0.025


def _squared_distance_to_segment(point, start, end):
    px, py = point
    ax, ay = start
    bx, by = end
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        return (px - ax) ** 2 + (py - ay) ** 2
    ratio = max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    nearest_x, nearest_y = ax + ratio * dx, ay + ratio * dy
    return (px - nearest_x) ** 2 + (py - nearest_y) ** 2


def simplify_ring(ring, tolerance=SIMPLIFICATION_TOLERANCE):
    """Douglas-Peucker sobre un anillo; conserva cierre y un mínimo válido."""
    points = list(ring[:-1] if ring and ring[0] == ring[-1] else ring)
    if len(points) <= 4:
        return list(ring)

    keep = {0, len(points) - 1}
    stack = [(0, len(points) - 1)]
    threshold = tolerance * tolerance
    while stack:
        start_index, end_index = stack.pop()
        start, end = points[start_index], points[end_index]
        best_index, best_distance = None, threshold
        for index in range(start_index + 1, end_index):
            distance = _squared_distance_to_segment(points[index], start, end)
            if distance > best_distance:
                best_index, best_distance = index, distance
        if best_index is not None:
            keep.add(best_index)
            stack.extend(((start_index, best_index), (best_index, end_index)))

    simplified = [points[index] for index in sorted(keep)]
    if len(simplified) < 3:
        return list(ring)
    return simplified + [simplified[0]]


def compact_geojson_geometry(shape: shapefile.Shape) -> dict:
    geometry = shape.__geo_interface__
    polygons = (
        [geometry["coordinates"]]
        if geometry["type"] == "Polygon"
        else geometry["coordinates"]
    )
    simplified = [
        [simplify_ring(ring) for ring in polygon]
        for polygon in polygons
    ]
    return {
        "type": geometry["type"],
        "coordinates": simplified[0] if geometry["type"] == "Polygon" else simplified,
    }


with CSV_PATH.open(encoding="utf-8-sig", newline="") as source:
    rows = list(csv.DictReader(source))

territories = {
    row["codigo_iso3"]: {
        "iso3": row["codigo_iso3"],
        "iso2": row["codigo_iso2"],
        "nombre": row["nombre_es"] or row["nombre_m49"],
        "area": row["area_codigo"],
        "area_nombre": row["area_nombre"],
        "incluir_mapa": row["incluir_mapa"] == "SI",
        "incluir_calculos": row["incluir_calculos"] == "SI",
        "tipo_entidad": row["tipo_entidad"],
        "tratamiento": row["tratamiento_fuente"],
    }
    for row in rows
}

areas = []
for code in AREA_ORDER:
    members = [item for item in territories.values() if item["area"] == code]
    areas.append(
        {
            "codigo": code,
            "nombre": AREA_DISPLAY_NAMES[code],
            "nombre_maestro": members[0]["area_nombre"] if members else code,
            "paises_csv": len(members),
            "iso3": [item["iso3"] for item in members if item["incluir_mapa"]],
        }
    )

reader = shapefile.Reader(str(SHP_PATH), encoding="utf-8")
field_names = [field[0] for field in reader.fields[1:]]
features = []
unresolved_map = []
mapped_iso3 = set()

for shape_record in reader.iterShapeRecords():
    record = dict(zip(field_names, shape_record.record))
    candidates = []
    for key in ("ISO_A3", "ADM0_A3", "GU_A3", "SU_A3", "SOV_A3"):
        value = record.get(key)
        if value and value != "-99" and value not in candidates:
            candidates.append(value)

    match = next((territories[code] for code in candidates if code in territories), None)
    if match and match["incluir_mapa"]:
        mapped_iso3.add(match["iso3"])
        props = {
            "iso3": match["iso3"],
            "name": match["nombre"],
            "area": match["area"],
            "area_name": match["area_nombre"],
            "included": match["incluir_calculos"],
            "type": match["tipo_entidad"],
        }
    else:
        props = {
            "iso3": candidates[0] if candidates else record.get("ADM0_A3", "—"),
            "name": record.get("NAME_ES") or record.get("NAME") or "Entidad sin nombre",
            "area": None,
            "area_name": "Fuera de los cálculos",
            "included": False,
            "type": record.get("TYPE", ""),
        }
        unresolved_map.append(
            {
                "nombre_cartografia": props["name"],
                "codigos_cartografia": candidates,
                "motivo": "Sin correspondencia ISO3 exacta en el CSV o excluir del mapa.",
            }
        )

    features.append(
        {
            "type": "Feature",
            "properties": props,
            "geometry": compact_geojson_geometry(shape_record.shape),
        }
    )

missing_geometry = sorted(
    code
    for code, item in territories.items()
    if item["incluir_mapa"] and code not in mapped_iso3
)

checks = {
    code: territories.get(code, {}).get("area")
    for code in ("MEX", "RUS", "BLR", "GEO", "ARM", "AZE", "IRN", "CYP", "CHN", "HKG", "MAC", "TWN", "IND")
}

report = {
    "fuente_territorial": str(CSV_PATH.relative_to(PROJECT)).replace("\\", "/"),
    "fuente_cartografica": "Natural Earth Admin 0 Countries 1:10m, versión 5.1.1, dominio público",
    "entidades_csv": len(territories),
    "entidades_cartograficas": len(features),
    "iso3_coloreados": len(mapped_iso3),
    "iso3_csv_sin_geometria": missing_geometry,
    "entidades_cartograficas_sin_correspondencia": unresolved_map,
    "verificaciones_solicitadas": checks,
}

correspondences = {
    "criterio": (
        "Relación diagnóstica; no contiene equivalencias aplicadas. "
        "Toda diferencia permanece neutral hasta una decisión editorial explícita."
    ),
    "cartografia_sin_correspondencia_en_areas": unresolved_map,
    "maestro_territorial_sin_geometria_independiente": [
        {
            "iso3": code,
            "nombre": territories[code]["nombre"],
            "area": territories[code]["area"],
            "observacion": (
                "No se encontró una geometría independiente con correspondencia ISO3 "
                "en Natural Earth Admin 0 Countries 1:10m."
            ),
        }
        for code in missing_geometry
    ],
    "codigos_cartograficos_no_iso3_estandar": [
        {
            "nombre_cartografia": item["nombre_cartografia"],
            "codigos": item["codigos_cartografia"],
        }
        for item in unresolved_map
    ],
    "territorios_demasiado_pequenos_o_integrados_en_otra_geometria": [
        {
            "iso3": code,
            "nombre": territories[code]["nombre"],
            "estado": "Pendiente de distinguir entre tamaño insuficiente e integración cartográfica.",
        }
        for code in missing_geometry
    ],
}

(BASE / "areas.json").write_text(
    json.dumps({"areas": areas, "territorios": territories}, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
(BASE / "world.geojson").write_text(
    json.dumps({"type": "FeatureCollection", "features": features}, ensure_ascii=False, separators=(",", ":")),
    encoding="utf-8",
)
(BASE / "informe-correspondencias.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
(BASE / "correspondencias-cartograficas.json").write_text(
    json.dumps(correspondences, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
print(json.dumps(report, ensure_ascii=False, indent=2))
