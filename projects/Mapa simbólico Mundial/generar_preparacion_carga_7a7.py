"""Genera los artefactos de preparación de carga 7A.7; no conecta con MySQL."""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
rows = list(csv.DictReader((ROOT / "datos-area-indicadores-complementarios-7a6.csv").open(encoding="utf-8-sig")))
public = [r for r in rows if not (r["codigo_indicador"] == "ECO_PC" and r["codigo_area"] == "MDE")]
nonpublic = [r for r in rows if (r["codigo_indicador"] == "ECO_PC" and r["codigo_area"] == "MDE")]

for r in nonpublic:
    r["estado"] = "NO PUBLICABLE"
    r["observaciones"] = "Sin valor activo: retirada de publicación por cobertura 93.5486% y ausencia de PIB nominal sirio comparable."

fields = list(rows[0])
for name, data in (("datos-area-publicables-7a7.csv", public), ("datos-area-no-publicables-7a7.csv", nonpublic)):
    with (ROOT / name).open("w", encoding="utf-8", newline="") as h:
        w = csv.DictWriter(h, fieldnames=fields); w.writeheader(); w.writerows(data)
assert len(public) == 53 and len(nonpublic) == 1
assert len({(r["codigo_indicador"], r["codigo_area"]) for r in public}) == 53

def esc(s): return str(s).replace("'", "''")
values = []
for r in public:
    values.append("('%s','%s',%s,%s,'%s',%s,'%s','%s')" % (
        r["codigo_area"], r["codigo_indicador"], r["anio_referencia"], r["valor"],
        esc(r["metodo"]), r["cobertura_pct"], esc(r["observaciones"]),
        esc("WB_WDI" if r["codigo_indicador"] in ("POB_URB", "ECO_PC", "HUM_EV") else "UNDP_HDR" if r["codigo_indicador"] == "HUM_IDH" else "OWID")))

