# Fase 1B.4 — Modelo lógico de datos y Tabla de Datos Consolidados

## Retícula Global 2025

## 1. Objetivo

Diseñar la estructura lógica que permitirá almacenar, calcular, consultar y presentar los datos de Retícula Global 2025.

La estructura deberá servir para:

* mantener las nueve áreas;
* asignar países y territorios;
* registrar indicadores;
* conservar fuentes y años;
* almacenar valores nacionales;
* calcular datos consolidados por área;
* conservar versiones históricas;
* generar la portada, las fichas y las páginas temáticas;
* evitar duplicidades;
* permitir actualizaciones futuras sin rehacer la aplicación.

Esta fase define el modelo. No implica todavía crear las tablas en MySQL ni modificar la aplicación.

---

# 2. Principio general

La Tabla de Datos Consolidados no se almacenará como una única tabla ancha con una columna por indicador.

Ese diseño produciría:

* demasiadas columnas;
* dificultad para añadir indicadores;
* mezcla de datos, fuentes y años;
* problemas para conservar históricos;
* repetición de información;
* consultas poco flexibles.

Se utilizará un modelo relacional en el que:

* los indicadores se definen una sola vez;
* los valores se almacenan por país, área, año e indicador;
* las fuentes se relacionan con cada dato;
* los agregados se calculan y conservan;
* la tabla consolidada visible se genera mediante consultas.

---

# 3. Capas del modelo

El modelo tendrá cinco capas.

## 3.1 Capa territorial

Define:

* áreas;
* países;
* territorios;
* asignaciones;
* excepciones M49.

## 3.2 Capa conceptual

Define:

* bloques temáticos;
* indicadores;
* unidades;
* métodos de agregación;
* prioridades;
* niveles de visibilidad.

## 3.3 Capa documental

Define:

* fuentes;
* organismos;
* conjuntos de datos;
* enlaces;
* fechas de consulta;
* licencias;
* observaciones.

## 3.4 Capa estadística

Almacena:

* valores nacionales;
* valores territoriales;
* agregados por área;
* cobertura;
* cálculos;
* versiones.

## 3.5 Capa editorial

Almacena:

* títulos;
* resúmenes;
* textos de área;
* textos temáticos;
* explicaciones didácticas;
* advertencias;
* estados de publicación.

---

# 4. Esquema general de relaciones

Relaciones principales:

```text
rg_bloques
   │
   └── rg_indicadores
           │
           ├── rg_datos_pais
           │       ├── rg_paises
           │       └── rg_fuentes
           │
           └── rg_datos_area
                   ├── rg_areas
                   └── rg_fuentes

rg_areas
   ├── rg_paises
   ├── rg_datos_area
   ├── rg_textos_area
   └── rg_area_indicadores

rg_indicadores
   ├── rg_indicador_fuentes
   ├── rg_area_indicadores
   └── rg_textos_indicador
```

---

# 5. Tabla `rg_areas`

## Función

Registrar las nueve áreas geopolíticas.

## Campos propuestos

| Campo                 | Tipo lógico | Obligatorio | Función                        |
| --------------------- | ----------- | ----------: | ------------------------------ |
| `id`                  | entero      |          sí | Identificador interno          |
| `codigo`              | texto corto |          sí | Código único del área          |
| `slug`                | texto corto |          sí | Identificador utilizado en URL |
| `nombre`              | texto       |          sí | Nombre visible                 |
| `nombre_corto`        | texto       |          sí | Nombre resumido                |
| `descripcion`         | texto largo |          no | Definición general             |
| `criterio_asignacion` | texto largo |          no | Regla territorial              |
| `color_principal`     | texto corto |          no | Color visual                   |
| `color_secundario`    | texto corto |          no | Variante visual                |
| `orden_visual`        | entero      |          sí | Orden en interfaz              |
| `activo`              | booleano    |          sí | Si aparece en la aplicación    |
| `fecha_revision`      | fecha       |          no | Última revisión conceptual     |

## Códigos provisionales

| Código | Área                          |
| ------ | ----------------------------- |
| `EUR`  | Europa                        |
| `NAC`  | Norteamérica y Caribe         |
| `SAM`  | Sudamérica                    |
| `REU`  | Rusia y Eurasia postsoviética |
| `CHN`  | China                         |
| `SAI`  | Subcontinente indio           |
| `MDE`  | Oriente Medio                 |
| `APC`  | Asia-Pacífico                 |
| `AFR`  | África                        |

