# Fase 1B — Definición del modelo conceptual de Retícula Global 2025

## 1. Finalidad de la fase

Definir la arquitectura conceptual, informativa y didáctica de Retícula Global 2025 antes de continuar con modificaciones técnicas.

La aplicación debe ofrecer una representación estática y comprensible de la estructura general del mundo, previa a la interpretación de noticias, conflictos, economía, política internacional o redes sociales.

No pretende sustituir un atlas, una base estadística profesional ni un estudio académico. Su función es proporcionar una primera imagen ordenada y comparable del mundo.

## 2. Principio general

La información se organizará en tres niveles complementarios:

### Nivel 1 — Visión global

Página principal con:

* mapa mundial dividido en nueve áreas;
* explicación breve del proyecto;
* indicadores esenciales;
* tabla consolidada resumida;
* pocas gráficas comparativas;
* acceso a cada área;
* acceso a las páginas temáticas.

### Nivel 2 — Fichas de las nueve áreas

Cada área dispondrá de una ficha o página propia con:

* composición territorial;
* población;
* superficie;
* economía;
* capacidad militar;
* desigualdad;
* educación;
* sanidad;
* desarrollo humano;
* energía, emisiones y otros indicadores futuros;
* gráficos o elementos visuales propios;
* explicación narrativa del perfil del área.

### Nivel 3 — Páginas temáticas comparativas

Cada bloque de indicadores dispondrá de una página que compare conjuntamente las nueve áreas.

Bloques iniciales previstos:

1. territorio y población;
2. economía;
3. capacidad militar;
4. desigualdad y distribución;
5. educación;
6. sanidad y condiciones de vida;
7. desarrollo humano;
8. energía, recursos y emisiones;
9. tendencias demográficas y posición futura.

Estas páginas evitarán tener que concentrar toda la información en la portada o repetir explicaciones extensas en el mapa.

## 3. Decisiones ya adoptadas

### 3.1 Número de áreas

Se conservarán inicialmente las nueve áreas existentes en la aplicación.

Antes de calcular datos se deberá comprobar:

* nombre exacto de cada área;
* países incluidos;
* territorios excluidos;
* solapamientos;
* países de adscripción dudosa;
* coherencia geográfica, económica y geopolítica del agrupamiento.

No se alterará el número de áreas sin una justificación conceptual clara.

### 3.2 Tabla de Datos Consolidados

La Tabla de Datos Consolidados será la fuente central del proyecto.

Todos los contenidos visuales, gráficos, fichas y comparaciones deberán derivarse de esta tabla o de tablas auxiliares relacionadas.

La tabla no será únicamente un elemento mostrado en pantalla. Será también el modelo estructurado que permita:

* mantener coherencia entre páginas;
* comparar las nueve áreas;
* actualizar datos;
* identificar la fuente de cada cifra;
* generar gráficos;
* seleccionar indicadores resumidos para la portada;
* desarrollar posteriormente nuevas formas de visualización.

### 3.3 Personajes o avatares

La representación de las áreas mediante personajes queda congelada.

No se descarta como desarrollo futuro, pero no formará parte de la primera versión seria de la aplicación.

Motivos:

* riesgo de estereotipos;
* dificultad para representar indicadores complejos;
* falta de una codificación visual suficientemente madura;
* posible exceso de carga gráfica;
* necesidad de consolidar primero los datos y su significado.

La aplicación comenzará con recursos visuales controlados y habituales en una web profesional:

* colores;
* iconos;
* cifras destacadas;
* escalas;
* barras;
* símbolos;
* mapas;
* gráficos muy seleccionados;
* patrones comparativos.

## 4. Secuencia de trabajo

### Fase 1B.1 — Inventario y definición de las nueve áreas

Objetivo:

Confirmar la división territorial actualmente utilizada.

Trabajo:

* identificar los nombres de las nueve áreas;
* inventariar los países incluidos en cada una;
* localizar países o territorios no asignados;
* revisar casos fronterizos;
* justificar cada agrupación;
* comprobar si el conjunto se aproxima razonablemente a la población mundial total;
* evitar duplicidades.

Resultado esperado:

`areas-reticula-global-1b1.md`

El documento incluirá una tabla:

| Área | Países incluidos | Población aproximada | Justificación | Casos dudosos |
| ---- | ---------------- | -------------------: | ------------- | ------------- |

Decisión de cierre:

* áreas confirmadas;
* áreas pendientes;
* cambios imprescindibles antes de calcular datos.

### Fase 1B.2 — Diccionario de indicadores

Objetivo:

Definir qué se quiere medir antes de buscar cifras.

Para cada indicador se deberá establecer:

* nombre;
* definición;
* unidad;
* significado didáctico;
* año de referencia;
* fuente preferente;
* forma de agregación por área;
* limitaciones;
* nivel de presentación.

Clasificación inicial:

#### A. Territorio y población

* superficie;
* población;
* porcentaje de población mundial;
* porcentaje de superficie mundial;
* densidad;
* población urbana;
* crecimiento demográfico;
* edad mediana.

