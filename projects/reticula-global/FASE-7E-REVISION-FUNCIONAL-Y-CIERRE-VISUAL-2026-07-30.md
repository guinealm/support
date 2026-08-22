# Fase 7E.1 — Inventario funcional y cierre visual

Fecha: 30 de julio de 2026  
Ámbito público: `https://support.jumalenin.com/projects/mapa-mundi/`

## 1. Objetivo

Inventariar la versión pública actual de Retícula Global y preparar la lista de comprobación funcional, visual y de accesibilidad que deberá ejecutarse en 7E.2. Esta fase no modifica la aplicación, la API, MySQL, SQL, los datos ni la metodología.

## 2. Rutas y vistas

| Vista o recurso | Ruta pública | Función | Estado HTTP observado |
|---|---|---|---:|
| Entrada histórica | `/projects/mapa_mundi.html` | Conserva enlaces antiguos y dirige a la ruta canónica | 200 |
| Aplicación principal | `/projects/mapa-mundi/` | Mapa, perfil medio y comparación | 200 |
| Ficha dinámica | `/projects/mapa-mundi/area.html?codigo=CODIGO` | Plantilla única de macroárea | 200 para los nueve códigos |
| API general | `/api/reticula/v1/datos.php` | Perfil medio completo | 200 |
| API por indicador | `/api/reticula/v1/datos.php?indicador=CODIGO` | Cinco indicadores principales de la comparación | 200 en las cinco consultas |
| API por área | `/api/reticula/v1/datos.php?area=CODIGO` | Datos de una ficha | 200 para MDE en la comprobación |

La entrada histórica no devuelve una redirección HTTP 3xx. Es una página 200 que utiliza `meta refresh`, `window.location.replace()` y un enlace visible hacia `./mapa-mundi/`.

### Códigos válidos de ficha

| Orden | Código | Macroárea | Ruta |
|---:|---|---|---|
| 1 | AFR | África | `area.html?codigo=AFR` |
| 2 | APC | Asia-Pacífico | `area.html?codigo=APC` |
| 3 | CHN | China | `area.html?codigo=CHN` |
| 4 | EUR | Europa | `area.html?codigo=EUR` |
| 5 | MDE | Oriente Medio | `area.html?codigo=MDE` |
| 6 | NAC | Norteamérica, Centroamérica y Caribe | `area.html?codigo=NAC` |
| 7 | RUE | Rusia-Eurasia | `area.html?codigo=RUE` |
| 8 | SAI | Subcontinente indio | `area.html?codigo=SAI` |
| 9 | SAM | Sudamérica | `area.html?codigo=SAM` |

Las nueve variantes devolvieron HTTP 200. El código se valida en JavaScript; un código ajeno al catálogo debe mostrar un error comprensible y no datos de otra macroárea.

## 3. Recursos públicos

La aplicación pública contiene:

- `index.html`, `mapa.css` y `mapa.js`;
- `area.html`, `area.css` y `area.js`;
- `world.geojson`;
- `areas.json`;
- `territorios.json`;
- `paleta.json`;
- `datos-indicadores.json`;
- documentación metodológica no utilizada como recurso de ejecución.

Todos los recursos de ejecución enumerados respondieron HTTP 200 el 30 de julio de 2026.

## 4. Bloques de la página principal

1. Cabecera breve y enlace de retorno a Support.
2. Introducción y título principal.
3. Barra de controles:
   - mostrar u ocultar fronteras;
   - selector «Resaltar»;
   - enlace condicional «Ver ficha de…»;
   - descarga SVG.
4. Mapa vectorial Equal Earth:
   - países con ISO3;
   - color por macroárea;
   - territorios excluidos en trama neutral;
   - tooltip con país, ISO3 y macroárea;
   - selección de macroárea.
5. Leyenda:
   - nueve áreas;
   - código y nombre;
   - número de entidades;
   - selector cromático por área;
   - restauración de la paleta.
6. Perfil medio de la población:
   - nueve tarjetas;
   - cinco indicadores disponibles;
   - urbanización pendiente;
   - fuentes, años, cobertura, estado y observaciones;
   - dos enlaces independientes a cada ficha.
7. Comparación de macroáreas:
   - cinco indicadores principales;
   - valores naturales;
   - puntuaciones relativas 1–10;
   - barras visuales;
   - ordenación por columna;
   - selección coordinada con el mapa;
   - enlaces a fichas.
8. Nota militar y desplegable metodológico.
9. Pie con fuente cartográfica y edición.

## 5. Bloques de las fichas

1. Cabecera y «Volver al mapa».
2. Hero con nombre, código, color y silueta.
3. Navegación anterior/siguiente en el orden de las nueve áreas.
4. Estado de carga y aviso condicional de respaldo.
5. Territorio:
   - entidades;
   - superficie;
   - proporción territorial;
   - tabla desplegable de países y territorios.
6. Demografía:
   - población;
   - proporción;
   - densidad.
7. Perfil medio:
   - `TERR_DENS`;
   - `POB_EDAD`;
   - `HUM_EV`;
   - `ECO_PC`;
   - `HUM_IDH`;
   - `POB_URB` pendiente.
8. Economía.
9. Dimensión militar sin índice compuesto.
10. Fuentes, años y fórmulas.
11. Pie y retorno al mapa.

## 6. Interacciones inventariadas

### Mapa y leyenda

- Cambio del color de una macroárea y persistencia en `sessionStorage`.
- Restauración de la paleta inicial.
- Activación y desactivación de fronteras.
- Selección mediante el selector superior.
- Selección mediante país en el mapa.
- Tooltip mediante puntero, foco y pulsación.
- Resaltado y atenuación de las demás áreas.
- Aparición y actualización del enlace «Ver ficha de…».
- Descarga de una copia SVG sin atributos interactivos.

### Perfil medio

- Enlace del nombre de cada macroárea.
- Enlace «Ver ficha».
- Desplegable nativo de fuente, año y observaciones.
- Estado de carga y mensaje de error.
- Conservación de la tarjeta aunque falte un indicador.

### Tabla comparativa

