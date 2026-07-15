# Fase 1B.7 — Selección definitiva de gráficas y representaciones

## Retícula Global 2025

## 1. Objetivo

Definir el conjunto inicial de gráficas y representaciones visuales que utilizará Retícula Global 2025.

La selección deberá:

* responder a preguntas didácticas concretas;
* comparar las nueve áreas;
* evitar duplicar la Tabla de Datos Consolidados;
* funcionar en escritorio y móvil;
* utilizar pocos formatos;
* mantener continuidad con la visual actual;
* permitir una primera implantación suficientemente completa;
* evitar que la aplicación se convierta en un portal estadístico inabarcable.

Esta fase decide qué visualizaciones se construirán. No implica todavía programarlas ni sustituir las existentes.

---

# 2. Principio general

Una gráfica solo se incorporará cuando permita entender una relación que resulte menos clara mediante una cifra o una tabla.

Cada visualización deberá responder a esta secuencia:

1. ¿Qué pregunta plantea?
2. ¿Qué datos necesita?
3. ¿Qué conclusión principal debería obtener el lector?
4. ¿Qué tipo de gráfica la explica mejor?
5. ¿Puede entenderse en móvil?
6. ¿Tiene una alternativa textual?
7. ¿Duplica otra visualización?

## Regla de contención

La primera versión completa utilizará:

* un máximo de tres gráficas en portada;
* entre una y tres gráficas por página temática;
* entre cero y dos gráficas por ficha de área;
* una representación principal por indicador.

No se crearán varias gráficas distintas para contar esencialmente la misma idea.

---

# 3. Familias visuales aprobadas

## 3.1 Barras horizontales

Uso principal:

* comparar un indicador entre las nueve áreas;
* mostrar clasificaciones;
* facilitar lectura de nombres largos;
* permitir visualización móvil.

Aplicaciones:

* población;
* superficie;
* PIB;
* PIB por habitante;
* gasto militar;
* esperanza de vida;
* Gini;
* emisiones.

Será el tipo de gráfica más utilizado.

## 3.2 Barras agrupadas

Uso principal:

* comparar dos indicadores relacionados con unidades compatibles o porcentajes comparables.

Aplicaciones:

* porcentaje de población mundial frente a porcentaje de PIB mundial;
* población actual frente a población en 2050;
* producción energética frente a consumo;
* años medios frente a años esperados de escolarización.

## 3.3 Gráficos de dispersión

Uso principal:

* mostrar relaciones entre dos variables;
* identificar áreas que se apartan de una tendencia general.

Aplicaciones:

* PIB por habitante frente a IDH;
* PIB por habitante frente a esperanza de vida;
* población frente a PIB;
* emisiones por habitante frente a PIB por habitante.

Se limitarán a relaciones realmente comprensibles.

## 3.4 Líneas temporales

Uso principal:

* mostrar evolución;
* comparar presente y futuro.

Aplicaciones posibles:

* población;
* peso económico;
* emisiones;
* gasto militar.

No se usarán en la primera versión si solo se dispone de un año actual y una proyección.

## 3.5 Mapas temáticos

Uso principal:

* localizar visualmente las nueve áreas;
* mostrar un indicador sobre la geografía.

Aplicaciones:

* mapa general de áreas;
* población;
* PIB;
* emisiones;
* desarrollo humano.

El mapa principal no deberá convertirse en nueve mapas temáticos simultáneos.

## 3.6 Matrices cualitativas

Uso principal:

* representar dimensiones que no disponen de una cifra homogénea.

Aplicaciones:

* capacidad militar;
* autonomía energética;
* capacidad tecnológica;
* inteligencia artificial.

La matriz deberá incluir criterios y explicación.

---

# 4. Representaciones descartadas inicialmente

No se utilizarán en la primera implantación:

* gráficos tridimensionales;
* velocímetros;
* relojes;
* donuts múltiples;
* tartas con nueve segmentos pequeños;
* radares con muchas variables;
* nubes de iconos;
* mapas animados;
* diagramas Sankey complejos;
* gráficos de burbujas con demasiadas dimensiones;
* personajes proporcionales;
* puntuaciones sintéticas sin metodología;
* animaciones automáticas.