#### B. Economía

* PIB nominal;
* porcentaje del PIB mundial;
* PIB en paridad de poder adquisitivo;
* PIB por habitante;
* estructura económica;
* productividad o renta disponible, cuando sea viable.

#### C. Capacidad militar

* gasto militar;
* porcentaje del gasto militar mundial;
* gasto militar por habitante;
* fuerzas nucleares;
* industria militar;
* capacidad tecnológica;
* capacidad de proyección;
* índice sintético, únicamente si se define una metodología transparente.

#### D. Desigualdad

* índice de Gini;
* pobreza;
* distribución de ingresos;
* diferencias internas;
* limitaciones derivadas de agregar países muy distintos.

#### E. Educación

* alfabetización;
* años esperados de escolarización;
* años medios de escolarización;
* acceso a educación secundaria;
* acceso a educación superior.

#### F. Sanidad y condiciones de vida

* esperanza de vida;
* mortalidad infantil;
* gasto sanitario;
* cobertura sanitaria;
* médicos por población, si resulta comparable;
* acceso a agua potable y saneamiento.

#### G. Desarrollo humano

* índice de desarrollo humano;
* desarrollo humano ajustado por desigualdad;
* pobreza multidimensional, cuando existan datos suficientes.

#### H. Energía, clima y recursos

* consumo energético;
* emisiones totales;
* emisiones por habitante;
* dependencia de combustibles fósiles;
* recursos estratégicos;
* vulnerabilidad climática.

Resultado esperado:

`diccionario-indicadores-reticula-global-1b2.md`

### Fase 1B.3 — Fuentes, fecha de corte y metodología

Objetivo:

Establecer una política de datos antes de realizar investigación intensiva.

Debe definirse:

* año base preferente;
* tratamiento de indicadores cuyo último año disponible sea diferente;
* fuentes prioritarias;
* procedimiento para sumar datos nacionales;
* tratamiento de medias ponderadas;
* tratamiento de países sin datos;
* redondeo;
* trazabilidad;
* fecha de actualización;
* diferencia entre dato observado, estimación e índice elaborado.

Jerarquía orientativa de fuentes:

1. organismos internacionales especializados;
2. bases de datos públicas de reconocido prestigio;
3. institutos estadísticos nacionales;
4. centros de investigación especializados;
5. fuentes divulgativas secundarias para explicación, no como base principal.

Resultado esperado:

`metodologia-y-fuentes-reticula-global-1b3.md`

### Fase 1B.4 — Diseño lógico de la Tabla de Datos Consolidados

Objetivo:

Crear la estructura maestra de datos sin completar todavía necesariamente todas las cifras.

La tabla debe distinguir:

* datos absolutos;
* datos por habitante;
* porcentajes mundiales;
* medias ponderadas;
* índices;
* clasificaciones cualitativas;
* fuente;
* año;
* observaciones.

No conviene diseñarla como una única tabla visual gigantesca.

Se recomienda trabajar con:

#### Tabla principal de áreas

Una fila por área y columnas con los indicadores esenciales.

#### Tabla de metadatos

Una fila por indicador:

* definición;
* unidad;
* fuente;
* fecha;
* fórmula;
* limitaciones.

#### Tablas temáticas auxiliares

Para indicadores complejos o con varias dimensiones.

Resultado esperado:

`modelo-datos-consolidados-reticula-global-1b4.md`

y, cuando corresponda, una primera plantilla CSV, JSON o tabla Markdown.

### Fase 1B.5 — Arquitectura de contenidos

Objetivo:

Decidir dónde se presenta cada dato.

Para cada indicador se marcará uno o varios destinos:

* portada;
* mapa;
* tabla resumida;
* ficha de área;
* página temática;
* gráfico;
* explicación metodológica.

Regla general:

#### Portada

Solo debe contener los datos que ayudan a formar una primera imagen mundial:

* población;
* superficie;
* peso económico;
* capacidad militar resumida;
* uno o dos indicadores sociales;
* acceso a información detallada.

#### Ficha de área

Debe explicar el perfil completo del área, con contexto y excepciones internas.

#### Página temática

Debe comparar el mismo indicador entre las nueve áreas y explicar su significado.

Resultado esperado:

`arquitectura-contenidos-reticula-global-1b5.md`

### Fase 1B.6 — Sistema visual inicial

Objetivo:

Definir una presentación seria, clara y ligera.

Elementos permitidos inicialmente:

* color propio de cada área;
* iconos consistentes;
* cifras destacadas;
* tarjetas;
* barras comparativas;
* escalas proporcionales;
* pequeños diagramas;
* gráficos de barras;
* gráficos de dispersión cuando aporten una relación clara;
* mapas temáticos;
* señales de tendencia.

Elementos pospuestos:

* personajes;
* atuendos;
* caricaturas;
* figuras humanas proporcionales;
* metáforas visuales difíciles de interpretar;
* animaciones complejas;
* grandes paneles estadísticos.

