# Fase 1D.1 — Diagnóstico técnico y contrato de datos para conectar la web con MySQL

Fecha: 20 de julio de 2026  
Proyecto: Retícula Global 2025 / Mapa simbólico mundial  
Estado: diagnóstico y diseño; sin implantación

## 1. Resultado ejecutivo

La primera edición de datos está preparada para ser publicada mediante una API PHP de solo lectura. El modelo normalizado permite obtener las nueve áreas, ocho bloques, 27 indicadores y 243 valores de área sin modificar MySQL.

La entrada local validada es `Mapa simbolico v5.html`. Es un prototipo autónomo: contiene HTML, CSS y JavaScript en el mismo archivo, usa Tailwind CSS y Chart.js desde CDN y presenta una retícula, dos gráficas y una matriz con datos estáticos. No consume una API. Su rótulo “10 Áreas” y sus valores de demostración no corresponden a la edición congelada de nueve áreas, por lo que no deben tratarse como datos de producción.

No existe un `public_html` del Mapa simbólico mundial dentro de `sites/support`, ni se ha identificado en este proyecto una API PHP o configuración de base de datos existente. El `public_html` adyacente de NHMA contiene una página predeterminada de Hostinger y no determina todavía el destino de despliegue. Antes de implantar 1D.2 hay que fijar el dominio o subdirectorio público real y comprobar que PHP dispone de PDO MySQL.

Se recomienda **GO condicionado para 1D.2**: puede construirse y probarse localmente el núcleo de conexión y el endpoint de estado, pero no desplegarlo hasta confirmar la raíz pública, la ubicación privada de secretos y un usuario MySQL con privilegios exclusivamente `SELECT`.

## 2. Estado actual verificado

La edición congelada y validada es:

| Elemento | Estado |
|---|---:|
| Periodo | `RG2025_V1` |
| Nombre | Retícula Global 2025 — Primera edición |
| Estado MySQL | `congelado` |
| Activo | 1 |
| Áreas activas | 9 |
| Países y territorios activos | 244 |
| Bloques activos | 8 |
| Indicadores activos | 27 |
| Registros activos de área | 243 |
| Registros esperados por indicador | 9 |
| Duplicidades activas | 0 |
| Datos activos sin fuente | 0 |

La Fase 1C.9 dejó `rg_v_datos_consolidados` sin cambios y documentó, sin crearla, una posible `rg_v_primera_edicion`. El periodo no dispone de fecha de cierre ni observaciones en la tabla; esa información permanece en documentación.

## 3. Inventario relevante revisado

### 3.1 Aplicación y presentación

- `Mapa simbolico v1.html` a `Mapa simbolico v5.html`: prototipos históricos autónomos.
- `Mapa simbolico v5.html`: entrada local validada en la Fase 1A y candidata a base de integración.
- Componentes actuales en v5:
  - retícula esquemática de áreas con interacción local;
  - gráfica de dispersión `scatterChart`;
  - gráfica de barras `barChart`;
  - “Matriz de Datos Consolidados (10 Áreas)” estática;
  - modal/visor documental simulado;
  - estilos y lógica embebidos.
- Dependencias externas: Tailwind CSS por CDN, Chart.js por CDN y Google Fonts.
- No se detectaron `fetch`, `XMLHttpRequest`, endpoints ni carga dinámica de datos.
- No hay archivos JavaScript o CSS separados específicos de esta aplicación.

### 3.2 PHP, despliegue y configuración

- No hay archivos PHP en `sites/support` vinculados a Retícula Global.
- No hay configuración de base de datos del proyecto.
- No hay `public_html` propio dentro de `sites/support`.
- Se revisó el `public_html` adyacente de NHMA: su `default.php` es la página de bienvenida de Hostinger, no un patrón de aplicación reutilizable.
- Como referencia externa a Support, `sites/staging/projects/corrupcion/api/` demuestra un patrón PHP/PDO funcional: respuestas JSON, `strict_types`, `utf8mb4`, excepciones PDO, `FETCH_ASSOC` y emulación de consultas preparadas desactivada. Es reutilizable conceptualmente, pero no debe copiarse sin corregir dos aspectos:
  - no devolver mensajes internos de excepciones al cliente;
  - no dejar el archivo de credenciales dentro de una carpeta públicamente direccionable.