Podrán reconsiderarse si posteriormente responden a una necesidad concreta.

---

# 5. Gráficas de portada

La portada tendrá tres visualizaciones principales.

## 5.1 Gráfica P1 — Población y superficie

### Pregunta

> ¿Dónde vive la población mundial y cuánto territorio ocupa cada área?

### Datos

* porcentaje de población mundial;
* porcentaje de superficie mundial.

### Representación recomendada

Barras agrupadas horizontales.

Para cada área:

* barra de población;
* barra de superficie.

### Qué debe enseñar

* áreas con mucha población y poco territorio;
* áreas extensas pero relativamente poco pobladas;
* diferencias entre tamaño físico y peso humano.

### Ejemplos de lectura esperada

* China y el Subcontinente indio concentran mucha población.
* Rusia-Eurasia ocupa una gran superficie con menor peso demográfico.
* África combina gran extensión con una población creciente.

### Móvil

* barras horizontales;
* una fila por área;
* posibilidad de alternar población y superficie si el ancho es insuficiente.

### Texto complementario

Una frase deberá explicar que extensión y población no son equivalentes.

### Prioridad

**Obligatoria.**

---

## 5.2 Gráfica P2 — Población y peso económico

### Pregunta

> ¿Qué relación existe entre la parte de la humanidad que vive en cada área y la parte de la economía mundial que produce?

### Datos

* porcentaje de población mundial;
* porcentaje del PIB nominal mundial.

### Representación recomendada

Barras agrupadas horizontales.

### Alternativa

Gráfico de dispersión:

* eje X: porcentaje de población mundial;
* eje Y: porcentaje del PIB mundial.

La versión de barras será inicialmente más didáctica.

### Qué debe enseñar

* áreas cuyo peso económico supera su peso demográfico;
* áreas con gran población y menor participación económica;
* diferencia entre tamaño humano y poder económico.

### Móvil

Barras agrupadas, no dispersión.

### Texto complementario

Debe explicar que el PIB total no indica por sí mismo cómo vive cada persona.

### Prioridad

**Obligatoria.**

---

## 5.3 Gráfica P3 — Riqueza, desarrollo y desigualdad

### Pregunta

> ¿Una mayor riqueza por habitante se traduce siempre en mayor desarrollo y menor desigualdad?

### Datos

* PIB por habitante;
* IDH;
* Gini.

### Representación recomendada

Gráfico de dispersión:

* eje X: PIB por habitante;
* eje Y: IDH;
* Gini mostrado mediante etiqueta, símbolo auxiliar o ficha asociada.

### Restricción

Gini no se representará inicialmente mediante el tamaño de la burbuja si dificulta la interpretación.

Podrá mostrarse mediante:

* cifra junto al nombre;
* borde;
* panel al seleccionar;
* pequeña barra complementaria.

### Qué debe enseñar

* relación general entre renta y desarrollo;
* áreas con desarrollo alto respecto a su renta;
* áreas con desigualdad elevada;
* límites del PIB por habitante como medida de bienestar.

### Móvil

Dos posibilidades:

1. dispersión simplificada;
2. lista ordenada con PIB por habitante, IDH y Gini.

La alternativa móvil deberá conservar la conclusión principal.

### Prioridad

**Obligatoria.**

---

# 6. Gráficas de Territorio y población

La página temática utilizará tres visualizaciones.

## 6.1 Gráfica TP1 — Población total

### Pregunta

> ¿Cuántas personas viven en cada área?

### Tipo

Barras horizontales.

### Datos

* población total;
* porcentaje mundial.

### Prioridad

Obligatoria.

---

## 6.2 Gráfica TP2 — Superficie y densidad

### Pregunta

> ¿Cómo cambia la imagen cuando comparamos extensión y concentración de población?

### Representación

Dos barras alineadas o dos gráficos consecutivos:

* superficie;
* densidad.

No deberán colocarse en el mismo eje porque utilizan unidades distintas.

### Prioridad

Obligatoria.

---

## 6.3 Gráfica TP3 — Población actual y 2050

### Pregunta

> ¿Qué áreas ganarán o perderán peso demográfico?

### Tipo

Barras agrupadas.

### Datos

* población del año base;
* población proyectada en 2050;
* variación porcentual.

