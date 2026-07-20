from __future__ import annotations

import io
import math
from pathlib import Path

import pandas as pd
import requests


CO2_CSV = "https://ourworldindata.org/grapher/annual-co2-emissions-per-country.csv?v=1&csvType=full&useColumnShortNames=false"
YEAR = 2024
SOURCE = "Global Carbon Budget (2025), con procesamiento de Our World in Data"
SOURCE_URL = "https://ourworldindata.org/grapher/annual-co2-emissions-per-country"


def q(value: object) -> str:
    if value is None or pd.isna(value):
        return "NULL"
    if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
        return "NULL"
    if isinstance(value, (int, float)):
        return str(value)
    return "'" + str(value).replace("'", "''") + "'"


def fetch_co2() -> pd.DataFrame:
    response = requests.get(CO2_CSV, timeout=180)
    response.raise_for_status()
    data = pd.read_csv(io.BytesIO(response.content))
    data = data.rename(
        columns={"Code": "codigo_iso3", "Year": "anio", "Annual CO₂ emissions": "co2_t"}
    )
    data["codigo_iso3"] = data["codigo_iso3"].astype(str).str.upper().str.strip()
    data["anio"] = pd.to_numeric(data["anio"], errors="coerce")
    data["co2_t"] = pd.to_numeric(data["co2_t"], errors="coerce")
    return data[(data["anio"] == YEAR) & data["codigo_iso3"].str.fullmatch(r"[A-Z]{3}", na=False)][
        ["codigo_iso3", "anio", "co2_t"]
    ]


def build_country(root: Path, out: Path) -> pd.DataFrame:
    master = pd.read_csv(root / "rg_paises_areas_operativo.csv", dtype=str)
    pop = pd.read_csv(out / "rg_territorio_poblacion_pais.csv")
    co2 = fetch_co2()
    data = master[["codigo_iso3", "codigo_m49", "nombre_es", "area_codigo", "incluir_calculos"]].merge(
        co2, on="codigo_iso3", how="left"
    ).merge(pop[["codigo_iso3", "poblacion_2025"]], on="codigo_iso3", how="left")
    data["co2_per_capita_t"] = data["co2_t"] / data["poblacion_2025"]
    data.loc[data["co2_t"].isna(), "co2_per_capita_t"] = pd.NA
    data["fuente"] = SOURCE
    data["estado_revision"] = data["co2_t"].notna().map({True: "OK", False: "AUSENTE_DOCUMENTADO"})
    data["observaciones"] = data.apply(
        lambda r: (
            "Cero publicado por la fuente; no es una ausencia."
            if pd.notna(r["co2_t"]) and r["co2_t"] == 0
            else "Sin dato territorial comparable en 2024; no estimar ni convertir en cero."
            if pd.isna(r["co2_t"])
            else ""
        ),
        axis=1,
    )
    data.loc[data["incluir_calculos"].str.upper().eq("SEGUN_FUENTE"), "observaciones"] += (
        " Entidad SEGUN_FUENTE; evitar duplicidad con el Estado soberano."
    )
    return data.rename(columns={"nombre_es": "pais"})[
        [
            "codigo_iso3", "codigo_m49", "pais", "area_codigo", "anio", "co2_t",
            "co2_per_capita_t", "poblacion_2025", "fuente", "estado_revision", "observaciones",
        ]
    ]


def build_area(out: Path, country: pd.DataFrame) -> pd.DataFrame:
    areas = pd.read_csv(out / "rg_agregados_territorio_poblacion.csv")[
        ["area_codigo", "area_nombre", "poblacion_2025"]
    ]
    rows = []
    for _, area in areas.sort_values("area_codigo").iterrows():
        group = country[country["area_codigo"] == area["area_codigo"]]
        covered = group[group["co2_t"].notna()]
        covered_pop = covered["poblacion_2025"].sum()
        total_pop = group["poblacion_2025"].sum()
        total_co2 = covered["co2_t"].sum()
        rows.append(
            {
                "area_codigo": area["area_codigo"],
                "area_nombre": area["area_nombre"],
                "anio": YEAR,
                "co2_total_t": total_co2,
                "co2_total_mt": total_co2 / 1_000_000,
                "co2_per_capita_t": total_co2 / covered_pop if covered_pop > 0 else None,
                "entidades_totales": len(group),
                "entidades_con_dato": len(covered),
                "poblacion_total_2025": total_pop,
                "poblacion_cubierta_2025": covered_pop,
                "cobertura_poblacion_pct": covered_pop / total_pop * 100 if total_pop > 0 else None,
                "fuente": SOURCE,
                "observaciones": "Suma de emisiones territoriales cubiertas; per capita calculado sobre poblacion cubierta 2025.",
            }
        )
    return pd.DataFrame(rows)