### 3.3 Modelo, SQL y documentación

Se revisaron el modelo lógico de 1B.4, el esquema mínimo, las cargas y comprobaciones 1C, la auditoría integral 26, la congelación 27, el cierre 1C.9 y la propuesta de vista de primera edición.

Tablas relevantes:

| Tabla | Uso en la futura API |
|---|---|
| `rg_periodos` | edición activa y estado de congelación |
| `rg_areas` | catálogo y orden visual de las nueve áreas |
| `rg_bloques` | ocho bloques temáticos |
| `rg_indicadores` | catálogo, unidad y descripción de los 27 indicadores |
| `rg_datos_area` | valor, periodo, año, cobertura, método y observaciones |
| `rg_fuentes` | fuente principal, tipo y URL |
| `rg_paises` | conteo de entidades; no es necesario para la primera tabla de área |
| `rg_datos_pais` | detalle/recalculabilidad futura; no debe exponerse en 1D.2 |

Vistas existentes:

- `rg_v_datos_consolidados`: expone área, indicador, valor, unidad, año, método, cobertura y observaciones para filas activas.
- `rg_v_portada_territorio_poblacion`: resumen especializado de territorio y población.

Limitación principal: `rg_v_datos_consolidados` no incluye periodo, bloque, fuente principal, años mínimo/máximo ni estados de los catálogos. Además, filtra por `rg_datos_area.activo=1`, pero no por una edición concreta. Si se añade otra edición activa en el futuro, consultar solo esta vista podría mezclar periodos.

## 4. Riesgos y condicionantes

1. **Destino público sin confirmar.** No debe asumirse que el `public_html` de NHMA sea el destino del Mapa simbólico mundial.
2. **Selección de edición no garantizada por esquema.** `rg_periodos.activo` no tiene una restricción que garantice una única fila activa. La API debe exigir exactamente una edición con `activo=1` y `estado='congelado'`; si el resultado no es uno, debe fallar de forma visible y no elegir arbitrariamente.
3. **Vista consolidada insuficiente para versionado.** Es válida como apoyo, no como única fuente del contrato público.
4. **Prototipo desalineado.** La tabla actual habla de diez áreas y contiene datos estáticos. La integración debe sustituir su fuente de datos, no validar esos valores.
5. **Monolito frontal.** HTML, CSS y JavaScript embebidos aumentan el riesgo de regresiones. La primera integración debe limitarse a la Tabla de Datos Consolidados.
6. **Secretos.** Una credencial en Git o bajo una URL pública sería un bloqueo crítico.
7. **Privilegios.** Usar el usuario administrativo de phpMyAdmin sería inaceptable; se requiere un usuario dedicado de solo lectura.
8. **Errores sensibles.** Las excepciones PDO, DSN, usuario, host, rutas y SQL no deben aparecer en JSON público.
9. **Ceros y ausencias.** `0` es un valor posible y documentado; `null` representa ausencia. La capa PHP y JavaScript no puede convertir `null`, cadena vacía o error en cero.
10. **Metadatos temporales.** Un solo `anio_referencia` no sustituye `anio_minimo` y `anio_maximo`; los tres deben conservarse.
11. **Dependencias CDN.** Son un riesgo operativo existente, pero su revisión o sustitución queda fuera de 1D.1 y del primer contrato de datos.
12. **Volcado local.** `u794456529_map_sim_Mund.sql` contiene una copia de trabajo y debe permanecer fuera de Git y fuera del árbol público.

## 5. Arquitectura propuesta

### 5.1 Flujo

