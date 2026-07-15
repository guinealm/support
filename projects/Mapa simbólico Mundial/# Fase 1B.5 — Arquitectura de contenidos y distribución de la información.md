# Fase 1B.5 — Arquitectura de contenidos y distribución de la información

## Retícula Global 2025

## 1. Objetivo

Definir cómo se organiza y presenta la información de Retícula Global 2025 antes de diseñar la interfaz o implementar la base de datos.

La arquitectura debe permitir:

* entender el mundo de un vistazo;
* profundizar sin saturar;
* comparar las nueve áreas;
* consultar cada área de forma individual;
* estudiar cada tema de forma transversal;
* mostrar metodología y fuentes;
* funcionar correctamente en escritorio y móvil;
* crecer sin convertir la aplicación en un portal estadístico excesivo.

---

# 2. Principio editorial

La aplicación se organizará según esta regla:

> **Primero formar una imagen mental; después permitir la comparación; finalmente ofrecer profundidad y fuentes.**

La información se distribuirá en cuatro niveles:

1. visión global;
2. comparación resumida;
3. detalle por área o tema;
4. metodología y fuentes.

No se mostrará toda la información simultáneamente.

---

# 3. Estructura general de navegación

La aplicación tendrá estas secciones principales:

```text
Retícula Global 2025
│
├── Inicio / Visión global
│
├── Áreas
│   ├── Europa
│   ├── Norteamérica y Caribe
│   ├── Sudamérica
│   ├── Rusia y Eurasia postsoviética
│   ├── China
│   ├── Subcontinente indio
│   ├── Oriente Medio
│   ├── Asia-Pacífico
│   └── África
│
├── Temas
│   ├── Territorio y población
│   ├── Economía
│   ├── Desigualdad y pobreza
│   ├── Educación
│   ├── Sanidad y condiciones de vida
│   ├── Desarrollo humano
│   ├── Capacidad militar
│   ├── Energía y clima
│   └── Tecnología y futuro
│
├── Datos consolidados
│
└── Metodología y fuentes
```

No es necesario que todas estas secciones aparezcan como elementos permanentes en el menú principal.

La navegación podrá organizarse mediante:

* Inicio;
* Áreas;
* Temas;
* Datos;
* Metodología.

---

# 4. Página principal

## 4.1 Función

La portada debe responder rápidamente a estas preguntas:

* ¿Qué es Retícula Global?
* ¿Cómo se divide el mundo?
* ¿Cuánta población, superficie y riqueza concentra cada área?
* ¿Qué diferencias básicas existen entre las nueve áreas?
* ¿Dónde puedo profundizar?

No debe intentar explicar todos los indicadores.

---

## 4.2 Cabecera

La cabecera incluirá:

* identidad visual de Jumalenin;
* nombre del proyecto;
* navegación principal;
* acceso a metodología;
* indicación visible de la edición o fecha de datos.

Nombre recomendado:

> **Retícula Global 2025**

Subtítulo:

> **Una imagen básica de la estructura del mundo**

Nombre alternativo visible secundario:

> Mapa simbólico mundial

Este nombre puede conservarse como explicación histórica o descriptiva, pero no debe competir con el nombre principal.

---

## 4.3 Introducción breve

Texto orientativo:

> Retícula Global divide el mundo en nueve grandes áreas para comparar su territorio, población, economía, desarrollo, capacidad estratégica y tendencias futuras. No pretende sustituir un atlas ni una base estadística: busca ofrecer una imagen inicial, clara y razonada, del mundo en el que vivimos.

La introducción no debería superar aproximadamente 70 palabras en la portada.

---

# 5. Mapa global

## 5.1 Función

El mapa será el principal elemento de entrada.

Debe permitir:

* reconocer las nueve áreas;
* identificar su extensión;
* relacionar cada área con su posición real;
* acceder a su ficha;
* activar datos resumidos.

## 5.2 Proyección

Se utilizará preferentemente:

* Winkel Tripel; o
* Robinson, si técnicamente resulta más adecuada.

No se utilizará Mercator como representación principal.

## 5.3 Información visible

En estado inicial, el mapa mostrará:

* color de cada área;
* nombre o abreviatura;
* leyenda;
* límites territoriales;
* indicación de que se trata de una agrupación didáctica.

Al seleccionar un área podrá aparecer una tarjeta breve con:

* nombre;
* población;
* porcentaje de población mundial;
* superficie;
* PIB total;
* acceso a la ficha.

## 5.4 Comportamiento

En escritorio:

* selección mediante clic;
* información emergente o panel lateral;
* resaltado del área.

En móvil:

* selección táctil;
* tarjeta debajo del mapa;
* evitar ventanas flotantes pequeñas;
* permitir desplazamiento y ampliación solo si resulta necesario.

## 5.5 Restricción

El mapa no mostrará simultáneamente:

* todos los indicadores;
* gráficos superpuestos;
* etiquetas extensas;
* cifras demasiado pequeñas;
* animaciones continuas.

---

# 6. Resumen de las nueve áreas

Debajo del mapa aparecerá una cuadrícula o lista de nueve tarjetas.

Cada tarjeta incluirá:

* nombre del área;
* color;
* población;
* superficie;
* PIB total;
* una frase de perfil;
* acceso a la ficha.

Ejemplo conceptual:

> **África**
> 1.500 millones de habitantes
> 30,4 millones de km²
> Población joven, gran extensión y elevado crecimiento demográfico.

Las frases deberán ser descriptivas, no promocionales ni estereotipadas.

---

# 7. Indicadores esenciales en portada

La portada utilizará un conjunto reducido de indicadores.

## 7.1 Primera visualización

Se mostrarán inicialmente:

1. población;
2. porcentaje de población mundial;
3. superficie;
4. porcentaje de superficie mundial;
5. PIB total;
6. PIB por habitante;
7. porcentaje del PIB mundial;
8. Gini;
9. IDH;
10. esperanza de vida;
11. gasto militar o porcentaje del gasto mundial.

## 7.2 Distribución

No deben aparecer como once columnas simultáneas.

Se organizarán en tres grupos:

### Tamaño

* población;
* superficie;
* densidad.

### Economía y distribución

* PIB total;
* PIB por habitante;
* Gini.

### Vida y poder

* IDH;
* esperanza de vida;
* gasto militar.

Los porcentajes mundiales pueden mostrarse como información secundaria.

---

# 8. Tabla resumida de portada

La portada incluirá una tabla comparativa reducida.

## Columnas recomendadas

| Área | Población | Superficie | PIB | PIB/hab. | Gini | IDH | Gasto militar |
| ---- | --------: | ---------: | --: | -------: | ---: | --: | ------------: |

## Reglas

* encabezados comprensibles;
* unidades visibles;
* redondeo;
* posibilidad de ordenar en escritorio;
* desplazamiento horizontal controlado en móvil;
* enlace a la tabla consolidada completa;
* señal discreta cuando el dato sea aproximado.

## Versión móvil

En móvil podrá transformarse en:

* tarjetas comparativas;
* selector de indicador;
* tabla reducida con tres o cuatro columnas;
* botón “Ver todos los datos”.

---

# 9. Gráficas de portada

La portada tendrá un máximo inicial de tres gráficas.

## Gráfica 1 — Población y superficie

Pregunta:

> ¿Dónde vive la población mundial y cuánto territorio ocupa cada área?

Representación:

* barras dobles;
* o dos gráficos alineados.

## Gráfica 2 — Población y peso económico

Pregunta:

> ¿Qué relación existe entre el porcentaje de población y el porcentaje de PIB mundial?

Representación:

* barras comparativas;
* o gráfico de dispersión sencillo.

## Gráfica 3 — Riqueza media y desarrollo

Pregunta:

> ¿Cómo se relacionan el PIB por habitante, el IDH y la desigualdad?

Representación inicial:

* dispersión PIB por habitante–IDH;
* Gini como información complementaria, no necesariamente como tercer eje visual.

No se incorporarán más gráficas hasta comprobar que estas aportan comprensión real.

---

# 10. Acceso por áreas

## 10.1 Página índice de áreas

La sección Áreas mostrará las nueve agrupaciones mediante:

* mapa;
* tarjetas;
* resumen;
* datos esenciales;
* acceso a cada ficha.

Esta página puede coincidir parcialmente con la portada, pero no debe duplicarla por completo.

## 10.2 URL conceptual

Ejemplos:

```text
areas/europa
areas/africa
areas/china
areas/oriente-medio
```

La forma técnica definitiva dependerá de la estructura actual de Support y de la futura implementación.

---

# 11. Ficha de área

## 11.1 Función

Cada ficha debe responder:

* qué territorios forman el área;
* cuál es su dimensión;
* cómo vive su población;
* cuál es su peso económico y estratégico;
* qué diferencias internas contiene;
* qué tendencias pueden definir su futuro.

## 11.2 Estructura común

### A. Cabecera de área

* nombre;
* color;
* mapa de localización;
* frase descriptiva;
* fecha de datos.

### B. Cifras esenciales

* población;
* superficie;
* porcentaje mundial;
* PIB;
* PIB por habitante;
* Gini;
* IDH;
* esperanza de vida;
* gasto militar.

### C. Perfil general

Texto de entre 100 y 180 palabras.

Debe explicar:

* qué define al área;
* su diversidad interna;
* su posición global;
* una o dos tensiones esenciales.

### D. Territorio y población

* composición territorial;
* población;
* densidad;
* edad;
* urbanización;
* crecimiento;
* proyección a 2050.

### E. Economía

* PIB;
* riqueza por habitante;
* estructura económica;
* comercio;
* desigualdad.

### F. Condiciones de vida

* IDH;
* esperanza de vida;
* educación;
* mortalidad infantil;
* agua y saneamiento.

### G. Capacidad estratégica

* gasto militar;
* industria;
* capacidad nuclear;
* misiles;
* drones;
* inteligencia;
* logística;
* alianzas.

No todos estos puntos tendrán necesariamente una cifra.

### H. Energía y clima

* consumo;
* dependencia exterior;
* recursos;
* emisiones;
* vulnerabilidad.

### I. Tecnología y futuro

* acceso a Internet;
* investigación;
* semiconductores;
* inteligencia artificial;
* tendencias demográficas.

### J. Diferencias internas

Sección obligatoria.

Debe evitar presentar el área como homogénea.

Ejemplos de diferencias:

* renta;
* regímenes políticos;
* urbanización;
* idiomas;
* religión;
* desarrollo;
* seguridad;
* disponibilidad de recursos.

### K. Fortalezas y vulnerabilidades

Formato breve:

| Fortalezas    | Vulnerabilidades |
| ------------- | ---------------- |
| 3–5 elementos | 3–5 elementos    |

### L. Fuentes

* fuentes principales;
* años;
* enlace a metodología;
* advertencias específicas.

---

# 12. Páginas temáticas

## 12.1 Función

Las páginas temáticas compararán las nueve áreas bajo una misma pregunta.

No deben limitarse a mostrar una tabla.

Cada página contendrá:

1. pregunta principal;
2. explicación breve;
3. indicadores esenciales;
4. gráfica principal;
5. tabla comparativa;
6. lectura de resultados;
7. excepciones;
8. acceso a las fichas;
9. metodología.

---

## 12.2 Territorio y población

Pregunta principal:

> ¿Cómo se reparten el territorio y la población mundial?

Contenido:

* superficie;
* población;
* porcentaje mundial;
* densidad;
* crecimiento;
* edad mediana;
* urbanización;
* población a 2050.

Gráficas:

* población;
* superficie;
* población actual frente a 2050.

