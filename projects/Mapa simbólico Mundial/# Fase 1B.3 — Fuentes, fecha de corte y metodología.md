# Fase 1B.3 — Fuentes, fecha de corte y metodología

## Retícula Global 2025

## 1. Objetivo

Establecer las reglas que se utilizarán para:

* seleccionar las fuentes;
* elegir el año de cada dato;
* asignar países y territorios a las nueve áreas;
* agregar datos nacionales;
* tratar valores ausentes;
* documentar excepciones;
* calcular los indicadores regionales;
* conservar la trazabilidad;
* evitar comparaciones engañosas.

Esta fase no exige todavía recopilar todos los datos ni construir la base de datos definitiva.

Su resultado será el marco metodológico que deberá respetarse durante la recopilación y la implementación.

---

# 2. Principio general

Retícula Global 2025 debe utilizar:

1. datos comparables;
2. fuentes identificables;
3. reglas reproducibles;
4. cálculos comprensibles;
5. advertencias visibles cuando exista incertidumbre;
6. una actualización asumible para un proyecto personal.

No se buscará una falsa precisión.

El objetivo es presentar una imagen mundial suficientemente rigurosa y didáctica, no construir una base estadística equivalente a las de los organismos internacionales.

---

# 3. Fecha nominal del proyecto

El nombre visible seguirá siendo:

## Retícula Global 2025

La denominación identifica la versión conceptual del proyecto, pero no obliga a que todos los datos correspondan exactamente al año natural 2025.

La aplicación deberá diferenciar:

* nombre o edición del proyecto;
* año del dato;
* fecha de actualización de la base;
* fecha de consulta de la fuente.

## Regla propuesta

La primera edición completa se presentará como:

> **Retícula Global 2025 — Datos disponibles y revisados hasta 2026**

Esto permite incorporar:

* cifras económicas de 2025 cuando estén disponibles;
* gasto militar de 2025;
* datos sociales cuyo último valor comparable sea de 2023 o 2024;
* proyecciones demográficas procedentes de la revisión oficial vigente;
* datos energéticos o climáticos con el último año consolidado.

---

# 4. Política temporal

## 4.1 No utilizar un único año obligatorio

No se exigirá que todos los indicadores correspondan al mismo año.

Esto provocaría:

* pérdida de indicadores sociales importantes;
* uso de datos antiguos aunque existan cifras más recientes;
* numerosos huecos;
* falsa homogeneidad.

## 4.2 Año preferente

Para la primera carga se aplicará este orden:

1. dato definitivo de 2025;
2. dato definitivo de 2024;
3. último dato disponible entre 2022 y 2023;
4. dato anterior, únicamente si sigue siendo útil y se advierte;
5. estimación o proyección identificada como tal.

## 4.3 Ventana ordinaria

La ventana temporal preferente será:

> **2023–2025**

Se admitirán datos anteriores cuando:

* la fuente no publique el indicador anualmente;
* sea un indicador social con retraso estadístico;
* no exista una alternativa comparable;
* se indique claramente el año.

## 4.4 Datos futuros

Las proyecciones deberán mostrar siempre:

* año de referencia;
* horizonte;
* escenario utilizado;
* organismo responsable.

Para población en 2050 se utilizará preferentemente la variante media de **World Population Prospects 2024**, que ofrece estimaciones y proyecciones para 237 países o áreas.

---

# 5. Jerarquía de fuentes

## Nivel 1 — Fuente oficial especializada

Debe ser la opción preferente.

Ejemplos:

* ONU;
* Banco Mundial;
* FMI;
* PNUD;
* OMS;
* UNESCO;
* SIPRI;
* Agencia Internacional de la Energía;
* Global Carbon Project;
* institutos estadísticos oficiales.

## Nivel 2 — Fuente académica o centro especializado

Se utilizará cuando no exista una fuente internacional homogénea o cuando se trate de ámbitos emergentes.

Ejemplos:

* Stanford AI Index;
* centros de investigación estratégica;
* universidades;
* proyectos académicos con metodología publicada.

## Nivel 3 — Agregador o plataforma de divulgación

Puede utilizarse cuando:

* identifica claramente la fuente original;
* permite descargar datos;
* explica su tratamiento;
* facilita la comparación.

