# Fase 1B.2 — Diccionario inicial de indicadores

## Retícula Global 2025

## 1. Objetivo

Definir qué datos utilizará Retícula Global 2025, qué pregunta responde cada uno y en qué nivel de la aplicación debe mostrarse.

Esta fase no recopila todavía todos los valores ni fija definitivamente las fuentes. Su función es cerrar el contenido conceptual de la futura Tabla de Datos Consolidados.

## 2. Principio didáctico

Cada indicador debe cumplir al menos una de estas funciones:

* ayudar a comprender el tamaño de un área;
* explicar su peso en el mundo;
* describir las condiciones de vida de su población;
* mostrar cómo se distribuyen riqueza y oportunidades;
* explicar su capacidad estratégica;
* anticipar tendencias futuras;
* corregir percepciones simplificadas o estereotipos.

La aplicación seguirá una estructura por capas:

### Portada

Presenta una imagen inicial clara, con pocos indicadores esenciales.

### Ficha de área

Describe cada una de las nueve áreas con mayor profundidad.

### Página temática

Compara un mismo bloque de indicadores entre todas las áreas.

### Metodología

Explica fuentes, años, cálculos, limitaciones y decisiones de agregación.

## 3. Campos del diccionario

Cada indicador se documentará mediante estos campos:

| Campo                   | Contenido                                             |
| ----------------------- | ----------------------------------------------------- |
| Código                  | Identificador técnico breve                           |
| Indicador               | Nombre visible                                        |
| Pregunta didáctica      | Qué ayuda a entender                                  |
| Unidad                  | Forma de medida                                       |
| Tipo                    | Total, porcentaje, media, mediana, índice o categoría |
| Agregación              | Suma, media ponderada, cálculo derivado o valoración  |
| Nivel principal         | Portada, ficha, página temática o metodología         |
| Representación          | Cifra, barra, icono, mapa, escala o gráfica           |
| Prioridad               | Esencial, explicativa, estratégica o ampliación       |
| Dificultad metodológica | Baja, media o alta                                    |
| Observaciones           | Precauciones de interpretación                        |

---

# 4. Bloque A — Territorio

## A1. Superficie

| Campo              | Definición                                               |
| ------------------ | -------------------------------------------------------- |
| Código             | TERR_SUP                                                 |
| Pregunta didáctica | ¿Qué extensión ocupa esta área?                          |
| Unidad             | km² y porcentaje de la superficie mundial considerada    |
| Tipo               | Total y porcentaje                                       |
| Agregación         | Suma de superficies nacionales y territoriales incluidas |
| Nivel principal    | Portada, ficha y página temática                         |
| Representación     | Cifra, barra proporcional y mapa                         |
| Prioridad          | Esencial                                                 |
| Dificultad         | Baja                                                     |

Debe distinguirse entre superficie terrestre y superficie total si las fuentes incluyen aguas interiores.

## A2. Porcentaje de superficie mundial

| Campo              | Definición                                            |
| ------------------ | ----------------------------------------------------- |
| Código             | TERR_PCT                                              |
| Pregunta didáctica | ¿Qué parte del mundo ocupa?                           |
| Unidad             | %                                                     |
| Tipo               | Porcentaje derivado                                   |
| Agregación         | Superficie del área dividida por el total considerado |
| Nivel principal    | Portada y página temática                             |
| Representación     | Barra o proporción                                    |
| Prioridad          | Esencial                                              |
| Dificultad         | Baja                                                  |

## A3. Densidad de población

| Campo              | Definición                              |
| ------------------ | --------------------------------------- |
| Código             | TERR_DENS                               |
| Pregunta didáctica | ¿Está muy poblado ese territorio?       |
| Unidad             | habitantes por km²                      |
| Tipo               | Cálculo derivado                        |
| Agregación         | Población total dividida por superficie |
| Nivel principal    | Ficha y página temática                 |
| Representación     | Cifra y barra                           |
| Prioridad          | Explicativa                             |
| Dificultad         | Baja                                    |

La densidad media puede ocultar grandes espacios deshabitados y concentraciones urbanas.

---

# 5. Bloque B — Población

## B1. Población total

| Campo              | Definición                             |
| ------------------ | -------------------------------------- |
| Código             | POB_TOTAL                              |
| Pregunta didáctica | ¿Cuántas personas viven en esta área?  |
| Unidad             | habitantes y millones de habitantes    |
| Tipo               | Total                                  |
| Agregación         | Suma                                   |
| Nivel principal    | Portada, mapa, ficha y página temática |
| Representación     | Cifra destacada, barra y mapa          |
| Prioridad          | Esencial                               |
| Dificultad         | Baja                                   |

