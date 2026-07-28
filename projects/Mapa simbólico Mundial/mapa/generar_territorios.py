"""Genera la lista territorial pública desde el maestro operativo RG2025."""

import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE.parent / "reticula_global_1c2_runner" / "rg_paises_areas_operativo.csv"
OUTPUT = BASE / "territorios.json"

AREAS = ("AFR", "APC", "CHN", "EUR", "MDE", "NAC", "RUE", "SAI", "SAM")


def main() -> None:
    grouped = {code: [] for code in AREAS}
    with SOURCE.open(encoding="utf-8-sig", newline="") as stream:
        for row in csv.DictReader(stream):
            code = row["area_codigo"]
            if code not in grouped:
                continue
            grouped[code].append(
                {
                    "iso3": row["codigo_iso3"],
                    "nombre": row["nombre_es"],
                    "tipo": row["tipo_entidad"],
                    "soberania": row["estado_soberania"],
                    "incluir_mapa": row["incluir_mapa"],
                    "incluir_calculos": row["incluir_calculos"],
                    "entidad_soberana_iso3": row["entidad_soberana_iso3"] or None,
                    "observaciones": row["observaciones"] or None,
                }
            )

    payload = {
        "edicion": "RG2025_V1",
        "fuente": "../reticula_global_1c2_runner/rg_paises_areas_operativo.csv",
        "areas": [
            {
                "codigo": code,
                "entidades": sorted(grouped[code], key=lambda item: item["nombre"]),
            }
            for code in AREAS
        ],
    }
    OUTPUT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
