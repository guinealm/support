# 1. Identificación de la aplicación

Aplicación analizada: **Mapa simbólico mundial / Retícula Global 2025**.

La aplicación vive en la carpeta histórica **projects/Mapa simbólico Mundial/** y su versión validada en esta fase es **Mapa simbolico v5.html**. No existe una carpeta literal `projects/reticula-global/` en este workspace; la versión equivalente encontrada es la carpeta con nombre en español y sus iteraciones v1-v5.

# 2. Ubicación y archivo de entrada

- Carpeta: `c:\jumalenin-ecosistema\sites\support\projects\Mapa simbólico Mundial`
- Archivo de entrada validado: `Mapa simbolico v5.html`
- No hay `index.html` dentro de esta carpeta.
- Las versiones anteriores `Mapa simbolico v1.html` a `Mapa simbolico v4.html` siguen presentes como iteraciones previas.

La ruta usada en la validación local fue:

- `http://127.0.0.1:8000/projects/Mapa%20simb%C3%B3lico%20Mundial/Mapa%20simbolico%20v5.html`

# 3. Inventario de archivos

Árbol simplificado de la carpeta actual:

```text
Mapa simbólico Mundial/
├── Mapa simbolico v1.html
├── Mapa simbolico v1.html.txt
├── Mapa simbolico v2.html
├── Mapa simbolico v3.html
├── Mapa simbolico v4.html
├── Mapa simbolico v5.html
├── directorio
├── error link.png
├── mapa_mundo_paises_editable.pptx
├── Introducción.docx / Introducción.pdf
├── Bloque I Norteamérica (La Fortaleza Continental).docx / .pdf
├── Bloque II Europa (La Península Atlántica y su Frontera Oriental).docx / .pdf
├── Bloque III Rusia y el Espacio Post-Soviético (Eurasia Norte).docx / .pdf
├── Bloque IV China (El Reino Medio Industrial).docx / .pdf
├── Bloque V Sur de Asia (El Núcleo Demográfico).docx / .pdf
├── Bloque VI ASEAN (La Encrucijada Marítima).docx / .pdf
├── Bloque VII Asia-Pacífico Avanzado (El Arco Tecnológico).docx / .pdf
├── Bloque VIII Medio Oriente y Turquía (El Pivote Energético).docx / .pdf
├── Bloque IX África (El Gigante Dormido).docx / .pdf
├── Bloque X Sudamérica (La Reserva Estratégica).docx / .pdf
├── Conclusión La Retícula del Nuevo Orden.docx / .pdf
└── Síntesis Comparativa La Tabla de Poder Global UTM 2025.docx / .pdf
```

Archivos claramente antiguos o de apoyo:

- `Mapa simbolico v1.html.txt` parece un borrador o exportación auxiliar.
- `directorio` funciona como listado simple de documentos.
- `error link.png` parece un recurso de prueba o depuración.
- `Mapa simbolico v1.html` a `Mapa simbolico v4.html` son iteraciones previas con estructuras distintas.

No se encontraron CSS ni JavaScript locales separados dentro de esta carpeta. El contenido funcional está embebido en el HTML.

# 4. Rutas y dependencias

Dependencias externas detectadas en `Mapa simbolico v5.html`:

- Tailwind desde `https://cdn.tailwindcss.com`
- Chart.js desde `https://cdn.jsdelivr.net/npm/chart.js`
- Google Fonts desde `https://fonts.googleapis.com/...`
- Imagen de fondo de mapa desde Wikimedia: `https://upload.wikimedia.org/...World_map_blank_without_borders...png`

Dependencias locales detectadas:

- Todos los PDFs y DOCX de los bloques están en la misma carpeta y se referencian por nombre dentro del HTML.
- No se usan rutas relativas a CSS o JS locales.

Hallazgos sobre rutas:

- No hay favicon local en la carpeta; el HTML tampoco declara uno propio.
- No hay enlaces rotos de navegación interna porque el visor no navega a otros HTML; abre un modal con contenido simulado.
- El recurso de Wikimedia dio fallo de red en la validación local (`net::ERR_BLOCKED_BY_ORB`), así que la capa de fondo es frágil.
- La aplicación no carga PDF binarios reales; el visor simula el contenido del documento.

# 5. Procedimiento de ejecución local

Se ejecutó un servidor HTTP local mínimo en la raíz de Support y se abrió la ruta del HTML desde navegador.

Procedimiento usado:

1. Levantar servidor local en `c:\jumalenin-ecosistema\sites\support`.
2. Abrir `Mapa simbolico v5.html` mediante `http://127.0.0.1:8000/...`.
3. Recargar la página para comprobar estabilidad.
4. Probar apertura y cierre del visor modal.

Resultado:

- La página cargó correctamente.
- Los gráficos se renderizaron.
- El modal respondió a la interacción.
- Se registró un fallo de red en el fondo remoto de Wikimedia.
- Apareció un aviso de Chart.js sobre uso de CDN en producción, pero no un error de ejecución.

# 6. Descripción del funcionamiento actual

## Lo que está explícito en la interfaz

- La página se presenta como un atlas geopolítico de 10 bloques.
- Cada bloque tiene un nombre regional, un código de bloque y un texto descriptivo breve.
- Hay dos gráficos comparativos: población vs poder económico y fuerza militar + tecnológica.
- Hay una tabla consolidada con área, población, fuerza militar, recursos económicos y nota estratégica.
- Un botón/tarjeta final abre la conclusión en un visor modal.

## Lo que se deduce del código

- La aplicación no abre PDFs reales; usa un modal con texto de muestra que cambia según el bloque pulsado.
- El fondo es decorativo y pretende simular una proyección satelital con una retícula.
- Los datos de cada bloque están codificados en el HTML, no vienen de JSON o CSV.
- Los colores se usan como sistema de codificación por región, pero no existe una leyenda formal.

## Finalidad aparente

La finalidad conceptual parece ser comparar grandes áreas geopolíticas como unidades simbólicas, no representar fronteras exactas. La retícula sirve como metáfora de orden global, proyección estratégica y peso relativo de cada bloque.

# 7. Evaluación de comprensión conceptual

Una persona nueva puede entender que está viendo un mapa/atlas estratégico con bloques regionales, pero no entiende todo con precisión de inmediato.

Puntos claros:

- Hay 10 bloques identificados.
- Hay una comparación de poder, población y recursos.
- Cada bloque abre una ficha explicativa.

Ambigüedades conceptuales:

- No se explica con suficiente claridad si los bloques son geográficos, políticos, militares o una mezcla simbólica de los tres.
- No existe una leyenda que traduzca colores, tamaños o jerarquías.
- La relación entre el mapa de fondo, la retícula y la tabla de datos no queda totalmente explicitada.
- El título “Mapa simbólico mundial” describe la intención general, pero no deja claro que la pieza es un atlas estratégico de bloques con datos comparativos y visor simulado.

# 8. Pruebas de controles e interacciones

Controles disponibles en la versión validada:

- Bloques del mapa principal.
- Filas clicables de la tabla.
- Tarjeta final de conclusión.
- Botón de cierre del modal.
- Cierre del modal al hacer clic fuera del contenido.

Resultados de prueba:

- Al pulsar un bloque, se abre el modal con el nombre del documento correspondiente.
- La fila equivalente de la tabla hace lo mismo.
- El botón de cierre funciona correctamente.
- El cierre por clic fuera del modal funciona correctamente.
- No se detectó estado incoherente tras abrir y cerrar varias veces.

Observaciones:

- No hay filtros, selectores, zoom ni controles de teclado específicos.
- No hay tooltips interactivos ni arrastre en esta versión.
- El comportamiento de los bloques depende del clic, no de navegación real a PDF.

# 9. Pruebas de escritorio y móvil

Resultados medidos en navegador local:

| Tamaño | Resultado general |
|---|---|
| 1440 × 900 | Correcto, sin overflow horizontal visible. |
| 1366 × 768 | Correcto, sin overflow horizontal visible. |
| 768 × 1024 | Correcto, pero la tabla ocupa mucho ancho y requiere scroll interno. |
| 360 × 800 | Funciona, pero la tabla excede el ancho y depende del contenedor desplazable. |
| 800 × 360 | Funciona, con pantalla apretada y bastante contenido vertical. |

Hallazgos visuales en responsive:

- No apareció desbordamiento horizontal del documento completo.
- La tabla es más ancha que la pantalla en tablet y móvil, aunque está protegida por el contenedor de scroll horizontal.
- El mapa conserva su estructura, pero queda comprimido en pantalla pequeña.
- La página es usable en móvil, pero la lectura exige mucho desplazamiento vertical.

# 10. Problemas funcionales

- El fondo de mapa remoto desde Wikimedia falló en la validación local, así que la capa visual principal depende de una red externa frágil.
- La aplicación no carga ni muestra PDFs reales; el visor es solo una simulación textual.
- La app depende de Tailwind, Chart.js y Google Fonts desde CDN; si cualquiera falla, la experiencia se degrada de forma notable.
- No existe una entrada `index.html` en la carpeta del proyecto, así que el arranque depende de conocer el nombre exacto del HTML.

# 11. Problemas conceptuales

- La pieza mezcla representación geográfica, simbólica y estratégica sin una explicación inicial suficiente.
- No hay leyenda formal para colores, tamaños y jerarquías.
- No queda claro si el fondo representa una geografía real o solo una alusión visual.
- El título general es correcto a nivel poético, pero no define bien el alcance funcional de la aplicación.

# 12. Problemas visuales

- La cabecera, el mapa, los gráficos y la tabla compiten por atención en una sola página larga.
- En móvil el contenido se siente denso y con poco aire entre bloques.
- La tabla requiere atención adicional para leerse en pantallas pequeñas.
- El fondo oscuro y la retícula ayudan al tono, pero el fondo real del mapa no llegó a cargarse en la validación local.

# 13. Deuda técnica

- Toda la lógica está embebida en un único HTML grande.
- No hay separación entre datos, presentación y comportamiento.
- La codificación de bloques, métricas y textos está duplicada entre mapa, tabla y modal.
- Existen varias versiones históricas en la misma carpeta, lo que incrementa la confusión de mantenimiento.
- Hay artefactos auxiliares no usados directamente por la UI visible, como `directorio`, `Mapa simbolico v1.html.txt` y `error link.png`.
- Las dependencias externas no están controladas localmente.

# 14. Lista priorizada de mejoras

| Prioridad | Tipo de problema | Consecuencia | Corrección propuesta | Riesgo |
|---|---|---|---|---|
| P1 | Funcional | El fondo principal puede no cargarse | Sustituir la imagen remota por un recurso local o incorporar un fallback fiable | Medio |
| P1 | Funcional | La app depende de CDNs para verse y analizarse bien | Aislar o empaquetar las dependencias críticas | Medio |
| P2 | Conceptual | El usuario no sabe si ve geografía real o símbolo | Añadir una explicación inicial y una leyenda clara | Bajo |
| P2 | Funcional | El visor no abre PDFs reales | Definir si el comportamiento debe ser visor real o simulación, y unificarlo | Medio |
| P2 | Técnico | Hay varias versiones paralelas | Consolidar la versión activa y documentar las obsoletas | Bajo |
| P3 | Visual | La lectura móvil es densa | Reorganizar jerarquía y espaciado en una fase posterior | Bajo |
| P3 | Técnico | Código HTML monolítico | Separar datos, estilos y lógica cuando se pase a corrección estructural | Bajo |

# 15. Riesgos de iniciar cambios

- Si se corrige la versión equivocada, se puede dejar intacta la que realmente se publica.
- Si se cambia el fondo o las dependencias externas sin decidir primero el comportamiento deseado, la experiencia conceptual puede desalinearse.
- Si se empieza por estilo antes de fijar la semántica de los bloques, la lectura seguirá siendo ambigua.
- Si se intenta limpiar la carpeta sin definir el archivo activo, se corre el riesgo de tocar iteraciones históricas útiles como referencia.

# 16. Decisión final GO/NO-GO

## GO

Se puede iniciar la siguiente fase de correcciones funcionales porque:

- la aplicación ha podido ejecutarse en local;
- se ha identificado su estructura;
- los principales problemas están delimitados;
- no existen dudas esenciales sobre el archivo que debe modificarse, que en esta validación es `Mapa simbolico v5.html`;
- las correcciones pueden realizarse sin reorganizar todavía el proyecto.

## Entrega final

- Archivo creado: [diagnostico-funcional-reticula-global-1a.md](diagnostico-funcional-reticula-global-1a.md)
- No se ha modificado ningún archivo de la aplicación.
- Tres hallazgos más importantes:
  - el fondo remoto de Wikimedia es frágil y falló en la validación local;
  - la aplicación funciona, pero el visor es una simulación y no un PDF real;
  - existen varias versiones HTML en la misma carpeta, aunque la más completa y validada es `Mapa simbolico v5.html`.
- Decisión: **GO**