## B2. Porcentaje de población mundial

| Campo              | Definición                                        |
| ------------------ | ------------------------------------------------- |
| Código             | POB_PCT                                           |
| Pregunta didáctica | ¿Qué parte de la humanidad vive aquí?             |
| Unidad             | %                                                 |
| Tipo               | Porcentaje                                        |
| Agregación         | Población del área dividida por población mundial |
| Nivel principal    | Portada y página temática                         |
| Representación     | Barra proporcional                                |
| Prioridad          | Esencial                                          |
| Dificultad         | Baja                                              |

## B3. Crecimiento demográfico

| Campo              | Definición                                       |
| ------------------ | ------------------------------------------------ |
| Código             | POB_CREC                                         |
| Pregunta didáctica | ¿Su población crece, se estabiliza o disminuye?  |
| Unidad             | % anual                                          |
| Tipo               | Tasa                                             |
| Agregación         | Media ponderada por población o cálculo agregado |
| Nivel principal    | Ficha y página temática                          |
| Representación     | Flecha, cifra y gráfica                          |
| Prioridad          | Explicativa                                      |
| Dificultad         | Media                                            |

## B4. Población proyectada a 2050

| Campo              | Definición                                      |
| ------------------ | ----------------------------------------------- |
| Código             | POB_2050                                        |
| Pregunta didáctica | ¿Qué peso demográfico puede tener en el futuro? |
| Unidad             | habitantes y variación porcentual               |
| Tipo               | Proyección                                      |
| Agregación         | Suma de proyecciones nacionales                 |
| Nivel principal    | Ficha y página temática                         |
| Representación     | Gráfica actual–2050                             |
| Prioridad          | Estratégica                                     |
| Dificultad         | Media                                           |

## B5. Edad mediana

| Campo              | Definición                                                 |
| ------------------ | ---------------------------------------------------------- |
| Código             | POB_EDAD                                                   |
| Pregunta didáctica | ¿Es una población joven o envejecida?                      |
| Unidad             | años                                                       |
| Tipo               | Mediana                                                    |
| Agregación         | Cálculo poblacional agregado; no media simple entre países |
| Nivel principal    | Ficha y página temática                                    |
| Representación     | Cifra, escala o icono                                      |
| Prioridad          | Explicativa                                                |
| Dificultad         | Media                                                      |

## B6. Población urbana

| Campo              | Definición                                   |
| ------------------ | -------------------------------------------- |
| Código             | POB_URB                                      |
| Pregunta didáctica | ¿Qué parte de la población vive en ciudades? |
| Unidad             | %                                            |
| Tipo               | Porcentaje                                   |
| Agregación         | Media ponderada por población                |
| Nivel principal    | Ficha y página temática                      |
| Representación     | Barra                                        |
| Prioridad          | Ampliación                                   |
| Dificultad         | Baja                                         |

---

# 6. Bloque C — Economía

## C1. PIB nominal total

| Campo              | Definición                       |
| ------------------ | -------------------------------- |
| Código             | ECO_PIB                          |
| Pregunta didáctica | ¿Qué tamaño tiene su economía?   |
| Unidad             | dólares corrientes               |
| Tipo               | Total                            |
| Agregación         | Suma                             |
| Nivel principal    | Portada, ficha y página temática |
| Representación     | Cifra y barra                    |
| Prioridad          | Esencial                         |
| Dificultad         | Media                            |

## C2. Porcentaje del PIB mundial

| Campo              | Definición                                    |
| ------------------ | --------------------------------------------- |
| Código             | ECO_PIB_PCT                                   |
| Pregunta didáctica | ¿Qué parte de la economía mundial representa? |
| Unidad             | %                                             |
| Tipo               | Porcentaje                                    |
| Agregación         | PIB del área dividido por PIB mundial         |
| Nivel principal    | Portada y página temática                     |
| Representación     | Barra proporcional                            |
| Prioridad          | Esencial                                      |
| Dificultad         | Media                                         |

## C3. PIB en paridad de poder adquisitivo

| Campo              | Definición                                                     |
| ------------------ | -------------------------------------------------------------- |
| Código             | ECO_PPA                                                        |
| Pregunta didáctica | ¿Cuánto produce teniendo en cuenta las diferencias de precios? |
| Unidad             | dólares internacionales                                        |
| Tipo               | Total                                                          |
| Agregación         | Suma                                                           |
| Nivel principal    | Ficha y página temática                                        |
| Representación     | Barra comparativa con PIB nominal                              |
| Prioridad          | Explicativa                                                    |
| Dificultad         | Media                                                          |