- Ordenación ascendente y descendente por seis columnas.
- Actualización de `aria-sort` y anuncio del criterio.
- Selección de fila mediante clic, Enter o barra espaciadora.
- Segundo accionamiento para volver a todas las áreas.
- Sincronización con el selector y el mapa.
- Enlace independiente «Ver ficha».
- Desplazamiento horizontal limitado al contenedor en pantallas estrechas.

### Fichas

- Carga por parámetro `codigo`.
- Anterior y siguiente con navegación circular.
- Retorno al mapa desde cabecera y pie.
- Despliegue de territorios, fuentes del perfil y fórmulas.
- Respaldo local si la consulta de área falla.

## 7. Fuentes de datos y estrategia de carga

- La página principal consulta `/api/reticula/v1/datos.php` para el perfil medio.
- La comparación consulta en paralelo `POB_TOTAL`, `TERR_SUP`, `ECO_PIB`, `MIL_GASTO` y `MIL_NUC`, con timeout de cinco segundos.
- `datos-indicadores.json` es el respaldo de la comparación y de las fichas.
- La ficha consulta `/api/reticula/v1/datos.php?area=CODIGO`.
- `areas.json`, `territorios.json`, `paleta.json` y `world.geojson` son recursos relativos de la aplicación.

## 8. Estados especiales

| Estado | Presentación o comportamiento esperado |
|---|---|
| Carga del mapa | Mensaje visible y `aria-busy="true"` hasta completar |
| Error general | Mensaje comprensible; no dejar el bloque vacío |
| Uso de respaldo | Aviso visible de RG2025_V1 |
| Indicador ausente | «Dato no disponible»; nunca `null`, `undefined`, `NaN` o cero inventado |
| `POB_URB` | «Pendiente de incorporación» |
| `ECO_PC/MDE` | Valor visible, advertencia permanente de cobertura incompleta y metadatos desplegables |
| Territorio excluido | Trama gris neutral y fuera de cálculos |
| Sin área seleccionada | Nueve áreas visibles y enlace superior a ficha oculto |
| Área seleccionada | Área resaltada, fila marcada y enlace a ficha visible |
| Paleta personalizada | Colores conservados durante la sesión |
| Valor nuclear cero | Cero válido, no confundir con ausencia |
| Código de ficha inválido | Error explícito; no sustituir silenciosamente por otra área |

## 9. Accesibilidad inventariada

- Un `h1` por vista y `h2` para bloques.
- Tarjetas del perfil construidas como `article` con `h3` y `dl`.
- Tablas con `caption`, `thead`, `th` y `scope`.
- Controles nativos para botones, enlaces, selectores y `details`.
- Foco global visible de 3 px.
- Estados mediante `role="status"`, `aria-live`, `role="alert"` y `aria-busy`.
- Mapa navegable por foco y tooltip accesible.
- `prefers-reduced-motion` aplicado a transiciones y desplazamiento.
- Color acompañado de nombre, código, texto y estados.

## 10. Responsive inventariado

- Página principal:
  - espacio amplio: mapa/leyenda y perfil en tres columnas;
  - hasta 1000 px: leyenda reorganizada y perfil en dos columnas;
  - hasta 680 px: una columna;
  - hasta 390 px: valores del perfil debajo de sus etiquetas.
- Fichas:
  - hero en dos columnas y métricas en tres;
  - hasta 760 px: hero, métricas, fuentes y perfil en una columna.
- Las tablas territoriales y comparativas tienen contenedores de desplazamiento horizontal propios.
- Textos, valores, observaciones y URLs admiten salto de línea.

## 11. Hallazgos para revisar en 7E.2

1. La ruta histórica funciona mediante redirección en el documento, pero no mediante una respuesta HTTP 3xx. Es compatible con navegador, aunque debe comprobarse el comportamiento con JavaScript desactivado y tecnologías de asistencia.
2. Las filas de la tabla reciben foco y admiten Enter/Espacio, pero la regla `.comparison-table tbody tr:focus-visible` elimina el contorno y se apoya en un cambio de fondo discreto. Debe verificarse si el foco resulta inequívoco.
3. Cada geometría del mapa es un punto de tabulación. Esto permite consultar países por teclado, pero puede producir un recorrido muy largo antes de llegar a los bloques siguientes.
4. El texto del error general del mapa menciona el servidor local y el README, aunque la salida pública no incluye `README.md`. Conviene comprobar el mensaje público ante un fallo real.
5. La ficha usa datos locales de respaldo si falla la API de área; debe comprobarse que los cinco indicadores del perfil no desaparezcan si el respaldo no contiene alguno de ellos.
6. La carga principal del perfil no tiene timeout propio, a diferencia de las cinco consultas de comparación. Debe comprobarse el comportamiento ante una respuesta que no termina.
7. El retorno desde una ficha apunta a `./` y no conserva la macroárea seleccionada ni la posición de desplazamiento. Es una decisión funcional aceptable, pero debe validarse editorialmente.
8. No hay una declaración visible de versión del código desplegado. La coincidencia entre commit y publicación debe verificarse mediante el procedimiento de despliegue.

Estos hallazgos no implican por sí solos un NO-GO; son puntos de decisión para el cierre.

## 12. Lista de comprobación para 7E.2

### A. Rutas y carga

- [ ] La entrada histórica conduce a la ruta canónica.
- [ ] La página principal devuelve 200 y carga sin 404.
- [ ] Las nueve URLs de ficha devuelven 200.
- [ ] CSS, JavaScript, GeoJSON y cuatro JSON cargan.
- [ ] La API general, las cinco consultas por indicador y las consultas por área responden.
- [ ] No aparecen rutas locales, staging ni referencias rotas.
- [ ] No hay errores JavaScript ni promesas rechazadas sin tratar.

### B. Mapa

- [ ] Mapa mundial completo, Equal Earth, fondo claro y fronteras discretas.
- [ ] Nueve colores diferenciables y territorios excluidos en trama gris.
- [ ] Tooltip correcto mediante puntero, foco y pulsación.
- [ ] Selección por país y selector coherente.
- [ ] Mostrar/ocultar fronteras funciona.
- [ ] Enlace superior a ficha aparece, se actualiza y se oculta correctamente.
- [ ] Cambio de color afecta mapa, leyenda y tabla.
- [ ] Restaurar colores recupera la paleta.
- [ ] El SVG descargado es válido y puede abrirse.

