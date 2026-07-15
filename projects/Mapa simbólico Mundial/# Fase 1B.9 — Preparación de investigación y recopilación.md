# Fase 1B.9 — Preparación de investigación y recopilación

## Retícula Global 2025

## 1. Objetivo

Preparar la investigación necesaria para construir la primera versión real de la Tabla de Datos Consolidados y redactar las dos fichas piloto.

La fase deberá determinar:

* qué datos se recopilan primero;
* qué fuentes concretas se utilizan;
* cómo se descargan y conservan;
* cómo se asignan los países a las nueve áreas;
* cómo se calculan los agregados;
* cómo se validan;
* cómo se cargan posteriormente en MySQL;
* cómo se controla el avance;
* cuándo puede comenzar la redacción de las fichas.

Esta fase no pretende investigar todavía todos los bloques aprobados ni completar el proyecto entero.

---

# 2. Principio de ejecución

La investigación se realizará por lotes cerrados.

No se recopilarán simultáneamente:

* todos los indicadores;
* todas las fuentes;
* todas las capacidades militares cualitativas;
* toda la información energética;
* toda la dimensión tecnológica;
* todos los textos de las nueve fichas.

## Regla general

> Cada lote debe terminar con datos utilizables, agregados por área, revisados y preparados para su incorporación a la aplicación.

No se considerará avance suficiente acumular enlaces o archivos sin procesar.

---

# 3. Alcance de la primera investigación

La primera investigación se limitará a los indicadores necesarios para:

* la portada;
* la Tabla de Datos Consolidados resumida;
* las cuatro primeras páginas temáticas;
* las dos fichas piloto;
* la estructura básica de las nueve fichas.

## Indicadores iniciales

### Territorio y población

1. Superficie terrestre.
2. Población.
3. Porcentaje de población mundial.
4. Porcentaje de superficie mundial.
5. Densidad.
6. Edad mediana.
7. Población proyectada a 2050.

### Economía

8. PIB nominal.
9. Porcentaje del PIB mundial.
10. PIB por habitante.

### Desarrollo humano y desigualdad

11. IDH.
12. Gini.
13. Esperanza de vida.

### Capacidad militar

14. Gasto militar.
15. Porcentaje del gasto militar mundial.
16. Gasto militar sobre PIB.

## Ajuste de alcance

El conjunto inicial pasa de 15 a **16 indicadores**, porque el gasto militar sobre PIB es necesario para distinguir entre:

* volumen absoluto;
* peso mundial;
* esfuerzo económico relativo.

---

# 4. Lotes de investigación

## Lote 0 — Maestro territorial

### Objetivo

Crear la tabla definitiva de países y territorios asignados a las nueve áreas.

### Contenido

Para cada entidad:

* código M49;
* código ISO2;
* código ISO3;
* nombre;
* región M49;
* subregión M49;
* área Retícula Global;
* tipo de entidad;
* excepción;
* nota de asignación;
* inclusión en cálculos.

### Casos que deben quedar resueltos

* Chipre;
* Rusia;
* Bielorrusia;
* Cáucaso;
* Irán;
* Hong Kong;
* Macao;
* Taiwán;
* territorios dependientes;
* Antártida.

### Resultado

`rg_paises_areas.csv`

### Condición de cierre

* ninguna duplicidad;
* ninguna entidad sin asignación, salvo exclusión explícita;
* suma territorial razonable;
* población mundial cubierta;
* excepciones documentadas.

---

## Lote 1 — Territorio y población

### Indicadores

* superficie;
* población;
* densidad;
* porcentaje mundial;
* edad mediana;
* población a 2050.

### Fuente principal

**ONU — World Population Prospects 2024** para población, edad y proyecciones. La revisión vigente incluye estimaciones y proyecciones para países y áreas y ofrece tablas, mapas, resultados y documentación metodológica.

### Fuente territorial

* ONU M49;
* Banco Mundial para superficie terrestre, si ofrece mejor descarga homogénea;
* fuente complementaria únicamente para resolver huecos.

