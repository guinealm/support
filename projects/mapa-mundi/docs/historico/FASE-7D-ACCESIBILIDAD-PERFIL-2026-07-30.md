# Fase 7D — Accesibilidad del perfil medio

Fecha: 30 de julio de 2026

## 1. Objetivo

Revisar y mejorar la accesibilidad, el funcionamiento y la adaptación responsive del bloque «Perfil medio de la población» en la página principal y en las fichas de macroárea, sin modificar datos, metodología, API ni MySQL.

## 2. Inventario inicial

- La página principal ya utilizaba un `h2` para el bloque, un `article` y un `h3` por macroárea, una lista de definición `dl` para indicadores y valores, enlaces independientes para el nombre y «Ver ficha», y un `details` nativo.
- La ficha ya utilizaba un `h2`, una lista de definición y un `details` nativo para el perfil.
- Los nueve códigos estaban definidos en el orden `AFR`, `APC`, `CHN`, `EUR`, `MDE`, `NAC`, `RUE`, `SAI` y `SAM`.
- Los enlaces se construían con `area.html?codigo=CODIGO`.
- Existía una regla global de foco visible y reglas responsive a 1000/680 px en la página principal y 760 px en las fichas.

## 3. Problemas encontrados

- La advertencia metodológica de `ECO_PC/MDE` estaba dentro del elemento desplegable tanto en la página principal como en la ficha; por tanto, no permanecía visible con el `details` cerrado.
- El estado de carga del perfil principal no estaba identificado expresamente como estado, mientras que el contenedor completo tenía `aria-live`, con riesgo de anunciar repetidamente todas las tarjetas.
- El error de carga no se convertía en alerta únicamente cuando ocurría un error real.
- Los resúmenes de las tarjetas repetían el mismo texto sin un nombre accesible contextualizado por macroárea.
- Las fuentes se mostraban como texto aunque la API proporcionara una URL.
- Los metadatos largos y las URLs podían desbordar tarjetas estrechas.
- Si una macroárea carecía de todos los indicadores del perfil, podía desaparecer su tarjeta en lugar de conservarse con «Dato no disponible».
- El foco visible era correcto, pero podía reforzarse para que no dependiera de un cambio mínimo de color.

## 4. Correcciones realizadas

- La advertencia «Dato con cobertura incompleta. Comparabilidad limitada.» se trasladó fuera de los desplegables y permanece visible.
- El estado de carga utiliza `role="status"` y `aria-live="polite"`; el error real cambia a `role="alert"`.
- Cada tarjeta queda asociada semánticamente a su encabezado mediante `aria-labelledby`.
- Cada `summary` del perfil principal incluye el nombre de su macroárea en el nombre accesible.
- Se conservan año, cobertura, estado y observaciones, y la fuente se convierte en enlace cuando existe `fuente_principal.url`.
- Se garantiza la creación de las nueve tarjetas a partir del maestro territorial; un indicador ausente se presenta como «Dato no disponible».
- Se reforzaron el foco, el ajuste de textos largos y el comportamiento de las parejas `dt`/`dd` en móvil.

## 5. Archivos modificados

- `projects/mapa-mundi/index.html`
- `projects/mapa-mundi/mapa.js`
- `projects/mapa-mundi/mapa.css`
- `projects/mapa-mundi/area.js`
- `projects/mapa-mundi/area.css`
- `projects/mapa-mundi/docs/historico/FASE-7D-ACCESIBILIDAD-PERFIL-2026-07-30.md`

## 6. Navegación por teclado

Los nombres enlazados, los enlaces «Ver ficha», los elementos `summary`, «Volver al mapa» y la navegación anterior/siguiente siguen siendo controles HTML nativos. El orden del DOM coincide con el orden visual y no se han añadido valores `tabindex` positivos. La apertura y cierre de `details` conserva el comportamiento nativo de teclado.

## 7. Foco visible

Los controles interactivos reciben un contorno sólido de 3 px con separación de 3 px. Los `summary` conservan el foco visible y reciben un radio mínimo para evitar que el contorno resulte confuso. No se elimina el foco mediante `outline: none`.

