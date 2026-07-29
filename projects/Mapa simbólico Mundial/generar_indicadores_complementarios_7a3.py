"""Genera los artefactos de preparación de la Fase 7A.3.

Solo lee archivos locales congelados y escribe artefactos de trabajo. No conecta
con MySQL, la API ni la web.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "reticula_global_1c2_runner" / "output_1c2"
AREAS = ("AFR", "APC", "CHN", "EUR", "MDE", "NAC", "RUE", "SAI", "SAM")
PERIODO = "RG2025_V1"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def number(value: str | None) -> float | None:
    if value is None or value.strip() == "":
        return None
    return float(value)


def year_is(value: str | None, expected: int) -> bool:
    parsed = number(value)
    return parsed is not None and int(parsed) == expected


def population_lookup() -> dict[tuple[str, int], float]:
    result: dict[tuple[str, int], float] = {}
    for row in read_csv(OUTPUT / "raw" / "population-with-un-projections.csv"):
        code = row["Code"].strip()
        if len(code) != 3:
            continue
        year = int(row["Year"])
        observed = number(row["Population"])
        projected = number(row["Population (Projected)"])
        value = observed if observed is not None else projected
        if value is not None:
            result[(code, year)] = value
    return result


def median_lookup() -> dict[tuple[str, int], float]:
    result: dict[tuple[str, int], float] = {}
    for row in read_csv(OUTPUT / "raw" / "median-age.csv"):
        code = row["Code"].strip()
        if len(code) != 3:
            continue
        year = int(row["Year"])
        observed = number(row["Median age"])
        projected = number(row["Median age (Projected)"])
        value = observed if observed is not None else projected
        if value is not None:
            result[(code, year)] = value
    return result


def coverage_state(value: float, observation: bool = False) -> str:
    if value < 95:
        return "COBERTURA INSUFICIENTE"
    return "VALIDADO CON OBSERVACIÓN" if observation else "VALIDADO"


def main() -> None:
    territory = read_csv(OUTPUT / "rg_territorio_poblacion_pais.csv")
    economy = {
        row["codigo_iso3"]: row
        for row in read_csv(OUTPUT / "rg_economia_pais.csv")
    }
    human = {
        row["codigo_iso3"]: row
        for row in read_csv(OUTPUT / "rg_desarrollo_humano_pais.csv")
    }
    population = population_lookup()
    median = median_lookup()

    countries = [
        {
            "code": row["codigo_iso3"],
            "area": row["area_codigo"],
            "name": row["nombre_es"],
            # SEGUN_FUENTE entra cuando la fuente publica la entidad por separado.
            # Los CSV nacionales ya resolvieron esa decisión sin crear otra lista.
            "eligible": row["incluir_calculos"].strip().upper() in ("SI", "SEGUN_FUENTE"),
            "surface": number(row["superficie_km2"]),
            "surface_year": row["anio_superficie"],
            "population_2025": number(row["poblacion_2025"]),
        }
        for row in territory
        if row["area_codigo"] in AREAS
    ]
    by_area: dict[str, list[dict[str, object]]] = defaultdict(list)
    for country in countries:
        by_area[str(country["area"])].append(country)

    results: list[dict[str, object]] = []
    incidents: list[dict[str, str]] = []
    coverage_rows: list[dict[str, str]] = []

    definitions = {
        "TERR_DENS": ("hab/km2", "Poblacion 2025 / superficie terrestre 2023"),
        "POB_URB": ("%", "Poblacion urbana / poblacion total cubierta * 100"),
        "POB_EDAD": ("anios", "Media ponderada aproximada de medianas nacionales 2023"),
        "HUM_EV": ("anios", "Media nacional 2023 ponderada por poblacion 2023"),
        "ECO_PC": ("USD_corrientes_por_hab", "PIB nominal 2024 / poblacion cubierta 2024"),
        "HUM_IDH": ("indice_0_1", "IDH nacional 2023 ponderado por poblacion 2023"),
    }

    for indicator in definitions:
        for area in AREAS:
            area_countries = [c for c in by_area[area] if c["eligible"]]
            included: list[tuple[dict[str, object], float, float | None]] = []
            total_population = 0.0
            population_year = 2025 if indicator == "TERR_DENS" else 2024 if indicator == "ECO_PC" else 2023

            for country in area_countries:
                code = str(country["code"])
                pop = (
                    country["population_2025"]
                    if population_year == 2025
                    else population.get((code, population_year))
                )
                if pop is not None:
                    total_population += float(pop)

                value: float | None = None
                reason = ""
                if indicator == "TERR_DENS":
                    value = country["surface"]
                    reason = "Falta superficie terrestre 2023" if value is None else ""
                elif indicator == "POB_URB":
                    reason = "No existe serie nacional de poblacion urbana incorporada"
                elif indicator == "POB_EDAD":
                    value = median.get((code, 2023))
                    reason = "Falta edad mediana nacional 2023" if value is None else ""
                elif indicator == "HUM_EV":
                    row = human.get(code)
                    if row and year_is(row["anio_esperanza_vida"], 2023):
                        value = number(row["esperanza_vida"])
                    reason = "Falta esperanza de vida nacional 2023" if value is None else ""
                elif indicator == "ECO_PC":
                    row = economy.get(code)
                    if row and year_is(row["anio_pib"], 2024):
                        value = number(row["pib_usd"])
                    if row and value is None and number(row["pib_usd"]) is not None:
                        reason = f"PIB disponible solo para {row['anio_pib']}; se exige 2024"
                    elif value is None:
                        reason = "Falta PIB nominal nacional 2024"
                elif indicator == "HUM_IDH":
                    row = human.get(code)
                    if row and year_is(row["anio_idh"], 2023):
                        value = number(row["idh"])
                    reason = "Falta IDH nacional 2023" if value is None else ""

                usable = value is not None and pop is not None and indicator != "POB_URB"
                coverage_rows.append(
                    {
                        "codigo_indicador": indicator,
                        "codigo_pais": code,
                        "codigo_area": area,
                        "incluido": "SI" if usable else "NO",
                        "motivo": "" if usable else reason or f"Falta poblacion {population_year}",
                    }
                )
                if usable:
                    included.append((country, float(value), float(pop)))
                else:
                    incident_type = (
                        "DATO_NO_INCORPORADO"
                        if indicator == "POB_URB"
                        else "PERIODO_INCOMPATIBLE"
                        if "se exige" in reason
                        else "DATO_AUSENTE"
                    )
                    description = reason or f"Falta poblacion nacional {population_year}"
                    incidents.append(
                        {
                            "codigo_indicador": indicator,
                            "codigo_pais": code,
                            "codigo_area": area,
                            "tipo_incidencia": incident_type,
                            "descripcion": description,
                            "accion_propuesta": (
                                "Incorporar una fuente nacional comparable antes de calcular"
                                if indicator == "POB_URB"
                                else "Mantener ausente; localizar dato comparable del mismo periodo"
                            ),
                        }
                    )

            covered_population = sum(item[2] for item in included)
            coverage = (
                covered_population / total_population * 100
                if total_population > 0
                else 0.0
            )
            value: float | None
            observation = ""
            if indicator == "TERR_DENS":
                surface = sum(item[1] for item in included)
                value = covered_population / surface if surface > 0 else None
                observation = "Cociente de totales; superficie estructural 2023 y poblacion 2025."
            elif indicator == "POB_URB":
                value = None
                observation = "No existe dato nacional incorporado; no se imputa cero."
            elif indicator in ("POB_EDAD", "HUM_EV", "HUM_IDH"):
                value = (
                    sum(item[1] * item[2] for item in included) / covered_population
                    if covered_population > 0
                    else None
                )
                if indicator == "POB_EDAD":
                    observation = "Aproximacion: media ponderada de medianas, no mediana regional publicada."
                elif indicator == "HUM_IDH":
                    observation = "IDH medio ponderado; no es un IDH oficial del area."
                else:
                    observation = "Media nacional ponderada; no es una tabla de mortalidad regional."
            else:
                total_gdp = sum(item[1] for item in included)
                value = total_gdp / covered_population if covered_population > 0 else None
                observation = "Solo PIB nominal y poblacion de 2024 para las mismas entidades."

            if indicator == "POB_URB":
                state = "PENDIENTE DE DATO"
            elif value is None:
                state = "NO CALCULABLE"
            else:
                state = coverage_state(
                    coverage,
                    observation=indicator in ("TERR_DENS", "POB_EDAD", "HUM_EV", "HUM_IDH", "ECO_PC"),
                )
            results.append(
                {
                    "periodo": PERIODO,
                    "codigo_area": area,
                    "codigo_indicador": indicator,
                    "valor": value,
                    "unidad": definitions[indicator][0],
                    "cobertura_pct": coverage,
                    "metodo": definitions[indicator][1],
                    "estado": state,
                    "observaciones": (
                        f"{observation} Incluidos {len(included)} de {len(area_countries)}; "
                        f"poblacion cubierta {covered_population:.0f} de {total_population:.0f}."
                    ),
                    "included": [str(item[0]["code"]) for item in included],
                    "missing": [
                        str(c["code"])
                        for c in area_countries
                        if str(c["code"]) not in {str(item[0]["code"]) for item in included}
                    ],
                    "population_year": population_year,
                    "countries_total": len(area_countries),
                    "countries_included": len(included),
                }
            )

    write_outputs(results, incidents, coverage_rows)


def sql_text(results: list[dict[str, object]]) -> str:
    loadable = [
        row
        for row in results
        if row["valor"] is not None
        and row["estado"] in ("VALIDADO", "VALIDADO CON OBSERVACIÓN")
    ]
    values = []
    for row in loadable:
        observation = str(row["observaciones"]).replace("'", "''")
        method = str(row["metodo"]).replace("'", "''")
        year = int(row["population_year"])
        values.append(
            "('{area}','{indicator}',{year},{value:.10f},'{method}',{total},{included},{coverage:.6f},"
            "'{observation}')".format(
                area=row["codigo_area"],
                indicator=row["codigo_indicador"],
                year=year,
                value=float(row["valor"]),
                method=method,
                total=int(row["countries_total"]),
                included=int(row["countries_included"]),
                coverage=float(row["cobertura_pct"]),
                observation=observation,
            )
        )
    return """-- PROPUESTA PROVISIONAL 7A.3. NO EJECUTADA.