## Regla

El código y el `slug` no deberán cambiar una vez utilizados en producción, aunque se ajuste el nombre visible.

---

# 6. Tabla `rg_paises`

## Función

Registrar países y territorios utilizados en los cálculos.

## Campos propuestos

| Campo              | Tipo lógico | Obligatorio | Función                                 |
| ------------------ | ----------- | ----------: | --------------------------------------- |
| `id`               | entero      |          sí | Identificador interno                   |
| `codigo_m49`       | texto corto |          no | Código ONU M49                          |
| `codigo_iso2`      | texto corto |          no | Código ISO alfa-2                       |
| `codigo_iso3`      | texto corto |          no | Código ISO alfa-3                       |
| `nombre`           | texto       |          sí | Nombre visible                          |
| `nombre_oficial`   | texto       |          no | Nombre oficial                          |
| `region_m49`       | texto       |          no | Región ONU                              |
| `subregion_m49`    | texto       |          no | Subregión ONU                           |
| `area_id`          | entero      |          sí | Área de Retícula Global                 |
| `tipo_entidad`     | categoría   |          sí | País, territorio, región administrativa |
| `es_excepcion`     | booleano    |          sí | Si se desvía de M49                     |
| `nota_asignacion`  | texto largo |          no | Explicación de la excepción             |
| `incluir_calculos` | booleano    |          sí | Participación en agregados              |
| `activo`           | booleano    |          sí | Entidad vigente                         |
| `fecha_revision`   | fecha       |          no | Última revisión                         |

## Valores de `tipo_entidad`

* `PAIS`
* `TERRITORIO`
* `REGION_ESPECIAL`
* `ENTIDAD_ESTADISTICA`

## Casos relevantes

### Hong Kong y Macao

Se almacenarán como entidades diferenciadas.

Su inclusión en cálculos dependerá de la cobertura de cada fuente.

### Taiwán

Se almacenará como entidad estadística diferenciada dentro de Asia-Pacífico.

### Antártida

Podrá figurar para fines cartográficos, pero con:

* `incluir_calculos = false`;
* sin área asignada o con tratamiento especial.

---

# 7. Tabla `rg_bloques`

## Función

Definir los grandes grupos temáticos.

## Campos

| Campo          | Tipo lógico | Función        |
| -------------- | ----------- | -------------- |
| `id`           | entero      | Identificador  |
| `codigo`       | texto corto | Código único   |
| `nombre`       | texto       | Nombre visible |
| `descripcion`  | texto largo | Alcance        |
| `orden_visual` | entero      | Orden          |
| `activo`       | booleano    | Estado         |

## Bloques iniciales

| Código | Bloque                          |
| ------ | ------------------------------- |
| `TERR` | Territorio                      |
| `POB`  | Población                       |
| `ECO`  | Economía                        |
| `DES`  | Desigualdad y pobreza           |
| `EDU`  | Educación                       |
| `SAL`  | Sanidad y condiciones de vida   |
| `DH`   | Desarrollo humano               |
| `MIL`  | Capacidad militar y estratégica |
| `ENE`  | Energía, recursos y clima       |
| `TEC`  | Tecnología y futuro             |

---

# 8. Tabla `rg_indicadores`

## Función

Definir cada indicador una sola vez.

## Campos

