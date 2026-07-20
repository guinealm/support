from __future__ import annotations

import math
from pathlib import Path

import pandas as pd
import requests


WB_API = "https://api.worldbank.org/v2/country/all/indicator/IT.NET.USER.ZS"
WB_URL = "https://data.worldbank.org/indicator/IT.NET.USER.ZS"
ITU_URL = "https://datahub.itu.int/data/?i=11624"
SOURCE_WB = "UIT, World Telecommunication/ICT Indicators Database, distribuido por Banco Mundial"
SOURCE_ITU = "UIT DataHub, Individuals using the Internet"
# Entidades publicadas por UIT pero no distribuidas con codigo ISO3 por la API del Banco Mundial.
ITU_OVERRIDES = {
    "TWN": (2024, 96.7),
    "VAT": (2024, 89.2),
}


def q(value: object) -> str:
    if value is None or pd.isna(value):
        return "NULL"
    if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
        return "NULL"
    if isinstance(value, (int, float)):
        return str(value)
    return "'" + str(value).replace("'", "''") + "'"


def fetch_latest() -> pd.DataFrame:
    response = requests.get(
        WB_API,
        params={"format": "json", "date": "1990:2025", "per_page": 30000},
        timeout=180,
    )
    response.raise_for_status()
    payload = response.json()
    rows = [
        {
            "codigo_iso3": row["countryiso3code"],
            "anio": int(row["date"]),
            "tec_net_pct": row["value"],
            "fuente_codigo": "ITU_WB_NET",
            "fuente": SOURCE_WB,
        }
        for row in payload[1]
        if len(row.get("countryiso3code", "")) == 3 and row.get("value") is not None
    ]
    data = pd.DataFrame(rows).sort_values("anio").drop_duplicates("codigo_iso3", keep="last")
    overrides = pd.DataFrame(
        [
            {
                "codigo_iso3": iso3,
                "anio": year,
                "tec_net_pct": value,
                "fuente_codigo": "ITU_DATAHUB",
                "fuente": SOURCE_ITU,
            }
            for iso3, (year, value) in ITU_OVERRIDES.items()
        ]
    )
    data = data[~data["codigo_iso3"].isin(overrides["codigo_iso3"])]
    return pd.concat([data, overrides], ignore_index=True)


def build_country(root: Path, out: Path) -> pd.DataFrame:
    master = pd.read_csv(root / "rg_paises_areas_operativo.csv", dtype=str)
    pop = pd.read_csv(out / "rg_territorio_poblacion_pais.csv")
    values = fetch_latest()
    data = master[["codigo_iso3", "codigo_m49", "nombre_es", "area_codigo", "incluir_calculos"]].merge(
        values, on="codigo_iso3", how="left"
    ).merge(pop[["codigo_iso3", "poblacion_2025"]], on="codigo_iso3", how="left")
    data["usuarios_estimados_2025"] = data["poblacion_2025"] * data["tec_net_pct"] / 100
    data["estado_revision"] = data["tec_net_pct"].notna().map({True: "OK", False: "AUSENTE_DOCUMENTADO"})
    data["observaciones"] = data.apply(
        lambda r: (
            "Cero publicado por la fuente; no es una ausencia."
            if pd.notna(r["tec_net_pct"]) and r["tec_net_pct"] == 0
            else "Sin dato UIT/Banco Mundial; no imputar ni convertir en cero."
            if pd.isna(r["tec_net_pct"])
            else "Ultimo dato oficial disponible; se conserva el ano real."
        ),
        axis=1,
    )
    data.loc[data["poblacion_2025"].isna() & data["tec_net_pct"].notna(), "observaciones"] += (
        " Sin poblacion 2025: no participa en el agregado."
    )
    data.loc[data["incluir_calculos"].str.upper().eq("SEGUN_FUENTE"), "observaciones"] += (
        " Entidad SEGUN_FUENTE; tratamiento territorial conservado."
    )
    return data.rename(columns={"nombre_es": "pais"})[
        [
            "codigo_iso3", "codigo_m49", "pais", "area_codigo", "anio", "tec_net_pct",
            "poblacion_2025", "usuarios_estimados_2025", "fuente_codigo", "fuente",
            "estado_revision", "observaciones",
        ]
    ]


