# Generación de archivos de Retícula Global

Esta es la ubicación canónica de los tres generadores de la aplicación:

- `generar_datos.py`: prepara `areas.json`, `world.geojson` y los informes de correspondencia;
- `generar_indicadores.py`: prepara `datos-indicadores.json`;
- `generar_territorios.py`: prepara `territorios.json`.

## Fuentes

- Natural Earth: `fuentes/natural-earth-source/`;
- maestro territorial: `C:/jumalenin-ecosistema/archivo/reticula-global-2025/reticula_global_1c2_runner/rg_paises_areas_operativo.csv`;
- agregados congelados: `C:/jumalenin-ecosistema/archivo/reticula-global-2025/reticula_global_1c2_runner/output_1c2/`.

El maestro y los agregados permanecen en el archivo histórico porque otros generadores documentados también dependen de ellos. Esta referencia evita duplicarlos o romper esos procesos.

## Restricción

No ejecutar estos scripts sin autorización expresa. Su ejecución escribe archivos JSON o GeoJSON de la aplicación activa. G1 solo autorizó su traslado y la actualización de rutas.

Natural Earth Admin 0 Countries 1:10m es una fuente cartográfica abierta de dominio público; la versión se conserva en el archivo `fuentes/natural-earth-source/ne_10m_admin_0_countries.VERSION.txt`.