load = """-- FASE 7A.7. PROPUESTA NO EJECUTADA.
-- DDL de respaldo antes de la transacción; no ejecutar sin preflight y copia verificada.
USE `u794456529_map_sim_Mund`;
SET NAMES utf8mb4;
CREATE TABLE rg_backup_datos_area_7a7_20260729 LIKE rg_datos_area;
CREATE TABLE rg_backup_indicadores_7a7_20260729 (codigo VARCHAR(40) PRIMARY KEY, existia TINYINT NOT NULL);
INSERT INTO rg_backup_indicadores_7a7_20260729
SELECT 'POB_URB', IF(COUNT(*)>0,1,0) FROM rg_indicadores WHERE codigo='POB_URB';
INSERT INTO rg_backup_datos_area_7a7_20260729
SELECT da.* FROM rg_datos_area da
JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id
WHERE p.codigo='RG2025_V1' AND i.codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH');
CREATE TEMPORARY TABLE tmp_rg_area_7a7 (
 codigo_area CHAR(3) NOT NULL, codigo_indicador VARCHAR(40) NOT NULL,
 anio_referencia SMALLINT NOT NULL, valor DECIMAL(22,10) NOT NULL,
 metodo_calculo VARCHAR(120) NOT NULL, cobertura_pct DECIMAL(8,4) NOT NULL,
 observaciones TEXT, fuente_codigo VARCHAR(40) NOT NULL,
 PRIMARY KEY(codigo_area,codigo_indicador));
INSERT INTO tmp_rg_area_7a7
(codigo_area,codigo_indicador,anio_referencia,valor,metodo_calculo,cobertura_pct,observaciones,fuente_codigo)
VALUES
""" + ",\n".join(values) + ";\n\n" + r"""START TRANSACTION;
-- POB_URB es el código aprobado en el diccionario; se crea solo si está ausente.
INSERT INTO rg_indicadores (id,codigo,bloque_id,nombre,unidad,descripcion,activo)
SELECT (SELECT COALESCE(MAX(id),0)+1 FROM rg_indicadores),'POB_URB',b.id,
       'Población urbana','porcentaje_poblacion','Población urbana como porcentaje de la población total',1
FROM rg_bloques b WHERE b.codigo='POB'
  AND NOT EXISTS (SELECT 1 FROM rg_indicadores WHERE codigo='POB_URB');
SET @per_7a7 := (SELECT id FROM rg_periodos WHERE codigo='RG2025_V1' AND activo=1);
SET @next_7a7 := (SELECT COALESCE(MAX(id),0) FROM rg_datos_area);
-- Inserta únicamente las nueve filas nuevas de POB_URB; el preflight exige que no existan.
INSERT INTO rg_datos_area
(id,area_id,indicador_id,periodo_id,anio_referencia,valor,metodo_calculo,paises_totales,paises_con_dato,porcentaje_cobertura,anio_minimo,anio_maximo,fuente_principal_id,tipo_procedencia,estado_dato,fecha_calculo,observaciones,activo)
SELECT (@next_7a7:=@next_7a7+1),a.id,i.id,@per_7a7,t.anio_referencia,t.valor,t.metodo_calculo,NULL,NULL,t.cobertura_pct,t.anio_referencia,t.anio_referencia,f.id,'CALCULO_7A7','OK',CURDATE(),t.observaciones,1
FROM tmp_rg_area_7a7 t JOIN rg_areas a ON a.codigo=t.codigo_area JOIN rg_indicadores i ON i.codigo=t.codigo_indicador JOIN rg_fuentes f ON f.codigo=t.fuente_codigo
WHERE t.codigo_indicador='POB_URB';
-- Actualiza los 44 registros existentes publicables de los otros cinco indicadores.
UPDATE rg_datos_area da JOIN rg_areas a ON a.id=da.area_id JOIN rg_indicadores i ON i.id=da.indicador_id
JOIN rg_periodos p ON p.id=da.periodo_id JOIN tmp_rg_area_7a7 t ON t.codigo_area=a.codigo AND t.codigo_indicador=i.codigo
JOIN rg_fuentes f ON f.codigo=t.fuente_codigo
SET da.anio_referencia=t.anio_referencia,da.valor=t.valor,da.metodo_calculo=t.metodo_calculo,
 da.porcentaje_cobertura=t.cobertura_pct,da.anio_minimo=t.anio_referencia,da.anio_maximo=t.anio_referencia,
 da.fuente_principal_id=f.id,da.tipo_procedencia='CALCULO_7A7',da.estado_dato='OK',da.fecha_calculo=CURDATE(),da.observaciones=t.observaciones,da.activo=1
WHERE p.codigo='RG2025_V1' AND t.codigo_indicador<>'POB_URB' AND NOT (i.codigo='ECO_PC' AND a.codigo='MDE');
-- Retira el dato antiguo parcial, sin sustituirlo por cero o NULL.
UPDATE rg_datos_area da JOIN rg_areas a ON a.id=da.area_id JOIN rg_indicadores i ON i.id=da.indicador_id JOIN rg_periodos p ON p.id=da.periodo_id
SET da.activo=0,da.estado_dato='NO_PUBLICABLE',da.observaciones='Retirado de publicación en Fase 7A.7: cobertura 93.5486%; Siria sin PIB nominal comparable.'
WHERE p.codigo='RG2025_V1' AND i.codigo='ECO_PC' AND a.codigo='MDE' AND da.activo=1;
-- Validaciones dentro de la transacción: si alguna devuelve discrepancias, hacer ROLLBACK manual.
SELECT i.codigo,COUNT(*) AS activos,COUNT(DISTINCT a.codigo) AS areas,SUM(da.valor IS NULL) AS nulos
FROM rg_datos_area da JOIN rg_indicadores i ON i.id=da.indicador_id JOIN rg_areas a ON a.id=da.area_id JOIN rg_periodos p ON p.id=da.periodo_id
WHERE da.activo=1 AND p.codigo='RG2025_V1' AND i.codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH') GROUP BY i.codigo;
-- El operador debe confirmar los resultados esperados antes de COMMIT.
COMMIT;
"""
(ROOT / "29_carga_indicadores_complementarios_7a7.sql").write_text(load, encoding="utf-8")