-- Requiere validacion definitiva en una fase posterior.
USE `u794456529_map_sim_Mund`;
SET NAMES utf8mb4;

-- La tabla de respaldo permite ejecutar 94_reversion_indicadores_complementarios_7a3.sql.
-- Confirmar antes que no exista una copia de una ejecucion anterior.
CREATE TABLE rg_backup_datos_area_7a3 LIKE rg_datos_area;
INSERT INTO rg_backup_datos_area_7a3
SELECT da.*
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
WHERE p.codigo='RG2025_V1'
  AND i.codigo IN ('TERR_DENS','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH');

CREATE TEMPORARY TABLE tmp_rg_area_7a3 (
  codigo_area CHAR(3) NOT NULL,
  codigo_indicador VARCHAR(40) NOT NULL,
  anio_referencia SMALLINT NOT NULL,
  valor DECIMAL(22,10) NOT NULL,
  metodo_calculo VARCHAR(255) NOT NULL,
  paises_totales SMALLINT UNSIGNED NOT NULL,
  paises_con_dato SMALLINT UNSIGNED NOT NULL,
  cobertura_pct DECIMAL(8,4) NOT NULL,
  observaciones TEXT NULL,
  PRIMARY KEY (codigo_area,codigo_indicador)
);

INSERT INTO tmp_rg_area_7a3
(codigo_area,codigo_indicador,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,cobertura_pct,observaciones)
VALUES
""" + ",\n".join(values) + """;