### Prioridad

Obligatoria para la dimensión futura.

---

# 7. Gráficas de Economía

## 7.1 Gráfica ECO1 — PIB total

### Pregunta

> ¿Dónde se concentra la producción económica mundial?

### Tipo

Barras horizontales.

### Datos

* PIB nominal;
* porcentaje del PIB mundial.

### Prioridad

Obligatoria.

---

## 7.2 Gráfica ECO2 — PIB por habitante

### Pregunta

> ¿Qué riqueza económica media corresponde a cada habitante?

### Tipo

Barras horizontales.

### Regla

Ordenar de mayor a menor.

Debe acompañarse de una nota:

> La media no describe cómo se reparte la riqueza.

### Prioridad

Obligatoria.

---

## 7.3 Gráfica ECO3 — Población frente a PIB

### Pregunta

> ¿Qué áreas producen más o menos de lo que sugeriría su peso demográfico?

### Tipo

Barras agrupadas con porcentajes mundiales.

### Prioridad

Obligatoria.

## Decisión

No se añadirá inicialmente una gráfica específica de PIB PPA en la portada o en la primera página económica.

El PIB PPA aparecerá:

* en tabla;
* en ficha;
* en explicación;
* y podrá recibir una visualización posterior.

---

# 8. Gráficas de Desarrollo humano, desigualdad y condiciones de vida

Esta página conjunta tendrá inicialmente tres visualizaciones.

## 8.1 Gráfica DH1 — IDH

### Pregunta

> ¿Qué nivel combinado de salud, educación e ingresos alcanza cada área?

### Tipo

Barras horizontales sobre escala 0–1.

### Texto necesario

Debe explicar qué integra el IDH y qué no mide.

### Prioridad

Obligatoria.

---

## 8.2 Gráfica DH2 — Gini

### Pregunta

> ¿En qué áreas se reparte la renta de forma más o menos desigual?

### Tipo

Barras horizontales.

### Escala

0–100.

### Etiqueta obligatoria

> Gini medio aproximado del área.

### Texto necesario

Debe advertir que:

* no es un Gini oficial del conjunto;
* se obtiene mediante ponderación;
* puede utilizar datos de años diferentes.

### Prioridad

Obligatoria.

---

## 8.3 Gráfica DH3 — PIB por habitante y esperanza de vida

### Pregunta

> ¿Cómo se relacionan la riqueza media y la duración de la vida?

### Tipo

Dispersión.

### Datos

* PIB por habitante;
* esperanza de vida.

### Qué debe enseñar

* la renta importa;
* la relación no es completamente automática;
* existen diferencias en eficacia sanitaria y social.

### Prioridad

Obligatoria.

## Información complementaria

Educación, mortalidad infantil, agua y saneamiento podrán aparecer en:

* tabla;
* tarjetas;
* fichas;
* ampliación posterior.

No será necesario crear una gráfica independiente para cada indicador en la primera versión.

---

# 9. Gráficas de Capacidad militar y estratégica

Esta página deberá combinar datos cuantitativos y una representación cualitativa.

## 9.1 Gráfica MIL1 — Gasto militar

### Pregunta

> ¿Qué parte de los recursos militares mundiales concentra cada área?

### Tipo

Barras horizontales.

### Datos

* gasto militar total;
* porcentaje mundial.

### Prioridad

Obligatoria.

---

## 9.2 Gráfica MIL2 — Esfuerzo militar

### Pregunta

> ¿Qué proporción de su economía dedica cada área a defensa?

### Tipo

Barras horizontales.

### Datos

* gasto militar como porcentaje del PIB.

### Qué debe enseñar

* gastar mucho en términos absolutos no es lo mismo que realizar un gran esfuerzo relativo.

### Prioridad

Obligatoria si la cobertura resulta suficiente.

---

## 9.3 Matriz MIL3 — Capacidades estratégicas

### Pregunta

> ¿Qué capacidades permiten a un área defenderse, sostener un conflicto o actuar fuera de su territorio?

### Tipo

Matriz cualitativa.

### Filas

Las nueve áreas.

### Columnas iniciales