```text
Navegador
  -> GET HTTPS, mismo origen
API PHP /api/reticula/v1/
  -> validación y consultas preparadas
PDO MySQL, usuario SELECT-only
  -> tablas rg_* de la edición congelada
```

La API será deliberadamente pequeña, sin framework y sin acceso de escritura. Un bootstrap común debe encargarse de conexión, respuesta JSON, resolución de edición y errores. Cada endpoint solo aceptará `GET` y parámetros incluidos en una lista cerrada.

### 5.2 Ubicación

Una vez confirmado el destino de despliegue:

```text
<document-root>/api/reticula/v1/
  status.php
  areas.php
  catalogo.php
  datos.php
  area.php
  bootstrap.php

<fuera-de-document-root>/config/reticula-db.php
```

Si el alojamiento no permite incluir un archivo situado fuera de `public_html`, se usarán variables de entorno o una ubicación privada proporcionada por el hosting y protegida a nivel de servidor. La alternativa mínima es un archivo local no versionado, denegado expresamente por configuración web y verificado mediante una petición HTTP que debe devolver 403/404; no es la opción preferente.

El repositorio debe incluir solo un ejemplo sin secretos, por ejemplo `reticula-db.example.php`, y reglas de exclusión para el archivo local real. Nunca se incluirán host, base, usuario o contraseña reales en documentación, código cliente, respuestas JSON o commits.

### 5.3 Configuración PDO

- extensión `pdo_mysql` habilitada;
- DSN con `charset=utf8mb4`;
- `PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION`;
- `PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC`;
- `PDO::ATTR_EMULATE_PREPARES => false`;
- usuario MySQL dedicado con `SELECT` solo sobre las tablas/vistas necesarias;
- conexión sin sentencias de escritura, transacciones de modificación ni SQL dinámico;
- HTTPS obligatorio en producción;
- registro interno de errores con identificador de petición, sin detalles técnicos al cliente.

### 5.4 Resolución inequívoca de la edición

En cada petición de datos, el bootstrap resolverá el periodo por estas reglas:

1. buscar `codigo='RG2025_V1'`, `activo=1` y `estado='congelado'`;
2. comprobar que existe exactamente una fila;
3. comprobar adicionalmente que existe exactamente una edición activa y congelada en el sistema;
4. usar su `id` como parámetro enlazado en todas las consultas a `rg_datos_area`;
5. si cualquiera de las comprobaciones falla, responder `503 EDITION_STATE_INVALID` y no publicar datos parciales.

Aunque el código sea único por índice, la comprobación global evita seleccionar silenciosamente una edición cuando dos periodos estén marcados activos.

### 5.5 Consulta de las entidades del contrato

- Edición: `rg_periodos` por código, estado y activo.
- Áreas: `rg_areas` activas, ordenadas por `orden_visual`, con código como identificador público estable.
- Bloques: `rg_bloques` activos; el orden inicial puede definirse mediante una lista de códigos acordada o añadirse más adelante al esquema. No debe usarse el `id` como orden editorial.
- Indicadores: `rg_indicadores` activos unidos a `rg_bloques`; código como identificador público.
- Valores: `rg_datos_area` filtrada por `periodo_id` y `activo=1`, unida a área e indicador.
- Fuente: `rg_fuentes` mediante `fuente_principal_id`, incluyendo código, nombre, tipo y URL.
- Método y observaciones: `metodo_calculo`, `estado_dato`, `tipo_procedencia` y `observaciones` de `rg_datos_area`.
- Años: `anio_referencia`, `anio_minimo` y `anio_maximo` sin sustituir unos por otros.
- Cobertura: `paises_totales`, `paises_con_dato` y `porcentaje_cobertura`.

## 6. Convenciones del contrato JSON

Todos los endpoints usarán UTF-8, nombres de campos en `snake_case`, números JSON como números y ausencias reales como `null`.

Respuesta correcta:

```json
{
  "ok": true,
  "data": {},
  "meta": {
    "api_version": "1",
    "edicion": {
      "codigo": "RG2025_V1",
      "nombre": "Retícula Global 2025 - Primera edición",
      "estado": "congelado"
    },
    "total": 0
  },
  "errors": []
}
```

Respuesta de error:

```json
{
  "ok": false,
  "data": null,
  "meta": {
    "api_version": "1",
    "request_id": "identificador-opaco"
  },
  "errors": [
    {
      "code": "INVALID_PARAMETER",
      "message": "Parámetro no válido."
    }
  ]
}
```

Normas comunes:

- `200` para respuestas correctas, incluso si un filtro válido produce una lista vacía.
- `400` para parámetros ausentes o con formato/código no permitido.
- `404` para un área o indicador válido sintácticamente pero inexistente/inactivo.
- `405` para métodos distintos de `GET`, con cabecera `Allow: GET`.
- `503` para conexión no disponible o estado de edición incoherente.
- `500` para fallo interno no clasificable.
- Nunca se devolverán SQL, trazas, rutas, credenciales ni mensajes de PDO.
- Los códigos de área, bloque e indicador se validarán con longitud y patrón estricto y se enlazarán en consultas preparadas.
- Se devolverá `Cache-Control` explícito; por ser una edición congelada, los catálogos y datos admiten caché pública moderada con `ETag` o `Last-Modified` determinado por despliegue, no inventado desde una fecha inexistente en `rg_periodos`.

## 7. Endpoints propuestos

### 7.1 Estado general y edición activa

**Ruta:** `GET /api/reticula/v1/status.php`  
**Parámetros:** ninguno. Se rechazan parámetros desconocidos.  
**Consulta:** `rg_periodos` y conteos activos de `rg_areas`, `rg_paises`, `rg_bloques`, `rg_indicadores` y `rg_datos_area`, restringiendo los datos de área al `periodo_id` resuelto.  
**Finalidad:** prueba operativa y detección de una edición incoherente antes de cargar la interfaz.

```json
{
  "ok": true,
  "data": {
    "estado_aplicacion": "ok",
    "edicion": {
      "codigo": "RG2025_V1",
      "nombre": "Retícula Global 2025 - Primera edición",
      "estado": "congelado",
      "activa": true
    },
    "conteos": {
      "areas": 9,
      "paises_territorios": 244,
      "bloques": 8,
      "indicadores": 27,
      "datos_area": 243
    }
  },
  "meta": { "api_version": "1" },
  "errors": []
}
```

Errores específicos: `503 DATABASE_UNAVAILABLE`, `503 EDITION_STATE_INVALID`, `503 DATASET_INCOMPLETE` si no coinciden los invariantes congelados. El endpoint no debe revelar versión de MySQL, host ni tiempos SQL detallados.

### 7.2 Catálogo de áreas

**Ruta:** `GET /api/reticula/v1/areas.php`  
**Parámetros:** ninguno.  
**Consulta:** `rg_areas`, `activo=1`, orden por `orden_visual`.  
**Respuesta:** lista de nueve áreas.

```json
{
  "ok": true,
  "data": [
    {
      "codigo": "AFR",
      "slug": "africa",
      "nombre": "África",
      "nombre_corto": "África",
      "color": "#000000",
      "orden_visual": 1
    }
  ],
  "meta": { "api_version": "1", "total": 9 },
  "errors": []
}
```

No se exponen IDs internos. Un color nulo se entrega como `null`, nunca se inventa. Si el catálogo no contiene nueve áreas, `503 DATASET_INCOMPLETE`.

### 7.3 Catálogo de bloques e indicadores

**Ruta:** `GET /api/reticula/v1/catalogo.php`  
**Parámetros opcionales:** `bloque=TEC`.  
**Consulta:** `rg_bloques` unido a `rg_indicadores`, ambos activos.  
**Respuesta:** bloques con sus indicadores anidados.