Ejemplo:

* Our World in Data.

Siempre que sea posible se almacenará también la fuente primaria en la que se apoya.

## Nivel 4 — Fuentes periodísticas o comerciales

No deben ser la fuente principal de una cifra estructural.

Podrán utilizarse para:

* explicar acontecimientos;
* describir capacidades recientes;
* contextualizar cambios;
* documentar hechos no cubiertos por bases estadísticas.

## Regla

Una cifra no debe incorporarse únicamente porque aparezca en:

* una noticia;
* una infografía sin metodología;
* una clasificación comercial;
* una página de opinión;
* una tabla sin fecha ni fuente.

---

# 6. Fuente territorial

La clasificación territorial base será **ONU M49**.

M49 asigna códigos numéricos normalizados a países, áreas y agrupaciones geográficas y se utiliza como referencia común para el procesamiento y la difusión estadística.

La tabla de países deberá guardar:

* código M49;
* código ISO alfa-3;
* nombre normalizado;
* región M49;
* subregión M49;
* área de Retícula Global;
* indicador de excepción;
* explicación de la excepción.

---

# 7. Excepciones territoriales

## 7.1 Chipre

Se asignará a Europa, aunque M49 lo sitúe en Western Asia.

Motivo:

* adscripción práctica e institucional;
* coherencia didáctica;
* excepción explícita y reproducible.

## 7.2 Rusia y Bielorrusia

Se extraerán de Europa y se incorporarán a:

> Rusia y Eurasia postsoviética.

## 7.3 Cáucaso

Armenia, Azerbaiyán y Georgia se incorporarán a:

> Rusia y Eurasia postsoviética.

Se excluyen de Oriente Medio.

## 7.4 México

Se integra en Norteamérica y Caribe.

La decisión coincide con su pertenencia M49 a Central America y con la estructura definida para esta área.

## 7.5 China, Hong Kong y Macao

Se consolidarán en el área China.

Los datos deberán evitar:

* sumar Hong Kong y Macao si el valor de China ya los incluye;
* excluirlos si la fuente presenta China continental por separado;
* mezclar series con coberturas territoriales diferentes.

Cada fuente deberá indicar su cobertura.

## 7.6 Irán

### Decisión propuesta

Irán se trasladará de Southern Asia a Oriente Medio como excepción geopolítica.

La regla queda:

> Oriente Medio = Western Asia, menos Cáucaso y Chipre, más Irán.

Razones:

* mejora la comprensión didáctica;
* su papel energético, militar y diplomático se analiza habitualmente dentro de Oriente Medio;
* evita una adscripción poco intuitiva al “Subcontinente indio”;
* la excepción queda documentada y es reproducible.

## 7.7 Taiwán

Taiwán se incorporará estadísticamente a Asia-Pacífico cuando exista una fuente separada.

Reglas:

* se conservará como unidad diferenciada;
* no se duplicará si una fuente lo integra en el total de China;
* se documentará la denominación utilizada por cada organismo;
* su inclusión será estadística y no una declaración sobre reconocimiento diplomático.

## 7.8 Territorios dependientes

Regla preferente:

> Mantener el territorio en el área geográfica que le corresponde según M49, salvo que la fuente ya lo integre en el Estado soberano.

Ejemplos:

* territorios caribeños en Norteamérica y Caribe;
* territorios oceánicos en Asia-Pacífico;
* territorios africanos en África.

Se evitará sumar dos veces:

* el dato del Estado soberano;
* el dato separado de su territorio.

## 7.9 Antártida

Se excluye de:

* población;
* economía;
* desarrollo humano;
* capacidad militar;
* comparación territorial ordinaria.

Podrá mostrarse gráficamente en el mapa sin asignación a ninguna de las nueve áreas.

---

# 8. Fuentes preferentes por bloque

## 8.1 Territorio

### Fuente preferente

* ONU M49;
* Banco Mundial;
* FAO, si fuese necesario precisar superficie terrestre.

### Regla

Usar una única definición de superficie en todas las áreas.

No mezclar:

* superficie terrestre;
* superficie total;
* zona económica exclusiva;
* aguas marítimas.

La primera versión utilizará:

> superficie terrestre o land area, en km².

---

## 8.2 Población

### Fuente preferente

**ONU — World Population Prospects 2024.**

La base ofrece estimaciones históricas y proyecciones oficiales para países y áreas y constituye la referencia principal para población actual, edad y proyecciones.

### Indicadores

* población total;
* crecimiento;
* edad mediana;
* proyección a 2050.

### Fuente secundaria

Banco Mundial, para determinados indicadores demográficos o urbanos.

---

## 8.3 Economía

### Fuente preferente

* Banco Mundial, World Development Indicators;
* FMI, cuando se necesiten estimaciones económicas más recientes;
* estadísticas nacionales, solo para completar huecos.

El Banco Mundial ofrece series internacionales de PIB, PIB por habitante y numerosos indicadores demográficos, económicos y sociales.

### Regla para PIB nominal

Usar:

> PIB en dólares estadounidenses corrientes.

### Regla para PIB PPA

Utilizarlo como indicador complementario, nunca como sustituto silencioso del PIB nominal.

### Prohibición

No sumar PIB:

* en monedas nacionales;
* en precios constantes con años base diferentes;
* nominal y PPA en una misma columna.

---

## 8.4 Desigualdad

### Fuente preferente

* Banco Mundial;
* PNUD para desarrollo ajustado por desigualdad;
* OCDE o fuentes regionales, solo como apoyo.

### Gini

Se utilizará el último dato disponible dentro de una ventana temporal definida.

Cada valor nacional deberá guardar:

* año;
* definición de ingreso o consumo;
* fuente;
* posible ruptura metodológica.

### Agregado regional

El Gini de un área no puede calcularse rigurosamente mediante una simple media de los Gini nacionales.

Para la primera versión se utilizará:

> media ponderada por población de los Gini nacionales disponibles.

Debe etiquetarse como:

> **Gini medio aproximado del área**

No como “Gini del área”.

La metodología y cobertura deberán estar visibles.

---

## 8.5 Educación

### Fuentes preferentes

* UNESCO Institute for Statistics;
* PNUD;
* Banco Mundial.

### Prioridad

Para la primera versión:

* años medios de escolarización;
* años esperados de escolarización;
* alfabetización, si la cobertura es suficiente.

Los años medios y esperados forman parte de la dimensión educativa del IDH. El PNUD define el IDH mediante salud, educación e ingresos.

---

## 8.6 Sanidad y condiciones de vida

### Fuentes preferentes

* OMS;
* Banco Mundial;
* UNICEF;
* programa conjunto OMS/UNICEF para agua y saneamiento.

### Primera versión

* esperanza de vida;
* mortalidad infantil;
* agua potable;
* saneamiento.

El Banco Mundial documenta la esperanza de vida a partir de fuentes de Naciones Unidas, oficinas nacionales y bases estadísticas internacionales.

---

## 8.7 Desarrollo humano

### Fuente preferente

**PNUD — Human Development Reports.**

El centro de datos del PNUD cubre 193 países y territorios y contiene el IDH y medidas complementarias de desigualdad, género y pobreza.

### Regla

No recalcular el IDH desde cero en la primera versión.

Se utilizarán:

* valores nacionales publicados por el PNUD;
* media ponderada por población para obtener una aproximación regional.

La cifra se denominará:

> **IDH medio ponderado del área**

No “IDH oficial del área”, salvo que el PNUD publique exactamente esa agrupación.

---

## 8.8 Capacidad militar

### Gasto militar

Fuente preferente:

**SIPRI Military Expenditure Database.**

La edición disponible en 2026 contiene series comparables hasta 2025 y se actualiza anualmente; SIPRI advierte además que los valores históricos pueden revisarse cuando aparecen fuentes mejores.

### Armas nucleares

Fuentes preferentes:

* SIPRI;
* Federation of American Scientists, como apoyo especializado.

### Industria, drones, misiles e inteligencia militar

No existe una única base internacional homogénea.

Se utilizarán:

* SIPRI;
* IISS, si se dispone de acceso;
* informes oficiales;
* centros especializados;
* documentación técnica;
* fuentes abiertas contrastadas.

### Regla

Separar:

#### Datos cuantitativos