| Campo                       | Tipo lógico | Obligatorio | Función                                        |
| --------------------------- | ----------- | ----------: | ---------------------------------------------- |
| `id`                        | entero      |          sí | Identificador                                  |
| `bloque_id`                 | entero      |          sí | Bloque temático                                |
| `codigo`                    | texto corto |          sí | Código único                                   |
| `nombre`                    | texto       |          sí | Nombre visible                                 |
| `nombre_corto`              | texto       |          no | Etiqueta breve                                 |
| `pregunta_didactica`        | texto       |          sí | Qué ayuda a comprender                         |
| `descripcion`               | texto largo |          no | Definición                                     |
| `unidad`                    | texto corto |          sí | Unidad visible                                 |
| `tipo_dato`                 | categoría   |          sí | Total, tasa, índice, etc.                      |
| `metodo_agregacion`         | categoría   |          sí | Suma, ponderación, cálculo                     |
| `formula`                   | texto largo |          no | Fórmula legible                                |
| `ponderador`                | texto corto |          no | Población, nacimientos, PIB, etc.              |
| `prioridad`                 | categoría   |          sí | Esencial, explicativa, estratégica, ampliación |
| `dificultad`                | categoría   |          sí | Baja, media, alta, muy alta                    |
| `nivel_portada`             | booleano    |          sí | Puede aparecer en portada                      |
| `nivel_ficha`               | booleano    |          sí | Puede aparecer en ficha                        |
| `nivel_tematica`            | booleano    |          sí | Puede aparecer en página temática              |
| `nivel_metodologia`         | booleano    |          sí | Requiere explicación metodológica              |
| `representacion_preferente` | texto       |          no | Barra, cifra, mapa, gráfica                    |
| `decimales_presentacion`    | entero      |          no | Redondeo                                       |
| `valor_minimo`              | decimal     |          no | Control                                        |
| `valor_maximo`              | decimal     |          no | Control                                        |
| `es_estimado`               | booleano    |          sí | Si suele ser una estimación                    |
| `activo`                    | booleano    |          sí | Si se recopila                                 |
| `version_inicial`           | booleano    |          sí | Si entra en primera versión                    |
| `observaciones`             | texto largo |          no | Precauciones                                   |

## Valores de `tipo_dato`

* `TOTAL`
* `PORCENTAJE`
* `MEDIA`
* `MEDIANA`
* `TASA`
* `INDICE`
* `CATEGORIA`
* `PROYECCION`
* `CALCULADO`

## Valores de `metodo_agregacion`

* `SUMA`
* `PORCENTAJE_MUNDIAL`
* `DIVISION_TOTALES`
* `MEDIA_PONDERADA`
* `MEDIANA_PAISES`
* `PONDERACION_ESPECIFICA`
* `VALOR_CUALITATIVO`
* `SIN_AGREGACION`
* `CALCULO_PERSONALIZADO`

---

# 9. Tabla `rg_fuentes`

## Función

Registrar las fuentes utilizadas.

## Campos

| Campo                  | Tipo lógico | Obligatorio | Función                        |
| ---------------------- | ----------- | ----------: | ------------------------------ |
| `id`                   | entero      |          sí | Identificador                  |
| `organismo`            | texto       |          sí | Entidad responsable            |
| `titulo`               | texto       |          sí | Base, informe o conjunto       |
| `descripcion`          | texto largo |          no | Contenido                      |
| `url_principal`        | texto largo |          no | Página principal               |
| `url_datos`            | texto largo |          no | Descarga o consulta            |
| `tipo_fuente`          | categoría   |          sí | Oficial, académica, secundaria |
| `licencia`             | texto       |          no | Condiciones de uso             |
| `fecha_publicacion`    | fecha       |          no | Fecha del conjunto             |
| `fecha_consulta`       | fecha       |          sí | Trazabilidad                   |
| `cobertura_temporal`   | texto       |          no | Años disponibles               |
| `cobertura_geografica` | texto       |          no | Países o regiones              |
| `observaciones`        | texto largo |          no | Limitaciones                   |
| `activo`               | booleano    |          sí | Uso vigente                    |

## Valores de `tipo_fuente`

* `OFICIAL_INTERNACIONAL`
* `OFICIAL_NACIONAL`
* `ACADEMICA`
* `CENTRO_ESPECIALIZADO`
* `AGREGADOR`
* `COMERCIAL`
* `PERIODISTICA`
* `OTRA`

---

# 10. Tabla `rg_indicador_fuentes`

## Función

Relacionar cada indicador con sus fuentes preferentes y alternativas.

## Campos

| Campo              | Tipo lógico | Función              |
| ------------------ | ----------- | -------------------- |
| `id`               | entero      | Identificador        |
| `indicador_id`     | entero      | Indicador            |
| `fuente_id`        | entero      | Fuente               |
| `prioridad_fuente` | entero      | Orden de preferencia |
| `es_preferente`    | booleano    | Fuente principal     |
| `observaciones`    | texto largo | Cobertura o uso      |

Esta tabla permite que:

* población use ONU como fuente principal;
* Banco Mundial actúe como alternativa;
* una fuente especializada se utilice solo para determinados países.

---

# 11. Tabla `rg_datos_pais`

## Función

Almacenar valores por país o territorio.

## Campos