### C. Perfil medio principal

- [ ] Existen exactamente nueve tarjetas.
- [ ] Cada tarjeta muestra los cinco indicadores o «Dato no disponible».
- [ ] `POB_URB` muestra «Pendiente de incorporación».
- [ ] Nombre y «Ver ficha» conducen al mismo código.
- [ ] Los desplegables conservan fuente, año, cobertura, estado y observaciones.
- [ ] `ECO_PC/MDE` muestra valor y advertencia con `details` cerrado.
- [ ] Ningún fallo de un indicador elimina la tarjeta completa.

### D. Comparación

- [ ] Nueve filas y cinco indicadores.
- [ ] Valores naturales, barras y puntuaciones son coherentes.
- [ ] Ordenación funciona en ambos sentidos y anuncia el criterio.
- [ ] Clic, Enter y Espacio seleccionan/deseleccionan filas.
- [ ] Selección sincronizada con mapa y selector.
- [ ] «Ver ficha» no activa accidentalmente la fila.
- [ ] Primera columna y desplazamiento horizontal son utilizables en móvil.

### E. Fichas

- [ ] Nombre, código, color y silueta correctos en las nueve áreas.
- [ ] Datos territoriales, demográficos, económicos y militares corresponden al área.
- [ ] Perfil medio con cinco indicadores y urbanización pendiente.
- [ ] MDE conserva la limitación metodológica.
- [ ] Lista territorial, fuentes y fórmulas se despliegan.
- [ ] Anterior/siguiente respetan el orden y funcionan en los extremos.
- [ ] «Volver al mapa» funciona desde cabecera y pie.
- [ ] Código inválido muestra error comprensible.

### F. Estados y resiliencia

- [ ] Estados de carga visibles y anunciados sin repeticiones.
- [ ] Caída de la API activa el respaldo y muestra aviso.
- [ ] Una celda ausente no se convierte en cero.
- [ ] Cero nuclear válido permanece como cero.
- [ ] Error de recurso crítico deja un mensaje útil.
- [ ] Timeouts no dejan la interfaz indefinidamente bloqueada.

### G. Accesibilidad

- [ ] Jerarquía de encabezados coherente.
- [ ] Recorrido completo con Tab en orden visual.
- [ ] Foco claramente visible en todos los controles y filas.
- [ ] Enter/Espacio activan los controles previstos.
- [ ] `details`/`summary` funcionan con teclado.
- [ ] Tooltip del mapa es accesible por foco.
- [ ] Tablas se comprenden mediante encabezados y caption.
- [ ] Contraste razonable y ninguna información depende solo del color.
- [ ] Zoom al 200 % mantiene contenido y controles utilizables.
- [ ] Evaluar si el número de geometrías enfocables resulta aceptable.

### H. Visual y responsive

- [ ] Comprobar 1440, 1024, 768, 390, 360 y 320 px.
- [ ] Sin desplazamiento horizontal global.
- [ ] Mapa, leyenda, perfiles y controles no se superponen.
- [ ] Nombres largos completos.
- [ ] Advertencias y metadatos no desbordan.
- [ ] Tabla comparativa limita su desplazamiento a su contenedor.
- [ ] Fichas AFR, APC, MDE, NAC y RUE verificadas visualmente.
- [ ] `prefers-reduced-motion` evita movimientos innecesarios.

### I. Compatibilidad y cierre

- [ ] Navegadores de escritorio basados en Chromium y Firefox.
- [ ] Navegador móvil disponible.
- [ ] URL histórica y canónica documentadas.
- [ ] Commit desplegado identificado.
- [ ] No se modificaron datos, API, MySQL, SQL ni metodología.
- [ ] Incidencias clasificadas como bloqueantes o no bloqueantes.

## 13. Criterio propuesto de decisión

### GO para cerrar 7E.2

Se emitirá GO únicamente si:

- todas las rutas y recursos críticos responden;
- existen nueve áreas en mapa, perfil, tabla y fichas;
- las interacciones principales funcionan con puntero y teclado;
- no hay errores JavaScript bloqueantes ni 404;
- no aparecen valores inventados ni se pierde el tratamiento de `POB_URB` o `ECO_PC/MDE`;
- mapa, tabla y fichas son utilizables a 360/390 px y con zoom al 200 %;
- descarga SVG, navegación y respaldo funcionan;
- los problemas restantes son exclusivamente editoriales o menores y quedan documentados.

### NO-GO

Se emitirá NO-GO si se detecta cualquiera de estos casos:

- una vista principal o ficha relevante no carga;
- falta una macroárea o se cruzan sus datos;
- un control esencial, navegación o descarga no funciona;
- se muestran `null`, `undefined`, `NaN` o ceros usados como ausencia;
- la limitación de `ECO_PC/MDE` deja de ser visible o `POB_URB` se presenta como dato disponible;
- el teclado no permite realizar acciones esenciales o el foco no puede localizarse;
- la versión móvil es inutilizable o existe desplazamiento horizontal global grave;
- la API o el respaldo dejan el contenido sin una salida comprensible.

## 14. Resultado de 7E.1

**INVENTARIO COMPLETADO — APTO PARA INICIAR 7E.2.**

La comprobación HTTP de solo lectura confirma disponibilidad de las rutas y recursos inventariados. La validación funcional y visual completa corresponde a 7E.2. No se modificaron archivos funcionales, API, PHP, MySQL, SQL, JSON, metodología ni la web pública.

## 7E.2 — Revisión funcional completa

Fecha de revisión: 30 de julio de 2026  
Versión revisada: `https://support.jumalenin.com/projects/mapa-mundi/`

### Alcance y método

Se realizaron peticiones HTTP de solo lectura sobre la aplicación, sus nueve fichas, sus recursos y la API pública. Se contrastaron las respuestas con el HTML, CSS y JavaScript desplegados y con los archivos locales versionados. La API general devolvió `ok: true`, edición `RG2025_V1`, 243 registros y nueve áreas.

