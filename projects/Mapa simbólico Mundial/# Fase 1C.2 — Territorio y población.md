# Fase 1C.2 — Territorio y población

## Retícula Global 2025

## 1. Objetivo

Incorporar al maestro territorial los primeros datos cuantitativos necesarios para construir la Tabla de Datos Consolidados:

1. superficie terrestre;
2. población 2025;
3. porcentaje de población mundial;
4. porcentaje de superficie mundial;
5. densidad de población;
6. edad mediana;
7. población proyectada a 2050;
8. variación demográfica 2025–2050.

La fase deberá producir valores por país o territorio y agregados para las nueve áreas.

---

## 2. Fuentes

### 2.1 Población, edad mediana y proyección

Fuente principal:

**United Nations, Department of Economic and Social Affairs, Population Division — World Population Prospects 2024.**

Se utilizará el escenario medio.

Años:

* población base: 2025;
* proyección: 2050;
* edad mediana: 2025.

Los datos de 2025 y 2050 son estimaciones o proyecciones, no recuentos censales realizados exactamente en esas fechas.

### 2.2 Superficie terrestre

Fuente principal:

**FAO, distribuida mediante World Development Indicators del Banco Mundial.**

Indicador:

`AG.LND.TOTL.K2`

Definición:

Superficie terrestre en kilómetros cuadrados, excluyendo aguas interiores importantes, plataforma continental y zonas económicas exclusivas.

Año:

Se utilizará el último valor disponible por entidad, normalmente 2023.

La superficie se considera estructuralmente estable aunque el año publicado sea anterior a 2025.

---

## 3. Indicadores

| Código         | Indicador                        | Unidad     | Método                                    |
| -------------- | -------------------------------- | ---------- | ----------------------------------------- |
| `TERR_SUP`     | Superficie terrestre             | km²        | Suma                                      |
| `TERR_PCT`     | Porcentaje de superficie mundial | %          | Superficie del área / total               |
| `POB_TOTAL`    | Población 2025                   | habitantes | Suma                                      |
| `POB_PCT`      | Porcentaje de población mundial  | %          | Población del área / total                |
| `TERR_DENS`    | Densidad                         | hab./km²   | Población / superficie                    |
| `POB_EDAD`     | Edad mediana                     | años       | Cálculo agregado o aproximación ponderada |
| `POB_2050`     | Población 2050                   | habitantes | Suma                                      |
| `POB_VAR_2050` | Variación 2025–2050              | %          | `(P2050 / P2025 - 1) × 100`               |

---

## 4. Reglas de agregación

### 4.1 Superficie

La superficie de cada área será:

`Σ superficie terrestre de las entidades incluidas`

No se incluirán:

* Antártida;
* territorios sin población permanente cuando distorsionen la comparación;
* superficies marítimas;
* zonas económicas exclusivas.

Los territorios dependientes se incorporarán únicamente cuando:

* la fuente publique un valor separado;
* el territorio no esté incluido en el Estado soberano;
* no se produzca duplicidad.

### 4.2 Población

La población de cada área será:

`Σ población de las entidades incluidas`

Se comprobará especialmente el tratamiento de:

* China;
* Hong Kong;
* Macao;
* Taiwán;
* Kosovo;
* territorios dependientes.

### 4.3 Densidad

La densidad se calculará mediante:

`población total del área / superficie terrestre total del área`

No se calculará como promedio de las densidades de los países.

### 4.4 Edad mediana

La edad mediana de un conjunto no puede obtenerse mediante una media simple de las edades medianas nacionales.

Orden preferente:

1. calcularla a partir de la distribución por edades agregada de ONU WPP;
2. utilizar un agregado oficial equivalente, si existe;
3. provisionalmente, usar una media ponderada por población claramente etiquetada como aproximación.

La primera opción es la metodológicamente correcta.

### 4.5 Proyección 2050

Se sumarán las proyecciones nacionales del escenario medio.

La variación se calculará sobre los valores agregados:

`(población área 2050 / población área 2025 - 1) × 100`

No se promediarán los porcentajes nacionales.

---

## 5. Archivos de entrada

### Maestro territorial

`rg_paises_areas_operativo.csv`

### Población ONU

Archivo oficial CSV de indicadores demográficos de WPP 2024, escenario medio.

Campos necesarios:

* código M49;
* nombre;
* año;
* población total;
* edad mediana, si está incluida.

### Superficie

Descarga del indicador:

`AG.LND.TOTL.K2`

Campos necesarios:

* código ISO3;
* año;
* superficie terrestre.

---

## 6. Archivos de salida

### Datos normalizados por entidad

`rg_territorio_poblacion_pais.csv`

Columnas:

| Campo               | Contenido            |
| ------------------- | -------------------- |
| `codigo_iso3`       | Código ISO           |
| `codigo_m49`        | Código ONU           |
| `pais`              | Nombre               |
| `area_codigo`       | Área                 |
| `superficie_km2`    | Superficie terrestre |
| `anio_superficie`   | Año                  |
| `poblacion_2025`    | Habitantes           |
| `poblacion_2050`    | Habitantes           |
| `edad_mediana_2025` | Años                 |
| `fuente_superficie` | Fuente               |
| `fuente_poblacion`  | Fuente               |
| `estado_revision`   | Estado               |
| `observaciones`     | Incidencias          |