### Resultado

* datos nacionales;
* datos agregados por área;
* cobertura;
* años;
* fuente;
* informe de validación.

### Archivos de trabajo

* `rg_poblacion_pais.csv`
* `rg_superficie_pais.csv`
* `rg_poblacion_2050_pais.csv`
* `rg_agregados_territorio_poblacion.csv`

---

## Lote 2 — Economía

### Indicadores

* PIB nominal;
* porcentaje del PIB mundial;
* PIB por habitante.

### Fuente principal

**Banco Mundial — World Development Indicators**.

El Banco Mundial ofrece series internacionales de PIB, PIB por habitante y otros indicadores económicos, sociales y demográficos, con opciones de descarga y comparación.

### Fuente alternativa

**FMI**, cuando:

* el Banco Mundial no disponga de dato reciente;
* se quiera utilizar una estimación de 2025;
* la cobertura sea insuficiente.

### Regla de coherencia

La primera versión deberá elegir una de estas dos opciones:

#### Opción preferente

Usar el último año consolidado del Banco Mundial con cobertura suficiente.

#### Opción alternativa

Usar estimaciones FMI 2025 para todas las entidades disponibles.

No se mezclarán de forma indiscriminada PIB Banco Mundial y FMI sin registrar el origen.

### Resultado

* PIB por país;
* PIB agregado por área;
* PIB por habitante calculado;
* porcentaje mundial;
* cobertura;
* diferencias respecto de la fuente alternativa.

### Archivos

* `rg_pib_pais.csv`
* `rg_agregados_economia.csv`

---

## Lote 3 — Desarrollo humano y condiciones de vida

### Indicadores

* IDH;
* esperanza de vida.

### Fuente principal para IDH

**PNUD — Human Development Reports Data Center**.

El centro de datos del PNUD cubre 193 países y territorios y permite consultar el IDH y medidas complementarias de desigualdad, género y pobreza.

### Fuente para esperanza de vida

* ONU World Population Prospects;
* o Banco Mundial si se decide mantener un único flujo de descarga para varios indicadores.

El Banco Mundial documenta la esperanza de vida utilizando fuentes internacionales y estadísticas nacionales.

### Regla

El IDH agregado se denominará:

> IDH medio ponderado del área.

No se presentará como un valor oficial publicado para esa agrupación.

### Resultado

* IDH nacional;
* esperanza de vida;
* medias ponderadas;
* cobertura;
* advertencias.

### Archivos

* `rg_idh_pais.csv`
* `rg_esperanza_vida_pais.csv`
* `rg_agregados_desarrollo.csv`

---

## Lote 4 — Desigualdad

### Indicador

* Gini.

### Fuente principal

Banco Mundial.

### Dificultad

Alta, debido a:

* años distintos;
* falta de datos;
* diferencias entre renta y consumo;
* cambios metodológicos;
* cobertura irregular.

### Procedimiento

1. Descargar el último valor disponible por país.
2. Limitar inicialmente la búsqueda a una ventana preferente.
3. Registrar el año individual.
4. Distinguir renta y consumo cuando la fuente lo indique.
5. Calcular media ponderada por población.
6. calcular cobertura.
7. etiquetar el resultado como aproximado.

### Ventana inicial

Preferencia:

* 2022–2025.

Ampliación:

* hasta 2019 si fuese necesario para alcanzar cobertura aceptable.

### Regla de publicación

* cobertura superior al 90 %: publicación ordinaria;
* 75–90 %: advertencia;
* inferior al 75 %: no presentar como dato central sin revisión.

### Resultado

* Gini por país;
* Gini aproximado por área;
* cobertura;
* rango de años;
* lista de países sin dato.

### Archivos

* `rg_gini_pais.csv`
* `rg_agregados_gini.csv`
* `rg_informe_cobertura_gini.md`

---

## Lote 5 — Gasto militar

### Indicadores

* gasto militar;
* porcentaje mundial;
* gasto militar sobre PIB.