El entorno no dispone de navegador controlable. Las afirmaciones sobre estructura, enlaces, condiciones, timeout, respaldo y teclado proceden de evidencia HTTP o inspección del código desplegado. Las comprobaciones que requieren percepción visual o interacción real se registran como observaciones y no como verificadas.

La lista recibida para 7E.2 contenía los códigos alternativos `IND`, `MEA`, `NAM` y `RUS`. El contrato vigente y la aplicación usan exclusivamente `SAI`, `MDE`, `NAC` y `RUE`. Se verificaron las nueve rutas canónicas y se documentó la discrepancia sin cambiar la regionalización.

### Evidencia de red y datos

- Página principal: HTTP 200, 7337 bytes, 0,196 s en la medición.
- `mapa.js`: HTTP 200, 25 170 bytes, 0,202 s.
- `world.geojson`: HTTP 200, 4 276 117 bytes, 0,540 s.
- API general: HTTP 200, JSON, 243 563 bytes, 0,317 s.
- Las nueve fichas canónicas y todos los recursos de ejecución devolvieron HTTP 200.
- `TERR_DENS`, `POB_EDAD`, `HUM_EV`, `ECO_PC` y `HUM_IDH`: nueve registros, nueve áreas únicas y cero valores nulos en cada serie.
- `ECO_PC/MDE`: valor `13124.895709`, año 2024, fuente `WB_WDI`, cobertura `82.6387`, estado `LIMITACION` y observaciones presentes.
- No se observaron bucles de solicitudes ni peticiones HTTP fallidas en las comprobaciones directas.

### Tabla de pruebas

| ID | Vista o componente | Prueba | Resultado | Severidad | Evidencia | Acción propuesta |
|---|---|---|---|---|---|---|
| PUB-01 | Entrada histórica | Disponibilidad | Correcto | — | HTTP 200 | Mantener |
| PUB-02 | Aplicación | Página y recursos críticos | Correcto | — | HTML, CSS, JS y JSON/GeoJSON responden 200 | Mantener |
| PUB-03 | API | Endpoint general | Correcto | — | HTTP 200, JSON y `ok: true` | Mantener |
| PUB-04 | Página principal | Estructura de mapa, perfil y tabla | Correcto | — | Bloques e identificadores presentes en HTML/JS | Mantener |
| PUB-05 | Página principal | Ausencia visual de duplicados | Observación | No bloqueante | Requiere navegador; no hay duplicación estructural detectada | Confirmar visualmente |
| PUB-06 | Página principal | Ausencia de scroll horizontal global | Observación | No bloqueante | CSS limita las tablas, pero requiere medición visual | Confirmar a 360–390 px |
| NAV-01 | Ficha AFR | Ruta y datos territoriales | Correcto | — | HTTP 200 y clave única en áreas/territorios/respaldo | Mantener |
| NAV-02 | Ficha APC | Ruta y datos territoriales | Correcto | — | HTTP 200 y clave única | Mantener |
| NAV-03 | Ficha CHN | Ruta y datos territoriales | Correcto | — | HTTP 200 y clave única | Mantener |
| NAV-04 | Ficha EUR | Ruta y datos territoriales | Correcto | — | HTTP 200 y clave única | Mantener |
| NAV-05 | Ficha MDE | Ruta y datos territoriales | Correcto | — | HTTP 200 y clave única | Mantener |
| NAV-06 | Ficha NAC | Ruta y datos territoriales | Correcto | — | HTTP 200 y clave única | Mantener |
| NAV-07 | Ficha RUE | Ruta y datos territoriales | Correcto | — | HTTP 200 y clave única | Mantener |
| NAV-08 | Ficha SAI | Ruta y datos territoriales | Correcto | — | HTTP 200 y clave única | Mantener |
| NAV-09 | Ficha SAM | Ruta y datos territoriales | Correcto | — | HTTP 200 y clave única | Mantener |
| NAV-10 | Especificación 7E.2 | Códigos `IND`, `MEA`, `NAM`, `RUS` | Observación | No bloqueante | No son códigos válidos; la aplicación los rechaza | Usar `SAI`, `MDE`, `NAC`, `RUE` |
| PRO-01 | Perfil | `TERR_DENS` | Correcto | — | 9 filas, 9 áreas, 0 nulos | Mantener |
| PRO-02 | Perfil | `POB_EDAD` | Correcto | — | 9 filas, 9 áreas, 0 nulos | Mantener |
| PRO-03 | Perfil | `HUM_EV` | Correcto | — | 9 filas, 9 áreas, 0 nulos | Mantener |
| PRO-04 | Perfil | `ECO_PC` | Correcto | — | 9 filas, 9 áreas, 0 nulos | Mantener limitaciones |
| PRO-05 | Perfil | `HUM_IDH` | Correcto | — | 9 filas, 9 áreas, 0 nulos | Mantener |
| PRO-06 | Perfil | `POB_URB` pendiente | Correcto | — | Texto literal en página y ficha | Mantener |
| PRO-07 | Perfil | Fuente, año, cobertura y observaciones | Correcto | — | Campos conservados y `details/summary` nativos | Mantener |
| PRO-08 | Perfil | Ausencias y valores inventados | Correcto | — | Validación de nulos y `Number.isFinite`; texto explícito | Mantener |
| MDE-01 | API | Registro `ECO_PC/MDE` | Correcto | — | Estado `LIMITACION`, cobertura 82,6387 % | Mantener |
| MDE-02 | Página y ficha | Advertencia asociada a `ECO_PC` | Correcto | — | Condición desplegada por estado `LIMITACION` | Mantener |
| MDE-03 | Ficha MDE | Permanencia visual en móvil | Observación | No bloqueante | CSS permite salto; requiere navegador | Confirmar a 360–390 px |
| MDE-04 | Otras áreas | Advertencia no indebida | Correcto | — | Condición estricta por `estado === LIMITACION` | Mantener |
| API-01 | API | Carga normal | Correcto | — | Endpoint general y filtros responden 200 | Mantener |
| API-02 | Comparación | Timeout | Correcto | — | `AbortController`, 5000 ms | Mantener |
| API-03 | Perfil principal | Timeout de la petición general | Defecto menor | Menor | `renderPopulationProfile()` no usa `AbortController` | Añadir timeout de 5 s en 7E.3 |
| API-04 | Comparación | Respaldo por celda | Correcto | — | Cinco series locales, nueve áreas; no transforma ausencia en cero | Mantener |
| API-05 | Fichas | Alcance del respaldo | Observación | No bloqueante | Respaldo contiene solo cinco indicadores principales; perfil queda explícitamente no disponible | Documentar límite |
| API-06 | Perfil y fichas | Presentación de ausencia | Correcto | — | «Dato no disponible» | Mantener |
| API-07 | Respaldo | Distinción para el usuario | Correcto | — | Avisos visibles de RG2025_V1 | Mantener |
| API-08 | Resiliencia | Caída simulada | Observación | No bloqueante | No se alteró el servidor; comportamiento deducido del código | Ejecutar prueba controlada en 7E.3/7E.4 |
| API-09 | Perfil principal | Respaldo propio | Observación | No bloqueante | No hay datos complementarios en el JSON local; el fallo muestra un error explícito | Mantener mensaje o decidir alcance |
| RED-01 | Entrada histórica | JavaScript activo | Correcto | — | `window.location.replace("./mapa-mundi/")` | Mantener |
| RED-02 | Entrada histórica | Sin JavaScript | Correcto | — | `meta refresh` y enlace visible | Mantener |
| RED-03 | Entrada histórica | Tipo de redirección | Observación | No bloqueante | Respuesta 200, no HTTP 3xx | Aceptar o migrar posteriormente |
| KEY-01 | Aplicación | Tab y Shift+Tab reales | Observación | No bloqueante | No hay navegador controlable | Validar manualmente |
| KEY-02 | Controles nativos | Enter y Espacio | Correcto | — | Botones, enlaces, selectores y `summary`; filas gestionan ambas teclas | Mantener |
| KEY-03 | Aplicación y fichas | Regla general de foco | Correcto | — | Contorno sólido de 3 px | Mantener |
| KEY-04 | Tabla comparativa | Foco de filas | Defecto menor | Menor | La regla específica establece `outline: 0` y solo cambia ligeramente el fondo | Añadir foco inequívoco en 7E.3 |
| KEY-05 | Mapa | Cantidad de paradas de Tab | Defecto menor | Menor | 258 geometrías con `tabindex="0"` | Aplicar patrón de foco reducido en 7E.3 |
| KEY-06 | Aplicación | Ausencia real de trampas | Observación | No bloqueante | No hay manejadores que capturen Tab; falta recorrido real | Confirmar manualmente |
| RESP-01 | CSS | Puntos de ruptura | Correcto | — | 1000/680/390 px y 760 px en fichas | Mantener |
| RESP-02 | Móvil | 360–390 px | Observación | No bloqueante | Requiere navegador | Validar página y MDE |
| RESP-03 | Tableta | 768 px | Observación | No bloqueante | Requiere navegador | Validar mapa, tarjetas y ficha |
| RESP-04 | Escritorio | Más de 1200 px | Observación | No bloqueante | Requiere navegador | Validar composición completa |