1. industria militar;
2. producción y reposición;
3. misiles y fuegos de precisión;
4. drones;
5. inteligencia y vigilancia;
6. mando y comunicaciones;
7. guerra electrónica y ciberdefensa;
8. logística;
9. alianzas;
10. proyección exterior.

### Escala

* limitada;
* media;
* alta;
* muy alta.

O bien:

* 1 a 5, con criterios explícitos.

### Regla

No se mostrará una media final ni un total.

### Qué debe enseñar

* la capacidad militar es multidimensional;
* un presupuesto menor puede compensarse parcialmente con tecnología, inteligencia, apoyo exterior o adaptación;
* la capacidad para iniciar una guerra no es la misma que para mantenerla.

### Prioridad

Obligatoria conceptualmente, aunque su carga completa pueda realizarse en una segunda iteración.

---

# 10. Gráficas de Energía, recursos y clima

Esta página corresponde a la segunda implantación, pero se fija ya su estructura.

## 10.1 Gráfica ENE1 — Producción y consumo

### Pregunta

> ¿Qué áreas producen la energía que consumen y cuáles dependen del exterior?

### Tipo

Barras agrupadas.

### Datos

* producción energética;
* consumo energético.

### Prioridad

Alta.

---

## 10.2 Gráfica ENE2 — Dependencia exterior

### Pregunta

> ¿Qué parte de la energía debe obtenerse fuera del área?

### Tipo

Barras horizontales divergentes.

Posibles resultados:

* exportador neto;
* equilibrio;
* importador neto.

### Prioridad

Alta.

---

## 10.3 Gráfica ENE3 — Emisiones por habitante

### Pregunta

> ¿Cuánto CO₂ emite, en promedio, cada habitante?

### Tipo

Barras horizontales.

### Datos

* emisiones territoriales por habitante.

### Prioridad

Alta.

## Información adicional

Las emisiones totales aparecerán en la tabla y podrán compararse con las emisiones por habitante.

---

# 11. Gráficas de Tecnología, inteligencia artificial y futuro

Esta página también corresponde a la segunda implantación.

## 11.1 Representación TEC1 — Cadena de valor tecnológica

### Pregunta

> ¿Qué necesita un área para desarrollar inteligencia artificial avanzada?

### Tipo

Diagrama explicativo.

### Secuencia

1. energía;
2. semiconductores;
3. centros de datos;
4. capacidad de cómputo;
5. talento;
6. modelos;
7. aplicaciones;
8. adopción;
9. gobernanza.

### Función

Explicar el sistema antes de comparar áreas.

### Prioridad

Obligatoria para esta página.

---

## 11.2 Matriz TEC2 — Capacidades en IA

### Pregunta

> ¿En qué partes de la cadena de la inteligencia artificial destaca o depende cada área?

### Tipo

Matriz cualitativa.

### Columnas iniciales

* chips;
* cómputo;
* centros de datos;
* investigación;
* talento;
* modelos propios;
* inversión;
* adopción;
* regulación;
* autonomía tecnológica.

### Regla

No generar todavía un índice global de IA.

### Prioridad

Alta.

---

## 11.3 Gráfica TEC3 — Investigación y desarrollo

### Pregunta

> ¿Qué esfuerzo dedica cada área a crear conocimiento y tecnología?

### Tipo

Barras horizontales.

### Datos

* gasto en I+D como porcentaje del PIB;
* gasto total, como dato complementario.

### Prioridad

Alta.

---

# 12. Gráficas en fichas de área

Cada ficha podrá contener inicialmente un máximo de dos visualizaciones.

## Gráfica F1 — Perfil del área frente al mundo

### Función

Comparar el área con el promedio mundial o con las demás áreas.

### Indicadores posibles

* población;
* superficie;
* PIB;
* PIB por habitante;
* IDH;
* Gini;
* gasto militar.

### Representación

Barras horizontales pequeñas.

### Regla

No utilizar radar.

## Gráfica F2 — Tendencia relevante

Se seleccionará según el perfil del área.

Ejemplos:

* población a 2050;
* envejecimiento;
* energía;
* emisiones;
* peso económico;
* gasto militar;
* tecnología.

## Restricción

Las nueve fichas conservarán una estructura común, aunque la segunda gráfica pueda variar.

---