```json
{
  "ok": true,
  "data": [
    {
      "codigo": "TEC",
      "nombre": "Tecnología, digitalización e innovación",
      "indicadores": [
        {
          "codigo": "TEC_NET",
          "nombre": "Población usuaria de Internet",
          "unidad": "porcentaje de población",
          "descripcion": null
        }
      ]
    }
  ],
  "meta": { "api_version": "1", "total_bloques": 8, "total_indicadores": 27 },
  "errors": []
}
```

Un filtro inexistente devuelve `404 BLOCK_NOT_FOUND`. La consulta usará el código enlazado; no se admiten nombres de columnas, ordenaciones ni fragmentos SQL enviados por el cliente.

### 7.4 Datos consolidados por área e indicador

**Ruta:** `GET /api/reticula/v1/datos.php`  
**Parámetros opcionales:** `area=AFR`, `bloque=TEC`, `indicador=TEC_NET`. Los filtros pueden combinarse; no se expone un parámetro de periodo en la primera edición pública.  
**Consulta:** `rg_datos_area` unida a `rg_periodos`, `rg_areas`, `rg_indicadores`, `rg_bloques` y `rg_fuentes`; filtros activos y `periodo_id` resuelto. La vista `rg_v_datos_consolidados` no será la única fuente por sus limitaciones de periodo y trazabilidad.  
**Respuesta:** formato largo, adecuado para generar la primera tabla funcional y reutilizable por gráficas posteriores.

```json
{
  "ok": true,
  "data": [
    {
      "area": { "codigo": "AFR", "nombre": "África" },
      "bloque": { "codigo": "TEC", "nombre": "Tecnología, digitalización e innovación" },
      "indicador": {
        "codigo": "TEC_NET",
        "nombre": "Población usuaria de Internet",
        "unidad": "porcentaje de población"
      },
      "valor": 0.0,
      "anio_referencia": 2024,
      "anio_minimo": 2024,
      "anio_maximo": 2025,
      "cobertura": {
        "entidades_totales": 0,
        "entidades_con_dato": 0,
        "porcentaje": 0.0
      },
      "metodo_calculo": "texto documentado",
      "tipo_procedencia": "agregado",
      "estado_dato": "validado",
      "fuente_principal": {
        "codigo": "WB_ITU",
        "nombre": "UIT / Banco Mundial",
        "tipo": "organismo internacional",
        "url": "https://ejemplo.invalid"
      },
      "observaciones": null
    }
  ],
  "meta": {
    "api_version": "1",
    "edicion": { "codigo": "RG2025_V1", "estado": "congelado" },
    "total": 1
  },
  "errors": []
}
```

Los números del ejemplo ilustran tipos, no valores reales. `valor=0` se conserva como cero; una ausencia sería `null`. Para la edición completa, el total sin filtros debe ser 243; otra cifra provoca `503 DATASET_INCOMPLETE`. Filtros inexistentes devuelven `404 AREA_NOT_FOUND`, `BLOCK_NOT_FOUND` o `INDICATOR_NOT_FOUND`.

### 7.5 Detalle de una sola área

**Ruta:** `GET /api/reticula/v1/area.php?codigo=AFR`  
**Parámetro obligatorio:** `codigo`; patrón recomendado `^[A-Z0-9_]{2,10}$`.  
**Parámetros opcionales:** `bloque=TEC`.  
**Consulta:** las mismas tablas que `datos.php`, filtradas por área y periodo, más metadatos de `rg_areas`. No necesita datos nacionales en esta fase.  
**Respuesta:** área con bloques e indicadores anidados; debe contener 27 valores sin filtro de bloque.