| Campo               | Tipo lógico    | Obligatorio | Función                       |
| ------------------- | -------------- | ----------: | ----------------------------- |
| `id`                | entero grande  |          sí | Identificador                 |
| `pais_id`           | entero         |          sí | País o territorio             |
| `indicador_id`      | entero         |          sí | Indicador                     |
| `anio`              | entero         |          sí | Año del dato                  |
| `valor`             | decimal amplio |          no | Valor numérico normalizado    |
| `valor_texto`       | texto          |          no | Categoría o dato textual      |
| `unidad_original`   | texto          |          no | Unidad de origen              |
| `valor_original`    | texto          |          no | Valor tal como se publicó     |
| `fuente_id`         | entero         |          sí | Fuente                        |
| `tipo_procedencia`  | categoría      |          sí | Directo, estimado, calculado  |
| `estado_dato`       | categoría      |          sí | Disponible, provisional, etc. |
| `version_fuente`    | texto          |          no | Edición del conjunto          |
| `fecha_publicacion` | fecha          |          no | Fecha del dato                |
| `fecha_carga`       | fecha-hora     |          sí | Incorporación al sistema      |
| `fecha_revision`    | fecha-hora     |          no | Última comprobación           |
| `calidad`           | categoría      |          no | Alta, media, baja             |
| `observaciones`     | texto largo    |          no | Incidencias                   |
| `activo`            | booleano       |          sí | Versión vigente               |

## Restricción lógica

No debe existir más de un registro activo para la misma combinación de:

* país;
* indicador;
* año;
* fuente;
* versión.

## Valores de `estado_dato`

* `DISPONIBLE`
* `PROVISIONAL`
* `ESTIMADO`
* `AUSENTE`
* `NO_APLICABLE`
* `NO_COMPARABLE`

## Valores de `tipo_procedencia`

* `FUENTE_DIRECTA`
* `ESTIMACION_FUENTE`
* `CALCULO_RETICULA`
* `CORRECCION_MANUAL`

---

# 12. Tabla `rg_datos_area`

## Función

Almacenar los valores consolidados para cada una de las nueve áreas.

## Campos

| Campo                  | Tipo lógico    | Obligatorio | Función                    |
| ---------------------- | -------------- | ----------: | -------------------------- |
| `id`                   | entero grande  |          sí | Identificador              |
| `area_id`              | entero         |          sí | Área                       |
| `indicador_id`         | entero         |          sí | Indicador                  |
| `anio_referencia`      | entero         |          sí | Año principal              |
| `valor`                | decimal amplio |          no | Resultado numérico         |
| `valor_texto`          | texto          |          no | Categoría                  |
| `metodo_calculo`       | categoría      |          sí | Suma, media, etc.          |
| `formula_aplicada`     | texto largo    |          no | Fórmula                    |
| `paises_totales`       | entero         |          sí | Entidades previstas        |
| `paises_con_dato`      | entero         |          sí | Entidades cubiertas        |
| `poblacion_total_area` | decimal amplio |          no | Población total            |
| `poblacion_cubierta`   | decimal amplio |          no | Población con dato         |
| `porcentaje_cobertura` | decimal        |          no | Cobertura                  |
| `anio_minimo`          | entero         |          no | Año más antiguo utilizado  |
| `anio_maximo`          | entero         |          no | Año más reciente utilizado |
| `fuente_principal_id`  | entero         |          no | Fuente dominante           |
| `tipo_procedencia`     | categoría      |          sí | Cálculo o valoración       |
| `estado_dato`          | categoría      |          sí | Disponible, provisional    |
| `nivel_confianza`      | categoría      |          no | Alto, medio, bajo          |
| `fecha_calculo`        | fecha-hora     |          sí | Ejecución                  |
| `version_calculo`      | texto          |          no | Versión metodológica       |
| `observaciones`        | texto largo    |          no | Advertencias               |
| `activo`               | booleano       |          sí | Resultado vigente          |

## Clave lógica

Una combinación de:

* área;
* indicador;
* año de referencia;
* versión de cálculo

debe ser única.

---

# 13. Tabla `rg_datos_area_detalle`

## Función

Conservar qué datos nacionales participaron en cada agregado.

Es importante para reproducir y auditar los cálculos.

## Campos

| Campo              | Tipo lógico   | Función                  |
| ------------------ | ------------- | ------------------------ |
| `id`               | entero grande | Identificador            |
| `dato_area_id`     | entero        | Resultado agregado       |
| `dato_pais_id`     | entero        | Valor nacional utilizado |
| `incluido`         | booleano      | Participación            |
| `peso_aplicado`    | decimal       | Ponderación              |
| `motivo_exclusion` | texto         | Explicación              |
| `observaciones`    | texto largo   | Notas                    |