### Resumen cuantitativo

- Pruebas registradas: **50**.
- Resultados correctos: **34**.
- Defectos bloqueantes: **0**.
- Defectos menores: **3**.
- Observaciones no bloqueantes: **13**.

### Incidencias reproducibles

#### 7E2-01 — El perfil principal no tiene timeout

- Vinculación: `API-03`.
- Archivo implicado: `projects/mapa-mundi/mapa.js`.
- Evidencia: la comparación y las fichas usan `AbortController` y 5000 ms, pero la petición general de `renderPopulationProfile()` no.
- Efecto: una conexión que permanece abierta puede mantener indefinidamente el estado de carga del perfil.
- Corrección propuesta: timeout de cinco segundos y conservación del mensaje de error existente.

#### 7E2-02 — Foco insuficiente en filas comparativas

- Vinculación: `KEY-04`.
- Archivo implicado: `projects/mapa-mundi/mapa.css`.
- Evidencia: `.comparison-table tbody tr:focus-visible` aplica `outline: 0`.
- Efecto: el cambio de fondo es discreto y puede no permitir localizar inequívocamente la fila enfocada.
- Corrección propuesta: contorno o sombra interior de alto contraste sin alterar la selección por macroárea.

#### 7E2-03 — Recorrido excesivo por el mapa

- Vinculación: `KEY-05`.
- Archivo implicado: `projects/mapa-mundi/mapa.js`.
- Evidencia: las 258 geometrías reciben `tabindex="0"`.
- Efecto: para llegar desde el mapa al perfil y a la tabla mediante Tab es necesario atravesar hasta 258 paradas.
- Corrección propuesta: patrón de foco reducido o navegación interna del mapa que conserve acceso a la información sin añadir todas las geometrías al orden de tabulación general.

### Consola y red

No se detectaron 404 ni respuestas API fallidas en las peticiones directas. Los tiempos observados fueron inferiores a un segundo por recurso en esta medición. `world.geojson` es el recurso más pesado, con aproximadamente 4,28 MB.

No se observaron bucles de solicitudes en el código: la página principal realiza cinco consultas filtradas para la comparación y una consulta general para el perfil; cada ficha realiza una consulta por área. No fue posible inspeccionar una consola de navegador real ni promesas rechazadas durante renderizado, por lo que esa comprobación permanece pendiente.

### Timeout y respaldo

- Comparación: timeout de cinco segundos; respaldo completo para sus cinco indicadores; recuperación por celda; aviso visible si se usa cualquier respaldo.
- Ficha: timeout de cinco segundos; si falla la API, usa los cinco indicadores principales del JSON local y muestra aviso. Los cinco indicadores complementarios no están en ese respaldo y se presentan como «Dato no disponible».
- Perfil principal: consulta general sin timeout y sin respaldo complementario. Un fallo produce un mensaje visible y no inventa valores.
- El usuario distingue API normal, respaldo y ausencia mediante el aviso de respaldo y los textos explícitos.

### Foco y tabulación