# 13. Tabla y gráfica: funciones diferentes

La tabla responderá:

> ¿Cuál es el valor exacto o aproximado?

La gráfica responderá:

> ¿Qué comparación o relación debo recordar?

No se duplicará una tabla completa en forma de gráfica si no existe una conclusión clara.

---

# 14. Texto obligatorio junto a cada gráfica

Cada gráfica incluirá:

1. título;
2. pregunta didáctica;
3. unidad;
4. año o ventana temporal;
5. fuente resumida;
6. una conclusión principal;
7. advertencia metodológica cuando corresponda.

## Ejemplo

> **Población y peso económico**
> Norteamérica y Europa concentran una proporción del PIB mundial muy superior a su porcentaje de población. África y el Subcontinente indio presentan la situación inversa.

La conclusión deberá generarse a partir de los datos reales, no escribirse de forma permanente antes de completar la base.

---

# 15. Alternativas móviles

Cada tipo de gráfica deberá disponer de una alternativa.

| Escritorio          | Alternativa móvil                              |
| ------------------- | ---------------------------------------------- |
| Barras horizontales | Barras horizontales desplazables verticalmente |
| Barras agrupadas    | Selector entre los dos indicadores             |
| Dispersión          | Lista ordenada o gráfica simplificada          |
| Matriz              | Tarjetas por área o por dimensión              |
| Mapa temático       | Lista de áreas con color y valor               |
| Línea temporal      | Dos puntos comparados o barra de variación     |

La versión móvil no tiene que reproducir exactamente el diseño de escritorio, pero sí la misma idea.

---

# 16. Gráficas existentes

Durante el diagnóstico técnico deberá clasificarse cada gráfica actual.

## Criterios

### Conservar

Cuando:

* responde a una pregunta útil;
* utiliza datos válidos;
* se entiende;
* funciona en móvil;
* encaja visualmente.

### Ajustar

Cuando:

* la idea es válida;
* necesita otros datos, etiquetas o formato.

### Sustituir

Cuando:

* es genérica;
* utiliza cifras simuladas;
* no explica nada;
* duplica la tabla;
* no funciona en móvil;
* contradice el modelo aprobado.

### Eliminar

Cuando:

* carece de función;
* añade ruido;
* utiliza datos sin fuente;
* dificulta la lectura.

---

# 17. Lista definitiva de visualizaciones para la primera implantación

## Portada — 3

1. Población y superficie.
2. Población y PIB mundial.
3. PIB por habitante, IDH y Gini.

## Territorio y población — 3

4. Población total.
5. Superficie y densidad.
6. Población actual y 2050.

## Economía — 3

7. PIB total.
8. PIB por habitante.
9. Población frente a PIB.

## Desarrollo humano y desigualdad — 3

10. IDH.
11. Gini.
12. PIB por habitante frente a esperanza de vida.

## Capacidad militar — 3

13. Gasto militar.
14. Gasto militar sobre PIB.
15. Matriz de capacidades estratégicas.

## Fichas — hasta 18

* una gráfica común por cada área;
* una gráfica específica opcional por área.

## Total inicial

* 15 visualizaciones globales o temáticas;
* 9 gráficas comunes de ficha;
* hasta 9 gráficas específicas.

No es obligatorio completar las nueve gráficas específicas en la primera implantación.

---

# 18. Alcance mínimo recomendado

Para considerar terminada la primera implantación deberán estar completas:

* las tres gráficas de portada;
* las tres de territorio y población;
* las tres de economía;
* las tres de desarrollo humano y desigualdad;
* las dos cuantitativas militares;
* una primera versión de la matriz militar;
* una gráfica común en cada ficha.

Esto supone:

* 15 visualizaciones centrales;
* 9 visualizaciones de ficha;
* 24 elementos visuales como máximo inicial obligatorio.

Aunque el número parezca alto, reutilizan pocos tipos:

* barras;
* barras agrupadas;
* dispersión;
* matriz.

---

# 19. Control de carga de trabajo

Para evitar agotamiento se aplicarán tres reglas.

## Regla 1 — Plantillas reutilizables

Se crearán componentes genéricos para:

* barras;
* barras agrupadas;
* dispersión;
* matriz;
* leyenda;
* fuentes.