Esta tabla permite responder:

> ¿Qué países y años se utilizaron para obtener el Gini medio de África?

---

# 14. Tabla `rg_periodos`

## Función

Definir las distintas ediciones o cortes de publicación.

## Campos

| Campo            | Tipo lógico | Función                           |
| ---------------- | ----------- | --------------------------------- |
| `id`             | entero      | Identificador                     |
| `codigo`         | texto corto | Ejemplo: `RG2025_V1`              |
| `nombre`         | texto       | Nombre de la edición              |
| `fecha_corte`    | fecha       | Cierre                            |
| `ventana_inicio` | entero      | Primer año preferente             |
| `ventana_fin`    | entero      | Último año preferente             |
| `descripcion`    | texto largo | Alcance                           |
| `estado`         | categoría   | Preparación, publicado, archivado |
| `activo`         | booleano    | Edición vigente                   |

## Utilidad

Permite conservar:

* Retícula Global 2025;
* revisiones futuras;
* datos históricos;
* cambios metodológicos.

---

# 15. Relación entre datos y periodos

Puede resolverse de dos formas:

### Opción A

Añadir `periodo_id` directamente a `rg_datos_area`.

### Opción B

Crear una tabla intermedia:

`rg_periodo_datos_area`

## Recomendación

Usar `periodo_id` en `rg_datos_area`, porque simplifica:

* la publicación;
* las consultas;
* la selección de la edición vigente.

Los valores nacionales pueden mantenerse independientes del periodo, ya que una misma cifra puede utilizarse en distintas ediciones.

---

# 16. Tabla `rg_area_indicadores`

## Función

Decidir qué indicadores se muestran en cada área y en qué orden.

## Campos

| Campo                   | Tipo lógico | Función              |
| ----------------------- | ----------- | -------------------- |
| `id`                    | entero      | Identificador        |
| `area_id`               | entero      | Área                 |
| `indicador_id`          | entero      | Indicador            |
| `mostrar_portada`       | booleano    | Presencia en portada |
| `mostrar_ficha`         | booleano    | Presencia en ficha   |
| `destacado`             | booleano    | Indicador relevante  |
| `orden_visual`          | entero      | Posición             |
| `comentario_especifico` | texto       | Excepción editorial  |

Esta tabla permite destacar, por ejemplo:

* envejecimiento en Europa;
* crecimiento demográfico en África;
* autonomía energética en Rusia-Eurasia;
* capacidad tecnológica en Asia-Pacífico.

Sin alterar la estructura común de las fichas.

---

# 17. Tabla `rg_textos_area`

## Función

Almacenar los contenidos editoriales de cada área.

## Campos

| Campo              | Tipo lógico | Función                        |
| ------------------ | ----------- | ------------------------------ |
| `id`               | entero      | Identificador                  |
| `area_id`          | entero      | Área                           |
| `periodo_id`       | entero      | Edición                        |
| `seccion`          | categoría   | Resumen, economía, salud, etc. |
| `titulo`           | texto       | Título visible                 |
| `texto`            | texto largo | Contenido                      |
| `texto_breve`      | texto       | Resumen                        |
| `orden_visual`     | entero      | Posición                       |
| `estado_editorial` | categoría   | Borrador, revisado, publicado  |
| `fecha_revision`   | fecha-hora  | Control                        |
| `fuentes_resumen`  | texto largo | Referencias                    |
| `activo`           | booleano    | Publicación                    |

## Valores de `seccion`

* `RESUMEN`
* `TERRITORIO`
* `POBLACION`
* `ECONOMIA`
* `DESIGUALDAD`
* `EDUCACION`
* `SANIDAD`
* `DESARROLLO`
* `MILITAR`
* `ENERGIA`
* `TECNOLOGIA`
* `FUTURO`
* `FORTALEZAS`
* `VULNERABILIDADES`
* `DIFERENCIAS_INTERNAS`

---

# 18. Tabla `rg_textos_tema`

## Función

Almacenar contenidos de las páginas temáticas.

## Campos