---

## 12.3 Economía

Pregunta principal:

> ¿Dónde se concentra la actividad económica y qué riqueza media genera?

Contenido:

* PIB nominal;
* porcentaje mundial;
* PIB PPA;
* PIB por habitante;
* estructura económica;
* comercio.

Gráficas:

* PIB total;
* PIB por habitante;
* población frente a PIB.

---

## 12.4 Desigualdad y pobreza

Pregunta principal:

> ¿Cómo se reparte la riqueza dentro de cada área?

Contenido:

* Gini;
* pobreza;
* IDH ajustado por desigualdad;
* cobertura de datos;
* diferencias internas.

Gráficas:

* Gini por áreas;
* PIB por habitante frente a Gini;
* pérdida de desarrollo por desigualdad, cuando exista.

Debe explicarse claramente que:

* riqueza media y desigualdad no son lo mismo;
* una media regional puede ocultar diferencias nacionales;
* el Gini regional será aproximado.

---

## 12.5 Educación

Pregunta principal:

> ¿Qué oportunidades educativas tiene la población?

Contenido:

* alfabetización;
* años medios de escolarización;
* años esperados;
* educación secundaria;
* diferencias de género, cuando resulte viable.

Gráficas:

* años medios y esperados;
* educación frente a IDH.

---

## 12.6 Sanidad y condiciones de vida

Pregunta principal:

> ¿Cómo se traduce el desarrollo en vidas más largas y seguras?

Contenido:

* esperanza de vida;
* mortalidad infantil;
* gasto sanitario;
* cobertura;
* agua;
* saneamiento.

Gráficas:

* esperanza de vida;
* mortalidad infantil;
* renta frente a esperanza de vida.

---

## 12.7 Desarrollo humano

Pregunta principal:

> ¿Cómo combinan las áreas salud, educación e ingresos?

Contenido:

* IDH;
* IDH ajustado;
* esperanza de vida;
* educación;
* renta;
* desigualdad.

Gráficas:

* clasificación IDH;
* PIB por habitante frente a IDH;
* IDH frente a Gini.

---

## 12.8 Capacidad militar y estratégica

Pregunta principal:

> ¿Qué capacidad tiene cada área para defenderse, influir y sostener un conflicto?

Contenido cuantitativo:

* gasto militar;
* porcentaje mundial;
* gasto sobre PIB;
* capacidad nuclear;
* exportaciones militares, si se incorpora.

Contenido cualitativo:

* industria propia;
* producción y reposición;
* misiles;
* drones;
* inteligencia y vigilancia;
* comunicaciones y mando;
* guerra electrónica;
* ciberdefensa;
* logística;
* proyección exterior;
* alianzas y apoyo exterior.

Subpreguntas didácticas:

* ¿Tener más presupuesto significa ser militarmente más fuerte?
* ¿Puede una fuerza menor compensar su debilidad con drones, misiles o inteligencia?
* ¿Puede mantener un conflicto largo?
* ¿Depende del apoyo de aliados?
* ¿Dispone de producción propia?

La página no deberá producir inicialmente una clasificación total del tipo “1.º, 2.º, 3.º”.

---

## 12.9 Energía, recursos y clima

Pregunta principal:

> ¿De dónde obtiene cada área la energía que sostiene su economía y qué riesgos afronta?

Contenido:

* consumo energético;
* consumo por habitante;
* producción;
* importaciones;
* dependencia exterior;
* diversidad de fuentes;
* combustibles fósiles;
* renovables;
* minerales críticos;
* emisiones totales;
* emisiones por habitante;
* vulnerabilidad climática.

Autonomía energética se tratará como una combinación de:

* recursos;
* producción;
* importaciones;
* transformación;
* redes;
* diversidad;
* seguridad de suministro.

No se resumirá inicialmente en una única puntuación.

---

## 12.10 Tecnología y futuro

Pregunta principal:

> ¿Qué capacidad tiene cada área para participar en la próxima transformación tecnológica?

Contenido general:

* acceso a Internet;
* investigación y desarrollo;
* patentes;
* universidades;
* semiconductores;
* centros de datos;
* infraestructura digital;
* capacidad industrial avanzada.

### Inteligencia artificial

Subsección específica:

* inversión en IA;
* investigación;
* talento;
* modelos desarrollados;
* capacidad de cómputo;
* semiconductores;
* centros de datos;
* adopción empresarial;
* aplicación pública;
* autonomía tecnológica;
* gobernanza;
* uso militar y estratégico.

Preguntas didácticas:

* ¿Quién desarrolla la inteligencia artificial?
* ¿Quién fabrica los chips?
* ¿Quién controla el cómputo y los centros de datos?
* ¿Quién adopta la tecnología?
* ¿Quién depende de proveedores exteriores?
* ¿Qué áreas pueden regularla o influir en sus reglas?

La IA se tratará como una dimensión propia, no como una nota secundaria.

---

# 13. Página de Datos Consolidados

## 13.1 Función

Será la referencia comparativa central.

Debe permitir:

* consultar las nueve áreas;
* cambiar de bloque;
* ordenar;
* filtrar;
* ver año y fuente;
* identificar aproximaciones;
* exportar datos, si se incorpora más adelante.

## 13.2 Vista inicial

No se abrirá mostrando todas las columnas.

Se iniciará con:

* selector de bloque;
* selector de indicador;
* tabla de nueve filas;
* gráfica asociada;
* explicación breve.

## 13.3 Modos de consulta

### Por área

Muestra todos los indicadores de una sola área.

### Por indicador

Compara un indicador entre las nueve áreas.

### Por bloque

Muestra varios indicadores relacionados.

### Vista completa

Disponible como opción secundaria para usuarios avanzados.

## 13.4 Información complementaria

Cada dato podrá mostrar:

* valor;
* unidad;
* año;
* fuente;
* cobertura;
* método;
* advertencia.

La información metodológica completa podrá abrirse bajo demanda.

---

# 14. Página de metodología y fuentes

## 14.1 Función

Sustentar la credibilidad sin cargar las páginas principales.

## 14.2 Contenido

* finalidad del proyecto;
* definición de las nueve áreas;
* clasificación M49;
* excepciones territoriales;
* fecha de corte;
* política temporal;
* diccionario de indicadores;
* fuentes;
* métodos de agregación;
* cobertura;
* datos ausentes;
* redondeo;
* aproximaciones;
* limitaciones;
* fecha de revisión.

## 14.3 Niveles de lectura

### Resumen metodológico

Una página breve y comprensible.

### Detalle técnico

Información ampliada por indicador.

### Fuente concreta

Enlace o referencia del conjunto utilizado.

---

# 15. Sistema de profundidad progresiva

Cada elemento seguirá tres niveles:

## Nivel 1 — Lectura inmediata

* cifra;
* color;
* icono;
* etiqueta;
* barra.

## Nivel 2 — Explicación

* texto breve;
* comparación;
* gráfica;
* contexto.

## Nivel 3 — Metodología

* fuente;
* año;
* fórmula;
* cobertura;
* limitaciones.

Ejemplo:

### Nivel 1

> Gini aproximado: 42,3

### Nivel 2

> La desigualdad media es elevada, aunque existen diferencias importantes entre los países del área.

### Nivel 3

> Media ponderada por población de los últimos datos nacionales disponibles entre 2022 y 2025, con una cobertura del 87 %.

---

# 16. Reglas de representación visual

## 16.1 Colores

Cada área tendrá un color estable.

El color deberá utilizarse en:

* mapa;
* tarjetas;
* gráficas;
* títulos;
* etiquetas.

No se utilizará como único método de identificación.

Cada área dispondrá también de:

* código;
* nombre;
* posible patrón o icono auxiliar.

## 16.2 Iconos