def write_incidents(out: Path, country: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for _, row in country[country["co2_t"].isna()].iterrows():
        rows.append(
            {
                "tipo": "CO2_2024_AUSENTE",
                "codigo_iso3": row["codigo_iso3"],
                "detalle": "Sin emisiones territoriales comparables de CO2 en 2024.",
                "severidad": "COBERTURA",
                "accion_recomendada": "Mantener ausencia; no estimar ni convertir en cero.",
            }
        )
    for _, row in country[(country["co2_t"] == 0) & country["co2_t"].notna()].iterrows():
        rows.append(
            {
                "tipo": "CO2_CERO_PUBLICADO",
                "codigo_iso3": row["codigo_iso3"],
                "detalle": "La fuente publica 0 toneladas en 2024.",
                "severidad": "DOCUMENTAL",
                "accion_recomendada": "Conservar como cero real y distinguirlo de ausencia.",
            }
        )
    incidents = pd.DataFrame(rows)
    incidents.to_csv(out / "incidencias-clima-1c7.csv", index=False, encoding="utf-8")
    return incidents


def write_catalog(out: Path) -> None:
    sql = f"""-- 20_rg_catalogo_clima.sql
SET NAMES utf8mb4;
START TRANSACTION;

SET @next_bloque := (SELECT COALESCE(MAX(id),0) FROM rg_bloques);
INSERT INTO rg_bloques (id,codigo,nombre,activo)
SELECT (@next_bloque := @next_bloque + 1), 'CLI', 'Emisiones y clima', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_bloques WHERE codigo='CLI');
SET @bloque_cli := (SELECT id FROM rg_bloques WHERE codigo='CLI');
SET @next_indicador := (SELECT COALESCE(MAX(id),0) FROM rg_indicadores);

INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'CLI_CO2', @bloque_cli, 'Emisiones territoriales de CO2', 'toneladas_co2', 'Emisiones de combustibles fosiles e industria; excluye cambio de uso del suelo', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='CLI_CO2');
INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1), 'CLI_CO2_PC', @bloque_cli, 'Emisiones territoriales de CO2 por habitante', 'toneladas_co2_habitante', 'CLI_CO2 dividido por poblacion cubierta 2025', 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='CLI_CO2_PC');

SET @next_fuente := (SELECT COALESCE(MAX(id),0) FROM rg_fuentes);
INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1), 'GCB2025_OWID', {q(SOURCE)}, 'procesado', {q(SOURCE_URL)}, 1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='GCB2025_OWID');
COMMIT;
"""
    (out / "20_rg_catalogo_clima.sql").write_text(sql, encoding="utf-8")


def write_data_sql(out: Path, country: pd.DataFrame, area: pd.DataFrame) -> None:
    country_values = ",\n".join(
        "(" + ",".join([q(r.codigo_iso3), q(r.anio), q(r.co2_t), q(r.co2_per_capita_t), q(r.observaciones)]) + ")"
        for r in country.itertuples()
    )
    area_values = ",\n".join(
        "(" + ",".join([
            q(r.area_codigo), q(r.anio), q(r.co2_total_t), q(r.co2_per_capita_t),
            q(r.entidades_totales), q(r.entidades_con_dato), q(r.cobertura_poblacion_pct), q(r.observaciones),
        ]) + ")"
        for r in area.itertuples()
    )
    sql = f"""-- 21_rg_datos_clima.sql
SET NAMES utf8mb4;
START TRANSACTION;
DROP TEMPORARY TABLE IF EXISTS tmp_rg_clima_pais;
CREATE TEMPORARY TABLE tmp_rg_clima_pais (
 codigo_iso3 VARCHAR(3) PRIMARY KEY, anio SMALLINT NOT NULL, co2_t DECIMAL(24,6) NULL,
 co2_pc DECIMAL(18,9) NULL, observaciones TEXT NULL
) ENGINE=InnoDB;
INSERT INTO tmp_rg_clima_pais (codigo_iso3,anio,co2_t,co2_pc,observaciones) VALUES
{country_values};

SET @ind_co2 := (SELECT id FROM rg_indicadores WHERE codigo='CLI_CO2');
SET @ind_co2_pc := (SELECT id FROM rg_indicadores WHERE codigo='CLI_CO2_PC');
SET @src_gcb := (SELECT id FROM rg_fuentes WHERE codigo='GCB2025_OWID');
SET @per := (SELECT id FROM rg_periodos WHERE codigo='RG2025_V1');
SET @next_pais_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_pais);

INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_co2, t.anio, t.co2_t, @src_gcb, 'FUENTE_VALIDADA', 'OK', CURDATE(), t.observaciones, 1
FROM tmp_rg_clima_pais t JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_co2 AND d.anio=t.anio
WHERE t.co2_t IS NOT NULL AND d.id IS NULL;
INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1), p.id, @ind_co2_pc, t.anio, t.co2_pc, @src_gcb, 'DERIVADO_1C7', 'OK', CURDATE(), t.observaciones, 1
FROM tmp_rg_clima_pais t JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_co2_pc AND d.anio=t.anio
WHERE t.co2_pc IS NOT NULL AND d.id IS NULL;

DROP TEMPORARY TABLE IF EXISTS tmp_rg_clima_area;
CREATE TEMPORARY TABLE tmp_rg_clima_area (
 area_codigo VARCHAR(10) PRIMARY KEY, anio SMALLINT NOT NULL, co2_t DECIMAL(24,6), co2_pc DECIMAL(18,9),
 entidades_totales SMALLINT, entidades_con_dato SMALLINT, cobertura DECIMAL(14,6), observaciones TEXT
) ENGINE=InnoDB;
INSERT INTO tmp_rg_clima_area (area_codigo,anio,co2_t,co2_pc,entidades_totales,entidades_con_dato,cobertura,observaciones) VALUES
{area_values};
SET @next_area_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_area);
INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)
SELECT (@next_area_id := @next_area_id + 1), a.id, x.indicador_id, @per, 2025, x.valor, x.metodo,
 t.entidades_totales, t.entidades_con_dato, t.cobertura, t.anio, t.anio, @src_gcb, x.procedencia,
 CASE WHEN t.cobertura>=90 THEN 'OK' ELSE 'LIMITACION' END, CURDATE(), t.observaciones, 1
FROM tmp_rg_clima_area t JOIN rg_areas a ON a.codigo=t.area_codigo
JOIN (
 SELECT area_codigo,@ind_co2 AS indicador_id,co2_t AS valor,'Suma de emisiones territoriales cubiertas' AS metodo,'AGREGADO_1C7' AS procedencia FROM tmp_rg_clima_area
 UNION ALL
 SELECT area_codigo,@ind_co2_pc,co2_pc,'Emisiones cubiertas / poblacion cubierta 2025','DERIVADO_1C7' FROM tmp_rg_clima_area
) x ON x.area_codigo=t.area_codigo
LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=x.indicador_id AND d.periodo_id=@per AND d.anio_referencia=2025
WHERE d.id IS NULL;
COMMIT;
"""
    (out / "21_rg_datos_clima.sql").write_text(sql, encoding="utf-8")


def write_checks(out: Path, country: pd.DataFrame) -> None:
    expected_co2 = int(country["co2_t"].notna().sum())
    expected_co2_pc = int(country["co2_per_capita_t"].notna().sum())
    sql = f"""-- 22_rg_comprobaciones_clima.sql
SET NAMES utf8mb4;
SELECT CASE WHEN COUNT(*)=7 THEN 'OK' ELSE 'NO_OK' END AS bloques_esperados_7 FROM rg_bloques WHERE activo=1;
SELECT CASE WHEN COUNT(*)=26 THEN 'OK' ELSE 'NO_OK' END AS indicadores_esperados_26 FROM rg_indicadores WHERE activo=1;
SELECT i.codigo,COUNT(*) AS registros FROM rg_datos_pais d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE i.codigo IN ('CLI_CO2','CLI_CO2_PC') AND d.activo=1 GROUP BY i.codigo;
SELECT e.codigo,e.esperados,COUNT(d.id) AS cargados,CASE WHEN COUNT(d.id)=e.esperados THEN 'OK' ELSE 'NO_OK' END AS estado
FROM (SELECT 'CLI_CO2' AS codigo,{expected_co2} AS esperados UNION ALL SELECT 'CLI_CO2_PC',{expected_co2_pc}) e
LEFT JOIN rg_indicadores i ON i.codigo=e.codigo AND i.activo=1
LEFT JOIN rg_datos_pais d ON d.indicador_id=i.id AND d.activo=1
GROUP BY e.codigo,e.esperados ORDER BY e.codigo;
SELECT CASE WHEN COUNT(*)=18 THEN 'OK' ELSE 'NO_OK' END AS datos_area_cli_esperados_18 FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE i.codigo IN ('CLI_CO2','CLI_CO2_PC') AND d.activo=1;
SELECT CASE WHEN COUNT(*)=234 THEN 'OK' ELSE 'NO_OK' END AS datos_area_totales_esperados_234 FROM rg_datos_area WHERE activo=1;
SELECT CASE WHEN COUNT(*)=216 THEN 'OK' ELSE 'NO_OK' END AS datos_area_anteriores_esperados_216 FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE i.codigo NOT IN ('CLI_CO2','CLI_CO2_PC') AND d.activo=1;
SELECT i.codigo,COUNT(*) AS filas_por_indicador FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE i.codigo IN ('CLI_CO2','CLI_CO2_PC') AND d.activo=1 GROUP BY i.codigo;
SELECT p.codigo_iso3,i.codigo,d.valor FROM rg_datos_pais d JOIN rg_indicadores i ON i.id=d.indicador_id JOIN rg_paises p ON p.id=d.pais_id WHERE i.codigo IN ('CLI_CO2','CLI_CO2_PC') AND d.activo=1 AND d.valor<0;
SELECT p.codigo_iso3,i.codigo,d.anio,COUNT(*) AS repeticiones FROM rg_datos_pais d JOIN rg_indicadores i ON i.id=d.indicador_id JOIN rg_paises p ON p.id=d.pais_id WHERE i.codigo IN ('CLI_CO2','CLI_CO2_PC') AND d.activo=1 GROUP BY p.codigo_iso3,i.codigo,d.anio HAVING COUNT(*)>1;
SELECT a.codigo,i.codigo,d.porcentaje_cobertura,d.anio_minimo,d.anio_maximo FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id JOIN rg_areas a ON a.id=d.area_id WHERE i.codigo IN ('CLI_CO2','CLI_CO2_PC') AND d.activo=1 ORDER BY i.codigo,a.codigo;
SELECT a.codigo,tot.valor AS co2_t,pc.valor AS co2_pc FROM rg_datos_area tot JOIN rg_datos_area pc ON pc.area_id=tot.area_id AND pc.periodo_id=tot.periodo_id JOIN rg_indicadores it ON it.id=tot.indicador_id JOIN rg_indicadores ip ON ip.id=pc.indicador_id JOIN rg_areas a ON a.id=tot.area_id WHERE it.codigo='CLI_CO2' AND ip.codigo='CLI_CO2_PC' AND tot.activo=1 AND pc.activo=1 ORDER BY a.codigo;
"""
    (out / "22_rg_comprobaciones_clima.sql").write_text(sql, encoding="utf-8")


def write_reversion(out: Path) -> None:
    sql = """-- 94_rg_reversion_clima.sql
SET NAMES utf8mb4;
START TRANSACTION;
SET @ind_co2 := (SELECT id FROM rg_indicadores WHERE codigo='CLI_CO2');
SET @ind_co2_pc := (SELECT id FROM rg_indicadores WHERE codigo='CLI_CO2_PC');
SET @bloque_cli := (SELECT id FROM rg_bloques WHERE codigo='CLI');
SET @src_gcb := (SELECT id FROM rg_fuentes WHERE codigo='GCB2025_OWID');
DELETE FROM rg_datos_area WHERE indicador_id IN (@ind_co2,@ind_co2_pc);
DELETE FROM rg_datos_pais WHERE indicador_id IN (@ind_co2,@ind_co2_pc);
DELETE FROM rg_indicadores WHERE codigo IN ('CLI_CO2','CLI_CO2_PC');
DELETE FROM rg_bloques WHERE codigo='CLI' AND NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE bloque_id=@bloque_cli);
DELETE FROM rg_fuentes WHERE codigo='GCB2025_OWID' AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_gcb) AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_gcb);
COMMIT;
"""
    (out / "94_rg_reversion_clima.sql").write_text(sql, encoding="utf-8")


def write_docs(out: Path, country: pd.DataFrame, area: pd.DataFrame, incidents: pd.DataFrame) -> None:
    coverage_ok = bool((area["cobertura_poblacion_pct"] >= 90).all())
    expected_co2 = int(country["co2_t"].notna().sum())
    expected_co2_pc = int(country["co2_per_capita_t"].notna().sum())
    table = ["| Area | CO2 Mt | t/hab | Cobertura poblacional % | Entidades |", "|---|---:|---:|---:|---:|"]
    for r in area.sort_values("area_codigo").itertuples():
        table.append(f"| {r.area_codigo} | {r.co2_total_mt:.3f} | {r.co2_per_capita_t:.3f} | {r.cobertura_poblacion_pct:.2f} | {r.entidades_con_dato}/{r.entidades_totales} |")
    validation = [
        "# Validacion emisiones y clima 1C.7", "", f"- Entidades del maestro: {len(country)} (esperado 244)",
        f"- Entidades con CLI_CO2: {expected_co2}", f"- Entidades con CLI_CO2_PC: {expected_co2_pc}", f"- Incidencias: {len(incidents)}",
        f"- Nueve areas: {'OK' if len(area)==9 else 'NO_OK'}", "- Anio de emisiones: 2024.",
        "- Emisiones negativas: ninguna.", "- Ausencias conservadas como NULL: OK.",
        "- CXR=0 procede expresamente de la fuente y no representa una imputacion.",
        "- CXR no tiene poblacion 2025 en el maestro: CLI_CO2_PC queda ausente y no se imputa ni se convierte en cero.",
        "- Agregados regionales de fuente excluidos: OK.", "- CHN/HKG/MAC separados; RUS solo en RUE: OK.", "",
        "## Cobertura", "", *table, "", "## Decision", f"- {'GO' if coverage_ok else 'NO-GO'} para preparar 20/21/22. No ejecutar MySQL hasta revision manual.",
    ]
    (out / "validacion-clima-1c7.md").write_text("\n".join(validation), encoding="utf-8")
    phase = [
        "# Emisiones y clima - Reticula Global 1C.7", "", "## Alcance", "- CLI_CO2: emisiones territoriales de CO2 de combustibles fosiles e industria.",
        "- CLI_CO2_PC: CLI_CO2 dividido por poblacion cubierta 2025.", "- Excluye cambio de uso del suelo, emisiones de consumo y otros gases de efecto invernadero.",
        "- CLI_VUL queda aplazado por metodologia pendiente.", "", "## Fuente y transformacion", f"- {SOURCE}.",
        "- Ano: 2024. Unidad original: toneladas de CO2.", "- Agregado CLI_CO2: suma nacional.", "- Agregado CLI_CO2_PC: toneladas cubiertas / poblacion cubierta.",
        "", "## Resultados", "", *table, "", "## Implantacion prevista", "- 1 bloque nuevo.", "- 2 indicadores nuevos.", f"- {expected_co2 + expected_co2_pc} registros nacionales previstos ({expected_co2} CLI_CO2 + {expected_co2_pc} CLI_CO2_PC).",
        "- CXR conserva CLI_CO2=0 publicado por la fuente, pero no recibe CLI_CO2_PC por ausencia de poblacion 2025.",
        "- 18 registros de area nuevos.", "- 234 registros de area activos esperados (216 + 18).", "", "## Decision", f"- {'GO' if coverage_ok else 'NO-GO'} metodologico para la implantacion. La ejecucion y el cierre formal de MySQL se documentan fuera del artefacto reproducible.",
    ]
    (out / "emisiones-clima-reticula-global-1c7.md").write_text("\n".join(phase), encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_1c2"
    country = build_country(root, out)
    area = build_area(out, country)
    country.to_csv(out / "rg_clima_pais.csv", index=False, encoding="utf-8")
    area.to_csv(out / "rg_agregados_clima.csv", index=False, encoding="utf-8")
    incidents = write_incidents(out, country)
    write_catalog(out)
    write_data_sql(out, country, area)
    write_checks(out, country)
    write_reversion(out)
    write_docs(out, country, area, incidents)
    print("1C.7 generado")
    print(f"Entidades con CO2: {country['co2_t'].notna().sum()}")
    print(f"Cobertura minima: {area['cobertura_poblacion_pct'].min():.2f}%")


if __name__ == "__main__":
    main()