## C4. PIB por habitante

| Campo              | Definición                                                            |
| ------------------ | --------------------------------------------------------------------- |
| Código             | ECO_PC                                                                |
| Pregunta didáctica | ¿Cuánta riqueza económica corresponde, en promedio, a cada habitante? |
| Unidad             | dólares por habitante                                                 |
| Tipo               | Cálculo derivado                                                      |
| Agregación         | PIB total del área dividido por población total                       |
| Nivel principal    | Portada, ficha y página temática                                      |
| Representación     | Cifra y barra                                                         |
| Prioridad          | Esencial                                                              |
| Dificultad         | Media                                                                 |

No debe calcularse mediante la media simple de los PIB por habitante nacionales.

## C5. Estructura económica

| Campo              | Definición                                         |
| ------------------ | -------------------------------------------------- |
| Código             | ECO_ESTR                                           |
| Pregunta didáctica | ¿De qué actividades vive principalmente esta área? |
| Unidad             | % del valor añadido                                |
| Tipo               | Distribución sectorial                             |
| Agregación         | Suma o ponderación del valor añadido               |
| Nivel principal    | Ficha y página temática                            |
| Representación     | Tres barras: agricultura, industria y servicios    |
| Prioridad          | Explicativa                                        |
| Dificultad         | Media                                              |

## C6. Comercio exterior

| Campo              | Definición                              |
| ------------------ | --------------------------------------- |
| Código             | ECO_COM                                 |
| Pregunta didáctica | ¿Qué peso tiene en el comercio mundial? |
| Unidad             | dólares y % mundial                     |
| Tipo               | Total y porcentaje                      |
| Agregación         | Suma                                    |
| Nivel principal    | Ficha y página temática                 |
| Representación     | Barra                                   |
| Prioridad          | Ampliación                              |
| Dificultad         | Media                                   |

---

# 7. Bloque D — Desigualdad y pobreza

## D1. Índice de Gini

| Campo              | Definición                                          |
| ------------------ | --------------------------------------------------- |
| Código             | DES_GINI                                            |
| Pregunta didáctica | ¿Cómo de desigualmente se reparte la renta?         |
| Unidad             | escala 0–100                                        |
| Tipo               | Índice                                              |
| Agregación         | Media ponderada por población con datos comparables |
| Nivel principal    | Ficha y página temática                             |
| Representación     | Escala, barra o semáforo continuo                   |
| Prioridad          | Esencial social                                     |
| Dificultad         | Alta                                                |

### Precauciones

* Los datos nacionales no siempre corresponden al mismo año.
* Existen diferencias metodológicas entre fuentes.
* La media regional puede ocultar países muy desiguales y otros más equilibrados.
* No debe presentarse como una medida completa de pobreza o bienestar.

## D2. Población bajo el umbral de pobreza

| Campo              | Definición                                                      |
| ------------------ | --------------------------------------------------------------- |
| Código             | DES_POBR                                                        |
| Pregunta didáctica | ¿Qué parte de la población vive con recursos muy insuficientes? |
| Unidad             | %                                                               |
| Tipo               | Porcentaje                                                      |
| Agregación         | Media ponderada por población                                   |
| Nivel principal    | Ficha y página temática                                         |
| Representación     | Barra                                                           |
| Prioridad          | Explicativa                                                     |
| Dificultad         | Alta                                                            |

Deberá decidirse si se usa pobreza internacional, pobreza nacional o ambas.

## D3. Desarrollo humano ajustado por desigualdad

| Campo              | Definición                                       |
| ------------------ | ------------------------------------------------ |
| Código             | DES_IDHI                                         |
| Pregunta didáctica | ¿Cuánto desarrollo se pierde por la desigualdad? |
| Unidad             | índice y pérdida porcentual                      |
| Tipo               | Índice                                           |
| Agregación         | Método pendiente                                 |
| Nivel principal    | Página temática y ficha                          |
| Representación     | Comparación IDH–IDH ajustado                     |
| Prioridad          | Estratégica                                      |
| Dificultad         | Alta                                             |

---

# 8. Bloque E — Educación

## E1. Alfabetización adulta

| Campo              | Definición                                              |
| ------------------ | ------------------------------------------------------- |
| Código             | EDU_ALF                                                 |
| Pregunta didáctica | ¿Qué parte de la población adulta sabe leer y escribir? |
| Unidad             | %                                                       |
| Tipo               | Porcentaje                                              |
| Agregación         | Media ponderada por población adulta                    |
| Nivel principal    | Ficha y página temática                                 |
| Representación     | Barra                                                   |
| Prioridad          | Explicativa                                             |
| Dificultad         | Media                                                   |

