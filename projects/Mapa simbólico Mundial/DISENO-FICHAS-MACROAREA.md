# Fase 6.6A — Diseño funcional de las fichas

## Decisión de ruta

Se adopta `projects/mapa-mundi/area.html?codigo=AFR`. Una única plantilla evita
duplicar nueve documentos, usa una ruta sin espacios ni acentos, permite enlaces
directos y conserva de forma nativa el historial atrás/adelante. Una estructura
`areas/AFR/` requeriría reescrituras del servidor o nueve archivos de entrada.

El prototipo inicial quedó limitado a AFR. En la fase 6.6B la misma plantilla
se habilitó para los nueve códigos, sin duplicar archivos HTML.

## Contrato de datos

La ficha realiza una sola petición principal:

`GET /api/reticula/v1/datos.php?area=AFR`

La respuesta real contiene `ok`, `data`, `meta` y `errors`. Para AFR devuelve
27 registros repartidos entre TERR (3), POB (5), ECO (3), HUM (3), MIL (5),
ENE (5), CLI (2) y TEC (1). Cada registro incluye área, bloque, indicador,
valor, años mínimo/máximo/de referencia, unidad, cobertura, método, estado,
procedencia, fuente con URL y observaciones.

La ficha valida HTTP 200, JSON, `ok === true`, edición `RG2025_V1`, código de
área coherente, indicadores sin duplicados y presencia de los cinco indicadores
principales. El tiempo máximo es cinco segundos.

Se recomienda una petición por área (opción A): entrega los datos y metadatos
necesarios con menor complejidad. Cuando se llegue desde el mapa, la ficha puede
recibir el código por URL; no conviene depender de memoria compartida porque
rompería los enlaces directos. `datos-indicadores.json` continúa como respaldo.

## Estructura

1. Cabecera con nombre, código, color, edición, retorno y silueta.
2. Territorio: entidades, listado, superficie y porcentaje.
3. Demografía: población, porcentaje y densidad.
4. Economía: PIB, PIB por habitante y porcentaje.
5. Dimensión militar: gasto, gasto por habitante, gasto/PIB, porcentaje y
   ojivas, sin índice compuesto.
6. Fuentes y metodología desplegable.

Las puntuaciones logarítmicas 1–10 son secundarias y solo acompañan los cinco
valores principales.

## Fórmulas derivadas

- Densidad = `POB_TOTAL / TERR_SUP`.
- PIB por habitante = `ECO_PIB / POB_TOTAL`.
- Porcentaje de población = `POB_TOTAL área / suma POB_TOTAL nueve áreas * 100`.
- Porcentaje de superficie = `TERR_SUP área / suma TERR_SUP nueve áreas * 100`.
- Porcentaje de PIB = `ECO_PIB área / suma ECO_PIB nueve áreas * 100`.
- Gasto por habitante = `MIL_GASTO / POB_TOTAL`.
- Gasto respecto al PIB = `MIL_GASTO / ECO_PIB comparable cubierto * 100`.
- Porcentaje de gasto = `MIL_GASTO área / suma MIL_GASTO nueve áreas * 100`.

Los derivados se calculan en el navegador y no se almacenan en MySQL.
Para gasto militar se prefieren los agregados validados `MIL_PC`, `MIL_PIB` y
`MIL_PCT` devueltos por la API, porque `MIL_PIB` tiene en cuenta la cobertura
comparable. Las fórmulas directas se reservan para el respaldo y se identifican
como tales.

## Lista territorial y navegación

`territorios.json` se genera mediante `generar_territorios.py` exclusivamente
desde `rg_paises_areas_operativo.csv`. Conserva nombre, ISO3, tipo, soberanía,
inclusión en mapa, inclusión en cálculos y observaciones. No hay listas
territoriales manuales en JavaScript.

En la fase de construcción completa, pulsar el área mantendrá el resaltado
actual y ofrecerá una acción explícita «Ver ficha». Las filas harán lo mismo sin
perder su selección. La ficha conserva el color de `paleta.json` y presenta un
enlace visible «Volver al mapa».

## Accesibilidad y adaptación

La ficha utiliza encabezados jerárquicos, tablas con encabezados, enlaces
identificables, estados anunciables, contraste textual y foco visible. El
color siempre aparece junto al nombre y código. En móvil adopta una sola
columna y mantiene desplazamiento propio únicamente en la tabla territorial.

## Limitaciones actuales

- Las nueve áreas comparten una plantilla; no existen páginas HTML separadas.
- No se añade ningún indicador ni índice compuesto.
- Los porcentajes se calculan contra las nueve áreas congeladas del respaldo,
  coherentes con `RG2025_V1`.
- La validación visual en navegador depende de disponer de un navegador
  controlable; las demás comprobaciones pueden realizarse por HTTP y sintaxis.