### Agregados por área

`rg_agregados_territorio_poblacion.csv`

Columnas:

| Campo                      | Contenido          |
| -------------------------- | ------------------ |
| `area_codigo`              | Área               |
| `area_nombre`              | Nombre             |
| `superficie_km2`           | Superficie         |
| `superficie_mundial_pct`   | Porcentaje mundial |
| `poblacion_2025`           | Población          |
| `poblacion_mundial_pct`    | Porcentaje mundial |
| `densidad_2025`            | Habitantes/km²     |
| `edad_mediana_2025`        | Edad               |
| `poblacion_2050`           | Proyección         |
| `variacion_2025_2050_pct`  | Variación          |
| `entidades_totales`        | Previstas          |
| `entidades_con_poblacion`  | Cubiertas          |
| `entidades_con_superficie` | Cubiertas          |
| `cobertura_poblacion_pct`  | Cobertura          |
| `observaciones`            | Notas              |

### Informe

`validacion-territorio-poblacion-1c2.md`

---

## 7. Validaciones obligatorias

### 7.1 Población mundial

La suma de las nueve áreas debe aproximarse al total mundial publicado por ONU para 2025.

Diferencia aceptable:

* inferior al 0,1 %, salvo territorios expresamente excluidos.

### 7.2 Población 2050

La suma debe aproximarse al total mundial del escenario medio para 2050.

### 7.3 Superficie

La suma no debe compararse con la superficie total del planeta, sino con la suma de superficie terrestre de las entidades incluidas.

La Antártida quedará fuera.

### 7.4 Duplicidades

Revisar:

* China, Hong Kong y Macao;
* Serbia y Kosovo;
* Francia y territorios franceses;
* Estados Unidos y sus territorios;
* Países Bajos y territorios caribeños;
* Reino Unido y dependencias.

### 7.5 Valores ausentes

Un valor ausente no se sustituirá por cero.

### 7.6 Valores anómalos

Detectar:

* población sin superficie;
* superficie sin población;
* densidades extremas;
* códigos sin correspondencia;
* valores agregados presentes en la fuente que no sean países.

---

## 8. Tratamiento de casos especiales

### China, Hong Kong y Macao

Se usarán los tres registros separados cuando ONU los publique separadamente.

Se comprobará que el total denominado China no incluya ya las regiones especiales.

### Taiwán

Se incluirá en Asia-Pacífico cuando la fuente publique un registro separado.

### Kosovo

Se incorporará únicamente si existe dato separado y no está contenido en Serbia.

### Palestina

Se incluirá en Oriente Medio con el dato de ONU.

### Territorios dependientes

Se aplicará `SEGUN_FUENTE`.

### Antártida

* visible en el mapa;
* excluida de todos los agregados de esta fase.

---

## 9. Tabla consolidada preliminar

La salida visible tendrá nueve filas:

| Área | Población 2025 | % mundial | Superficie | % superficie | Densidad | Edad mediana | Población 2050 | Variación |
| ---- | -------------: | --------: | ---------: | -----------: | -------: | -----------: | -------------: | --------: |

Esta será la primera tabla real utilizable para:

* la portada;
* el mapa;
* la página temática de territorio y población;
* las fichas de área;
* las primeras gráficas.

---

## 10. Gráficas que habilita esta fase

### Portada

* población frente a superficie.

### Página temática

* población total;
* superficie;
* densidad;
* población 2025 frente a 2050.

### Fichas

* peso demográfico y territorial del área;
* tendencia demográfica.

---

## 11. Carga en MySQL

Tras validar los CSV podrán crearse las primeras tablas físicas:

* `rg_areas`;
* `rg_paises`;
* `rg_bloques`;
* `rg_indicadores`;
* `rg_fuentes`;
* `rg_periodos`;
* `rg_datos_pais`;
* `rg_datos_area`.

Primera carga:

1. áreas;
2. países;
3. indicadores de territorio y población;
4. fuentes;
5. valores por entidad;
6. agregados por área.

---

## 12. Estado de avance

### Fase 1C.1

Maestro territorial generado, pendiente de revisión manual menor.

### Fase 1C.2

| Elemento            | Estado      |
| ------------------- | ----------- |
| Indicadores         | Definidos   |
| Fuentes             | Confirmadas |
| Métodos             | Definidos   |
| Formatos de entrada | Definidos   |
| Formatos de salida  | Definidos   |
| Descarga de datos   | Pendiente   |
| Normalización       | Pendiente   |
| Agregación          | Pendiente   |
| Validación          | Pendiente   |

### Avance de 1C.2

**30 %**

### Avance global efectivo aproximado

**10–12 %**

La fase conceptual está avanzada, pero la base estadística visible todavía no está construida.

---

## 13. Decisión

## GO para ejecutar la carga

La siguiente operación es descargar los archivos oficiales, cruzarlos con `rg_paises_areas_operativo.csv` y generar:

* `rg_territorio_poblacion_pais.csv`;
* `rg_agregados_territorio_poblacion.csv`;
* `validacion-territorio-poblacion-1c2.md`.

La Fase 1C.2 no debe cerrarse hasta que esos tres archivos existan y sus totales mundiales hayan sido comprobados.