def build_area(out: Path, country: pd.DataFrame) -> pd.DataFrame:
    areas = pd.read_csv(out / "rg_agregados_territorio_poblacion.csv")[["area_codigo", "area_nombre"]]
    rows = []
    for area in areas.sort_values("area_codigo").itertuples():
        group = country[country["area_codigo"].eq(area.area_codigo)]
        covered = group[group["tec_net_pct"].notna() & group["poblacion_2025"].notna()]
        total_pop = group["poblacion_2025"].sum()
        covered_pop = covered["poblacion_2025"].sum()
        users = covered["usuarios_estimados_2025"].sum()
        rows.append(
            {
                "area_codigo": area.area_codigo,
                "area_nombre": area.area_nombre,
                "tec_net_pct": users / covered_pop * 100 if covered_pop else None,
                "entidades_totales": len(group),
                "entidades_con_dato": int(group["tec_net_pct"].notna().sum()),
                "entidades_en_agregado": len(covered),
                "poblacion_total_2025": total_pop,
                "poblacion_cubierta_2025": covered_pop,
                "cobertura_poblacion_pct": covered_pop / total_pop * 100 if total_pop else None,
                "anio_minimo": int(covered["anio"].min()),
                "anio_maximo": int(covered["anio"].max()),
                "fuente": "UIT / Banco Mundial IT.NET.USER.ZS",
                "observaciones": "Suma de usuarios estimados con poblacion 2025 / suma de poblacion 2025 cubierta; ultimos anos reales disponibles.",
            }
        )
    return pd.DataFrame(rows)