reversal = r"""-- FASE 7A.7. REVERSIÓN NO EJECUTADA.
-- Requiere que exista el respaldo versionado creado por 29_carga...7a7.sql.
USE `u794456529_map_sim_Mund`;
SET NAMES utf8mb4;
START TRANSACTION;
DELETE da FROM rg_datos_area da JOIN rg_indicadores i ON i.id=da.indicador_id JOIN rg_periodos p ON p.id=da.periodo_id
WHERE p.codigo='RG2025_V1' AND i.codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH');
INSERT INTO rg_datos_area SELECT * FROM rg_backup_datos_area_7a7_20260729;
DELETE i FROM rg_indicadores i JOIN rg_backup_indicadores_7a7_20260729 b ON b.codigo=i.codigo WHERE i.codigo='POB_URB' AND b.existia=0;
COMMIT;
-- DROP TABLE rg_backup_datos_area_7a7_20260729;
-- DROP TABLE rg_backup_indicadores_7a7_20260729;
"""
(ROOT / "95_reversion_indicadores_complementarios_7a7.sql").write_text(reversal, encoding="utf-8")

validation = r"""-- FASE 7A.7. CONSULTAS DE PREFLIGHT/VALIDACIÓN. NO EJECUTADAS.
USE `u794456529_map_sim_Mund`;
SELECT codigo,COUNT(*) AS coincidencias FROM rg_indicadores WHERE codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH') GROUP BY codigo;
SELECT i.codigo,COUNT(*) AS activos,COUNT(DISTINCT a.codigo) AS areas,SUM(da.valor IS NULL) AS nulos
FROM rg_datos_area da JOIN rg_indicadores i ON i.id=da.indicador_id JOIN rg_areas a ON a.id=da.area_id JOIN rg_periodos p ON p.id=da.periodo_id
WHERE da.activo=1 AND p.codigo='RG2025_V1' AND i.codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH') GROUP BY i.codigo;
SELECT a.codigo,i.codigo,p.codigo,COUNT(*) AS repeticiones FROM rg_datos_area da JOIN rg_areas a ON a.id=da.area_id JOIN rg_indicadores i ON i.id=da.indicador_id JOIN rg_periodos p ON p.id=da.periodo_id WHERE da.activo=1 AND p.codigo='RG2025_V1' GROUP BY a.codigo,i.codigo,p.codigo HAVING COUNT(*)<>1;
SELECT COUNT(*) AS total_activos FROM rg_datos_area da JOIN rg_periodos p ON p.id=da.periodo_id WHERE da.activo=1 AND p.codigo='RG2025_V1' AND da.indicador_id IN (SELECT id FROM rg_indicadores WHERE codigo IN ('TERR_DENS','POB_URB','POB_EDAD','HUM_EV','ECO_PC','HUM_IDH'));
SELECT a.codigo,i.codigo,da.valor FROM rg_datos_area da JOIN rg_areas a ON a.id=da.area_id JOIN rg_indicadores i ON i.id=da.indicador_id JOIN rg_periodos p ON p.id=da.periodo_id WHERE da.activo=1 AND p.codigo='RG2025_V1' AND ((i.codigo='TERR_DENS' AND da.valor<=0) OR (i.codigo='POB_URB' AND (da.valor<0 OR da.valor>100)) OR (i.codigo='POB_EDAD' AND (da.valor<10 OR da.valor>60)) OR (i.codigo='HUM_EV' AND (da.valor<40 OR da.valor>90)) OR (i.codigo='ECO_PC' AND da.valor<=0) OR (i.codigo='HUM_IDH' AND (da.valor<0 OR da.valor>1)));
"""
(ROOT / "validaciones_indicadores_complementarios_7a7.sql").write_text(validation, encoding="utf-8")