### Fuente principal

**SIPRI Military Expenditure Database**.

La edición publicada en 2026 contiene series comparables hasta 2025 y puede revisar valores históricos cuando aparecen mejores fuentes.

### Año recomendado

2025.

### Procedimiento

1. Descargar la base SIPRI.
2. Normalizar nombres y códigos.
3. asignar países a áreas.
4. sumar gasto militar.
5. calcular porcentaje mundial.
6. calcular gasto agregado sobre PIB agregado.
7. registrar valores ausentes o estimados.

### Regla importante

El gasto militar sobre PIB del área se calculará como:

`gasto militar agregado / PIB agregado × 100`

No como media simple de los porcentajes nacionales.

### Resultado

* gasto por país;
* agregados por área;
* porcentaje mundial;
* esfuerzo sobre PIB;
* cobertura.

### Archivos

* `rg_gasto_militar_pais.csv`
* `rg_agregados_militares.csv`

---

# 5. Investigación cualitativa militar

La investigación cualitativa sobre:

* drones;
* misiles;
* inteligencia;
* guerra electrónica;
* logística;
* industria;
* alianzas;
* capacidad de reposición;

no debe mezclarse con la primera carga estadística.

## Fase separada

Se preparará después de cerrar los cinco lotes cuantitativos.

### Motivo

Estos indicadores:

* no tienen una fuente mundial única;
* necesitan criterios;
* requieren lectura de informes;
* cambian con rapidez;
* pueden generar discusiones subjetivas.

## Resultado posterior

Una matriz piloto para:

* Europa;
* África;
* Norteamérica y Caribe;
* Rusia-Eurasia;
* China.

Solo después se ampliará a las nueve áreas.

---

# 6. Estructura de carpetas de investigación

Sin mover la aplicación actual, se recomienda preparar una carpeta documental dentro del proyecto:

```text
reticula-global/
└── data-work/
    ├── 00_metodologia/
    ├── 01_territorios/
    ├── 02_poblacion/
    ├── 03_economia/
    ├── 04_desarrollo/
    ├── 05_desigualdad/
    ├── 06_militar/
    ├── raw/
    ├── normalized/
    ├── aggregated/
    ├── validation/
    └── exports/
```

## Función de cada nivel

### `raw`

Archivos originales descargados.

No deben modificarse.

### `normalized`

Datos limpiados:

* nombres;
* códigos;
* unidades;
* años;
* valores.

### `aggregated`

Resultados por área.

### `validation`

Informes de:

* cobertura;
* duplicidades;
* huecos;
* anomalías;
* sumas mundiales;
* diferencias entre fuentes.

### `exports`

Archivos finales preparados para:

* MySQL;
* JSON;
* revisión manual;
* documentación.

## Restricción

Esta estructura es conceptual hasta verificar la carpeta real de la aplicación y el resultado del diagnóstico de Codex.

---

# 7. Formato normalizado de datos nacionales

Todos los lotes deberán transformarse a una estructura común.

## Formato propuesto

| Campo              | Contenido                  |
| ------------------ | -------------------------- |
| `codigo_iso3`      | Código del país            |
| `codigo_m49`       | Código ONU                 |
| `pais`             | Nombre normalizado         |
| `area_codigo`      | Área Retícula Global       |
| `indicador_codigo` | Código del indicador       |
| `anio`             | Año                        |
| `valor`            | Valor numérico             |
| `unidad`           | Unidad                     |
| `fuente`           | Organismo                  |
| `dataset`          | Base concreta              |
| `url_fuente`       | Referencia                 |
| `fecha_consulta`   | Fecha                      |
| `estado`           | Directo, estimado, ausente |
| `observaciones`    | Notas                      |

Este formato permitirá importar datos de fuentes distintas sin cambiar la estructura.

---

# 8. Formato de agregados por área