## E2. Años medios de escolarización

| Campo              | Definición                                                                |
| ------------------ | ------------------------------------------------------------------------- |
| Código             | EDU_MEDIA                                                                 |
| Pregunta didáctica | ¿Cuántos años de educación ha recibido, en promedio, la población adulta? |
| Unidad             | años                                                                      |
| Tipo               | Media                                                                     |
| Agregación         | Media ponderada                                                           |
| Nivel principal    | Ficha y página temática                                                   |
| Representación     | Cifra y barra                                                             |
| Prioridad          | Esencial social                                                           |
| Dificultad         | Media                                                                     |

## E3. Años esperados de escolarización

| Campo              | Definición                                                |
| ------------------ | --------------------------------------------------------- |
| Código             | EDU_ESP                                                   |
| Pregunta didáctica | ¿Cuántos años de educación puede esperar recibir un niño? |
| Unidad             | años                                                      |
| Tipo               | Estimación                                                |
| Agregación         | Media ponderada por población infantil                    |
| Nivel principal    | Ficha y página temática                                   |
| Representación     | Cifra y barra                                             |
| Prioridad          | Explicativa                                               |
| Dificultad         | Media                                                     |

## E4. Acceso a educación secundaria

| Campo              | Definición                                          |
| ------------------ | --------------------------------------------------- |
| Código             | EDU_SEC                                             |
| Pregunta didáctica | ¿Cuántos jóvenes acceden a la educación secundaria? |
| Unidad             | %                                                   |
| Tipo               | Tasa                                                |
| Agregación         | Media ponderada                                     |
| Nivel principal    | Ficha                                               |
| Representación     | Barra                                               |
| Prioridad          | Ampliación                                          |
| Dificultad         | Media                                               |

---

# 9. Bloque F — Sanidad y condiciones de vida

## F1. Esperanza de vida

| Campo              | Definición                                     |
| ------------------ | ---------------------------------------------- |
| Código             | SAL_VIDA                                       |
| Pregunta didáctica | ¿Cuántos años puede esperar vivir una persona? |
| Unidad             | años                                           |
| Tipo               | Media                                          |
| Agregación         | Media ponderada por población                  |
| Nivel principal    | Portada, ficha y página temática               |
| Representación     | Cifra y barra                                  |
| Prioridad          | Esencial social                                |
| Dificultad         | Baja                                           |

## F2. Mortalidad infantil

| Campo              | Definición                                     |
| ------------------ | ---------------------------------------------- |
| Código             | SAL_INF                                        |
| Pregunta didáctica | ¿Cuántos niños mueren antes de cumplir un año? |
| Unidad             | muertes por cada 1.000 nacidos vivos           |
| Tipo               | Tasa                                           |
| Agregación         | Media ponderada por nacimientos                |
| Nivel principal    | Ficha y página temática                        |
| Representación     | Barra invertida                                |
| Prioridad          | Explicativa                                    |
| Dificultad         | Media                                          |

## F3. Gasto sanitario por habitante

| Campo              | Definición                                          |
| ------------------ | --------------------------------------------------- |
| Código             | SAL_GASTO                                           |
| Pregunta didáctica | ¿Cuántos recursos económicos se dedican a la salud? |
| Unidad             | dólares por habitante                               |
| Tipo               | Cálculo                                             |
| Agregación         | Gasto total dividido por población                  |
| Nivel principal    | Ficha y página temática                             |
| Representación     | Barra                                               |
| Prioridad          | Ampliación                                          |
| Dificultad         | Media                                               |

## F4. Cobertura sanitaria

| Campo              | Definición                                                     |
| ------------------ | -------------------------------------------------------------- |
| Código             | SAL_COB                                                        |
| Pregunta didáctica | ¿Puede la población acceder a servicios sanitarios esenciales? |
| Unidad             | índice o %                                                     |
| Tipo               | Índice                                                         |
| Agregación         | Pendiente                                                      |
| Nivel principal    | Ficha y página temática                                        |
| Representación     | Escala                                                         |
| Prioridad          | Estratégica                                                    |
| Dificultad         | Alta                                                           |

## F5. Acceso a agua potable