No se programará cada gráfica desde cero.

## Regla 2 — Datos comunes

Las gráficas se alimentarán de:

* la misma base;
* los mismos endpoints;
* los mismos códigos de indicador;
* los mismos colores de área.

## Regla 3 — Implantación por lotes

Orden:

1. una gráfica de barras completa;
2. reutilización para las demás barras;
3. una gráfica agrupada;
4. reutilización;
5. una dispersión;
6. matriz;
7. adaptación móvil.

---

# 20. Relación con MySQL

La selección de gráficas confirma las consultas principales.

## Consultas simples

* un indicador para nueve áreas;
* dos indicadores para nueve áreas;
* tres indicadores para nueve áreas.

## Consultas de ficha

* varios indicadores de una sola área;
* comparación con promedio mundial;
* serie actual y futura.

## Consultas cualitativas

* dimensión;
* nivel;
* explicación;
* fuente;
* confianza.

La base de datos deberá permitir recuperar:

* valor;
* unidad;
* año;
* color;
* orden;
* fuente;
* cobertura;
* advertencia.

---

# 21. Indicadores requeridos por la primera implantación

## Necesarios para gráficas centrales

* población total;
* porcentaje de población mundial;
* superficie;
* porcentaje de superficie mundial;
* densidad;
* población 2050;
* PIB nominal;
* porcentaje del PIB mundial;
* PIB por habitante;
* IDH;
* Gini;
* esperanza de vida;
* gasto militar;
* porcentaje del gasto militar mundial;
* gasto militar sobre PIB.

Coinciden casi completamente con el conjunto inicial aprobado.

## Consecuencia

La recopilación inicial puede mantenerse contenida.

No es necesario completar todavía:

* educación detallada;
* sanidad detallada;
* energía completa;
* IA;
* emisiones totales;
* pobreza;
* comercio;
* cobertura sanitaria.

---

# 22. Porcentaje de avance asociado

Dentro del cálculo general del proyecto:

## Gráficas de portada

Equivalen aproximadamente al 6 % del proyecto total.

## Gráficas temáticas iniciales

Equivalen aproximadamente al 7 %.

## Gráficas de fichas

Equivalen aproximadamente al 2 %.

## Total visualizaciones

Aproximadamente el 15 % del avance global.

No deberá considerarse completada una gráfica si:

* usa datos simulados;
* no tiene fuente;
* no funciona en móvil;
* no incluye texto explicativo;
* no conserva los colores de las áreas.

---

# 23. Decisiones adoptadas

1. Se utilizarán principalmente barras horizontales.
2. Habrá un máximo de tres gráficas en portada.
3. La primera versión tendrá cuatro páginas temáticas completas.
4. La dispersión se reservará para relaciones claras.
5. Gini se mostrará mediante barras.
6. La capacidad militar incluirá una matriz cualitativa.
7. La IA utilizará una cadena de valor y una matriz, en una implantación posterior.
8. No se crearán índices sintéticos militares, energéticos o tecnológicos.
9. Cada gráfica tendrá pregunta, fuente y conclusión.
10. Cada gráfica tendrá alternativa móvil.
11. Las fichas tendrán una gráfica común y una segunda opcional.
12. Se reutilizarán plantillas para reducir trabajo.
13. Las visualizaciones iniciales utilizarán casi exclusivamente los 15 indicadores prioritarios.
14. Las gráficas actuales deberán clasificarse antes de sustituirse.
15. La selección queda limitada a visualizaciones que enseñan una idea concreta.

---

# 24. Decisión final de la Fase 1B.7

## GO

La selección inicial de gráficas y representaciones queda aprobada conceptualmente.

Puede iniciarse:

# Fase 1B.8 — Plantilla definitiva de ficha de área

La siguiente fase deberá definir:

* estructura exacta;
* longitud de textos;
* indicadores obligatorios;
* componentes visuales;
* diferencias internas;
* fortalezas y vulnerabilidades;
* fuentes;
* comportamiento móvil;
* contenido mínimo para considerar completa cada una de las nueve fichas.

Después de 1B.8 podrá iniciarse la preparación de la investigación y la recopilación de datos, antes de redactar las nueve fichas completas.