| Campo                    | Contenido                   |
| ------------------------ | --------------------------- |
| `area_codigo`            | Área                        |
| `indicador_codigo`       | Indicador                   |
| `anio_referencia`        | Año principal               |
| `valor`                  | Resultado                   |
| `unidad`                 | Unidad                      |
| `metodo`                 | Suma, ponderación, división |
| `paises_totales`         | Total esperado              |
| `paises_con_dato`        | Total cubierto              |
| `poblacion_cubierta_pct` | Cobertura                   |
| `anio_minimo`            | Año mínimo                  |
| `anio_maximo`            | Año máximo                  |
| `fuente_principal`       | Fuente                      |
| `version_calculo`        | Versión                     |
| `observaciones`          | Advertencia                 |

---

# 9. Proceso de trabajo de cada lote

Cada lote seguirá exactamente estas etapas:

## Etapa 1 — Descarga

* guardar archivo original;
* registrar fuente;
* registrar fecha;
* registrar versión;
* no editar el original.

## Etapa 2 — Inspección

* columnas;
* unidades;
* años;
* cobertura;
* códigos;
* valores ausentes.

## Etapa 3 — Normalización

* nombres;
* códigos ISO/M49;
* formato decimal;
* unidad;
* año;
* valores especiales.

## Etapa 4 — Asignación territorial

Relacionar cada entidad con:

* una de las nueve áreas;
* excepción;
* inclusión o exclusión.

## Etapa 5 — Agregación

Aplicar:

* suma;
* división de totales;
* media ponderada;
* cálculo específico.

## Etapa 6 — Validación

Comprobar:

* total mundial;
* cobertura;
* duplicidades;
* valores extremos;
* ausencia de ceros falsos;
* coherencia entre indicadores.

## Etapa 7 — Exportación

Generar:

* CSV normalizado;
* CSV agregado;
* informe de validación;
* SQL o archivo de carga posterior.

## Etapa 8 — Aprobación

No pasar al siguiente lote hasta validar:

* estructura;
* cobertura;
* resultado;
* utilidad didáctica.

---

# 10. Validaciones obligatorias

## 10.1 Cobertura mundial

La suma de población de las nueve áreas debe aproximarse al total mundial de la fuente.

## 10.2 Cobertura territorial

La superficie debe excluir claramente:

* Antártida;
* mares;
* zonas económicas exclusivas.

## 10.3 Suma económica

La suma de PIB de las áreas debe compararse con el total mundial de la misma fuente.

## 10.4 Suma militar

Los porcentajes de gasto militar deben aproximarse al 100 %, descontando entidades sin datos o no cubiertas.

## 10.5 Valores por habitante

Deben recalcularse desde los totales agregados.

## 10.6 Medias ponderadas

Deben mostrar:

* población cubierta;
* países incluidos;
* rango de años.

## 10.7 Excepciones

Debe revisarse especialmente:

* China/Hong Kong/Macao;
* Taiwán;
* territorios dependientes;
* Irán;
* Chipre;
* países transcontinentales.

---

# 11. Herramientas de trabajo

## Hoja de cálculo

Útil para:

* inspección;
* revisión manual;
* comparación;
* detección de errores;
* validación visual.

No será la fuente maestra definitiva.

## Python

Recomendado para:

* leer CSV y Excel;
* normalizar;
* cruzar códigos;
* agregar;
* generar informes;
* repetir cálculos.

## MySQL

Se utilizará cuando los datos estén:

* normalizados;
* validados;
* aprobados.

## Codex

Podrá ayudar en:

* creación de scripts;
* estructura SQL;
* importaciones;
* endpoints;
* pruebas.

No deberá decidir:

* asignaciones geopolíticas;
* fuentes;
* metodología;
* interpretación editorial.

---

# 12. Momento de creación de MySQL

No conviene esperar a terminar toda la investigación para crear la base.

Tampoco conviene crear ahora todas las tablas previstas.

## Propuesta

Crear la primera base física después de cerrar:

* Lote 0 — maestro territorial;
* Lote 1 — territorio y población.

### Motivo

Estos dos lotes permiten validar:

* países;
* áreas;
* códigos;
* indicadores;
* fuentes;
* datos nacionales;
* agregados;
* importación.

## Primera implantación MySQL

Tablas mínimas:

1. `rg_areas`
2. `rg_paises`
3. `rg_bloques`
4. `rg_indicadores`
5. `rg_fuentes`
6. `rg_datos_pais`
7. `rg_periodos`
8. `rg_datos_area`

Las tablas restantes se añadirán cuando exista una necesidad comprobada.

---

# 13. Carga inicial en MySQL

## Paso 1

Crear estructura.

## Paso 2

Insertar:

* nueve áreas;
* bloques;
* 16 indicadores;
* fuentes iniciales;
* periodo `RG2025_V1`.

## Paso 3

Importar maestro de países.

## Paso 4

Importar territorio y población.

## Paso 5

Calcular o importar agregados de área.

## Paso 6

Crear consulta de control.

## Endpoint de estado

Ejemplo:

```json
{
  "proyecto": "reticula-global",
  "periodo": "RG2025_V1",
  "areas": 9,
  "paises": 0,
  "indicadores_previstos": 16,
  "indicadores_con_datos": 0,
  "datos_pais": 0,
  "datos_area": 0,
  "cobertura_poblacion": null,
  "ultima_actualizacion": null,
  "estado": "preparacion"
}
```

---

# 14. Investigación avanzada

## Utilidad

La investigación avanzada sí resulta adecuada a partir de esta fase.

## Uso inmediato

* localizar descargas oficiales;
* revisar metodologías;
* resolver códigos y coberturas;
* contrastar datos dudosos;
* documentar excepciones;
* preparar textos de contexto.

## Uso posterior

* capacidades militares cualitativas;
* autonomía energética;
* inteligencia artificial;
* diferencias internas;
* fortalezas;
* vulnerabilidades;
* tendencias futuras.

## Regla

La investigación avanzada se aplicará a una tarea cerrada.

Ejemplos:

* “Obtener población 2025 y proyección 2050 de todas las entidades”.
* “Revisar cobertura del Gini de Europa”.
* “Documentar la capacidad de producción de drones de Rusia-Eurasia”.

No se utilizará una petición genérica como:

> Investigar todo sobre África.

---

# 15. Preparación de las fichas piloto

Las fichas de Europa y África no deben redactarse antes de completar todos los lotes cuantitativos iniciales.

## Momento recomendado

Después de completar:

* territorio;
* población;
* economía;
* IDH;
* Gini;
* esperanza de vida;
* gasto militar.

## Investigación adicional para cada piloto

### Europa

* envejecimiento;
* Unión Europea frente a Europa total;
* diferencias este-oeste y norte-sur;
* dependencia energética;
* fragmentación militar;
* peso tecnológico.

### África

* crecimiento demográfico;
* diferencias regionales;
* urbanización;
* pobreza y desigualdad;
* recursos;
* vulnerabilidad climática;
* fragmentación política y económica.

## Resultado

Dos fichas completas que permitan comprobar:

* longitud;
* tono;
* utilidad de la plantilla;
* funcionamiento de las comparaciones;
* necesidad real de más indicadores.

---

# 16. Entregables de la fase

## Documentos

1. `plan-investigacion-reticula-global-1b9.md`
2. `maestro-territorial-reticula-global.md`
3. `registro-fuentes-reticula-global.md`
4. `procedimiento-normalizacion-reticula-global.md`
5. `procedimiento-validacion-reticula-global.md`

## Datos

1. `rg_paises_areas.csv`
2. archivos normalizados por lote;
3. agregados por área;
4. informes de cobertura;
5. exportación para MySQL.

## Base de datos

Solo después de aprobar los lotes 0 y 1.

---

# 17. Control de avance

La preparación de investigación y primera carga representa una parte importante del bloque de datos, cuyo peso global es del 30 %.

## Distribución propuesta