* gasto;
* porcentaje mundial;
* gasto sobre PIB;
* número estimado de ojivas;
* producción conocida;
* exportaciones o importaciones.

#### Valoraciones cualitativas

* industria propia;
* drones;
* misiles;
* inteligencia;
* guerra electrónica;
* logística;
* alianzas;
* capacidad de reposición.

Las valoraciones cualitativas deberán mostrar:

* escala;
* criterios;
* fuentes;
* fecha;
* grado de confianza.

---

## 8.9 Energía

### Fuente preferente

**Agencia Internacional de la Energía.**

La IEA recopila y difunde estadísticas de oferta y demanda energética y las organiza en balances energéticos e indicadores especializados.

### Limitación

Parte de los datos detallados de la IEA puede requerir:

* registro;
* suscripción;
* licencia específica.

Por ello se admitirán fuentes alternativas:

* ONU;
* Banco Mundial;
* Energy Institute;
* Ember;
* Our World in Data, con fuente original documentada.

### Autonomía energética

No se expresará inicialmente mediante un único índice.

Se dividirá en variables:

1. producción energética propia;
2. consumo total;
3. importaciones netas;
4. dependencia importadora;
5. diversidad de fuentes;
6. diversidad de proveedores;
7. peso de combustibles fósiles;
8. capacidad renovable;
9. capacidad de refino o transformación;
10. minerales críticos.

### Primera aproximación visible

> **Dependencia energética exterior**

Unidad:

* porcentaje de importaciones netas respecto al consumo;
* categoría complementaria de vulnerabilidad.

La IEA trata la seguridad energética como un concepto que incluye importaciones, fiabilidad de redes, perturbaciones de suministro, riesgos geopolíticos, ciberataques y fenómenos extremos.

---

## 8.10 Emisiones y clima

### Fuente preferente

* Global Carbon Project;
* datos procesados por Our World in Data;
* fuentes de Naciones Unidas cuando corresponda.

### Primera versión

Usar:

* emisiones territoriales de CO₂ procedentes de combustibles fósiles e industria;
* emisiones totales;
* emisiones por habitante.

Las emisiones territoriales se asignan al lugar donde se producen y no incluyen las emisiones incorporadas en los bienes importados.

### Advertencia

No mezclar sin explicación:

* CO₂;
* gases de efecto invernadero;
* cambio de uso del suelo;
* emisiones de consumo;
* emisiones territoriales.

---

## 8.11 Tecnología e inteligencia artificial

### Fuente general

* Banco Mundial;
* UNESCO;
* UIT;
* OCDE;
* WIPO;
* estadísticas nacionales.

### Fuente especializada en IA

**Stanford AI Index.**

El AI Index reúne y analiza información sobre capacidad técnica, inversión, adopción, economía, gobernanza y otros aspectos del desarrollo de la inteligencia artificial.

### Indicadores de IA propuestos

No crear todavía un “índice de IA”.

Trabajar por dimensiones:

1. inversión privada en IA;
2. investigación y publicaciones;
3. modelos avanzados desarrollados;
4. capacidad de cómputo;
5. centros de datos;
6. industria de semiconductores;
7. talento;
8. adopción empresarial;
9. adopción social;
10. gobernanza y regulación.

### Primera versión

Seleccionar únicamente dos o tres indicadores con cobertura internacional suficiente:

* inversión;
* investigación;
* adopción o infraestructura.

El propio AI Index señala que la medición independiente es cada vez más importante y que existen problemas crecientes de transparencia en el sector.

---

# 9. Métodos de agregación

## 9.1 Suma

Se utilizará para:

* población;
* superficie;
* PIB;
* gasto militar;
* emisiones;
* consumo energético;
* número de ojivas;
* inversión total.

Fórmula:

`valor del área = suma de valores de los países incluidos`

## 9.2 Porcentaje mundial

Fórmula:

`valor del área / valor mundial comparable × 100`

El denominador mundial debe:

* proceder de la misma fuente;
* corresponder al mismo año;
* utilizar la misma definición.

## 9.3 Indicador por habitante

Fórmula:

`total agregado del área / población total del área`

Aplicable a:

* PIB por habitante;
* gasto militar por habitante;
* emisiones por habitante;
* consumo energético por habitante.