```json
{
  "ok": true,
  "data": {
    "area": {
      "codigo": "AFR",
      "slug": "africa",
      "nombre": "África",
      "nombre_corto": "África",
      "color": "#000000",
      "orden_visual": 1
    },
    "bloques": [
      {
        "codigo": "TEC",
        "nombre": "Tecnología, digitalización e innovación",
        "indicadores": [
          {
            "codigo": "TEC_NET",
            "valor": null,
            "unidad": "porcentaje de población",
            "anio_referencia": 2024,
            "anio_minimo": 2024,
            "anio_maximo": 2025,
            "cobertura_porcentaje": 99.0,
            "fuente_principal": { "codigo": "WB_ITU", "nombre": "UIT / Banco Mundial" },
            "metodo_calculo": "texto documentado",
            "observaciones": null
          }
        ]
      }
    ]
  },
  "meta": {
    "api_version": "1",
    "edicion": { "codigo": "RG2025_V1", "estado": "congelado" },
    "total_indicadores": 27
  },
  "errors": []
}
```

Los valores del ejemplo no son datos de producción. Código ausente o mal formado: `400`. Área inactiva/inexistente: `404`. Una edición completa con menos o más de 27 filas: `503 DATASET_INCOMPLETE`.

## 8. Restricciones de seguridad por endpoint

Aplican a los cinco endpoints:

- solo `GET`; sin operaciones de escritura ni parámetros que alteren estado;
- PDO con consultas preparadas para todo valor procedente de la petición;
- usuario MySQL dedicado de solo lectura;
- mismo origen por defecto; no enviar `Access-Control-Allow-Origin: *` salvo necesidad documentada;
- HTTPS, cabeceras `Content-Type`, `X-Content-Type-Options: nosniff` y política de caché explícita;
- límites de longitud y lista cerrada de parámetros; rechazar parámetros desconocidos;
- mensajes de error genéricos y correlación mediante `request_id` opaco;
- logs fuera del directorio público y sin contraseñas;
- no exponer IDs internos, consultas, estructura física innecesaria ni datos nacionales en la primera presentación;
- desactivar visualización de errores PHP en producción;
- pruebas de que los archivos de configuración, copias SQL y logs no son descargables por HTTP.

No se necesita autenticación de usuario para datos públicos congelados, siempre que el acceso sea estrictamente de lectura. Sí conviene limitación de frecuencia en el servidor y caché para reducir abuso.

## 9. Necesidades MySQL

### 9.1 Para 1D.2

No hacen falta tablas ni vistas nuevas. Las consultas parametrizadas sobre las tablas actuales son más claras para resolver el periodo y aportar trazabilidad completa. Sí hace falta, como operación administrativa externa al código y expresamente autorizada cuando corresponda, un usuario con privilegios `SELECT` mínimos.

### 9.2 Vista adicional posible, no necesaria ahora

La vista documentada `rg_v_primera_edicion` sería cómoda para la tabla, pero su nombre y un filtro fijo a `RG2025_V1` la harían poco reutilizable. Si las consultas de 1D.4 resultan repetitivas o difíciles de mantener, sería preferible proponer una vista neutral, por ejemplo `rg_v_datos_publicables`, que incluya:

- código, nombre y estado del periodo;
- código, nombre, slug y orden del área;
- código y nombre del bloque;
- código, nombre, unidad y descripción del indicador;
- valor, los tres campos de año, cobertura completa, método, procedencia, estado y observaciones;
- código, nombre, tipo y URL de la fuente principal;
- filtros de actividad, pero sin fijar una edición concreta en el nombre.

La API seguiría seleccionando `periodo_codigo=:periodo` y verificando antes la unicidad del periodo activo/congelado. Crear esta vista solo se justificaría después de medir complejidad y comprobar el plan de ejecución. No debe crearse en 1D.1 ni como requisito previo de 1D.2.

### 9.3 Mejoras futuras de esquema, fuera de alcance

- una garantía operativa o estructural de una sola edición activa;
- campos de fecha de congelación y notas en `rg_periodos`;
- un campo de orden explícito en `rg_bloques` si el orden editorial debe residir en datos.

Estas mejoras no deben introducirse en la edición congelada durante la conexión inicial.

## 10. Primera presentación funcional

La Tabla de Datos Consolidados será el primer consumidor de la API. Debe construirse con `areas.php`, `catalogo.php` y `datos.php`, mostrando las 243 combinaciones en formato largo o pivotado en el cliente, con:

- área y bloque;
- indicador y unidad;
- valor, distinguiendo cero de ausencia;
- año de referencia y rango real;
- cobertura;
- fuente y observaciones metodológicas.

La retícula, las gráficas y el rediseño general permanecerán sin conexión durante esta primera implantación. La tabla estática de v5 no debe mezclarse con los datos reales: se sustituirá en una copia de trabajo o entorno de ensayo después de validar la API.

## 11. Secuencia propuesta 1D.2–1D.9

| Fase | Alcance | Criterio de salida |
|---|---|---|
| 1D.2 | Preparar estructura PHP, bootstrap común, configuración privada, usuario de lectura y `status.php` en entorno no público | estado correcto, edición única congelada, conteos 9/244/8/27/243, secretos no accesibles |
| 1D.3 | Implantar `areas.php` y `catalogo.php` con pruebas de contrato | 9 áreas, 8 bloques y 27 indicadores; orden y unidades verificados |
| 1D.4 | Implantar `datos.php`, trazabilidad completa y filtros | 243 filas sin filtros, filtros coherentes, cero distinto de `null` |
| 1D.5 | Implantar `area.php` y pruebas para las nueve áreas | 27 indicadores por área y metadatos coincidentes con el consolidado |
| 1D.6 | Crear en entorno de trabajo la primera Tabla de Datos Consolidados conectada | tabla funcional, accesible y verificable; sin tocar mapa ni gráficas |
| 1D.7 | Endurecimiento: errores, seguridad, caché, CORS, límites, logs y pruebas de indisponibilidad | revisión de seguridad y prueba de no exposición de secretos |
| 1D.8 | Integrar progresivamente los datos en componentes existentes autorizados | retícula y gráficas consumen el mismo contrato, sin rediseño general |
| 1D.9 | Validación de despliegue, comparación con MySQL, documentación y plan de reversión | aceptación funcional y operativa antes de publicar |

Cada fase debe conservar RG2025_V1 congelada y tratar el backend como solo lectura. Cualquier cambio de esquema o vista requiere una autorización y fase SQL separadas.

## 12. Criterios GO/NO-GO para comenzar 1D.2

### GO

- se confirma el document root y la URL de ensayo, sin modificar aún la web pública;
- el servidor dispone de PHP compatible y `pdo_mysql`;
- se define una ubicación de credenciales fuera de Git y preferentemente fuera del document root;
- se crea o confirma un usuario MySQL exclusivo con permisos `SELECT` mínimos;
- existe un entorno de prueba separado o una ruta no enlazada públicamente;
- se acepta el contrato JSON v1 y la regla de edición única activa/congelada;
- se mantiene una copia recuperable previa al despliegue de archivos;
- el volcado SQL y los secretos están excluidos del despliegue y del control de versiones.

### NO-GO

- solo están disponibles credenciales administrativas o con escritura;
- los secretos tendrían que guardarse en Git, JavaScript o una ruta descargable;
- no se conoce qué `public_html` corresponde al proyecto;
- no está disponible PDO MySQL;
- la API no puede restringirse a lectura o a HTTPS en producción;
- MySQL deja de presentar exactamente una edición `RG2025_V1` activa y congelada;
- los conteos dejan de ser 9/244/8/27/243 antes de iniciar la integración;
- se pretende conectar simultáneamente mapa, gráficas y tabla sin validar primero el endpoint de estado y la tabla consolidada.

## 13. Decisión

**GO condicionado para iniciar 1D.2 en entorno de trabajo.** El modelo de datos y el contrato son suficientes y no exigen una vista MySQL nueva. Los bloqueos previos al despliegue son confirmar el destino público real, PDO MySQL, la ubicación privada de secretos y el usuario de lectura.

Durante 1D.1 no se ejecutó SQL, no se alteró MySQL, no se descongeló `RG2025_V1`, no se modificó la web pública y no se inició el mapa interactivo ni el rediseño visual.