| Campo              | Tipo lógico | Función                               |
| ------------------ | ----------- | ------------------------------------- |
| `id`               | entero      | Identificador                         |
| `bloque_id`        | entero      | Bloque temático                       |
| `periodo_id`       | entero      | Edición                               |
| `tipo_texto`       | categoría   | Introducción, conclusión, advertencia |
| `titulo`           | texto       | Título                                |
| `texto`            | texto largo | Contenido                             |
| `orden_visual`     | entero      | Posición                              |
| `estado_editorial` | categoría   | Estado                                |
| `fecha_revision`   | fecha-hora  | Control                               |
| `activo`           | booleano    | Publicación                           |

---

# 19. Tabla `rg_notas_metodologicas`

## Función

Guardar advertencias específicas.

## Campos

| Campo             | Tipo lógico | Función                              |
| ----------------- | ----------- | ------------------------------------ |
| `id`              | entero      | Identificador                        |
| `indicador_id`    | entero      | Indicador afectado                   |
| `area_id`         | entero      | Área, si procede                     |
| `periodo_id`      | entero      | Edición                              |
| `tipo_nota`       | categoría   | Cobertura, excepción, interpretación |
| `titulo`          | texto       | Encabezado                           |
| `texto`           | texto largo | Explicación                          |
| `nivel_aviso`     | categoría   | Informativo, atención, crítico       |
| `mostrar_publico` | booleano    | Visibilidad                          |
| `activo`          | booleano    | Estado                               |

Ejemplos:

* Gini aproximado;
* IDH ponderado;
* datos de años distintos;
* cobertura territorial incompleta;
* Taiwán;
* Hong Kong y Macao;
* capacidad militar cualitativa.

---

# 20. Tabla `rg_graficas`

## Función

Definir las gráficas sin codificarlas rígidamente en el HTML.

## Campos

| Campo                 | Tipo lógico        | Función                  |
| --------------------- | ------------------ | ------------------------ |
| `id`                  | entero             | Identificador            |
| `codigo`              | texto corto        | Identificador            |
| `titulo`              | texto              | Título                   |
| `pregunta_didactica`  | texto              | Qué explica              |
| `tipo_grafica`        | categoría          | Barras, dispersión, etc. |
| `indicador_x_id`      | entero             | Eje X                    |
| `indicador_y_id`      | entero             | Eje Y                    |
| `indicador_tamano_id` | entero             | Tamaño opcional          |
| `periodo_id`          | entero             | Edición                  |
| `nivel_visual`        | categoría          | Portada, ficha, temática |
| `orden_visual`        | entero             | Posición                 |
| `configuracion`       | texto estructurado | Opciones                 |
| `activo`              | booleano           | Estado                   |

## Tipos iniciales

* `BARRAS`
* `BARRAS_DOBLES`
* `BARRAS_APILADAS`
* `DISPERSION`
* `LINEA`
* `COMPARACION`
* `MAPA_TEMATICO`

---

# 21. Tabla `rg_importaciones`

## Función

Registrar las cargas de datos.

## Campos

| Campo                    | Tipo lógico | Función                  |
| ------------------------ | ----------- | ------------------------ |
| `id`                     | entero      | Identificador            |
| `fuente_id`              | entero      | Fuente                   |
| `archivo_origen`         | texto       | CSV, JSON, Excel         |
| `fecha_importacion`      | fecha-hora  | Momento                  |
| `registros_leidos`       | entero      | Control                  |
| `registros_insertados`   | entero      | Control                  |
| `registros_actualizados` | entero      | Control                  |
| `registros_error`        | entero      | Control                  |
| `estado`                 | categoría   | Correcto, parcial, error |
| `informe`                | texto largo | Resultado                |

Esta tabla sería útil si posteriormente se automatizan cargas.

---

# 22. Tabla `rg_validaciones`

## Función

Registrar revisiones manuales o automáticas.

## Campos

| Campo              | Tipo lógico | Función                      |
| ------------------ | ----------- | ---------------------------- |
| `id`               | entero      | Identificador                |
| `tipo_objeto`      | categoría   | Dato país, dato área, texto  |
| `objeto_id`        | entero      | Registro validado            |
| `tipo_validacion`  | categoría   | Rango, fuente, editorial     |
| `resultado`        | categoría   | Correcto, advertencia, error |
| `mensaje`          | texto largo | Explicación                  |
| `fecha_validacion` | fecha-hora  | Momento                      |
| `revisado_por`     | texto       | Persona o proceso            |

---

# 23. Tabla consolidada visible