No se utilizará la media simple de los valores nacionales.

## 9.4 Media ponderada por población

Fórmula:

`Σ(valor nacional × población nacional) / Σ población cubierta`

Aplicable, con cautela, a:

* esperanza de vida;
* años de escolarización;
* IDH aproximado;
* alfabetización;
* Gini aproximado;
* acceso a Internet;
* agua;
* saneamiento.

## 9.5 Ponderación específica

Algunos indicadores requieren otro denominador:

* mortalidad infantil: nacimientos;
* urbanización: población;
* gasto sobre PIB: PIB agregado;
* acceso educativo: población del grupo de edad;
* dependencia energética: consumo energético.

## 9.6 Mediana

Se utilizará solo si responde a una pregunta concreta.

La mediana de países:

* describe al país intermedio;
* no describe necesariamente a la persona media del área.

No debe confundirse con una media ponderada por población.

## 9.7 Valor cualitativo

Se utilizará para:

* industria militar;
* capacidad de reposición;
* guerra electrónica;
* autonomía tecnológica;
* proyección exterior;
* inteligencia militar.

Cada escala cualitativa deberá disponer de una tabla explícita de criterios.

Ejemplo:

| Nivel | Significado                          |
| ----- | ------------------------------------ |
| 0     | Sin capacidad relevante identificada |
| 1     | Capacidad limitada y dependiente     |
| 2     | Capacidad regional parcial           |
| 3     | Capacidad regional sólida            |
| 4     | Capacidad avanzada y amplia          |
| 5     | Capacidad global o dominante         |

No se asignarán niveles por impresión general.

---

# 10. Cobertura mínima

Cada agregado debe guardar:

* número de países incluidos;
* número de países con dato;
* población cubierta;
* porcentaje de cobertura;
* año mínimo;
* año máximo.

## Regla de publicación

### Cobertura alta

Más del 90 % de la población del área.

Puede mostrarse normalmente.

### Cobertura aceptable

Entre 75 % y 90 %.

Puede mostrarse con una señal de advertencia.

### Cobertura insuficiente

Menos del 75 %.

No debe presentarse como dato representativo sin una advertencia destacada.

Para algunos indicadores territoriales o económicos podrá utilizarse cobertura por porcentaje del PIB o de la magnitud relevante, además de población.

---

# 11. Datos ausentes

## Regla general

No sustituir automáticamente un dato ausente por:

* cero;
* media mundial;
* dato de un país vecino;
* estimación no documentada.

## Estados posibles

* disponible;
* provisional;
* estimado por la fuente;
* calculado por Retícula Global;
* ausente;
* no aplicable;
* no comparable.

## Estimaciones propias

Solo se permitirán cuando:

* sean sencillas;
* estén explicadas;
* no alteren sustancialmente el resultado;
* se guarde el cálculo;
* se identifiquen visualmente.

---

# 12. Redondeo

La aplicación evitará cifras con precisión falsa.

## Reglas iniciales

### Población

* millones: un decimal;
* miles de millones: dos decimales cuando sea necesario;
* porcentajes: un decimal.

### Superficie

* millones de km²: dos decimales;
* porcentajes: un decimal.

### PIB y gasto militar

* billones o miles de millones;
* máximo dos cifras decimales;
* porcentajes: un decimal.

### PIB por habitante

* redondeo a decenas o centenas de dólares según magnitud.

### IDH

* tres decimales.

### Gini

* un decimal.

### Esperanza de vida

* un decimal.

### Emisiones por habitante

* un decimal.

La base de datos conservará el valor original con mayor precisión. El redondeo se aplicará únicamente en la presentación.

---

# 13. Trazabilidad

Cada valor deberá permitir saber:

* qué mide;
* a qué país o área corresponde;
* año;
* fuente;
* enlace;
* fecha de consulta;
* unidad original;
* valor original;
* valor transformado;
* método de agregación;
* cobertura;
* observaciones;
* responsable o proceso de carga.

## Tipos de procedencia

* `FUENTE_DIRECTA`
* `CALCULO_AREA`
* `MEDIA_PONDERADA`
* `ESTIMACION_FUENTE`
* `VALORACION_CUALITATIVA`
* `ESTIMACION_RETICULA`

