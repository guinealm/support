# Cierre de la Fase 6 — Primera versión visual

**Proyecto:** Retícula Global 2025  
**Entorno:** Support  
**Fecha de cierre:** 25 de julio de 2026  
**Estado final:** **GO**

## Objetivo

Construir, verificar y preparar para publicación una primera versión funcional
del Mapa simbólico mundial, independiente de MySQL y de la API, basada en la
edición congelada `RG2025_V1`.

## Alcance construido

- Mapa mundial vectorial interactivo en proyección Equal Earth.
- Coloreado automático desde el maestro territorial.
- Fronteras nacionales, información por país y tratamiento neutral de
  Antártida y entidades fuera de cálculo.
- Personalización y restauración de la paleta durante la sesión.
- Resaltado de macroáreas y descarga del mapa como SVG.
- Tabla comparativa ordenable y sincronizada con el mapa.
- Valores naturales y puntuaciones logarítmicas 1–10 para cinco indicadores.
- Adaptación de mapa, controles, leyenda y tabla a escritorio y móvil.

No se modificaron MySQL ni la API y no se añadieron indicadores nuevos.

## Nueve macroáreas

`AFR`, `APC`, `CHN`, `EUR`, `MDE`, `NAC`, `RUE`, `SAI` y `SAM`.

## Fuentes territoriales y cartográficas

- **Fuente territorial:** `reticula_global_1c2_runner/rg_paises_areas_operativo.csv`.
- **Cartografía:** Natural Earth, Admin 0 – Countries, 1:10m, versión 5.1.1,
  datos de dominio público.
- **Proyección:** Equal Earth; no se utiliza Mercator.
- Las discrepancias ISO3 no se resuelven mediante supuestos: quedan en
  `correspondencias-cartograficas.json`.

## Indicadores incluidos

| Código | Indicador | Año | Unidad | Fuente |
|---|---|---:|---|---|
| `POB_TOTAL` | Población total | 2025 | personas | ONU World Population Prospects 2024 |
| `TERR_SUP` | Superficie terrestre | 2023 | km² | FAOSTAT |
| `ECO_PIB` | PIB nominal | 2024 | USD corrientes | Banco Mundial WDI |
| `MIL_GASTO` | Gasto militar | 2025 | USD corrientes | SIPRI, edición 2026 |
| `MIL_NUC` | Inventario nuclear estimado | 2026 | ojivas | SIPRI Yearbook 2026 |

EUR y NAC incluyen algunos datos nacionales de PIB de 2023. APC incluye algunos
datos militares de 2024. Estas excepciones permanecen documentadas.

## Normalización 1–10

Las puntuaciones se calculan en el navegador de forma independiente para cada
indicador:

`1 + 9 × (log(valor) − log(mínimo)) / (log(máximo) − log(mínimo))`

Para ojivas se aplica `log(valor + 1)`. El mínimo recibe 1, el máximo 10, los
empates reciben la misma puntuación y los valores ausentes no participan en la
normalización. La interfaz muestra un decimal sin redondear los valores
intermedios.

## Exclusión del índice militar compuesto

No se calcula un índice militar único ni se combinan gasto y ojivas. Falta una
medida validada de tecnología y capacidad de proyección. `TEC_NET` no se emplea
como sustituto y no se introducen puntuaciones manuales.

## Resultados de verificación

- **6.2A — Verificación técnica:** GO. Estructura, JSON, rutas, códigos,
  correspondencias territoriales y servidor local verificados.
- **6.2B — Verificación visual del usuario:** GO. Fase cerrada por conformidad
  del usuario.
- **6.3A — Inventario operativo de datos:** GO con observaciones. Existen nueve
  agregados para los indicadores incluidos; no existe componente tecnológico
  militar validado.
- **6.3B — Tabla e indicadores visuales:** GO. Tabla, puntuaciones, ordenación,
  sincronización y adaptación móvil implementadas.
- **6.3C — Validación técnica final de la integración:** GO. Nueve áreas únicas,
  datos completos, extremos 1–10, ceros nucleares, generación reproducible y
  recursos HTTP comprobados.

## Observaciones no bloqueantes

- Natural Earth contiene 25 entidades cartográficas neutrales sin
  correspondencia exacta y el maestro contiene 11 códigos sin geometría
  independiente en esta edición.
- Los números de la leyenda representan entidades del maestro territorial y se
  muestran expresamente como “entidades”.
- El mapa utiliza actualmente archivos estáticos generados para poder funcionar
  en el servidor local.

## Archivos de la primera versión

### Creados

- `mapa/index.html`
- `mapa/mapa.css`
- `mapa/mapa.js`
- `mapa/world.geojson`
- `mapa/areas.json`
- `mapa/paleta.json`
- `mapa/correspondencias-cartograficas.json`
- `mapa/informe-correspondencias.json`
- `mapa/datos-indicadores.json`
- `mapa/generar_datos.py`
- `mapa/generar_indicadores.py`
- `mapa/README.md`
- `CIERRE-FASE-6-PRIMERA-VERSION-VISUAL-2026-07-25.md`

No se incluyen registros temporales del servidor, capturas, descargas SVG ni
copias de seguridad.

## Prueba local

`http://127.0.0.1:8088/`

Desde `mapa/`:

```powershell
python -m http.server 8088 --bind 127.0.0.1
```

## Pendientes para fases posteriores

- Integración real con `datos.php` bajo Support.
- Posible incorporación de tecnología y capacidad de proyección militar.
- Publicación de fichas de macroárea.
- Revisión específica de accesibilidad.
- Eventual exportación adicional a PNG/PDF.
- Posible ajuste posterior de la paleta.

La primera versión visual queda cerrada con estado **GO**.