| Campo              | Definición                                         |
| ------------------ | -------------------------------------------------- |
| Código             | VIDA_AGUA                                          |
| Pregunta didáctica | ¿Qué parte de la población dispone de agua segura? |
| Unidad             | %                                                  |
| Tipo               | Porcentaje                                         |
| Agregación         | Media ponderada                                    |
| Nivel principal    | Ficha y página temática                            |
| Representación     | Barra                                              |
| Prioridad          | Explicativa                                        |
| Dificultad         | Baja                                               |

## F6. Acceso a saneamiento

| Campo              | Definición                                                  |
| ------------------ | ----------------------------------------------------------- |
| Código             | VIDA_SAN                                                    |
| Pregunta didáctica | ¿Qué parte de la población dispone de saneamiento adecuado? |
| Unidad             | %                                                           |
| Tipo               | Porcentaje                                                  |
| Agregación         | Media ponderada                                             |
| Nivel principal    | Ficha y página temática                                     |
| Representación     | Barra                                                       |
| Prioridad          | Explicativa                                                 |
| Dificultad         | Baja                                                        |

---

# 10. Bloque G — Desarrollo humano

## G1. Índice de Desarrollo Humano

| Campo              | Definición                                                             |
| ------------------ | ---------------------------------------------------------------------- |
| Código             | DH_IDH                                                                 |
| Pregunta didáctica | ¿Qué nivel combinado de salud, educación e ingresos alcanza esta área? |
| Unidad             | índice 0–1                                                             |
| Tipo               | Índice                                                                 |
| Agregación         | Media ponderada por población o cálculo equivalente                    |
| Nivel principal    | Portada, ficha y página temática                                       |
| Representación     | Escala y barra                                                         |
| Prioridad          | Esencial                                                               |
| Dificultad         | Alta                                                                   |

Debe explicarse que el IDH resume dimensiones distintas y no describe por sí solo la desigualdad ni la calidad institucional.

## G2. Clasificación de desarrollo humano

| Campo              | Definición                                    |
| ------------------ | --------------------------------------------- |
| Código             | DH_NIVEL                                      |
| Pregunta didáctica | ¿En qué nivel general de desarrollo se sitúa? |
| Unidad             | categoría                                     |
| Tipo               | Clasificación                                 |
| Agregación         | Derivada del indicador anterior               |
| Nivel principal    | Ficha                                         |
| Representación     | Etiqueta                                      |
| Prioridad          | Explicativa                                   |
| Dificultad         | Media                                         |

---

# 11. Bloque H — Capacidad militar y estratégica

## H1. Gasto militar total

| Campo              | Definición                          |
| ------------------ | ----------------------------------- |
| Código             | MIL_GASTO                           |
| Pregunta didáctica | ¿Cuántos recursos dedica a defensa? |
| Unidad             | dólares                             |
| Tipo               | Total                               |
| Agregación         | Suma                                |
| Nivel principal    | Portada, ficha y página temática    |
| Representación     | Cifra y barra                       |
| Prioridad          | Esencial estratégica                |
| Dificultad         | Media                               |

## H2. Porcentaje del gasto militar mundial

| Campo              | Definición                                      |
| ------------------ | ----------------------------------------------- |
| Código             | MIL_PCT                                         |
| Pregunta didáctica | ¿Qué parte del gasto militar mundial concentra? |
| Unidad             | %                                               |
| Tipo               | Porcentaje                                      |
| Agregación         | Gasto del área dividido por el total mundial    |
| Nivel principal    | Portada y página temática                       |
| Representación     | Barra                                           |
| Prioridad          | Esencial estratégica                            |
| Dificultad         | Media                                           |

## H3. Gasto militar sobre PIB

| Campo              | Definición                                         |
| ------------------ | -------------------------------------------------- |
| Código             | MIL_PIB                                            |
| Pregunta didáctica | ¿Qué esfuerzo económico relativo dedica a defensa? |
| Unidad             | % del PIB                                          |
| Tipo               | Porcentaje                                         |
| Agregación         | Gasto militar total dividido por PIB total         |
| Nivel principal    | Ficha y página temática                            |
| Representación     | Barra                                              |
| Prioridad          | Explicativa                                        |
| Dificultad         | Media                                              |

## H4. Capacidad nuclear

| Campo              | Definición                                     |
| ------------------ | ---------------------------------------------- |
| Código             | MIL_NUC                                        |
| Pregunta didáctica | ¿Dispone de armas nucleares y en qué magnitud? |
| Unidad             | número estimado de ojivas y categoría          |
| Tipo               | Total estimado                                 |
| Agregación         | Suma                                           |
| Nivel principal    | Ficha y página temática                        |
| Representación     | Cifra, símbolo y escala                        |
| Prioridad          | Estratégica                                    |
| Dificultad         | Alta                                           |

