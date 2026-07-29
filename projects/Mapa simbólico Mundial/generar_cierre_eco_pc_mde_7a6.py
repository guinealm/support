"""Genera el CSV 7A.6 cambiando exclusivamente el estado ECO_PC/MDE."""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
source = ROOT / "datos-area-indicadores-complementarios-7a5.csv"
target = ROOT / "datos-area-indicadores-complementarios-7a6.csv"

with source.open("r", encoding="utf-8-sig", newline="") as handle:
    rows = list(csv.DictReader(handle))

for row in rows:
    if row["codigo_indicador"] == "ECO_PC" and row["codigo_area"] == "MDE":
        row["estado"] = "NO PUBLICABLE"
        row["observaciones"] = (
            "Siria no tiene PIB nominal 2024 comparable. El dato WDI 2022 se rechaza "
            "por desfase temporal; Yemen sí está incorporado mediante FMI. "
            "Cobertura 93.5486%; no publicar bajo criterio estricto."
        )

fields = list(rows[0])
with target.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

assert len(rows) == 54
assert len({(r["codigo_indicador"], r["codigo_area"]) for r in rows}) == 54