doc = r"""# Preparación de carga con dato no publicable — Fase 7A.7

Fecha: 2026-07-29  
Periodo: `RG2025_V1`

## Resultado preparado

Se preparan **53 valores publicables** y una combinación separada `ECO_PC/MDE` marcada `NO PUBLICABLE`. No se ejecutó ningún SQL de escritura y MySQL permanece sin cambios.

`POB_URB` no existía aún en el catálogo; el SQL usa el código aprobado y lo inserta condicionalmente dentro de la transacción solo si falta, sin crear un código alternativo. La fuente auxiliar de Taiwán se atribuye al código registrado `WB_WDI` a nivel de área y se conserva en las observaciones, porque el esquema actual no contiene códigos separados para DGBAS.

## Archivos de datos

- `datos-area-publicables-7a7.csv`: exactamente 53 claves.
- `datos-area-no-publicables-7a7.csv`: exactamente una fila, `ECO_PC/MDE`, sin valor público.

No se almacena cero ni una fila nula para representar Siria.

## Plan de operación futura

1. Crear, antes de la transacción, las tablas versionadas `rg_backup_datos_area_7a7_20260729` y `rg_backup_indicadores_7a7_20260729`.
2. Respaldar todas las filas existentes de `RG2025_V1` para `TERR_DENS`, `POB_URB`, `POB_EDAD`, `HUM_EV`, `ECO_PC` y `HUM_IDH`, incluidas las nueve áreas de `ECO_PC`.
3. Iniciar transacción.
4. Insertar `POB_URB` solo si el catálogo aún no lo contiene.
5. Actualizar los 44 registros existentes publicables y añadir las nueve filas `POB_URB`.
6. Desactivar el registro anterior `ECO_PC/MDE` con `activo=0` y `estado_dato=NO_PUBLICABLE`; no se reemplaza por cero ni por NULL.
7. Ejecutar validaciones y confirmar únicamente si el operador obtiene 53 activos y cero activos en `ECO_PC/MDE`.

El respaldo se identifica por fase y fecha y no se comparte con otros procesos. No se ejecuta DDL después de `START TRANSACTION`; la creación del respaldo ocurre antes de ella.

## Resultado esperado

| Indicador | Activos esperados |
|---|---:|
| `TERR_DENS` | 9 |
| `POB_URB` | 9 |
| `POB_EDAD` | 9 |
| `HUM_EV` | 9 |
| `HUM_IDH` | 9 |
| `ECO_PC` | 8 |
| **Total** | **53** |

`ECO_PC/MDE` debe devolver cero registros activos. Debe existir cero duplicidad, cero nulos cargados y cero ausencias convertidas en cero.

## Reversión

`95_reversion_indicadores_complementarios_7a7.sql` elimina únicamente las filas activas de los seis códigos en `RG2025_V1`, restaura el respaldo exacto y elimina el catálogo `POB_URB` solo si el marcador confirma que no existía antes. Los `DROP TABLE` del respaldo quedan comentados hasta verificar la restauración.

## Limitaciones del esquema

- `rg_datos_area` no tiene un estado específico `NO_PUBLICABLE`; se usa `activo=0`, `estado_dato=NO_PUBLICABLE` y una observación explícita.
- `rg_datos_area` exige `fuente_principal_id`, pero no tiene URL ni fuente auxiliar por fila; la procedencia auxiliar se conserva en `observaciones`.
- La clave única es `(area_id, indicador_id, periodo_id, anio_referencia)`; el preflight debe confirmar que no existe una segunda fila para esa combinación.
- La creación condicional de `POB_URB` solo es válida porque el código está aprobado y no hay duplicado de catálogo.

## Archivos SQL

- `29_carga_indicadores_complementarios_7a7.sql`: propuesta de carga, no ejecutada.
- `95_reversion_indicadores_complementarios_7a7.sql`: reversión exacta, no ejecutada.
- `validaciones_indicadores_complementarios_7a7.sql`: preflight y validaciones, no ejecutado.

## Estado

**PREPARACIÓN COMPLETADA — pendiente de aprobación para ejecutar la futura carga.**
"""
(ROOT / "PREPARACION-CARGA-INDICADORES-FASE-7A7.md").write_text(doc, encoding="utf-8")