Los controles HTML nativos y los enlaces a fichas tienen una base correcta. El foco global es visible, pero la regla particular de las filas comparativas anula el contorno y no ofrece una señal suficientemente inequívoca. Se considera defecto menor.

Las 258 geometrías tabulables hacen que la navegación secuencial por la página sea materialmente pesada. El mapa sigue siendo accesible por teclado, pero el coste de atravesarlo dificulta llegar a los bloques posteriores. Se considera defecto menor corregible sin modificar datos ni la API.

### Decisión final de 7E.2

**GO a 7E.3.**

No existen defectos bloqueantes ni se requiere modificar MySQL, datos o contrato de API. Las tres incidencias identificadas pueden corregirse de forma limitada en `mapa.js` y `mapa.css`. Las validaciones visuales y de consola pendientes deberán repetirse después de esas correcciones antes del cierre final.

## 7E.3 — Correcciones funcionales y visuales limitadas

Fecha: 30 de julio de 2026

### Alcance

Se corrigieron exclusivamente las incidencias `7E2-01`, `7E2-02` y `7E2-03`. No se modificaron fichas, indicadores, datos, API, MySQL, SQL, regionalización, redirección histórica ni metodología.

### Tabla de correcciones

| ID | Incidencia | Archivo | Corrección | Prueba | Resultado |
|---|---|---|---|---|---|
| 7E3-01 | Perfil principal sin timeout | `projects/mapa-mundi/mapa.js` | `AbortController`, señal en `fetch`, cancelación a 5000 ms, `clearTimeout` y mensajes diferenciados | Simulación de timeout, carga normal, respuesta parcial e inválida | Correcto |
| 7E3-02 | Foco insuficiente en filas | `projects/mapa-mundi/mapa.css` | Contorno interior de 3 px mediante `:focus-visible`, sin alterar dimensiones | Revisión de selector, contraste y ausencia de cambio de caja | Correcto |
| 7E3-03 | 258 geometrías tabulables | `projects/mapa-mundi/mapa.js`, `projects/mapa-mundi/index.html` | Foco itinerante entre nueve representantes de área; una entrada por Tab; flechas, Inicio/Fin, Enter y Espacio | Pruebas aisladas del manejador y conteo de áreas en GeoJSON | Correcto |

### 7E3-01 — Timeout del perfil principal

#### Causa

`renderPopulationProfile()` utilizaba `fetch()` sin señal de cancelación, aunque la comparación y las fichas ya compartían un límite de cinco segundos.

#### Solución

- Se reutiliza `API_TIMEOUT_MS = 5000`.
- La petición general recibe `signal` de un `AbortController`.
- El temporizador cancela realmente la petición.
- `clearTimeout()` se ejecuta en `finally`, tanto en éxito como en error.
- Un timeout muestra: «La carga del perfil medio ha superado el tiempo de espera de 5 segundos.»
- Un fallo de red o respuesta inválida conserva el mensaje general.
- Se valida `ok`, edición `RG2025_V1`, contenedor `data` y ausencia de registros duplicados.
- Una respuesta parcial conserva las nueve tarjetas, muestra «Dato no disponible» en las celdas ausentes y anuncia que el perfil está incompleto.
- No se activa un respaldo inexistente para los indicadores complementarios ni se presentan los cinco datos principales como sustitutos.

#### Pruebas

- Timeout simulado: la señal fue abortada, el estado cambió a `role="alert"` y apareció el mensaje específico.
- Carga normal: se renderizaron nueve áreas y el temporizador quedó cancelado después del éxito.
- Respuesta parcial: se mantuvo el estado visible con el mensaje de perfil incompleto.
- Respuesta inválida: no se renderizó como correcta y apareció el error general.
- Sintaxis JavaScript válida.

#### Resultado y riesgo residual

Resultado correcto. El riesgo residual se limita a la comprobación visual del mensaje y a una prueba real con red lenta en navegador durante 7E.4.

### 7E3-02 — Foco visible en filas comparativas

#### Causa

La regla específica de las filas establecía `outline: 0` y dejaba como única señal un cambio de fondo tenue.

#### Solución

Se aplica a `tr:focus-visible` un contorno sólido de 3 px en `var(--focus)` con `outline-offset: -3px`. El indicador queda dentro de la fila, no desplaza contenido y no aparece por una interacción ordinaria de puntero en navegadores compatibles con `:focus-visible`.

#### Pruebas

- El selector solo afecta al estado `:focus-visible`.
- El contorno no altera el modelo de caja.
- La selección cromática de área y el fondo de fila se conservan.
- Las fichas no contienen este componente y no requirieron cambios.

#### Resultado y riesgo residual

Resultado técnico correcto. Queda pendiente confirmar visualmente el contraste en la tabla desplegada.

### 7E3-03 — Navegación agrupada del mapa

#### Causa

Cada una de las 258 geometrías recibía `tabindex="0"`, por lo que Tab obligaba a atravesar todo el mapa antes de alcanzar el perfil y la tabla.

#### Solución

- Todas las geometrías se crean inicialmente con `tabindex="-1"` y conservan `role="img"`, nombre accesible y eventos de puntero.
- Se elige una geometría representativa por cada código canónico.
- Las nueve representantes se ordenan como `AFR`, `APC`, `CHN`, `EUR`, `MDE`, `NAC`, `RUE`, `SAI` y `SAM`.
- Solo la representante activa tiene `tabindex="0"`; las otras ocho usan `-1`.
- Flecha derecha/abajo avanza y flecha izquierda/arriba retrocede con recorrido circular.
- Inicio y Fin llevan a la primera y última área.
- Enter y Espacio ejecutan la misma selección que puntero/táctil.
- Al cambiar de área se actualizan los `tabindex` y se mueve el foco.
- Las representantes usan `role="button"`, nombre «Seleccionar [área] en el mapa» y `aria-keyshortcuts`.
- El SVG contenedor usa `role="group"` y la descripción de rol «mapa interactivo», de modo que los botones internos no queden absorbidos por un contenedor con rol de imagen.
- La descripción del SVG documenta las teclas disponibles.
- Las geometrías auxiliares siguen presentes para tecnologías de asistencia y continúan funcionando con ratón y pulsación.

#### Pruebas