START TRANSACTION;
UPDATE rg_datos_area da
JOIN rg_areas a ON a.id=da.area_id
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
JOIN tmp_rg_area_7a3 t ON t.codigo_area=a.codigo AND t.codigo_indicador=i.codigo
SET da.anio_referencia=t.anio_referencia,
    da.valor=t.valor,
    da.metodo_calculo=t.metodo_calculo,
    da.paises_totales=t.paises_totales,
    da.paises_con_dato=t.paises_con_dato,
    da.porcentaje_cobertura=t.cobertura_pct,
    da.anio_minimo=t.anio_referencia,
    da.anio_maximo=t.anio_referencia,
    da.tipo_procedencia='CALCULO_7A3',
    da.estado_dato=CASE WHEN t.cobertura_pct>=95 THEN 'OK' ELSE 'LIMITACION' END,
    da.fecha_calculo=CURDATE(),
    da.observaciones=t.observaciones
WHERE p.codigo='RG2025_V1';

SELECT ROW_COUNT() AS filas_actualizadas;
SELECT i.codigo,COUNT(*) AS filas
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
WHERE p.codigo='RG2025_V1'
  AND i.codigo IN ('TERR_DENS','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH')
GROUP BY i.codigo;
COMMIT;

-- POB_URB se excluye: no existen datos nacionales comparables incorporados.
"""


def reversal_text() -> str:
    return """-- REVERSION ASOCIADA A 28_carga_indicadores_complementarios_7a3.sql.