---

# 14. Revisión y actualización

## Primera carga

Se realizará por bloques, no intentando completar todos los indicadores simultáneamente.

Orden:

1. territorio;
2. población;
3. economía;
4. desarrollo humano;
5. desigualdad;
6. salud;
7. gasto militar;
8. energía y emisiones;
9. tecnología e IA;
10. capacidades cualitativas.

## Revisión ordinaria

Una revisión general anual será suficiente.

## Revisión especial

Podrá actualizarse antes un bloque cuando se publique:

* nueva revisión de población;
* nueva base SIPRI;
* nuevo informe del PNUD;
* actualización económica importante;
* cambio metodológico relevante.

## Historial

No se sobrescribirán los valores antiguos.

Cada actualización deberá crear:

* un nuevo registro anual;
* o una nueva versión del dato si la fuente revisa el mismo año.

---

# 15. Primera versión y control de alcance

El diccionario completo no obliga a recopilar todo en la primera versión.

## Conjunto inicial de 15 indicadores

### Territorio y población

1. superficie;
2. población;
3. densidad;
4. porcentaje de población mundial;
5. población proyectada a 2050;
6. edad mediana.

### Economía y distribución

7. PIB nominal;
8. porcentaje del PIB mundial;
9. PIB por habitante;
10. Gini medio aproximado.

### Desarrollo y vida

11. IDH medio ponderado;
12. esperanza de vida.

### Poder y sostenibilidad

13. gasto militar;
14. porcentaje del gasto militar mundial;
15. emisiones de CO₂ por habitante.

## Autonomía energética

Se preparará desde la primera versión, pero podrá incorporarse como indicador 16 cuando se compruebe que existe una fuente suficientemente homogénea.

## Regla de contención

No se incorporará un indicador nuevo a producción hasta que tenga:

* definición;
* pregunta didáctica;
* fuente;
* año;
* fórmula;
* cobertura;
* representación;
* ubicación concreta en la web.

---

# 16. Implicaciones para la base de datos

La metodología confirma la conveniencia de utilizar MySQL.

La base deberá separar:

* países y territorios;
* áreas;
* indicadores;
* fuentes;
* valores nacionales;
* valores agregados;
* metodología;
* versiones;
* textos explicativos.

## Decisión

La creación física de las tablas se pospone hasta completar:

* Fase 1B.4 — Modelo lógico de la Tabla de Datos Consolidados.

En 1B.4 se diseñará:

* esquema relacional;
* claves;
* tipos de dato;
* relaciones;
* almacenamiento de cobertura;
* versiones;
* agregados;
* textos;
* consultas necesarias para la web.

---

# 17. Decisiones adoptadas

1. ONU M49 será la base territorial.
2. Irán se asignará a Oriente Medio como excepción.
3. Taiwán se tratará en Asia-Pacífico con registro separado.
4. Se utilizará una ventana preferente 2023–2025.
5. No se forzará un único año para todos los indicadores.
6. Cada valor mostrará su año.
7. Las fuentes oficiales y especializadas tendrán prioridad.
8. Los datos absolutos se sumarán.
9. Los valores por habitante se calcularán desde los totales agregados.
10. Los indicadores sociales se ponderarán por población cuando proceda.
11. El Gini regional será una aproximación ponderada, no un Gini real conjunto.
12. El IDH regional se presentará como media ponderada aproximada.
13. Los indicadores cualitativos deberán tener escalas explícitas.
14. Se conservará el historial.
15. La primera versión se limitará a unos quince indicadores.
16. MySQL será la base estructural prevista.

---

# 18. Decisión final de la Fase 1B.3

## GO

Puede iniciarse la Fase 1B.4 — Diseño lógico de la Tabla de Datos Consolidados.

La metodología define suficientemente:

* unidades territoriales;
* excepciones;
* jerarquía de fuentes;
* política temporal;
* métodos de agregación;
* tratamiento de datos ausentes;
* cobertura mínima;
* trazabilidad;
* redondeo;
* actualización;
* límites de la primera versión.

No debe comenzar todavía la recopilación masiva de datos ni la creación definitiva de tablas MySQL hasta aprobar el modelo lógico de 1B.4.