## H5. Industria militar propia

| Campo              | Definición                                                      |
| ------------------ | --------------------------------------------------------------- |
| Código             | MIL_IND                                                         |
| Pregunta didáctica | ¿Puede producir de forma autónoma sistemas militares avanzados? |
| Unidad             | categoría                                                       |
| Tipo               | Valoración cualitativa                                          |
| Agregación         | Metodología pendiente                                           |
| Nivel principal    | Ficha                                                           |
| Representación     | Escala de niveles                                               |
| Prioridad          | Estratégica                                                     |
| Dificultad         | Alta                                                            |

## H6. Capacidad de proyección

| Campo              | Definición                                                |
| ------------------ | --------------------------------------------------------- |
| Código             | MIL_PROY                                                  |
| Pregunta didáctica | ¿Puede actuar militarmente fuera de su entorno inmediato? |
| Unidad             | categoría                                                 |
| Tipo               | Índice cualitativo                                        |
| Agregación         | Metodología pendiente                                     |
| Nivel principal    | Ficha y página temática                                   |
| Representación     | Escala                                                    |
| Prioridad          | Estratégica                                               |
| Dificultad         | Alta                                                      |

## H7. Índice militar sintético

| Campo              | Definición                              |
| ------------------ | --------------------------------------- |
| Código             | MIL_INDEX                               |
| Pregunta didáctica | ¿Cuál es su capacidad militar conjunta? |
| Unidad             | índice propio                           |
| Tipo               | Índice sintético                        |
| Agregación         | Fórmula pendiente                       |
| Nivel principal    | Portada, solo si resulta transparente   |
| Representación     | Escala                                  |
| Prioridad          | Pendiente                               |
| Dificultad         | Muy alta                                |

### Decisión provisional

No debe utilizarse hasta definir una metodología comprensible, reproducible y no basada únicamente en presupuesto militar.

---

# 12. Bloque I — Energía, recursos y clima

## I1. Consumo de energía primaria

| Campo              | Definición                         |
| ------------------ | ---------------------------------- |
| Código             | ENE_CONS                           |
| Pregunta didáctica | ¿Cuánta energía utiliza esta área? |
| Unidad             | TWh o exajulios                    |
| Tipo               | Total                              |
| Agregación         | Suma                               |
| Nivel principal    | Ficha y página temática            |
| Representación     | Barra                              |
| Prioridad          | Estratégica                        |
| Dificultad         | Media                              |

## I2. Consumo energético por habitante

| Campo              | Definición                              |
| ------------------ | --------------------------------------- |
| Código             | ENE_PC                                  |
| Pregunta didáctica | ¿Cuánta energía se utiliza por persona? |
| Unidad             | energía por habitante                   |
| Tipo               | Cálculo                                 |
| Agregación         | Consumo total dividido por población    |
| Nivel principal    | Ficha y página temática                 |
| Representación     | Barra                                   |
| Prioridad          | Explicativa                             |
| Dificultad         | Media                                   |

## I3. Emisiones de CO₂ totales

| Campo              | Definición                                                |
| ------------------ | --------------------------------------------------------- |
| Código             | CLI_CO2                                                   |
| Pregunta didáctica | ¿Cuánto contribuye actualmente a las emisiones mundiales? |
| Unidad             | toneladas de CO₂                                          |
| Tipo               | Total                                                     |
| Agregación         | Suma                                                      |
| Nivel principal    | Ficha y página temática                                   |
| Representación     | Barra                                                     |
| Prioridad          | Estratégica                                               |
| Dificultad         | Media                                                     |

## I4. Emisiones de CO₂ por habitante

| Campo              | Definición                                  |
| ------------------ | ------------------------------------------- |
| Código             | CLI_CO2_PC                                  |
| Pregunta didáctica | ¿Cuánto emite, en promedio, cada habitante? |
| Unidad             | toneladas por habitante                     |
| Tipo               | Cálculo                                     |
| Agregación         | Emisiones totales divididas por población   |
| Nivel principal    | Ficha y página temática                     |
| Representación     | Barra                                       |
| Prioridad          | Estratégica                                 |
| Dificultad         | Media                                       |

## I5. Participación de combustibles fósiles

| Campo              | Definición                                         |
| ------------------ | -------------------------------------------------- |
| Código             | ENE_FOS                                            |
| Pregunta didáctica | ¿Qué dependencia tiene del carbón, petróleo y gas? |
| Unidad             | % del consumo energético                           |
| Tipo               | Porcentaje                                         |
| Agregación         | Cálculo energético agregado                        |
| Nivel principal    | Ficha                                              |
| Representación     | Barra apilada                                      |
| Prioridad          | Ampliación                                         |
| Dificultad         | Media                                              |