-- NO EJECUTADA. Verificar primero que rg_backup_datos_area_7a3 existe y contiene 45 filas.
USE `u794456529_map_sim_Mund`;
SET NAMES utf8mb4;

SELECT COUNT(*) AS filas_respaldo FROM rg_backup_datos_area_7a3;

START TRANSACTION;
DELETE da
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
WHERE p.codigo='RG2025_V1'
  AND i.codigo IN ('TERR_DENS','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH');

INSERT INTO rg_datos_area
SELECT * FROM rg_backup_datos_area_7a3;

SELECT COUNT(*) AS filas_restauradas
FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
WHERE p.codigo='RG2025_V1'
  AND i.codigo IN ('TERR_DENS','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH');
COMMIT;

-- Ejecutar DROP solo despues de comprobar la restauracion:
-- DROP TABLE rg_backup_datos_area_7a3;
"""


def write_outputs(
    results: list[dict[str, object]],
    incidents: list[dict[str, str]],
    coverage_rows: list[dict[str, str]],
) -> None:
    data_path = ROOT / "datos-area-indicadores-complementarios-7a3.csv"
    with data_path.open("w", encoding="utf-8", newline="") as handle:
        fields = [
            "periodo",
            "codigo_area",
            "codigo_indicador",
            "valor",
            "unidad",
            "cobertura_pct",
            "metodo",
            "observaciones",
        ]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in results:
            writer.writerow(
                {
                    key: (
                        ""
                        if key == "valor" and row[key] is None
                        else f"{float(row[key]):.10f}".rstrip("0").rstrip(".")
                        if key == "valor"
                        else f"{float(row[key]):.4f}"
                        if key == "cobertura_pct"
                        else row[key]
                    )
                    for key in fields
                }
            )

    incident_path = ROOT / "incidencias-indicadores-complementarios-7a3.csv"
    with incident_path.open("w", encoding="utf-8", newline="") as handle:
        fields = [
            "codigo_indicador",
            "codigo_pais",
            "codigo_area",
            "tipo_incidencia",
            "descripcion",
            "accion_propuesta",
        ]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(incidents)

    coverage_path = ROOT / "cobertura-paises-indicadores-complementarios-7a3.csv"
    with coverage_path.open("w", encoding="utf-8", newline="") as handle:
        fields = ["codigo_indicador", "codigo_pais", "codigo_area", "incluido", "motivo"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(coverage_rows)

    (ROOT / "28_carga_indicadores_complementarios_7a3.sql").write_text(
        sql_text(results), encoding="utf-8"
    )
    (ROOT / "94_reversion_indicadores_complementarios_7a3.sql").write_text(
        reversal_text(), encoding="utf-8"
    )

    lines = [
        "# Preparación de datos de indicadores complementarios — Fase 7A.3",
        "",
        "Fecha: 2026-07-28  ",
        "Edición: `RG2025_V1`",
        "",
        "## Alcance",
        "",
        "Cálculo local reproducible a partir de los archivos nacionales y fuentes congeladas existentes. No se ha conectado ni escrito en MySQL; el SQL generado es una propuesta provisional no ejecutada.",
        "",
        "## Resultados por indicador y área",
        "",
        "| Indicador | Área | Valor calculado | Unidad | Periodo | Cobertura | Método | Estado | Observaciones |",
        "|---|---|---:|---|---|---:|---|---|---|",
    ]
    for row in results:
        value = "NO DISPONIBLE" if row["valor"] is None else f"{float(row['valor']):.6f}"
        lines.append(
            f"| `{row['codigo_indicador']}` | {row['codigo_area']} | {value} | "
            f"{row['unidad']} | {row['population_year']} | {float(row['cobertura_pct']):.2f} % | "
            f"{row['metodo']} | {row['estado']} | {row['observaciones']} |"
        )
    lines.extend(
        [
            "",
            "## Entidades incluidas y ausentes",
            "",
            "La relación completa, país por país, se conserva en `cobertura-paises-indicadores-complementarios-7a3.csv`. En cada fila se indica inclusión y motivo de exclusión. Las ausencias que requieren actuación se duplican de forma normalizada en `incidencias-indicadores-complementarios-7a3.csv`.",
            "",
        ]
    )
    for indicator in ("TERR_DENS", "POB_URB", "POB_EDAD", "HUM_EV", "ECO_PC", "HUM_IDH"):
        lines.append(f"### `{indicator}`")
        lines.append("")
        for row in [item for item in results if item["codigo_indicador"] == indicator]:
            included = ", ".join(row["included"]) or "ninguno"
            missing = ", ".join(row["missing"]) or "ninguno"
            lines.append(f"- **{row['codigo_area']}** — incluidos: {included}; ausentes: {missing}.")
        lines.append("")
    lines.extend(
        [
            "## Incidencias metodológicas",
            "",
            "- `POB_URB` no dispone de serie nacional incorporada y queda sin valor para las nueve áreas.",
            "- `POB_EDAD` es una media ponderada de medianas nacionales, no una mediana regional publicada.",
            "- `HUM_EV` es una media ponderada y no una esperanza de vida calculada desde una tabla regional conjunta.",
            "- `HUM_IDH` se denomina «IDH medio ponderado» y no es un IDH oficial de las macroáreas.",
            "- `ECO_PC` usa exclusivamente PIB nominal y población de 2024; los respaldos de otro año se excluyen.",
            "- `TERR_DENS` combina población 2025 con la superficie estructural disponible de 2023, mostrando ambos años.",
            "",
            "## Compatibilidad de fuentes, unidades y periodos",
            "",
            "- Densidad: población ONU WPP/OWID en personas y superficie FAOSTAT/OWID en km²; unidades compatibles.",
            "- Edad mediana: serie OWID 2023 en años y población 2023 de la misma familia demográfica; cálculo reproducible, pero aproximado.",
            "- Esperanza de vida: WDI 2023 en años y población 2023; cálculo reproducible.",
            "- PIB por habitante: solo se aceptan observaciones de PIB nominal 2024 en USD corrientes y población 2024. Los datos de 2023 se registran como incompatibilidad temporal y no entran en el cálculo.",
            "- IDH: PNUD 2023, escala 0–1, ponderado con población 2023; cálculo reproducible y denominación no oficial documentada.",
            "- Población urbana: no existe una serie incorporada con unidad, año y definición comparables; no es reproducible en esta fase.",
            "",
            "## Valores extremos",
            "",
        ]
    )
    for indicator in ("TERR_DENS", "POB_EDAD", "HUM_EV", "ECO_PC", "HUM_IDH"):
        rows = [r for r in results if r["codigo_indicador"] == indicator and r["valor"] is not None]
        if not rows:
            lines.append(f"- `{indicator}`: no calculable con los archivos disponibles.")
            continue
        low = min(rows, key=lambda item: float(item["valor"]))
        high = max(rows, key=lambda item: float(item["valor"]))
        lines.append(
            f"- `{indicator}`: mínimo {low['codigo_area']} = {float(low['valor']):.6f}; "
            f"máximo {high['codigo_area']} = {float(high['valor']):.6f}. "
            "Son extremos aritméticamente reproducibles; requieren revisión sustantiva en 7A.4."
        )
    lines.extend(
        [
            "",
            "## SQL provisional y reversión",
            "",
            "`28_carga_indicadores_complementarios_7a3.sql` prepara una copia completa de las 45 filas existentes, carga en una tabla temporal únicamente resultados con cobertura ≥95 % y actualiza esas filas. No contiene `POB_URB`. El archivo no se ha ejecutado.",
            "",
            "`94_reversion_indicadores_complementarios_7a3.sql` restaura exactamente las filas guardadas por la carga. La eliminación de la tabla de respaldo queda comentada y solo debe realizarse después de verificar la restauración.",
            "",
            "## Preparación para una futura carga",
            "",
            "- `TERR_DENS`: 9 de 9 áreas candidatas.",
            "- `POB_EDAD`: 9 de 9 áreas candidatas, siempre etiquetadas como aproximación.",
            "- `HUM_EV`: 9 de 9 áreas candidatas.",
            "- `ECO_PC`: 7 de 9 áreas candidatas; APC y MDE quedan fuera por cobertura inferior al 95 %.",
            "- `HUM_IDH`: 8 de 9 áreas candidatas; APC queda fuera por cobertura inferior al 95 %.",
            "- `POB_URB`: 0 de 9 áreas; pendiente de incorporar datos nacionales.",
            "",
            "## Resultado de preparación",
            "",
            "Los valores son propuestas reproducibles, no una validación definitiva. Solo son candidatos a carga los resultados calculables con cobertura ≥95 %. Las filas con cobertura inferior y todo `POB_URB` quedan excluidos del SQL provisional.",
        ]
    )
    (ROOT / "PREPARACION-DATOS-INDICADORES-FASE-7A3.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
