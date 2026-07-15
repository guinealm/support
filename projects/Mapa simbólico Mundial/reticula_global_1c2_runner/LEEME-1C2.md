# Ejecutor Fase 1C.2 — Retícula Global 2025

Este paquete completa la carga de territorio y población en el equipo local.

## Contenido

- `rg_paises_areas.csv`
- `rg_paises_areas_operativo.csv`
- `construir_territorio_poblacion_1c2.py`
- `requirements.txt`

## Ejecución desde VS Code / PowerShell

```powershell
cd <carpeta-del-paquete>
py -m pip install -r requirements.txt
py construir_territorio_poblacion_1c2.py
```

La salida se genera en:

`output_1c2/`

Archivos principales:

- `rg_territorio_poblacion_pais.csv`
- `rg_agregados_territorio_poblacion.csv`
- `validacion-territorio-poblacion-1c2.md`
- `incidencias_territorio_poblacion.csv`
- `fuentes_1c2.json`

## Fuentes descargadas por el script

- Población 2025 y 2050: ONU WPP 2024, servida por Our World in Data.
- Edad mediana 2025: ONU WPP 2024, servida por Our World in Data.
- Superficie terrestre: FAOSTAT 2025, servida por Our World in Data.

## Revisión obligatoria

Revisar especialmente:

- China, Hong Kong y Macao;
- Taiwán;
- Kosovo;
- territorios dependientes;
- filas marcadas `REVISAR`.

No importa datos a MySQL. Primero genera y valida los CSV.