## 8. Semántica

La jerarquía se mantiene en un `h1` de página y encabezados `h2` para los bloques. Cada tarjeta es un `article`, tiene un `h3` propio y contiene un `dl` con parejas `dt`/`dd`. Los desplegables y enlaces son elementos nativos, no `div` o `span` simulando controles.

## 9. Contraste y legibilidad

Se mantiene la identidad cromática. La advertencia metodológica utiliza texto marrón oscuro, borde lateral y fondo claro, por lo que no depende solo del color. El foco utiliza el color de tinta general para ofrecer contraste estable, incluida la ficha cuyo color de macroárea es variable.

## 10. Comportamiento responsive

- Página principal: tres columnas en escritorio, dos por debajo de 1000 px y una por debajo de 680 px.
- A 390 px o menos, cada valor pasa debajo de su etiqueta para evitar cortes en «Pendiente de incorporación».
- Las tarjetas y sus columnas tienen `min-width: 0`; valores, observaciones y URLs admiten salto de línea.
- Fichas: el perfil conserva dos columnas en escritorio y una secuencia vertical por debajo de 760 px, sin desplazamiento horizontal propio.

## 11. Tratamiento de desplegables

Los `details` siguen siendo nativos y accesibles por teclado. El resumen es descriptivo y los metadatos admiten salto de línea. La advertencia de `ECO_PC/MDE` queda visible sin abrir el desplegable; año, fuente, cobertura, estado y observaciones permanecen dentro.

## 12. Consistencia entre página y fichas

Ambas vistas conservan los nombres Densidad, Edad mediana, Esperanza de vida, PIB por habitante, IDH y Urbanización; los mismos criterios de formato numérico; `POB_URB` como «Pendiente de incorporación»; y la misma advertencia para `ECO_PC/MDE`.

## 13. Pruebas realizadas

- Revisión estática de los nueve códigos y de la construcción `area.html?codigo=CODIGO`.
- Revisión de la jerarquía `h1`/`h2`/`h3`, `article`, `dl`, `dt`, `dd`, `details` y `summary`.
- Revisión del orden de tabulación y ausencia de `tabindex` positivos en el bloque.
- Revisión de reglas de foco y de los puntos de ruptura responsive.
- Validación de sintaxis de `mapa.js` y `area.js` mediante el analizador JavaScript.
- `git diff --check` sin errores.
- Comprobación estática de los textos para valores ausentes, `POB_URB` y `ECO_PC/MDE`.

## 14. Validaciones visuales pendientes

El navegador controlable no está disponible en este entorno. Queda pendiente la comprobación visual del usuario en:

- página principal en escritorio;
- página principal a 390/360 px;
- una ficha normal;
- ficha de Oriente Medio;
- recorrido completo con Tab y activación de los desplegables con teclado.

## 15. Resultado

**GO CON OBSERVACIONES** — Las comprobaciones técnicas disponibles son correctas. El cierre definitivo queda condicionado a la validación visual y de teclado indicada.

## Validación pública y cierre

- URL principal validada: https://support.jumalenin.com/projects/mapa-mundi/
- Ficha de Oriente Medio validada: https://support.jumalenin.com/projects/mapa-mundi/area.html?codigo=MDE
- La presentación en escritorio y el comportamiento responsive se consideran correctos, sin desbordamientos ni roturas visuales.
- El foco visible permite identificar con claridad los controles activos.
- La navegación por teclado mantiene controles nativos y un orden lógico.
- Los elementos `<details>` y `<summary>` funcionan correctamente y conservan desplegables los datos de fuente, año, cobertura, estado y observaciones.
- La advertencia «Dato con cobertura incompleta. Comparabilidad limitada.» de `ECO_PC/MDE` permanece visible con el desplegable cerrado y asociada a la fila «PIB por habitante».
- `POB_URB` continúa presentándose como «Pendiente de incorporación».
- No se modificaron API, PHP, MySQL, SQL, JSON ni metodología.

**GO — Fase 7D cerrada.**
