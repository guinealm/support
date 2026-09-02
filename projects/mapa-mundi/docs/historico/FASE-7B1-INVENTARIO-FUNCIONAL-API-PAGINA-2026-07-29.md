# Fase 7B.1 — Inventario funcional de API y página actual

## Resumen ejecutivo

La aplicación pública identificada está en `projects/mapa-mundi/`. Su JavaScript usa el endpoint `/api/reticula/v1/datos.php` y un respaldo local `datos-indicadores.json`. La Tabla de Datos Consolidados histórica está en `projects/Mapa simbólico Mundial/tabla-datos-consolidados.html` y consume `api/reticula/v1/datos.php` con `fetch` relativo.

## Endpoint y flujo

- Endpoint local relativo: `/api/reticula/v1/datos.php`.
- URL pública deducible: `https://support.jumalenin.com/api/reticula/v1/datos.php`.
- Método: `GET`.
- Parámetros observados en `mapa.js`: `indicador` y, en fichas, `area`.
- La API devuelve registros por área; el mapa valida `ok`, edición `RG2025_V1`, nueve áreas y usa respaldo local si falla.
- La tabla histórica usa `fetch('api/reticula/v1/datos.php')` desde `tabla-datos-consolidados.html`.

## Indicadores

| Código | Estado observado |
|---|---|
| `TERR_DENS` | Preparado en datos/documentación; no forma parte de los cinco indicadores principales actuales de `mapa.js`. |
| `POB_EDAD` | Preparado en datos/documentación; no forma parte de los cinco indicadores principales actuales de `mapa.js`. |
| `HUM_EV` | Preparado en datos/documentación; no forma parte de los cinco indicadores principales actuales de `mapa.js`. |
| `ECO_PC` | Preparado; conserva limitación MDE documentada. |
| `HUM_IDH` | Preparado; no forma parte de los cinco indicadores principales actuales de `mapa.js`. |
| `POB_URB` | No cargado en MySQL ni presente como métrica principal; debe mostrarse como pendiente, sin valor. |

La API pública no se consultó desde este entorno; por tanto, la presencia real de estos seis códigos en la respuesta HTTP queda pendiente de prueba GET.

## Áreas

`mapa.js` define `EXPECTED_AREAS = [AFR, APC, CHN, EUR, MDE, NAC, RUE, SAI, SAM]`. `areas.json`, `territorios.json` y `datos-indicadores.json` usan `MDE` y el nombre visible Oriente Medio. No se observaron códigos `MEA` en los archivos revisados.

## Campos y tratamiento

`mapa.js` normaliza registros con área, indicador, valor, año, unidad, fuente y observaciones cuando llegan; conserva metadatos de respaldo y muestra aviso cuando usa el JSON local. El contrato exacto de la API y los campos que llegan al navegador deben confirmarse mediante GET real.

## Tabla de Datos Consolidados

Archivo: `projects/Mapa simbólico Mundial/tabla-datos-consolidados.html`.

- JavaScript embebido: funciones alrededor de las líneas 139 y 223.
- Carga: `fetch(API_URL)`.
- Endpoint: `api/reticula/v1/datos.php`.
- La tabla se genera dinámicamente en el HTML; se observaron agrupación, ordenación y renderizado de filas en el script embebido.
- No se identificó una ficha reutilizable dentro de esta página; las fichas dinámicas están en `projects/mapa-mundi/area.html` con `area.js`.

## Fuentes, años y MDE

Los JSON locales contienen año, unidad, fuente, cobertura, método y observaciones. `area.js` conserva observaciones y muestra datos de respaldo cuando corresponde. `ECO_PC/MDE` debe mantener su limitación metodológica; no se ha verificado en esta inspección que la API pública la exponga sin pérdida.

## Carencias para 7B.2

1. Confirmar mediante GET la respuesta real y los seis códigos.
2. Confirmar qué campos de fuente, estado y observación llegan al navegador.
3. Diseñar el bloque visible del perfil usando los cinco indicadores actualmente disponibles.
4. Mostrar `POB_URB` como “Pendiente de incorporación”.
5. Mantener visible la limitación de `ECO_PC/MDE`.

## Conclusión

**NO-GO para iniciar 7B.2.** La arquitectura local y los archivos están identificados, pero falta verificar mediante petición HTTP la respuesta real de la API y la llegada de metadatos al navegador.

Siguiente tarea propuesta: completar una verificación GET de solo lectura del endpoint y documentar su respuesta antes de diseñar la presentación visible.

## Verificación pública GET — Fase 7B.1B

Fecha de comprobación: 2026-07-29.

Se intentaron peticiones GET a:

- `https://support.jumalenin.com/api/reticula/v1/datos.php`
- el endpoint con `indicador=TERR_DENS`, `POB_EDAD`, `HUM_EV`, `ECO_PC`, `HUM_IDH` y `POB_URB`;
- `?indicador=ECO_PC&area=MDE`;
- la ruta relativa bajo `/projects/Mapa%20simb%C3%B3lico%20Mundial/api/reticula/v1/datos.php`.

Todas fallaron desde este entorno con `Unable to connect to the remote server`; no fue posible obtener código HTTP, Content-Type ni JSON. No se inventan registros ni campos de respuesta.

La inspección local confirma que `mapa.js` consume `ok`, edición, área, indicador, valor, año, unidad, fuente y observaciones, y que `area.js` usa el mismo endpoint con filtro `area`. La tabla histórica usa `fetch('api/reticula/v1/datos.php')`, que desde `/projects/Mapa simbólico Mundial/tabla-datos-consolidados.html` resolvería bajo ese directorio de proyecto, no necesariamente en `/api/reticula/v1/datos.php`; debe verificarse públicamente antes de corregirla.

## Incorporación de verificación externa

Una comprobación externa del 29 de julio de 2026 confirmó que `https://support.jumalenin.com/api/reticula/v1/datos.php` responde públicamente con JSON y registros organizados por área. Cada registro incluye área, bloque, indicador, valor, años, cobertura, método, procedencia, estado, fuente y observaciones.

El caso `ECO_PC/MDE` llega con `MDE`, `Oriente Medio`, valor `13124.895709`, año 2024, unidad `USD_corrientes_por_hab`, cobertura `82.6387 %`, método `PIB area / poblacion 2025 area`, estado `LIMITACION`, fuente Banco Mundial/WDI y observación de cobertura incompleta. Debe mostrarse con advertencia y nunca sustituirse por cero.

Para 7B.2 se podrá consultar una vez el endpoint general, filtrar en JavaScript los cinco indicadores (`TERR_DENS`, `POB_EDAD`, `HUM_EV`, `ECO_PC`, `HUM_IDH`), agrupar por `area.codigo`, ordenar por `area.orden_visual`, mostrar `POB_URB` como `Pendiente de incorporación` y conservar `estado_dato` y `observaciones`.

Se mantiene la observación de que `fetch('api/reticula/v1/datos.php')` en la tabla histórica puede resolver bajo el directorio de la página. No se corrige en esta tarea.

## Conclusión actualizada

**GO condicionado para iniciar 7B.2.** La implementación deberá usar `/api/reticula/v1/datos.php`, validar los cinco indicadores, mostrar ausencias explícitamente, no convertirlas en cero, conservar estados y observaciones, mostrar `POB_URB` como pendiente y tratar `ECO_PC/MDE` como dato limitado.