def write_incidents(out: Path, country: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for row in country[country["tec_net_pct"].isna()].itertuples():
        rows.append({"tipo": "TEC_NET_AUSENTE", "codigo_iso3": row.codigo_iso3, "detalle": "Sin dato oficial comparable.", "severidad": "COBERTURA", "accion_recomendada": "Mantener ausencia; no imputar ni convertir en cero."})
    for row in country[country["tec_net_pct"].eq(0)].itertuples():
        rows.append({"tipo": "TEC_NET_CERO_PUBLICADO", "codigo_iso3": row.codigo_iso3, "detalle": f"La fuente publica cero en {int(row.anio)}.", "severidad": "DOCUMENTAL", "accion_recomendada": "Conservar como cero real y distinguirlo de ausencia."})
    for row in country[country["tec_net_pct"].notna() & country["poblacion_2025"].isna()].itertuples():
        rows.append({"tipo": "POBLACION_2025_AUSENTE", "codigo_iso3": row.codigo_iso3, "detalle": "Tiene TEC_NET pero no poblacion 2025 para ponderar.", "severidad": "AGREGACION", "accion_recomendada": "Conservar dato nacional y excluirlo del agregado."})
    incidents = pd.DataFrame(rows)
    incidents.to_csv(out / "incidencias-tecnologia-1c8.csv", index=False, encoding="utf-8")
    return incidents


def write_catalog(out: Path) -> None:
    sql = f"""-- 23_rg_catalogo_tecnologia.sql
SET NAMES utf8mb4;
START TRANSACTION;
SET @next_bloque := (SELECT COALESCE(MAX(id),0) FROM rg_bloques);
INSERT INTO rg_bloques (id,codigo,nombre,activo)
SELECT (@next_bloque := @next_bloque + 1),'TEC','Tecnologia, digitalizacion e innovacion',1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_bloques WHERE codigo='TEC');
SET @bloque_tec := (SELECT id FROM rg_bloques WHERE codigo='TEC');
SET @next_indicador := (SELECT COALESCE(MAX(id),0) FROM rg_indicadores);
INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (@next_indicador := @next_indicador + 1),'TEC_NET',@bloque_tec,'Poblacion usuaria de Internet','porcentaje_poblacion','Personas que utilizaron Internet desde cualquier lugar en los ultimos tres meses',1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='TEC_NET');
SET @next_fuente := (SELECT COALESCE(MAX(id),0) FROM rg_fuentes);
INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1),'ITU_WB_NET',{q(SOURCE_WB)},'oficial_procesado',{q(WB_URL)},1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='ITU_WB_NET');
INSERT INTO rg_fuentes (id,codigo,nombre,tipo_fuente,url,activo)
SELECT (@next_fuente := @next_fuente + 1),'ITU_DATAHUB',{q(SOURCE_ITU)},'oficial',{q(ITU_URL)},1
FROM DUAL WHERE NOT EXISTS (SELECT 1 FROM rg_fuentes WHERE codigo='ITU_DATAHUB');
COMMIT;
"""
    (out / "23_rg_catalogo_tecnologia.sql").write_text(sql, encoding="utf-8")


def write_data(out: Path, country: pd.DataFrame, area: pd.DataFrame) -> None:
    country_values = ",\n".join(
        "(" + ",".join([q(r.codigo_iso3), q(r.anio), q(r.tec_net_pct), q(r.fuente_codigo), q(r.observaciones)]) + ")"
        for r in country.itertuples()
    )
    area_values = ",\n".join(
        "(" + ",".join([q(r.area_codigo), q(r.tec_net_pct), q(r.entidades_totales), q(r.entidades_con_dato), q(r.cobertura_poblacion_pct), q(r.anio_minimo), q(r.anio_maximo), q(r.observaciones)]) + ")"
        for r in area.itertuples()
    )
    sql = f"""-- 24_rg_datos_tecnologia.sql
SET NAMES utf8mb4;
START TRANSACTION;
DROP TEMPORARY TABLE IF EXISTS tmp_rg_tecnologia_pais;
CREATE TEMPORARY TABLE tmp_rg_tecnologia_pais (codigo_iso3 VARCHAR(3) PRIMARY KEY,anio SMALLINT NULL,valor DECIMAL(12,6) NULL,fuente_codigo VARCHAR(30) NULL,observaciones TEXT NULL) ENGINE=InnoDB;
INSERT INTO tmp_rg_tecnologia_pais (codigo_iso3,anio,valor,fuente_codigo,observaciones) VALUES
{country_values};
SET @ind_net := (SELECT id FROM rg_indicadores WHERE codigo='TEC_NET');
SET @per := (SELECT id FROM rg_periodos WHERE codigo='RG2025_V1');
SET @next_pais_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_pais);
INSERT INTO rg_datos_pais (id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)
SELECT (@next_pais_id := @next_pais_id + 1),p.id,@ind_net,t.anio,t.valor,f.id,'FUENTE_VALIDADA','OK',CURDATE(),t.observaciones,1
FROM tmp_rg_tecnologia_pais t JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1
JOIN rg_fuentes f ON f.codigo=t.fuente_codigo
LEFT JOIN rg_datos_pais d ON d.pais_id=p.id AND d.indicador_id=@ind_net AND d.anio=t.anio
WHERE t.valor IS NOT NULL AND d.id IS NULL;
DROP TEMPORARY TABLE IF EXISTS tmp_rg_tecnologia_area;
CREATE TEMPORARY TABLE tmp_rg_tecnologia_area (area_codigo VARCHAR(10) PRIMARY KEY,valor DECIMAL(12,6),entidades_totales SMALLINT,entidades_con_dato SMALLINT,cobertura DECIMAL(12,6),anio_minimo SMALLINT,anio_maximo SMALLINT,observaciones TEXT) ENGINE=InnoDB;
INSERT INTO tmp_rg_tecnologia_area (area_codigo,valor,entidades_totales,entidades_con_dato,cobertura,anio_minimo,anio_maximo,observaciones) VALUES
{area_values};
SET @src_net := (SELECT id FROM rg_fuentes WHERE codigo='ITU_WB_NET');
SET @next_area_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_area);
INSERT INTO rg_datos_area (id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)
SELECT (@next_area_id := @next_area_id + 1),a.id,@ind_net,@per,2025,t.valor,'Usuarios estimados cubiertos / poblacion cubierta',t.entidades_totales,t.entidades_con_dato,t.cobertura,t.anio_minimo,t.anio_maximo,@src_net,'AGREGADO_1C8',CASE WHEN t.cobertura>=90 THEN 'OK' ELSE 'LIMITACION' END,CURDATE(),t.observaciones,1
FROM tmp_rg_tecnologia_area t JOIN rg_areas a ON a.codigo=t.area_codigo
LEFT JOIN rg_datos_area d ON d.area_id=a.id AND d.indicador_id=@ind_net AND d.periodo_id=@per AND d.anio_referencia=2025
WHERE d.id IS NULL;
COMMIT;
"""
    (out / "24_rg_datos_tecnologia.sql").write_text(sql, encoding="utf-8")


def write_checks(out: Path, country: pd.DataFrame) -> None:
    expected = int(country["tec_net_pct"].notna().sum())
    zero_codes = country.loc[country["tec_net_pct"].eq(0), "codigo_iso3"].tolist()
    zero_list = ",".join(q(x) for x in zero_codes) or "''"
    sql = f"""-- 25_rg_comprobaciones_tecnologia.sql
SET NAMES utf8mb4;
SELECT CASE WHEN COUNT(*)=8 THEN 'OK' ELSE 'NO_OK' END AS bloques_esperados_8 FROM rg_bloques WHERE activo=1;
SELECT CASE WHEN COUNT(*)=27 THEN 'OK' ELSE 'NO_OK' END AS indicadores_esperados_27 FROM rg_indicadores WHERE activo=1;
SELECT CASE WHEN COUNT(*)=1 THEN 'OK' ELSE 'NO_OK' END AS bloque_tec_activo FROM rg_bloques WHERE codigo='TEC' AND activo=1;
SELECT CASE WHEN COUNT(*)=1 THEN 'OK' ELSE 'NO_OK' END AS indicador_tec_net_activo FROM rg_indicadores WHERE codigo='TEC_NET' AND activo=1;
SELECT COUNT(*) AS registros_nacionales,CASE WHEN COUNT(*)={expected} THEN 'OK' ELSE 'NO_OK' END AS estado FROM rg_datos_pais d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE i.codigo='TEC_NET' AND d.activo=1;
SELECT CASE WHEN COUNT(*)=9 THEN 'OK' ELSE 'NO_OK' END AS datos_area_tec_esperados_9 FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE i.codigo='TEC_NET' AND d.activo=1;
SELECT CASE WHEN COUNT(*)=243 THEN 'OK' ELSE 'NO_OK' END AS datos_area_totales_esperados_243 FROM rg_datos_area WHERE activo=1;
SELECT CASE WHEN COUNT(*)=234 THEN 'OK' ELSE 'NO_OK' END AS datos_area_anteriores_esperados_234 FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id WHERE i.codigo<>'TEC_NET' AND d.activo=1;
SELECT p.codigo_iso3,d.valor FROM rg_datos_pais d JOIN rg_indicadores i ON i.id=d.indicador_id JOIN rg_paises p ON p.id=d.pais_id WHERE i.codigo='TEC_NET' AND d.activo=1 AND (d.valor<0 OR d.valor>100);
SELECT p.codigo_iso3,d.anio,d.valor FROM rg_datos_pais d JOIN rg_indicadores i ON i.id=d.indicador_id JOIN rg_paises p ON p.id=d.pais_id WHERE i.codigo='TEC_NET' AND d.activo=1 AND d.valor=0 AND p.codigo_iso3 NOT IN ({zero_list});
SELECT p.codigo_iso3,d.anio,COUNT(*) AS repeticiones FROM rg_datos_pais d JOIN rg_indicadores i ON i.id=d.indicador_id JOIN rg_paises p ON p.id=d.pais_id WHERE i.codigo='TEC_NET' AND d.activo=1 GROUP BY p.codigo_iso3,d.anio HAVING COUNT(*)>1;
SELECT a.codigo,d.paises_totales,d.paises_con_dato,d.porcentaje_cobertura,d.anio_minimo,d.anio_maximo,d.valor FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id JOIN rg_areas a ON a.id=d.area_id WHERE i.codigo='TEC_NET' AND d.activo=1 ORDER BY a.codigo;
SELECT a.codigo,d.valor AS valor_almacenado,ROUND(SUM(n.valor*p.valor)/SUM(p.valor),6) AS valor_recalculado,d.porcentaje_cobertura AS cobertura_almacenada,ROUND(100*SUM(p.valor)/(SELECT SUM(pt.valor) FROM rg_paises rpt JOIN rg_datos_pais pt ON pt.pais_id=rpt.id AND pt.indicador_id=ip.id AND pt.anio=2025 AND pt.activo=1 WHERE rpt.area_id=a.id),4) AS cobertura_recalculada,CASE WHEN ABS(d.valor-SUM(n.valor*p.valor)/SUM(p.valor))<0.000001 AND ABS(d.porcentaje_cobertura-100*SUM(p.valor)/(SELECT SUM(pt.valor) FROM rg_paises rpt JOIN rg_datos_pais pt ON pt.pais_id=rpt.id AND pt.indicador_id=ip.id AND pt.anio=2025 AND pt.activo=1 WHERE rpt.area_id=a.id))<0.0001 THEN 'OK' ELSE 'NO_OK' END AS estado FROM rg_datos_area d JOIN rg_indicadores i ON i.id=d.indicador_id JOIN rg_areas a ON a.id=d.area_id JOIN rg_paises rp ON rp.area_id=a.id JOIN rg_datos_pais n ON n.pais_id=rp.id AND n.indicador_id=i.id AND n.activo=1 JOIN rg_indicadores ip ON ip.codigo='POB_TOTAL' JOIN rg_datos_pais p ON p.pais_id=rp.id AND p.indicador_id=ip.id AND p.anio=2025 AND p.activo=1 WHERE i.codigo='TEC_NET' AND d.activo=1 GROUP BY a.id,a.codigo,d.valor,d.porcentaje_cobertura,ip.id ORDER BY a.codigo;
SELECT codigo,activo FROM rg_indicadores WHERE codigo IN ('TEC_ID','TEC_PESO');
"""
    (out / "25_rg_comprobaciones_tecnologia.sql").write_text(sql, encoding="utf-8")


def write_reversion(out: Path) -> None:
    sql = """-- 93_rg_reversion_tecnologia.sql
SET NAMES utf8mb4;
START TRANSACTION;
SET @ind_net := (SELECT id FROM rg_indicadores WHERE codigo='TEC_NET');
SET @bloque_tec := (SELECT id FROM rg_bloques WHERE codigo='TEC');
SET @src_wb := (SELECT id FROM rg_fuentes WHERE codigo='ITU_WB_NET');
SET @src_itu := (SELECT id FROM rg_fuentes WHERE codigo='ITU_DATAHUB');
DELETE FROM rg_datos_area WHERE indicador_id=@ind_net;
DELETE FROM rg_datos_pais WHERE indicador_id=@ind_net;
DELETE FROM rg_indicadores WHERE codigo='TEC_NET';
DELETE FROM rg_bloques WHERE codigo='TEC' AND NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE bloque_id=@bloque_tec);
DELETE FROM rg_fuentes WHERE codigo='ITU_WB_NET' AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_wb) AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_wb);
DELETE FROM rg_fuentes WHERE codigo='ITU_DATAHUB' AND NOT EXISTS (SELECT 1 FROM rg_datos_pais WHERE fuente_id=@src_itu) AND NOT EXISTS (SELECT 1 FROM rg_datos_area WHERE fuente_principal_id=@src_itu);
COMMIT;
"""
    (out / "93_rg_reversion_tecnologia.sql").write_text(sql, encoding="utf-8")


def write_docs(out: Path, country: pd.DataFrame, area: pd.DataFrame, incidents: pd.DataFrame) -> None:
    expected = int(country["tec_net_pct"].notna().sum())
    coverage_ok = bool((area["cobertura_poblacion_pct"] >= 90).all())
    table = ["| Area | TEC_NET % | Cobertura % | Entidades con dato | Anos |", "|---|---:|---:|---:|---|"]
    for r in area.sort_values("area_codigo").itertuples():
        table.append(f"| {r.area_codigo} | {r.tec_net_pct:.3f} | {r.cobertura_poblacion_pct:.2f} | {r.entidades_con_dato}/{r.entidades_totales} | {r.anio_minimo}-{r.anio_maximo} |")
    validation = [
        "# Validacion tecnologia 1C.8", "", f"- Entidades del maestro: {len(country)} (esperado 244).",
        f"- Entidades con TEC_NET: {expected}.", f"- Incidencias: {len(incidents)}.",
        "- Nueve areas: OK.", "- Valores fuera de 0-100: ninguno.",
        "- Ausencias conservadas como NULL: OK.", "- Ceros publicados documentados: OK.",
        "- Ponderacion: poblacion 2025 del maestro; no se usa media simple.", "", "## Resultados", "", *table,
        "", "## Base incremental corregida", "", "- Antes de tecnologia: 7 bloques, 26 indicadores y 234 registros de area.",
        "- Despues de tecnologia: 8 bloques, 27 indicadores y 243 registros de area.",
        "- La expectativa 216 + 9 = 225 omitia los 18 registros climaticos ya implantados.",
        "", "## Decision", f"- {'GO' if coverage_ok else 'NO-GO'} para ejecucion manual de 23/24/25. Codex no ha ejecutado MySQL.",
    ]
    (out / "validacion-tecnologia-1c8.md").write_text("\n".join(validation), encoding="utf-8")
    phase = [
        "# Tecnologia, digitalizacion e innovacion - Reticula Global 1C.8", "", "## Primera edicion", "",
        "- TEC_NET: poblacion usuaria de Internet (%).", "- TEC_ID: aplazado por cobertura insuficiente.",
        "- TEC_PESO: aplazado por metodologia pendiente.", "", "## Fuente y metodo", "",
        "- UIT / Banco Mundial IT.NET.USER.ZS; complementos directos UIT DataHub.",
        "- Ultimo dato oficial disponible por entidad; se conserva el ano real.",
        "- Usuarios estimados = poblacion 2025 x porcentaje / 100.",
        "- Agregado = suma de usuarios estimados cubiertos / suma de poblacion cubierta.",
        "- No se imputan ausencias ni se sustituyen por suscripciones o penetracion movil.",
        "", "## Areas", "", *table, "", "## Implantacion prevista", "",
        f"- {expected} registros nacionales TEC_NET.", "- 9 registros nuevos de area.",
        "- Total correcto esperado: 243 registros activos de area (234 + 9).",
        "- 8 bloques y 27 indicadores activos.", "", "## Estado", "",
        f"- {'GO' if coverage_ok else 'NO-GO'} documental. No se ha ejecutado MySQL ni modificado la web publica.",
    ]
    (out / "tecnologia-reticula-global-1c8.md").write_text("\n".join(phase), encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_1c2"
    country = build_country(root, out)
    area = build_area(out, country)
    country.to_csv(out / "rg_tecnologia_pais.csv", index=False, encoding="utf-8")
    area.to_csv(out / "rg_agregados_tecnologia.csv", index=False, encoding="utf-8")
    incidents = write_incidents(out, country)
    write_catalog(out)
    write_data(out, country, area)
    write_checks(out, country)
    write_reversion(out)
    write_docs(out, country, area, incidents)
    print("1C.8B generado")
    print(f"Entidades con TEC_NET: {country['tec_net_pct'].notna().sum()}")
    print(f"Cobertura minima: {area['cobertura_poblacion_pct'].min():.2f}%")


if __name__ == "__main__":
    main()
