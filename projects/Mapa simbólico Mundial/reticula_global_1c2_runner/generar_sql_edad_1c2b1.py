from __future__ import annotations

from pathlib import Path

import pandas as pd


def q(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


def main() -> int:
    root = Path(__file__).resolve().parent
    out = root / "output_1c2"

    ent = pd.read_csv(out / "rg_territorio_poblacion_pais.csv", dtype=str)
    med = pd.read_csv(out / "raw" / "median-age.csv")

    # OWID tiene valores en "Median age" hasta 2023; 2025 aparece en columna proyectada.
    val_col = "Median age"
    med = med[
        med["Code"].notna()
        & med[val_col].notna()
        & (med["Year"] <= 2025)
    ].copy()
    med = (
        med.sort_values(["Code", "Year"])
        .groupby("Code", as_index=False)
        .tail(1)[["Code", "Year", val_col]]
        .rename(columns={"Code": "codigo_iso3", "Year": "anio_edad", val_col: "edad_mediana"})
    )

    x = ent.merge(med, on="codigo_iso3", how="left")
    x["edad_mediana"] = pd.to_numeric(x["edad_mediana"], errors="coerce")
    x["anio_edad"] = pd.to_numeric(x["anio_edad"], errors="coerce")
    x = x[x["edad_mediana"].notna()].copy()
    x = x[["codigo_iso3", "anio_edad", "edad_mediana"]].sort_values("codigo_iso3")

    lines: list[str] = []
    lines.append("-- 06_rg_correccion_edad_mediana.sql")
    lines.append("-- Correccion incremental 1C.2B.1: carga de edad mediana nacional y actualizacion de POB_EDAD por area")
    lines.append("SET NAMES utf8mb4;")
    lines.append("START TRANSACTION;")
    lines.append("")
    lines.append("DROP TEMPORARY TABLE IF EXISTS tmp_rg_edad_mediana_2025;")
    lines.append(
        "CREATE TEMPORARY TABLE tmp_rg_edad_mediana_2025 ("
        "codigo_iso3 VARCHAR(3) NOT NULL PRIMARY KEY, "
        "anio SMALLINT NOT NULL, "
        "valor DECIMAL(10,4) NOT NULL"
        ") ENGINE=MEMORY;"
    )
    lines.append("")

    values = []
    for r in x.itertuples(index=False):
        values.append(f"({q(str(r.codigo_iso3))},{int(r.anio_edad)},{float(r.edad_mediana):.4f})")

    lines.append("INSERT INTO tmp_rg_edad_mediana_2025 (codigo_iso3,anio,valor) VALUES")
    lines.append(",\n".join(values) + ";")
    lines.append("")

    lines.append("-- Inserta POB_EDAD solo para paises sin registro previo en (pais_id, indicador_id, anio)")
    lines.append("SET @next_id := (SELECT COALESCE(MAX(id),0) FROM rg_datos_pais);")
    lines.append(
        "INSERT INTO rg_datos_pais "
        "(id,pais_id,indicador_id,anio,valor,fuente_id,tipo_procedencia,estado_dato,fecha_carga,observaciones,activo)\n"
        "SELECT (@next_id := @next_id + 1) AS id, p.id, i.id, t.anio, t.valor, f.id, 'FUENTE_VALIDADA', 'OK', CURDATE(),\n"
        "       'Edad mediana aproximada: ultimo dato disponible <= 2025 (OWID).', 1\n"
        "FROM tmp_rg_edad_mediana_2025 t\n"
        "JOIN rg_paises p ON p.codigo_iso3=t.codigo_iso3 AND p.activo=1\n"
        "JOIN rg_indicadores i ON i.codigo='POB_EDAD'\n"
        "JOIN rg_fuentes f ON f.codigo='OWID'\n"
        "LEFT JOIN rg_datos_pais dp ON dp.pais_id=p.id AND dp.indicador_id=i.id AND dp.anio=t.anio\n"
        "WHERE dp.id IS NULL;"
    )
    lines.append("")

    lines.append("-- Si ya existian filas de POB_EDAD, actualiza valor y metadatos en lugar de duplicar")
    lines.append(
        "UPDATE rg_datos_pais dp\n"
        "JOIN rg_paises p ON p.id=dp.pais_id\n"
        "JOIN rg_indicadores i ON i.id=dp.indicador_id AND i.codigo='POB_EDAD'\n"
        "JOIN rg_fuentes f ON f.codigo='OWID'\n"
        "JOIN tmp_rg_edad_mediana_2025 t ON t.codigo_iso3=p.codigo_iso3 AND t.anio=dp.anio\n"
        "SET dp.valor=t.valor,\n"
        "    dp.fuente_id=f.id,\n"
        "    dp.tipo_procedencia='FUENTE_VALIDADA',\n"
        "    dp.estado_dato='OK',\n"
        "    dp.fecha_carga=CURDATE(),\n"
        "    dp.observaciones='Edad mediana aproximada: ultimo dato disponible <= 2025 (OWID).',\n"
        "    dp.activo=1;"
    )
    lines.append("")

    lines.append("-- Cobertura y agregacion ponderada por area (sin media simple)")
    lines.append("DROP TEMPORARY TABLE IF EXISTS tmp_rg_area_edad_cobertura;")
    lines.append(
        "CREATE TEMPORARY TABLE tmp_rg_area_edad_cobertura AS\n"
        "SELECT a.id AS area_id,\n"
        "       COUNT(p.id) AS paises_totales,\n"
        "       SUM(CASE WHEN de.valor IS NOT NULL AND dp.valor IS NOT NULL AND dp.valor>0 THEN 1 ELSE 0 END) AS paises_con_dato\n"
        "FROM rg_areas a\n"
        "LEFT JOIN rg_paises p ON p.area_id=a.id AND p.activo=1\n"
        "LEFT JOIN rg_indicadores ie ON ie.codigo='POB_EDAD'\n"
        "LEFT JOIN rg_indicadores ip ON ip.codigo='POB_TOTAL'\n"
        "LEFT JOIN rg_datos_pais de ON de.pais_id=p.id AND de.indicador_id=ie.id AND de.anio=2023 AND de.activo=1\n"
        "LEFT JOIN rg_datos_pais dp ON dp.pais_id=p.id AND dp.indicador_id=ip.id AND dp.anio=2025 AND dp.activo=1\n"
        "GROUP BY a.id;"
    )
    lines.append("")
    lines.append("DROP TEMPORARY TABLE IF EXISTS tmp_rg_area_edad_valor;")
    lines.append(
        "CREATE TEMPORARY TABLE tmp_rg_area_edad_valor AS\n"
        "SELECT p.area_id,\n"
        "       SUM(de.valor * dp.valor) / NULLIF(SUM(dp.valor),0) AS valor_edad\n"
        "FROM rg_paises p\n"
        "JOIN rg_indicadores ie ON ie.codigo='POB_EDAD'\n"
        "JOIN rg_indicadores ip ON ip.codigo='POB_TOTAL'\n"
        "JOIN rg_datos_pais de ON de.pais_id=p.id AND de.indicador_id=ie.id AND de.anio=2023 AND de.activo=1 AND de.valor IS NOT NULL\n"
        "JOIN rg_datos_pais dp ON dp.pais_id=p.id AND dp.indicador_id=ip.id AND dp.anio=2025 AND dp.activo=1 AND dp.valor IS NOT NULL AND dp.valor>0\n"
        "WHERE p.activo=1\n"
        "GROUP BY p.area_id;"
    )
    lines.append("")

    lines.append("-- Actualiza solo POB_EDAD en rg_datos_area (9 filas existentes)")
    lines.append(
        "UPDATE rg_datos_area da\n"
        "JOIN rg_indicadores i ON i.id=da.indicador_id AND i.codigo='POB_EDAD'\n"
        "JOIN rg_areas a ON a.id=da.area_id\n"
        "LEFT JOIN tmp_rg_area_edad_valor v ON v.area_id=a.id\n"
        "LEFT JOIN tmp_rg_area_edad_cobertura c ON c.area_id=a.id\n"
        "JOIN rg_fuentes f ON f.codigo='OWID'\n"
        "SET da.valor=v.valor_edad,\n"
        "    da.metodo_calculo='Media ponderada aproximada por poblacion 2025 (edad 2023 OWID)',\n"
        "    da.paises_totales=c.paises_totales,\n"
        "    da.paises_con_dato=c.paises_con_dato,\n"
        "    da.porcentaje_cobertura=CASE WHEN c.paises_totales>0 THEN ROUND((c.paises_con_dato*100.0)/c.paises_totales,4) ELSE NULL END,\n"
        "    da.anio_minimo=2023,\n"
        "    da.anio_maximo=2023,\n"
        "    da.fuente_principal_id=f.id,\n"
        "    da.tipo_procedencia='AGREGADO_1C2B_CORRECCION',\n"
        "    da.estado_dato=CASE WHEN v.valor_edad IS NULL THEN 'LIMITACION'\n"
        "                        WHEN c.paises_totales>0 AND ((c.paises_con_dato*100.0)/c.paises_totales)>=90 THEN 'OK'\n"
        "                        ELSE 'LIMITACION' END,\n"
        "    da.fecha_calculo=CURDATE(),\n"
        "    da.observaciones='Edad mediana aproximada; ultimo dato disponible <=2025 (actualmente 2023), ponderado por poblacion 2025.'\n"
        "WHERE da.activo=1;"
    )
    lines.append("")
    lines.append("COMMIT;")

    (out / "06_rg_correccion_edad_mediana.sql").write_text("\n".join(lines), encoding="utf-8")

    checks: list[str] = []
    checks.append("-- 07_rg_comprobacion_edad_mediana.sql")
    checks.append("SET NAMES utf8mb4;")
    checks.append("")
    checks.append(
        "SELECT i.codigo, COUNT(*) AS registros,\n"
        "       COUNT(dp.valor) AS valores_no_nulos\n"
        "FROM rg_datos_pais dp\n"
        "JOIN rg_indicadores i ON i.id = dp.indicador_id\n"
        "WHERE i.codigo = 'POB_EDAD'\n"
        "GROUP BY i.codigo;"
    )
    checks.append("")
    checks.append(
        "SELECT a.codigo AS area, da.valor, da.metodo_calculo,\n"
        "       da.paises_totales, da.paises_con_dato,\n"
        "       da.porcentaje_cobertura\n"
        "FROM rg_datos_area da\n"
        "JOIN rg_areas a ON a.id = da.area_id\n"
        "JOIN rg_indicadores i ON i.id = da.indicador_id\n"
        "WHERE i.codigo = 'POB_EDAD'\n"
        "ORDER BY a.codigo;"
    )
    checks.append("")
    checks.append("-- Debe seguir habiendo 72 filas en rg_datos_area")
    checks.append("SELECT COUNT(*) AS total_rg_datos_area FROM rg_datos_area WHERE activo=1;")
    checks.append("")
    checks.append("-- No debe haber duplicidades nacionales de POB_EDAD por (pais,anio)")
    checks.append(
        "SELECT p.codigo_iso3, dp.anio, COUNT(*) AS repeticiones\n"
        "FROM rg_datos_pais dp\n"
        "JOIN rg_indicadores i ON i.id=dp.indicador_id\n"
        "JOIN rg_paises p ON p.id=dp.pais_id\n"
        "WHERE i.codigo='POB_EDAD' AND dp.activo=1\n"
        "GROUP BY p.codigo_iso3, dp.anio\n"
        "HAVING COUNT(*)>1;"
    )
    checks.append("")
    checks.append("-- Control de los 8 indicadores de area (deben quedar 9 cada uno)")
    checks.append(
        "SELECT i.codigo, COUNT(*) AS registros_area\n"
        "FROM rg_datos_area da\n"
        "JOIN rg_indicadores i ON i.id=da.indicador_id\n"
        "WHERE da.activo=1\n"
        "GROUP BY i.codigo\n"
        "ORDER BY i.codigo;"
    )
    checks.append("")
    checks.append("-- Poblacion y porcentajes mundiales deben mantenerse")
    checks.append(
        "SELECT\n"
        "  SUM(CASE WHEN i.codigo='POB_PCT' THEN da.valor ELSE 0 END) AS suma_pob_pct,\n"
        "  SUM(CASE WHEN i.codigo='TERR_PCT' THEN da.valor ELSE 0 END) AS suma_terr_pct,\n"
        "  SUM(CASE WHEN i.codigo='POB_TOTAL' THEN da.valor ELSE 0 END) AS poblacion_2025,\n"
        "  SUM(CASE WHEN i.codigo='POB_2050' THEN da.valor ELSE 0 END) AS poblacion_2050\n"
        "FROM rg_datos_area da\n"
        "JOIN rg_indicadores i ON i.id=da.indicador_id\n"
        "WHERE da.activo=1;"
    )

    (out / "07_rg_comprobacion_edad_mediana.sql").write_text("\n".join(checks), encoding="utf-8")

    print(f"nacionales_con_valor={len(x)}")
    print(f"sql_06={out / '06_rg_correccion_edad_mediana.sql'}")
    print(f"sql_07={out / '07_rg_comprobacion_edad_mediana.sql'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
