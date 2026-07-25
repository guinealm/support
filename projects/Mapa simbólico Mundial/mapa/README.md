# Mapa simbólico mundial

Primera versión visual e independiente del mapa territorial de **Retícula Global
2025**, proyecto perteneciente a **Support**. Presenta las nueve macroáreas,
permite explorar y personalizar el mapa y añade una comparación de población,
superficie, PIB nominal, gasto militar y ojivas de la edición congelada
`RG2025_V1`.

La aplicación funciona con archivos estáticos generados. No consulta ni
modifica MySQL ni la Tabla de Datos Consolidados.

## Estructura

- `index.html`: interfaz del mapa y tabla comparativa.
- `mapa.css`: diseño editorial y adaptación móvil.
- `mapa.js`: proyección, interacción, puntuaciones, ordenación y descarga SVG.
- `world.geojson`: geometrías Natural Earth simplificadas para navegador.
- `areas.json`: asignación territorial generada desde el maestro operativo.
- `paleta.json`: colores iniciales de las nueve macroáreas.
- `datos-indicadores.json`: cinco indicadores agregados de `RG2025_V1`.
- `correspondencias-cartograficas.json`: diferencias ISO3 documentadas.
- `informe-correspondencias.json`: resumen de cobertura cartográfica.
- `generar_datos.py`: regeneración de territorio y geometrías.
- `generar_indicadores.py`: regeneración de los indicadores comparativos.

## Ejecutar

Desde `projects/Mapa simbólico Mundial/mapa/`:

```powershell
python -m http.server 8088 --bind 127.0.0.1
```

Abrir `http://127.0.0.1:8088/`. Es necesario servir la carpeta por HTTP para
que el navegador pueda cargar los archivos JSON.

## Regenerar los datos

La asignación territorial no está escrita en JavaScript. `generar_datos.py` lee exclusivamente:

`../reticula_global_1c2_runner/rg_paises_areas_operativo.csv`

y genera:

- `areas.json`: áreas, nombres y entidades del CSV;
- `world.geojson`: geometrías enriquecidas mediante correspondencia ISO3 exacta;
- `informe-correspondencias.json`: correspondencias pendientes y verificaciones solicitadas.
- `correspondencias-cartograficas.json`: relación separada de diferencias cartográficas, sin aplicar equivalencias.

Dependencias: Python 3 y `pyshp`. Si no está disponible:

```powershell
python -m pip install pyshp
```

Ejecutar:

```powershell
python generar_datos.py
```

No se resuelven discrepancias mediante supuestos: cualquier entidad cartográfica sin ISO3 exacto queda neutral y se registra en el informe.

La geometría 1:10m se simplifica de forma reproducible durante la generación
(`SIMPLIFICATION_TOLERANCE = 0.025`) para mantener la aplicación utilizable en
escritorio y móvil sin sustituir la fuente cartográfica ni alterar sus ISO3.

La tabla comparativa usa `datos-indicadores.json`, generado exclusivamente desde
los agregados validados de `RG2025_V1`:

```powershell
python generar_indicadores.py
```

El generador lee los CSV de territorio y población, economía y fuerza militar
de `../reticula_global_1c2_runner/output_1c2/`. No consulta MySQL ni contiene
valores transcritos en JavaScript.

## Cartografía y licencia

- **Fuente:** Natural Earth, `Admin 0 – Countries`, escala 1:10m, versión 5.1.1.
- **Archivo de origen:** `../natural-earth-source/ne_10m_admin_0_countries.shp`.
- **Procedencia:** https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/
- **Licencia:** datos de dominio público según Natural Earth.
- **Proyección de pantalla:** Equal Earth, proyección equivalente pseudocilíndrica; no se utiliza Mercator.

Los países mantienen fronteras finas. Las entidades que el CSV excluye de los cálculos y las entidades cartográficas sin correspondencia se muestran con gris tramado.

## Verificación de correspondencias

`informe-correspondencias.json` se regenera junto con el mapa y separa:

- los ISO3 del CSV que no tienen una geometría independiente en esta edición de Natural Earth;
- las entidades cartográficas que no tienen correspondencia ISO3 exacta en el CSV;
- las comprobaciones territoriales solicitadas para México, Rusia, Bielorrusia, Cáucaso, Irán, Chipre, China, Hong Kong, Macao, Taiwán e India.

No se añade ninguna equivalencia manual. Los elementos pendientes quedan neutrales y documentados. La información del país seleccionado aparece en la esquina superior izquierda del mapa, tanto al pasar el puntero como al recorrer los países con el teclado.

## Estado local de la interfaz

Los colores personalizados se guardan en `sessionStorage`: sobreviven a recargas dentro de la misma sesión del navegador y se descartan al terminarla. “Restaurar colores” recupera `paleta.json`.

La tabla calcula escalas logarítmicas 1–10 únicamente para comparar magnitudes
entre las nueve áreas. Conserva y muestra también los valores naturales. Gasto
militar y ojivas se presentan por separado.

## Limitaciones actuales

- No existe todavía integración directa con `datos.php`; el servidor estático
  utiliza `datos-indicadores.json`.
- No se calcula un índice militar compuesto: falta una medida validada de
  tecnología y capacidad de proyección.
- No hay fichas individuales de macroárea.
- La exportación disponible es SVG del mapa; no incluye PNG ni PDF.
- Las correspondencias cartográficas pendientes permanecen neutrales y
  documentadas, sin equivalencias silenciosas.
- La paleta es editable durante la sesión y puede revisarse en fases futuras.