La Tabla de Datos Consolidados será una vista generada a partir de:

* `rg_areas`;
* `rg_indicadores`;
* `rg_datos_area`;
* `rg_periodos`.

No será una tabla física independiente en la primera versión.

## Vista conceptual

`rg_v_datos_consolidados`

| Área | Indicador | Valor | Unidad | Año | Cobertura | Fuente | Advertencia |
| ---- | --------- | ----: | ------ | --: | --------: | ------ | ----------- |

## Vista resumida para portada

`rg_v_portada_areas`

Una fila por área con los indicadores esenciales:

| Área | Población | Superficie | PIB | PIB/hab. | Gini | IDH | Esperanza de vida | Gasto militar |
| ---- | --------: | ---------: | --: | -------: | ---: | --: | ----------------: | ------------: |

La vista podrá devolver también:

* color;
* `slug`;
* porcentaje mundial;
* año;
* señal de cobertura.

---

# 24. Tabla ancha auxiliar

Aunque el modelo principal sea relacional, puede ser útil generar una tabla ancha para:

* exportar a CSV;
* revisar datos;
* trabajar en Excel;
* comparar las nueve áreas;
* alimentar una gráfica externa.

Ejemplo:

`rg_export_datos_consolidados_2025.csv`

Esta tabla será un producto de exportación, no la fuente maestra.

---

# 25. Consultas principales que deberá soportar el modelo

## Portada

* obtener las nueve áreas;
* recuperar indicadores esenciales;
* mostrar porcentajes mundiales;
* ordenar áreas;
* recuperar colores y enlaces.

## Ficha de área

* obtener todos los indicadores activos;
* agruparlos por bloque;
* mostrar año, fuente y cobertura;
* recuperar textos;
* recuperar gráficas específicas.

## Página temática

* comparar las nueve áreas;
* ordenar por valor;
* mostrar diferencias;
* recuperar notas metodológicas;
* generar una o varias gráficas.

## Metodología

* consultar definición del indicador;
* fuente preferente;
* fórmula;
* cobertura;
* países incluidos;
* advertencias.

## Administración

* detectar datos ausentes;
* detectar datos antiguos;
* detectar cobertura insuficiente;
* recalcular áreas;
* revisar excepciones territoriales.

---

# 26. Reglas de integridad

## Integridad territorial

* cada país activo debe estar asignado a una sola área;
* las excepciones deben tener nota;
* no deben existir códigos ISO duplicados;
* una entidad excluida de cálculos debe indicarlo expresamente.

## Integridad de indicadores

* cada indicador debe pertenecer a un bloque;
* debe tener unidad;
* debe tener método de agregación;
* debe tener prioridad;
* debe indicar si entra en la versión inicial.

## Integridad estadística

* ningún dato numérico ausente debe almacenarse como cero;
* el año es obligatorio;
* la fuente es obligatoria;
* la unidad debe poder identificarse;
* los agregados deben conservar cobertura;
* las medias ponderadas deben identificar el ponderador.

## Integridad editorial

* los textos publicados deben corresponder a una edición;
* deben guardar fecha de revisión;
* no deben depender de cifras eliminadas o archivadas.

---

# 27. Control de versiones

## Datos nacionales

No se eliminarán físicamente cuando una fuente publique una revisión.

El registro anterior quedará:

* inactivo;
* vinculado a su versión;
* disponible para auditoría.

## Datos de área

Cada recálculo deberá generar una nueva versión si cambia:

* la metodología;
* la asignación territorial;
* la fuente;
* la cobertura;
* un valor nacional relevante.

## Textos

Los textos podrán conservar historial mediante:

* registros sucesivos;
* estado activo/inactivo;
* fecha de revisión.

No se considera necesario crear inicialmente un sistema editorial complejo.

---

# 28. Primera implementación mínima

Para evitar una base excesiva desde el principio, la primera implementación podría limitarse a:

1. `rg_areas`
2. `rg_paises`
3. `rg_bloques`
4. `rg_indicadores`
5. `rg_fuentes`
6. `rg_indicador_fuentes`
7. `rg_datos_pais`
8. `rg_periodos`
9. `rg_datos_area`
10. `rg_datos_area_detalle`
11. `rg_textos_area`
12. `rg_notas_metodologicas`

Las tablas siguientes pueden aplazarse:

* `rg_area_indicadores`;
* `rg_textos_tema`;
* `rg_graficas`;
* `rg_importaciones`;
* `rg_validaciones`.