| Trabajo                 | Peso dentro del bloque de datos | Peso del proyecto |
| ----------------------- | ------------------------------: | ----------------: |
| Maestro territorial     |                            10 % |               3 % |
| Territorio y población  |                            20 % |               6 % |
| Economía                |                            20 % |               6 % |
| IDH y esperanza de vida |                            15 % |             4,5 % |
| Gini                    |                            15 % |             4,5 % |
| Gasto militar           |                            15 % |             4,5 % |
| Validación conjunta     |                             5 % |             1,5 % |
| **Total**               |                       **100 %** |          **30 %** |

## Hito significativo

Al cerrar:

* maestro territorial;
* territorio y población;
* economía;

se habrá completado aproximadamente un **15 % del proyecto total** solo en datos.

No será todavía una versión visible completa, pero sí una base sólida y reutilizable.

---

# 18. Regla contra el agotamiento

## Máximo de un lote abierto

No iniciar un nuevo lote hasta:

* guardar originales;
* normalizar;
* agregar;
* validar;
* documentar;
* aprobar el anterior.

## Sin indicadores oportunistas

No incorporar un dato nuevo porque resulte interesante durante la investigación.

Se registrará en una lista:

`indicadores-candidatos-futuros.md`

## Sin fichas prematuras

No redactar textos extensos con datos provisionales.

## Sin automatización excesiva

No construir todavía:

* panel de administración;
* actualizador automático;
* importación universal;
* cuadros de mando complejos.

---

# 19. Orden definitivo de ejecución

1. Confirmar resultado del diagnóstico 1A.
2. Crear maestro territorial.
3. Recopilar territorio y población.
4. Validar agregados.
5. Crear MySQL mínimo.
6. Importar áreas, países e indicadores.
7. Importar territorio y población.
8. Crear consulta o endpoint de control.
9. Recopilar economía.
10. Recopilar IDH y esperanza de vida.
11. Recopilar Gini.
12. Recopilar gasto militar.
13. Validar los 16 indicadores.
14. Generar Tabla de Datos Consolidados inicial.
15. Redactar fichas piloto de Europa y África.
16. Revisar plantilla.
17. Preparar las siete fichas restantes.
18. Volver a Codex para la implantación funcional y visual.

---

# 20. Decisiones adoptadas

1. La investigación se realizará por lotes.
2. La primera carga tendrá 16 indicadores.
3. El maestro territorial será el primer entregable.
4. ONU WPP será la fuente demográfica principal.
5. Banco Mundial será la fuente económica y social principal.
6. PNUD será la fuente principal de IDH.
7. SIPRI será la fuente principal de gasto militar.
8. Gini se tratará como dato aproximado regional.
9. La investigación cualitativa militar se separará.
10. MySQL se creará después de territorio y población.
11. La primera base física será mínima.
12. Los archivos originales se conservarán sin modificación.
13. Cada lote tendrá informe de validación.
14. Las fichas piloto se redactarán después de la carga cuantitativa inicial.
15. Europa y África seguirán siendo los pilotos.
16. Solo habrá un lote abierto simultáneamente.
17. La investigación avanzada se aplicará a preguntas cerradas.
18. No se retomará la implantación completa en Codex hasta disponer de datos consolidados fiables.

---

# 21. Decisión final de la Fase 1B.9

## GO

La preparación de investigación queda definida.

La siguiente tarea será:

# Fase 1C.1 — Construcción del maestro territorial

## Resultado esperado

* lista exhaustiva de países y territorios;
* código M49;
* códigos ISO;
* asignación a las nueve áreas;
* excepciones;
* entidades incluidas o excluidas;
* comprobación de cobertura;
* archivo `rg_paises_areas.csv`;
* informe `maestro-territorial-reticula-global-1c1.md`.

## Papel de ChatGPT

* investigación y propuesta territorial;
* generación de la tabla;
* detección de excepciones;
* documentación metodológica.

## Papel de Codex

* revisión de la estructura existente;
* preparación posterior de scripts;
* importación y validación técnica;
* sin modificar aún la aplicación pública.