El sistema visual será una extensión específica de la identidad común de Jumalenin, sin modificar todavía Common.

Resultado esperado:

`criterios-visuales-reticula-global-1b6.md`

### Fase 1B.7 — Selección de gráficas

Objetivo:

Seleccionar pocas gráficas que expliquen relaciones importantes.

Gráficas iniciales candidatas:

1. población y porcentaje mundial;
2. superficie y densidad;
3. PIB total y PIB por habitante;
4. población frente a peso económico;
5. gasto militar frente a peso económico;
6. desarrollo humano frente a desigualdad;
7. esperanza de vida frente a renta;
8. emisiones totales frente a emisiones por habitante.

No deben incorporarse todas automáticamente.

Cada gráfica deberá superar estas preguntas:

* ¿qué idea concreta enseña?;
* ¿puede entenderse sin conocimientos estadísticos?;
* ¿aporta algo que no explica ya la tabla?;
* ¿permite comparar las nueve áreas?;
* ¿es legible en móvil?

Resultado esperado:

`graficas-prioritarias-reticula-global-1b7.md`

### Fase 1B.8 — Modelo de ficha de área

Objetivo:

Diseñar una plantilla común para las nueve áreas.

Estructura orientativa:

1. nombre y mapa de situación;
2. países y población;
3. resumen de identidad del área;
4. territorio;
5. población;
6. economía;
7. capacidad militar;
8. desigualdad;
9. educación;
10. sanidad;
11. desarrollo humano;
12. energía, recursos y emisiones;
13. fortalezas;
14. vulnerabilidades;
15. tendencias;
16. diferencias internas;
17. fuentes y fecha de actualización.

Resultado esperado:

`plantilla-ficha-area-reticula-global-1b8.md`

### Fase 1B.9 — Redacción de las nueve fichas

Objetivo:

Aplicar la plantilla común a cada área.

Las fichas combinarán:

* cifras verificadas;
* explicación redactada;
* comparación con el conjunto mundial;
* advertencias sobre diversidad interna;
* enlaces a páginas temáticas.

La redacción podrá generarse inicialmente con asistencia de ChatGPT, pero deberá quedar sustentada por datos y fuentes identificables.

Resultado esperado:

* nueve fichas homogéneas;
* una por cada área;
* revisión conjunta de coherencia y extensión.

## 5. Papel de Codex

Codex permanecerá en pausa durante las fases 1B.1 a 1B.5, salvo para:

* leer la estructura existente;
* extraer los nombres y países actuales;
* identificar cómo están almacenados los datos;
* facilitar inventarios técnicos sin modificar archivos.

Codex volverá a intervenir activamente cuando estén definidos:

* las nueve áreas;
* el diccionario de indicadores;
* la metodología;
* el modelo de datos;
* la arquitectura de contenidos.

La implementación técnica corresponderá a una fase posterior.

## 6. Investigación avanzada

La investigación avanzada no debe iniciarse todavía de forma masiva.

Antes deben quedar cerrados:

1. las nueve áreas;
2. la lista de indicadores;
3. las fórmulas de agregación;
4. las fuentes prioritarias;
5. el año de corte;
6. la estructura de la tabla.

Investigar antes de cerrar estos elementos produciría:

* cifras difíciles de integrar;
* datos de años incompatibles;
* duplicación de trabajo;
* indicadores interesantes pero no utilizables;
* dificultad para comparar áreas.

La investigación avanzada sí será especialmente útil en:

* recopilación de datos por país;
* agregación por áreas;
* construcción de series comparables;
* documentación del índice militar;
* revisión del Gini y otros indicadores sociales;
* redacción sustentada de las fichas;
* localización de metodologías profesionales de visualización;
* comparación de proyecciones demográficas y económicas.

## 7. Orden definitivo de ejecución

1. Fase 1A — Diagnóstico funcional.
2. Fase 1B.1 — Confirmación de las nueve áreas.
3. Fase 1B.2 — Diccionario de indicadores.
4. Fase 1B.3 — Fuentes, fecha de corte y metodología.
5. Fase 1B.4 — Diseño de la Tabla de Datos Consolidados.
6. Fase 1B.5 — Arquitectura de contenidos.
7. Fase 1B.6 — Sistema visual inicial.
8. Fase 1B.7 — Selección de gráficas.
9. Fase 1B.8 — Plantilla de ficha.
10. Investigación avanzada y cumplimentación de datos.
11. Fase 1B.9 — Redacción de las nueve fichas.
12. Regreso a Codex para implementación.

## 8. Primera tarea inmediata

La tarea inmediata será:

### Fase 1B.1 — Confirmación de las nueve áreas

Debe partir de la aplicación actual y responder:

* cuáles son exactamente;
* qué países contiene cada una;
* qué población y superficie cubren;
* qué países quedan fuera;
* qué decisiones geopolíticas discutibles existen;
* si se conserva o ajusta la división actual.

No se buscarán todavía todos los indicadores ni se redactarán las fichas completas.