## I6. Vulnerabilidad climática

| Campo              | Definición                                                                    |
| ------------------ | ----------------------------------------------------------------------------- |
| Código             | CLI_VUL                                                                       |
| Pregunta didáctica | ¿Qué exposición y capacidad de respuesta presenta frente al cambio climático? |
| Unidad             | índice                                                                        |
| Tipo               | Índice                                                                        |
| Agregación         | Metodología pendiente                                                         |
| Nivel principal    | Ficha y página temática                                                       |
| Representación     | Escala                                                                        |
| Prioridad          | Estratégica                                                                   |
| Dificultad         | Alta                                                                          |

---

# 13. Bloque J — Tecnología y futuro

## J1. Acceso a Internet

| Campo              | Definición                                 |
| ------------------ | ------------------------------------------ |
| Código             | TEC_NET                                    |
| Pregunta didáctica | ¿Qué parte de la población está conectada? |
| Unidad             | %                                          |
| Tipo               | Porcentaje                                 |
| Agregación         | Media ponderada por población              |
| Nivel principal    | Ficha y página temática                    |
| Representación     | Barra                                      |
| Prioridad          | Explicativa                                |
| Dificultad         | Baja                                       |

## J2. Investigación y desarrollo

| Campo              | Definición                                              |
| ------------------ | ------------------------------------------------------- |
| Código             | TEC_ID                                                  |
| Pregunta didáctica | ¿Qué esfuerzo dedica a crear conocimiento y tecnología? |
| Unidad             | % del PIB                                               |
| Tipo               | Porcentaje                                              |
| Agregación         | Gasto agregado dividido por PIB agregado                |
| Nivel principal    | Ficha y página temática                                 |
| Representación     | Barra                                                   |
| Prioridad          | Estratégica                                             |
| Dificultad         | Media                                                   |

## J3. Peso tecnológico

| Campo              | Definición                                                   |
| ------------------ | ------------------------------------------------------------ |
| Código             | TEC_PESO                                                     |
| Pregunta didáctica | ¿Qué capacidad tiene para desarrollar tecnologías avanzadas? |
| Unidad             | índice compuesto                                             |
| Tipo               | Índice                                                       |
| Agregación         | Metodología pendiente                                        |
| Nivel principal    | Ficha                                                        |
| Representación     | Escala                                                       |
| Prioridad          | Pendiente                                                    |
| Dificultad         | Muy alta                                                     |

No debe incorporarse inicialmente sin una metodología sólida.

---

# 14. Indicadores propuestos para la portada

La portada no debe mostrar todo el diccionario.

## Núcleo mínimo

1. Población total.
2. Porcentaje de población mundial.
3. Superficie.
4. Porcentaje de superficie mundial.
5. PIB total.
6. PIB por habitante.
7. Porcentaje del PIB mundial.
8. Gasto militar o porcentaje del gasto militar mundial.
9. IDH.
10. Esperanza de vida.

## Núcleo ampliado opcional

11. Gini.
12. Población proyectada a 2050.
13. Emisiones totales.
14. Emisiones por habitante.

La selección final dependerá de la claridad de la portada y de su funcionamiento en móvil.

---

# 15. Indicadores prioritarios para las fichas de área

Cada ficha debería contener, como mínimo:

* población;
* superficie;
* densidad;
* crecimiento demográfico;
* edad mediana;
* PIB total;
* PIB por habitante;
* estructura económica;
* Gini;
* IDH;
* esperanza de vida;
* educación;
* mortalidad infantil;
* gasto militar;
* capacidad nuclear;
* energía;
* emisiones;
* tendencia de población a 2050.

También deberá incorporar una explicación de las diferencias internas entre los países que forman el área.

---

# 16. Páginas temáticas propuestas

## 16.1 Territorio y población

Indicadores:

* superficie;
* población;
* densidad;
* crecimiento;
* urbanización;
* edad mediana;
* proyección a 2050.

## 16.2 Economía

Indicadores:

* PIB nominal;
* PIB PPA;
* PIB por habitante;
* peso mundial;
* estructura económica;
* comercio.

## 16.3 Desigualdad y pobreza

Indicadores:

* Gini;
* pobreza;
* IDH ajustado por desigualdad;
* comparación entre renta media y distribución.

## 16.4 Educación

Indicadores:

* alfabetización;
* años medios de escolarización;
* años esperados;
* secundaria.

## 16.5 Sanidad y condiciones de vida

Indicadores:

* esperanza de vida;
* mortalidad infantil;
* gasto sanitario;
* cobertura;
* agua;
* saneamiento.

## 16.6 Desarrollo humano

Indicadores:

* IDH;
* IDH ajustado por desigualdad;
* educación;
* salud;
* renta.

## 16.7 Capacidad militar

Indicadores:

* gasto total;
* porcentaje mundial;
* esfuerzo sobre PIB;
* capacidad nuclear;
* industria propia;
* proyección exterior.

## 16.8 Energía y clima

Indicadores:

* consumo energético;
* consumo por habitante;
* emisiones totales;
* emisiones por habitante;
* dependencia fósil;
* vulnerabilidad climática.

## 16.9 Tecnología y futuro

Indicadores:

* acceso a Internet;
* investigación y desarrollo;
* estructura demográfica futura;
* capacidad tecnológica, cuando exista metodología.

---

# 17. Indicadores aplazados

Quedan fuera de la primera recopilación, aunque permanecen en el modelo:

* índice militar sintético;
* calidad institucional;
* calidad educativa;
* cobertura sanitaria compuesta;
* peso tecnológico;
* recursos estratégicos;
* vulnerabilidad climática agregada;
* autonomía energética;
* capacidad de proyección militar;
* industria militar propia cuantificada.

Estos indicadores requieren una definición metodológica específica antes de presentarse como cifras comparables.

---

# 18. Prioridad de recopilación

## Prioridad 1 — Base de la Tabla de Datos Consolidados

* superficie;
* población;
* porcentaje mundial de población;
* densidad;
* PIB nominal;
* porcentaje del PIB mundial;
* PIB por habitante;
* IDH;
* esperanza de vida;
* gasto militar;
* porcentaje del gasto militar mundial.

## Prioridad 2 — Perfil social y demográfico

* crecimiento demográfico;
* proyección a 2050;
* edad mediana;
* población urbana;
* Gini;
* años medios de escolarización;
* mortalidad infantil;
* acceso a agua y saneamiento.

## Prioridad 3 — Explicación estratégica

* PIB PPA;
* estructura económica;
* capacidad nuclear;
* gasto militar sobre PIB;
* energía;
* emisiones totales;
* emisiones por habitante;
* investigación y desarrollo.

## Prioridad 4 — Indicadores complejos

* pobreza comparable;
* IDH ajustado por desigualdad;
* cobertura sanitaria;
* vulnerabilidad climática;
* peso tecnológico;
* índices militares cualitativos.

---

# 19. Decisiones propuestas para validación

## Propuesta 1

Aprobar como indicadores esenciales iniciales:

* población;
* superficie;
* PIB total;
* PIB por habitante;
* peso económico mundial;
* gasto militar;
* IDH;
* esperanza de vida.

## Propuesta 2

Incluir Gini como indicador social fundamental, pero no necesariamente en la primera visualización de portada.

## Propuesta 3

Incluir educación y sanidad mediante indicadores concretos, no mediante valoraciones genéricas de “buena” o “mala”.

## Propuesta 4

Mantener separados:

* tamaño económico;
* riqueza por habitante;
* desigualdad.

No deben resumirse en una única idea de área rica o pobre.

## Propuesta 5

No crear todavía un índice militar único.

## Propuesta 6

Incluir desde el principio una dimensión de futuro:

* población a 2050;
* edad mediana;
* emisiones;
* energía.

## Propuesta 7

Limitar la portada a un máximo aproximado de diez indicadores visibles simultáneamente por área.

## Propuesta 8

Conservar todos los demás indicadores para fichas, páginas temáticas y metodología.

---

# 20. Decisión de cierre de la Fase 1B.2

La Fase 1B.2 podrá considerarse cerrada cuando se valide:

1. la división de indicadores por bloques;
2. los indicadores esenciales;
3. los indicadores sociales prioritarios;
4. los indicadores estratégicos;
5. los indicadores aplazados por dificultad metodológica;
6. la selección preliminar para portada;
7. la estructura de fichas y páginas temáticas.

Después se iniciará:

# Fase 1B.3 — Fuentes, fecha de corte y metodología

Esta fase deberá determinar:

* año de referencia;
* fuente principal por indicador;
* método de agregación;
* tratamiento de datos ausentes;
* medias ponderadas;
* territorios dependientes;
* Taiwán;
* Irán;
* redondeo;
* trazabilidad;
* periodicidad de actualización.