---

# 29. Comparación con la base de datos de Corrupción

La experiencia de Corrupción es reutilizable en:

* creación de tablas;
* carga inicial;
* consultas PHP;
* uso de phpMyAdmin;
* separación entre MySQL y presentación;
* mantenimiento manual;
* vistas públicas;
* comprobación mediante endpoint de estado.

Retícula Global necesita un modelo más estructurado porque incorpora:

* datos históricos;
* indicadores múltiples;
* fuentes;
* cálculos;
* cobertura;
* versiones;
* textos explicativos.

No conviene copiar literalmente la estructura de Corrupción, pero sí reutilizar el procedimiento técnico aprendido.

---

# 30. Arquitectura de publicación recomendada

## MySQL

Fuente maestra para:

* datos nacionales;
* agregados;
* fuentes;
* textos;
* metodología.

## PHP o API mínima

Funciones:

* recuperar datos de portada;
* recuperar ficha de área;
* recuperar página temática;
* mostrar estado de la base;
* exportar JSON.

## JSON opcional

Puede generarse a partir de MySQL para:

* mejorar velocidad;
* simplificar el frontend;
* mantener una copia exportable;
* permitir pruebas locales.

## JavaScript

Se limitará a:

* interacciones;
* filtros;
* gráficas;
* mapa;
* presentación.

No deberá contener cifras estructurales escritas manualmente.

---

# 31. Endpoint de control recomendado

Siguiendo el modelo aplicado en Corrupción, sería útil disponer más adelante de:

`status.php`

Respuesta orientativa:

```json
{
  "proyecto": "reticula-global",
  "origen": "mysql",
  "areas_activas": 9,
  "paises_activos": 0,
  "indicadores_activos": 15,
  "datos_pais": 0,
  "datos_area": 0,
  "periodo_activo": "RG2025_V1",
  "ultima_actualizacion": null,
  "estado": "preparacion"
}
```

---

# 32. Riesgos del modelo

## Riesgo 1 — Exceso de tablas

Mitigación:

* implementar solo el núcleo mínimo;
* añadir tablas cuando exista una necesidad real.

## Riesgo 2 — Recopilación interminable

Mitigación:

* limitar la primera versión a 15 o 16 indicadores;
* cargar por bloques;
* publicar con niveles de cobertura claros.

## Riesgo 3 — Agregados metodológicamente débiles

Mitigación:

* separar datos oficiales de aproximaciones;
* guardar cobertura;
* mostrar advertencias;
* evitar índices sintéticos prematuros.

## Riesgo 4 — Web demasiado pesada

Mitigación:

* servir solo los datos necesarios;
* usar vistas;
* generar JSON compacto;
* limitar gráficas por página.

## Riesgo 5 — Mantenimiento complejo

Mitigación:

* una actualización general anual;
* fuentes preferentes estables;
* procedimientos de importación documentados;
* evitar automatizaciones avanzadas en la primera versión.

---

# 33. Decisiones adoptadas

1. MySQL será la fuente estructural principal.
2. Los indicadores se almacenarán en filas, no como columnas fijas.
3. Los datos nacionales y los agregados de área estarán separados.
4. Cada dato conservará año, fuente y estado.
5. Cada agregado conservará cobertura y método.
6. La Tabla de Datos Consolidados será una vista.
7. Los textos editoriales estarán separados de los datos.
8. Se conservarán versiones históricas.
9. La primera implementación utilizará un conjunto reducido de tablas.
10. Las gráficas se definirán después de conocer las necesidades reales.
11. JSON podrá utilizarse como capa de publicación.
12. La aplicación no contendrá cifras estructurales escritas directamente en JavaScript o HTML.

---

# 34. Decisión final de la Fase 1B.4

## GO

El modelo lógico es suficiente para iniciar la siguiente fase:

# Fase 1B.5 — Arquitectura de contenidos y distribución de la información

La siguiente fase decidirá:

* qué aparece en la portada;
* qué se muestra al abrir un área;
* qué información corresponde a cada página temática;
* cómo se navega entre mapa, áreas y temas;
* qué datos son visibles inicialmente;
* qué información se despliega bajo demanda;
* cómo evitar una aplicación excesivamente pesada.

La creación física de MySQL permanece aplazada hasta cerrar la arquitectura de contenidos y confirmar qué consultas necesitará realmente la web.