Se utilizarán iconos funcionales:

* población;
* territorio;
* economía;
* desigualdad;
* educación;
* salud;
* defensa;
* energía;
* tecnología.

No se utilizarán inicialmente:

* personajes;
* atuendos;
* caricaturas;
* representaciones culturales simplificadas.

## 16.3 Cifras

Las cifras destacadas deberán:

* incluir unidad;
* estar redondeadas;
* indicar año cuando sea relevante;
* mostrar aproximación;
* evitar decimales innecesarios.

## 16.4 Barras

Las barras serán preferibles a velocímetros, medidores circulares o gráficos decorativos.

## 16.5 Escalas cualitativas

Solo se usarán cuando:

* los criterios sean visibles;
* la escala esté definida;
* exista una explicación;
* no parezca una medida exacta.

---

# 17. Diseño para público infantil y general

La aplicación no será infantil en apariencia, pero deberá ser comprensible para lectores jóvenes.

## Reglas

* preguntas claras;
* frases breves;
* explicación de términos;
* comparaciones;
* unidades reconocibles;
* evitar jerga;
* no infantilizar;
* permitir profundización.

Ejemplo:

En lugar de:

> Índice agregado ponderado de paridad de poder adquisitivo.

Usar:

> La PPA intenta comparar cuánto puede comprarse realmente con el dinero en cada país.

Los términos técnicos podrán mantenerse si se explican.

---

# 18. Contenido narrativo

Cada página deberá contener una explicación.

No se aceptará una estructura formada únicamente por:

* cifras;
* tarjetas;
* gráficos;
* tablas.

## Extensión orientativa

### Portada

* introducción: 50–70 palabras;
* explicación por bloque: 30–60 palabras.

### Ficha de área

* resumen: 100–180 palabras;
* secciones: 60–140 palabras;
* diferencias internas: 80–150 palabras.

### Página temática

* introducción: 100–180 palabras;
* lectura de resultados: 150–300 palabras;
* metodología resumida: 50–100 palabras.

Estas cifras son orientativas, no límites rígidos.

---

# 19. Evitar duplicidades

La misma cifra puede aparecer en varios contextos, pero no debe repetirse la misma explicación extensa.

## Regla

* portada: resumen;
* ficha: interpretación del área;
* temática: comparación;
* metodología: cálculo.

Ejemplo con Gini:

* portada: valor y señal visual;
* ficha: significado en el área;
* página temática: comparación entre áreas;
* metodología: años, cobertura y ponderación.

---

# 20. Arquitectura móvil

## 20.1 Portada

Orden recomendado:

1. título e introducción;
2. mapa;
3. tarjeta del área seleccionada;
4. tarjetas de las nueve áreas;
5. selector de indicadores;
6. gráfica;
7. acceso a profundidad.

## 20.2 Ficha de área

* cifras esenciales en dos columnas;
* secciones desplegables o consecutivas;
* gráficos de ancho completo;
* tablas desplazables solo cuando sea inevitable.

## 20.3 Temas

* selector de indicador;
* gráfica;
* tabla de nueve áreas;
* explicación;
* metodología.

## 20.4 Restricción

No depender de:

* hover;
* tooltips pequeños;
* dobles clics;
* controles densos;
* mapas que exijan gran precisión táctil.

---

# 21. Página de inicio: versión mínima viable

La primera versión implementada podrá limitarse a:

1. cabecera;
2. introducción;
3. mapa de las nueve áreas;
4. tarjetas de áreas;
5. tabla resumida;
6. tres gráficas;
7. acceso a fichas;
8. acceso a datos;
9. metodología básica;
10. pie.

No será necesario completar inicialmente:

* las nueve páginas temáticas;
* todos los textos;
* todos los indicadores;
* IA completa;
* capacidades militares cualitativas;
* exportaciones;
* administración avanzada.

---

# 22. Fichas: versión mínima viable

Cada una de las nueve fichas podrá comenzar con:

* mapa;
* países;
* resumen;
* población;
* superficie;
* PIB;
* PIB por habitante;
* Gini;
* IDH;
* esperanza de vida;
* gasto militar;
* proyección demográfica;
* fortalezas;
* vulnerabilidades;
* fuentes.

El resto podrá incorporarse por bloques posteriores.

---

# 23. Páginas temáticas: orden de implantación

## Primera prioridad

1. territorio y población;
2. economía;
3. desarrollo humano;
4. capacidad militar.

## Segunda prioridad

5. desigualdad y pobreza;
6. energía y clima;
7. tecnología y futuro.

## Tercera prioridad

8. educación;
9. sanidad y condiciones de vida.

El orden no implica menor importancia educativa o sanitaria.

Se basa en:

* disponibilidad inicial de datos;
* conexión con el concepto de mapa geopolítico;
* utilidad para construir la primera imagen mundial;
* facilidad de implementación.

---

# 24. Relación con MySQL

La arquitectura confirma que la base deberá responder a cuatro tipos de consulta:

## Consulta global

Datos esenciales de las nueve áreas.

## Consulta por área

Todos los bloques de una sola área.

## Consulta por tema

Uno o varios indicadores para las nueve áreas.

## Consulta metodológica

Fuente, año, cobertura y método.

Estas consultas determinarán posteriormente:

* las vistas SQL;
* los endpoints PHP;
* los archivos JSON;
* la estructura del frontend.

---

# 25. Relación con Support

Retícula Global permanecerá dentro de:

```text
support/projects/reticula-global/
```

o la ruta equivalente que se confirme en el diagnóstico.

No se modificará en esta fase:

* la portada general de Support;
* Common;
* la estructura general del ecosistema;
* el repositorio;
* el despliegue.

La aplicación podrá incorporar reglas visuales propias, compatibles con la identidad común de Jumalenin, sin convertirlas todavía en estilos compartidos.

---

# 26. Control del alcance

Antes de incorporar una sección deberá responderse:

1. ¿Qué pregunta enseña?
2. ¿Qué dato utiliza?
3. ¿De qué fuente procede?
4. ¿Dónde debe aparecer?
5. ¿Qué representación necesita?
6. ¿Es comprensible en móvil?
7. ¿Duplica otra sección?
8. ¿Es necesaria en la primera versión?

Si no existe una respuesta clara, la sección se aplaza.

---

# 27. Decisiones adoptadas

1. La portada ofrecerá una visión global y no una enciclopedia.
2. El mapa será el principal punto de entrada.
3. Las nueve áreas tendrán tarjetas y fichas propias.
4. La información se organizará también por temas.
5. La Tabla de Datos Consolidados tendrá página propia.
6. Los datos mostrarán profundidad progresiva.
7. Gini se mantendrá entre los indicadores principales.
8. La capacidad militar incluirá recursos modernos y apoyo exterior.
9. La inteligencia artificial tendrá tratamiento explícito.
10. La autonomía energética se tratará como dimensión estratégica.
11. Los personajes permanecerán congelados.
12. Se usarán color, iconos, barras, mapas y pocas gráficas.
13. La primera versión se limitará a contenidos esenciales.
14. La arquitectura será compatible con escritorio y móvil.
15. La base de datos servirá a portada, áreas, temas y metodología.

---

# 28. Decisión final de la Fase 1B.5

## GO

La arquitectura de contenidos está suficientemente definida para iniciar:

# Fase 1B.6 — Sistema visual específico de Retícula Global

La siguiente fase deberá fijar:

* proyección y tratamiento del mapa;
* paleta de las nueve áreas;
* jerarquía visual;
* tarjetas;
* iconos;
* tablas;
* gráficas;
* escalas;
* tratamiento de advertencias;
* comportamiento en escritorio y móvil;
* relación con la identidad visual común de Jumalenin.

Todavía no se implementarán cambios en la aplicación ni se crearán las tablas MySQL.
