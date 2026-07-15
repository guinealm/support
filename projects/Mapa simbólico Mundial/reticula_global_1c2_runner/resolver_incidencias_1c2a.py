from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path

import pandas as pd


def weighted_mean(values: pd.Series, weights: pd.Series) -> float | None:
    mask = values.notna() & weights.notna() & (weights > 0)
    if not mask.any():
        return None
    return float((values[mask] * weights[mask]).sum() / weights[mask].sum())


def build_decisions() -> dict[str, dict[str, str | bool]]:
    return {
        "IOT": {
            "categoria": "B",
            "motivo": "Territorio sin poblacion permanente en la fuente principal; sin superficie separada.",
            "soberano": "GBR",
            "codigo_fuente": "SIN_CODIGO_SEPARADO",
            "fuente": "OWID/UN WPP 2024 + OWID/FAOSTAT 2025",
            "indicador": "POBLACION,SUPERFICIE",
            "participa_poblacion": False,
            "participa_superficie": False,
            "tratamiento": "EXCLUIR_INDICADOR",
            "nota": "Se mantiene en maestro y mapa; no se imputa cero.",
        },
        "CXR": {
            "categoria": "C",
            "motivo": "No aparece separado en fuente usada; se considera integrado en Australia para evitar duplicidad.",
            "soberano": "AUS",
            "codigo_fuente": "INTEGRADO_EN_AUS",
            "fuente": "OWID/UN WPP 2024 + OWID/FAOSTAT 2025",
            "indicador": "POBLACION,SUPERFICIE",
            "participa_poblacion": False,
            "participa_superficie": False,
            "tratamiento": "EXCLUIR_INDICADOR",
            "nota": "Sin registro separado comparable para 2025/2050.",
        },
        "CCK": {
            "categoria": "C",
            "motivo": "No aparece separado en fuente usada; se considera integrado en Australia para evitar duplicidad.",
            "soberano": "AUS",
            "codigo_fuente": "INTEGRADO_EN_AUS",
            "fuente": "OWID/UN WPP 2024 + OWID/FAOSTAT 2025",
            "indicador": "POBLACION,SUPERFICIE",
            "participa_poblacion": False,
            "participa_superficie": False,
            "tratamiento": "EXCLUIR_INDICADOR",
            "nota": "Sin registro separado comparable para 2025/2050.",
        },
        "ALA": {
            "categoria": "C",
            "motivo": "No aparece separado en fuente usada; se considera integrado en Finlandia para evitar duplicidad.",
            "soberano": "FIN",
            "codigo_fuente": "INTEGRADO_EN_FIN",
            "fuente": "OWID/UN WPP 2024 + OWID/FAOSTAT 2025",
            "indicador": "POBLACION,SUPERFICIE",
            "participa_poblacion": False,
            "participa_superficie": False,
            "tratamiento": "EXCLUIR_INDICADOR",
            "nota": "Sin registro separado comparable para 2025/2050.",
        },
        "NFK": {
            "categoria": "C",
            "motivo": "Poblacion no separada en fuente principal; superficie separada potencialmente no comparable con inclusion en soberano.",
            "soberano": "AUS",
            "codigo_fuente": "INTEGRADO_EN_AUS",
            "fuente": "OWID/UN WPP 2024 + OWID/FAOSTAT 2025",
            "indicador": "POBLACION,SUPERFICIE",
            "participa_poblacion": False,
            "participa_superficie": False,
            "tratamiento": "EXCLUIR_INDICADOR",
            "nota": "Se excluye superficie para evitar riesgo de doble conteo.",
        },
        "PCN": {
            "categoria": "B",
            "motivo": "Sin dato poblacional en la fuente principal y poblacion minima no estable para proyeccion homogenea.",
            "soberano": "GBR",
            "codigo_fuente": "SIN_CODIGO_SEPARADO",
            "fuente": "OWID/UN WPP 2024 + OWID/FAOSTAT 2025",
            "indicador": "POBLACION,SUPERFICIE",
            "participa_poblacion": False,
            "participa_superficie": False,
            "tratamiento": "EXCLUIR_INDICADOR",
            "nota": "Se excluye superficie para consistencia de tratamiento.",
        },
        "SJM": {
            "categoria": "C",
            "motivo": "No aparece separado en fuente usada; posible integracion en Noruega en series oficiales.",
            "soberano": "NOR",
            "codigo_fuente": "INTEGRADO_EN_NOR",
            "fuente": "OWID/UN WPP 2024 + OWID/FAOSTAT 2025",
            "indicador": "POBLACION,SUPERFICIE",
            "participa_poblacion": False,
            "participa_superficie": False,
            "tratamiento": "EXCLUIR_INDICADOR",
            "nota": "Sin separacion comparable en la fuente principal.",
        },
        "GGY": {
            "categoria": "F",
            "motivo": "Poblacion separada disponible; superficie ausente en fuente principal para este codigo.",
            "soberano": "GBR",
            "codigo_fuente": "GGY",
            "fuente": "OWID/UN WPP 2024 + OWID/FAOSTAT 2025",
            "indicador": "POBLACION,SUPERFICIE",
            "participa_poblacion": True,
            "participa_superficie": False,
            "tratamiento": "INCLUIR_POB_EXCLUIR_SUP",
            "nota": "No se imputa superficie alternativa sin comparabilidad metodologica cerrada.",
        },
        "JEY": {
            "categoria": "F",
            "motivo": "Poblacion separada disponible; superficie ausente en fuente principal para este codigo.",
            "soberano": "GBR",
            "codigo_fuente": "JEY",
            "fuente": "OWID/UN WPP 2024 + OWID/FAOSTAT 2025",
            "indicador": "POBLACION,SUPERFICIE",
            "participa_poblacion": True,
            "participa_superficie": False,
            "tratamiento": "INCLUIR_POB_EXCLUIR_SUP",
            "nota": "No se imputa superficie alternativa sin comparabilidad metodologica cerrada.",
        },
        "XKX": {
            "categoria": "E",
            "motivo": "Entidad estadistica auxiliar; sin registro separado en fuente usada y riesgo de duplicidad con Serbia.",
            "soberano": "SRB",
            "codigo_fuente": "NO_PRESENTE_EN_FUENTE",
            "fuente": "OWID/UN WPP 2024 + OWID/FAOSTAT 2025",
            "indicador": "POBLACION,SUPERFICIE",
            "participa_poblacion": False,
            "participa_superficie": False,
            "tratamiento": "EXCLUIR_INDICADOR",
            "nota": "Se mantiene SEGUN_FUENTE; excluido temporalmente del agregado hasta resolver sin duplicidad.",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="output_1c2")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    out = (root / args.out).resolve()

    entity_file = out / "rg_territorio_poblacion_pais.csv"
    agg_file = out / "rg_agregados_territorio_poblacion.csv"
    incid_file = out / "incidencias_territorio_poblacion.csv"
    val_file = out / "validacion-territorio-poblacion-1c2.md"

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_dir = out / f"backup_1c2a_{ts}"
    backup_dir.mkdir(parents=True, exist_ok=True)

    for src in [entity_file, agg_file, incid_file, val_file]:
        if src.exists():
            shutil.copy2(src, backup_dir / src.name)

    entity = pd.read_csv(entity_file, dtype={"codigo_m49": str})
    if "observaciones_datos" in entity.columns:
        entity["observaciones_datos"] = entity["observaciones_datos"].astype("string")
    base_backup = backup_dir
    incid_initial = pd.read_csv(backup_dir / "incidencias_territorio_poblacion.csv", dtype={"codigo_m49": str})
    if len(incid_initial) == 0:
        for prev_backup in sorted(out.glob("backup_1c2a_*")):
            cand = prev_backup / "incidencias_territorio_poblacion.csv"
            if not cand.exists():
                continue
            df_cand = pd.read_csv(cand, dtype={"codigo_m49": str})
            if len(df_cand) > 0:
                incid_initial = df_cand
                base_backup = prev_backup
                break
    agg_prev = pd.read_csv(base_backup / "rg_agregados_territorio_poblacion.csv")
    decisions = build_decisions()

    inv = incid_initial[incid_initial["codigo_iso3"].isin(decisions.keys())].copy()

    def missing_fields(row: pd.Series) -> str:
        missing = []
        for col, label in [
            ("poblacion_2025", "poblacion_2025"),
            ("poblacion_2050", "poblacion_2050"),
            ("superficie_km2", "superficie_km2"),
        ]:
            if pd.isna(row[col]):
                missing.append(label)
        return ",".join(missing) if missing else "ninguno"

    inventory_rows = []
    corr_rows = []

    for iso3, decision in decisions.items():
        mask = entity["codigo_iso3"].eq(iso3)
        if not mask.any():
            continue

        if not bool(decision["participa_poblacion"]):
            entity.loc[mask, ["poblacion_2025", "poblacion_2050", "edad_mediana_2025"]] = pd.NA
        if not bool(decision["participa_superficie"]):
            entity.loc[mask, ["superficie_km2", "anio_superficie"]] = pd.NA

        entity.loc[mask, "estado_revision"] = "LIMITACION_DOCUMENTADA"
        entity.loc[mask, "observaciones_datos"] = (
            f"1C.2A categoria {decision['categoria']}: {decision['motivo']} "
            f"Decision: {decision['tratamiento']}. Nota: {decision['nota']}"
        )

        row = entity.loc[mask].iloc[0]
        row_initial = inv[inv["codigo_iso3"].eq(iso3)].iloc[0]
        inventory_rows.append(
            {
                "ISO3": iso3,
                "Entidad": row_initial["nombre_es"],
                "Area": row_initial["area_codigo"],
                "Tipo de entidad": row_initial["tipo_entidad"],
                "Inclusion": row_initial["incluir_calculos"],
                "Poblacion 2025": row_initial["poblacion_2025"],
                "Poblacion 2050": row_initial["poblacion_2050"],
                "Superficie": row_initial["superficie_km2"],
                "Motivo probable": decision["motivo"],
                "Campo faltante exacto": missing_fields(row_initial),
            }
        )

        corr_rows.append(
            {
                "Entidad": row["nombre_es"],
                "ISO maestro": iso3,
                "Codigo fuente": decision["codigo_fuente"],
                "Fuente": decision["fuente"],
                "Indicador": decision["indicador"],
                "Tratamiento": decision["tratamiento"],
                "Nota": decision["nota"],
            }
        )

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
                "densidad_2025": p25 / area_km2 if pd.notna(p25) and pd.notna(area_km2) and area_km2 > 0 else pd.NA,
                "edad_mediana_2025_aprox": age_mean,
                "poblacion_2050": p50,
                "variacion_2025_2050_pct": ((p50 / p25) - 1) * 100 if pd.notna(p25) and pd.notna(p50) and p25 > 0 else pd.NA,
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

    unresolved = entity[entity["estado_revision"].eq("REVISAR")].copy()

    coverage = (
        entity.groupby(["area_codigo", "area_nombre"], dropna=False)
        .agg(
            entidades=("codigo_iso3", "count"),
            con_poblacion=("poblacion_2025", lambda s: int(s.notna().sum())),
            con_superficie=("superficie_km2", lambda s: int(s.notna().sum())),
        )
        .reset_index()
    )
    coverage["cobertura_poblacion_pct"] = coverage["con_poblacion"] / coverage["entidades"] * 100
    coverage["cobertura_superficie_pct"] = coverage["con_superficie"] / coverage["entidades"] * 100
    coverage = coverage.sort_values("area_codigo")

    diff = agg[["area_codigo", "poblacion_2025", "poblacion_2050", "superficie_km2", "densidad_2025"]].merge(
        agg_prev[["area_codigo", "poblacion_2025", "poblacion_2050", "superficie_km2", "densidad_2025"]],
        on="area_codigo",
        how="left",
        suffixes=("_nuevo", "_previo"),
    )
    for col in ["poblacion_2025", "poblacion_2050", "superficie_km2", "densidad_2025"]:
        diff[f"delta_{col}"] = diff[f"{col}_nuevo"] - diff[f"{col}_previo"]

    agg.to_csv(agg_file, index=False, encoding="utf-8-sig")
    entity.to_csv(entity_file, index=False, encoding="utf-8-sig")
    unresolved.to_csv(incid_file, index=False, encoding="utf-8-sig")

    corr = pd.DataFrame(corr_rows)
    corr_file = out / "correspondencias-especiales-1c2.csv"
    corr.to_csv(corr_file, index=False, encoding="utf-8-sig")

    inventory = pd.DataFrame(inventory_rows).sort_values("ISO3")
    resol_file = out / "resolucion-incidencias-territorio-poblacion-1c2a.md"

    report = f"""# Resolucion de incidencias territorio y poblacion - Fase 1C.2A

## Estado general

- Incidencias iniciales: **10**
- Incidencias pendientes tras 1C.2A: **{len(unresolved)}**
- Entidades con estado LIMITACION_DOCUMENTADA: **{entity['estado_revision'].eq('LIMITACION_DOCUMENTADA').sum()}**
- Copia de seguridad de salida previa: **{backup_dir.name}**
- Base comparativa de agregados previos: **{base_backup.name}**

## Inventario inicial de incidencias

{inventory.to_markdown(index=False)}

## Decisiones por entidad

{corr.to_markdown(index=False)}

## Cobertura por area

{coverage.to_markdown(index=False)}

## Agregados actualizados

{agg.to_markdown(index=False)}

## Diferencias respecto a agregados previos

{diff[['area_codigo','delta_poblacion_2025','delta_poblacion_2050','delta_superficie_km2','delta_densidad_2025']].to_markdown(index=False)}

## Validaciones finales

1. Nueve areas: **{len(agg)}**.
2. Suma mundial poblacion 2025: **{world_pop:,.0f}**.
3. Suma mundial poblacion 2050: **{agg['poblacion_2050'].sum():,.0f}**.
4. Suma porcentaje poblacion: **{agg['poblacion_mundial_pct'].sum():.6f}**.
5. Suma porcentaje superficie: **{agg['superficie_mundial_pct'].sum():.6f}**.
6. Ausentes convertidos en cero: **no**.
7. China/Hong Kong/Macao/Taiwan: **sin cambios de regla territorial**.
8. Serbia/Kosovo: Kosovo excluido temporalmente para evitar duplicidad.
9. Territorios dependientes: tratamiento por indicador documentado en correspondencias.
"""
    resol_file.write_text(report, encoding="utf-8")

    val = f"""# Validacion territorio y poblacion - Fase 1C.2 (actualizada en 1C.2A)

## Resumen

- Areas agregadas: **{len(agg)}**
- Entidades maestras: **{len(entity)}**
- Entidades con poblacion 2025: **{entity['poblacion_2025'].notna().sum()}**
- Entidades con poblacion 2050: **{entity['poblacion_2050'].notna().sum()}**
- Entidades con superficie: **{entity['superficie_km2'].notna().sum()}**
- Incidencias pendientes: **{len(unresolved)}**
- Poblacion total agregada 2025: **{world_pop:,.0f}**
- Superficie terrestre agregada: **{world_land:,.2f} km2**

## Agregados

{agg.to_markdown(index=False)}

## Cobertura por area

{coverage.to_markdown(index=False)}

## Nota

Las limitaciones aceptadas en 1C.2A quedaron documentadas en `resolucion-incidencias-territorio-poblacion-1c2a.md` y `correspondencias-especiales-1c2.csv`.
"""
    val_file.write_text(val, encoding="utf-8")

    print(f"Backup: {backup_dir}")
    print(f"Incidencias pendientes: {len(unresolved)}")
    print("Completado 1C.2A")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