- El GeoJSON contiene geometrías para las nueve áreas; se obtuvieron nueve representantes.
- Antes: 258 paradas de Tab. Después: una parada de Tab para entrar en el mapa y nueve destinos internos mediante flechas.
- Flecha derecha movió `tabindex="0"` y el foco a la siguiente área.
- Flecha izquierda desde la primera envolvió hasta la novena.
- Inicio y Fin enfocaron los extremos.
- Enter y Espacio impidieron el desplazamiento de página y activaron la selección.
- Los eventos `pointerenter`, `pointerup`, `pointerleave`, `focus` y `blur` permanecen.

#### Resultado y riesgo residual

Resultado técnico correcto. La interacción real con Tab/Shift+Tab, lector de pantalla, ratón y dispositivo táctil debe confirmarse en 7E.4.

### Regresión funcional

- Los cinco indicadores y sus funciones de formato no se modificaron.
- `POB_URB` continúa como «Pendiente de incorporación».
- La condición y el texto de `ECO_PC/MDE` no se modificaron.
- Los enlaces, `<details>`, tabla, descarga SVG, fichas y reglas responsive no se alteraron.
- Las nueve áreas siguen presentes en el maestro, GeoJSON y navegación.
- `git diff --check` no detectó errores.
- No se realizaron peticiones de escritura, commit ni publicación.

### Archivos modificados en 7E.3

- `projects/mapa-mundi/index.html`
- `projects/mapa-mundi/mapa.js`
- `projects/mapa-mundi/mapa.css`
- `projects/reticula-global/FASE-7E-REVISION-FUNCIONAL-Y-CIERRE-VISUAL-2026-07-30.md`

### Decisión final de 7E.3

**GO a 7E.4.**

Las tres incidencias están corregidas mediante cambios limitados y las pruebas técnicas disponibles son correctas. No se detectaron regresiones en la inspección de código. La validación visual, táctil y con navegador real corresponde a 7E.4.

## 7E.4 — Validación visual final y comprobación de regresiones

### Incidencia registrada antes de corrección

**7E4-01 — Foco del mapa dependiente del cambio de brillo.**

- Pasos de reproducción: entrar en el mapa mediante Tab y recorrer las áreas con flechas.
- Evidencia técnica: `.country:hover, .country:focus` aplica `filter: brightness(.82)` y `outline: none`.
- Impacto: el foco puede resultar ambiguo en geometrías pequeñas o fragmentadas y depende esencialmente de un cambio cromático.
- Archivo probablemente implicado: `projects/mapa-mundi/mapa.css`.
- Severidad: defecto menor.
- Corrección mínima propuesta: añadir a `:focus-visible` un trazo oscuro y sombra clara de contraste, manteniendo el brillo y sin alterar dimensiones.

### Entornos disponibles

- **Versión pública:** accesible por HTTP, pero todavía contiene la versión anterior a 7E.3. La inspección del JavaScript público no encontró `handleMapKeydown` ni el timeout dentro de `renderPopulationProfile()`.
- **Versión local:** `http://127.0.0.1:8088/projects/mapa-mundi/`, con los cambios de 7E.3 y la corrección mínima 7E4-01. Todos los recursos estáticos devolvieron HTTP 200.
- **Navegador controlable:** no disponible en el entorno. No se generaron evidencias visuales ni se atribuyen como realizadas pruebas perceptivas de foco, responsive, consola o zoom.
- El servidor estático local no ejecuta PHP; por tanto, la carga dinámica normal desde `/api/reticula/v1/datos.php` no es representativa en local. Los estados de timeout, respuesta parcial e inválida se comprobaron mediante pruebas aisladas del código real.

### Corrección mínima 7E4-01

Se añadió a las geometrías con `:focus-visible`:

- trazo oscuro de 2,4 px;
- dos sombras de contraste, clara y oscura;
- conservación del oscurecimiento ya existente;
- anulación específica de `no-borders` mientras la geometría tiene foco.

El estilo no altera dimensiones ni cambia el aspecto ordinario de ratón. El foco y la selección permanecen diferenciados: el foco usa trazo reforzado y sombras; la selección mantiene el trazo de área activa.

### Registro de resultados

| ID | Vista o prueba | Ancho/dispositivo | Resultado | Incidencia | Evidencia |
|---|---|---|---|---|---|
| 7E4-01 | Página principal pública | HTTP | Correcto | — | Respuesta 200 |
| 7E4-02 | Página principal local | HTTP | Correcto | — | HTML, CSS, JS y JSON/GeoJSON responden 200 |
| 7E4-03 | Despliegue de 7E.3 | Público/local | Observación | Cambios todavía no publicados | Comparación del JavaScript público y local |
| 7E4-04 | Jerarquía y composición visual | Escritorio | Observación | Sin navegador controlable | Estructura sin cambios; validación perceptiva pendiente |
| 7E4-05 | Foco de filas comparativas | CSS | Correcto | — | Contorno interior de 3 px; no altera caja |
| 7E4-06 | Percepción real del foco de filas | Escritorio/móvil | Observación | Sin navegador controlable | Pendiente de recorrido visual |
| 7E4-07 | Entrada al mapa mediante Tab | Modelo DOM | Correcto | — | Solo una representante conserva `tabindex="0"` |
| 7E4-08 | Salida con Tab/Shift+Tab | Modelo DOM | Correcto | — | Las otras 257 geometrías usan `tabindex="-1"` |
| 7E4-09 | Flechas y recorrido circular | Prueba aislada | Correcto | — | Derecha avanza; izquierda desde AFR llega a SAM |
| 7E4-10 | Inicio y Fin | Prueba aislada | Correcto | — | Enfoque de primera y última área |
| 7E4-11 | Enter y Espacio | Prueba aislada | Correcto | — | Ambos activan selección y previenen desplazamiento |
| 7E4-12 | Nueve áreas accesibles | GeoJSON/código | Correcto | — | Nueve representantes en orden canónico |
| 7E4-13 | Foco visual de mapa | CSS | Correcto | 7E4-01 corregida | Trazo oscuro y doble sombra en `:focus-visible` |
| 7E4-14 | Percepción del foco en áreas pequeñas | Escritorio/móvil | Observación | Sin navegador controlable | Validación visual pendiente |
| 7E4-15 | Ratón y táctil | Código | Correcto | — | Eventos `pointerenter` y `pointerup` conservados |
| 7E4-16 | Timeout | Prueba aislada | Correcto | — | Abort efectivo y mensaje público específico |
| 7E4-17 | Carga normal | Prueba aislada | Correcto | — | Nueve áreas renderizadas y temporizador limpiado |
| 7E4-18 | Respuesta parcial | Prueba aislada | Correcto | — | Mensaje visible y ausencias explícitas |
| 7E4-19 | Respuesta inválida | Prueba aislada | Correcto | — | `role="alert"` y error general controlado |
| 7E4-20 | Respaldo complementario | Código | Observación | No existe respaldo para estos cinco indicadores | No se sustituye por datos ajenos ni ceros |
| 7E4-21 | `POB_URB` | Código público/local | Correcto | — | «Pendiente de incorporación» conservado |
| 7E4-22 | `ECO_PC/MDE` | Público y código local | Correcto | — | Valor, condición `LIMITACION` y advertencia conservados |
| 7E4-23 | Nueve fichas | HTTP/datos | Correcto | — | Nueve rutas 200 y claves territoriales únicas |
| 7E4-24 | Revisión visual de nueve fichas | Móvil/escritorio | Observación | Sin navegador controlable | Pendiente |
| 7E4-25 | Responsive 360/390/768/1280–1440 | CSS | Correcto | — | Puntos de ruptura y reglas sin regresión |
| 7E4-26 | Responsive perceptivo y zoom 200 % | Navegador | Observación | Sin navegador controlable | Pendiente |
| 7E4-27 | Consola del navegador | Navegador | Observación | Sin navegador controlable | Pendiente |
| 7E4-28 | Red y recursos | Público/local | Correcto | — | Sin 404 en las comprobaciones HTTP |
| 7E4-29 | `git diff --check` | Local | Correcto | — | Sin errores |

### Número real de paradas y foco

- Geometrías totales: **258**.
- Elementos del mapa con `tabindex="0"`: **1**.
- Elementos del mapa con `tabindex="-1"`: **257**.
- Destinos internos accesibles mediante flechas: **9**, uno por macroárea.
- Foco efectivo simultáneo: **1**.
- Área inicial: `AFR`; flechas recorren el orden canónico y actualizan el único `tabindex="0"`.

### Timeout, respuesta parcial y respaldo

- Timeout: cancelación real mediante `AbortController` a los cinco segundos; mensaje no técnico y promesa gestionada.
- Respuesta parcial: se conservan nueve tarjetas, se señalan ausencias y aparece un aviso de perfil incompleto.
- Respuesta inválida o fallo de red: error visible mediante `role="alert"`.
- Respaldo: no existe una serie local de los cinco indicadores complementarios. La aplicación no presenta como completo el respaldo de indicadores principales ni inventa valores.

### Consola, red y regresiones

No se detectaron 404 en las comprobaciones HTTP locales ni públicas. La sintaxis JavaScript es válida y las pruebas aisladas no produjeron rechazos sin tratar. No fue posible abrir la consola de un navegador real.

No se detectaron regresiones técnicas en enlaces, cinco indicadores, `POB_URB`, `ECO_PC/MDE`, `<details>`, descarga SVG, reglas responsive, eventos de puntero o nueve fichas. La corrección 7E4-01 afectó únicamente a `mapa.css`.

### Evidencias

1. Respuestas HTTP 200 de la página y recursos locales.
2. Respuestas HTTP 200 de la página, API y fichas públicas.
3. Resultado de la simulación de timeout: señal abortada y mensaje específico.
4. Resultado de carga normal: nueve áreas y temporizador cancelado.
5. Resultado parcial e inválido: mensajes controlados.
6. Pruebas de flechas, recorrido circular, Inicio, Fin, Enter y Espacio.
7. Conteo de 258 geometrías, nueve representantes y una entrada de Tab.
8. Selectores CSS de foco de fila y mapa.
9. `git diff --check` sin errores.
10. Registro explícito de indisponibilidad del navegador controlable.

No se generaron capturas porque no existe un navegador controlable en este entorno.

### Archivos funcionales modificados durante 7E.4

- `projects/mapa-mundi/mapa.css` — corrección mínima 7E4-01.

No se modificaron en esta ronda `index.html`, `mapa.js`, `area.html`, `area.js` ni `area.css`. Los cambios pendientes en `index.html` y `mapa.js` pertenecen a 7E.3.

### Decisión final de 7E.4

**GO condicionado.**

La corrección mínima está aplicada y las comprobaciones técnicas son correctas. El paso a 7E.5 queda condicionado a una validación visual externa de:

- foco de una fila comparativa;
- foco y recorrido del mapa;
- página principal a 360/390, 768 y 1280–1440 px;
- una ficha normal y MDE;
- zoom al 200 %;
- consola sin errores durante interacción real.

No se realizó commit ni publicación. API, PHP, MySQL, SQL, JSON y datos permanecen sin cambios.

## Soporte de validación local

Para permitir la comprobación local sin modificar la API, `mapa.js` y `area.js` seleccionan el endpoint según el hostname:

- `127.0.0.1` o `localhost`: `/__reticula_api__/datos.php`;
- cualquier otro hostname, incluida producción: `/api/reticula/v1/datos.php`.

La API pública no devuelve `Access-Control-Allow-Origin`, por lo que un `fetch` directo desde localhost sería bloqueado por el navegador. El script interno `projects/reticula-global/servidor_validacion_local.py` resuelve `/__reticula_api__/datos.php` mediante un proxy GET de solo lectura hacia:

`https://support.jumalenin.com/api/reticula/v1/datos.php`

Procedimiento:

```powershell
python projects\reticula-global\servidor_validacion_local.py
```

URL:

`http://127.0.0.1:8088/projects/mapa-mundi/`

La selección y el proxy afectan únicamente a localhost. La ruta y el comportamiento públicos permanecen sin cambios. No se modificaron la API, PHP, MySQL, SQL, JSON, datos, indicadores ni metodología.
