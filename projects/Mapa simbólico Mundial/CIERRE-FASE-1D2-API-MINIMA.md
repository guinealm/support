# Cierre de la Fase 1D.2 — API MySQL mínima

Fecha: 20 de julio de 2026  
Estado: **preparada; validación PHP/MySQL real pendiente**

## 1. Alcance realizado

Se creó en el entorno de trabajo la infraestructura mínima para `GET /api/reticula/v1/status.php`. No se modificaron HTML, CSS o JavaScript, no se desplegó en la web pública y no se ejecutó ninguna sentencia en MySQL.

## 2. Archivos creados o modificados

- `.gitignore`: exclusión exacta de la configuración local y del volcado MySQL de trabajo.
- `projects/Mapa simbólico Mundial/config/reticula-db.example.php`: plantilla sin credenciales reales.
- `projects/Mapa simbólico Mundial/api/reticula/v1/bootstrap.php`: respuestas JSON, configuración privada y conexión PDO.
- `projects/Mapa simbólico Mundial/api/reticula/v1/status.php`: comprobación de edición y totales.
- `projects/Mapa simbólico Mundial/api/reticula/README.md`: instalación, prueba, Hostinger y errores.
- `projects/Mapa simbólico Mundial/CIERRE-FASE-1D2-API-MINIMA.md`: este cierre.

El diagnóstico 1D.1 preexistente permanece sin cambios. El volcado `u794456529_map_sim_Mund.sql` no se modificó.

## 3. Arquitectura aplicada

La API usa PHP sin framework y separa:

1. endpoint público versionado;
2. bootstrap común;
3. configuración privada externa, indicada mediante `RETICULA_DB_CONFIG`;
4. plantilla versionada sin secretos;
5. configuración local alternativa excluida de Git solo para ensayo.

PDO se inicializa con `utf8mb4`, excepciones, `FETCH_ASSOC` y emulación de consultas preparadas desactivada. El endpoint solo acepta GET sin parámetros y devuelve JSON UTF-8 con `nosniff` y `no-store`.

## 4. Consultas exclusivamente de lectura

El endpoint prepara y ejecuta dos selecciones:

1. selección de las filas de `rg_periodos` con `activo=1`, recuperando únicamente `id`, `codigo`, `nombre`, `estado` y `activo`;
2. conteos de filas activas en `rg_areas`, `rg_paises`, `rg_bloques`, `rg_indicadores` y `rg_datos_area`; el último conteo queda restringido mediante el `periodo_id` de la única edición activa.

No contiene operaciones de inserción, actualización, sustitución, alteración, creación, eliminación ni truncado. No usa vistas nuevas ni cambia el esquema.

## 5. Validaciones

Se distinguen expresamente:

- configuración privada ausente, incompleta o inválida;
- extensión PDO MySQL ausente;
- conexión MySQL no disponible;
- ninguna edición activa;
- más de una edición activa;
- edición activa distinta de `RG2025_V1`;
- edición activa no congelada;
- fallo de consulta;
- totales diferentes de 9 áreas, 244 países/territorios, 8 bloques, 27 indicadores o 243 datos de área del periodo.

Todas las incidencias devuelven un código público controlado y un `request_id`. No se exponen excepciones PDO, SQL, credenciales, nombres de servidor/base ni rutas.

## 6. Protección de credenciales

La configuración real no existe en los cambios. `.gitignore` excluye:

```text
/projects/Mapa simbólico Mundial/config/reticula-db.local.php
```

En producción se exige que `RETICULA_DB_CONFIG` señale un archivo privado fuera del document root. La plantilla versionada contiene solamente valores ficticios. También se añadió al ignore el volcado local existente para impedir su inclusión accidental en Git.

## 7. Formato JSON definitivo

Respuesta correcta:

```json
{
  "ok": true,
  "data": {
    "estado": "ok",
    "origen": "mysql",
    "edicion": {
      "codigo": "RG2025_V1",
      "nombre": "Retícula Global 2025 - Primera edición",
      "activa": true,
      "estado": "congelado"
    },
    "totales": {
      "areas": 9,
      "paises_territorios": 244,
      "bloques": 8,
      "indicadores": 27,
      "datos_area_activos": 243
    }
  },
  "meta": { "api_version": "1" },
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
      "code": "CONFIGURATION_ERROR",
      "message": "La configuración privada de la base de datos no está disponible."
    }
  ]
}
```

## 8. Pruebas realizadas

- lectura y contraste del diagnóstico 1D.1, cierre 1C.9, esquema vigente, auditoría 26, congelación 27, vistas documentadas y patrón PDO de referencia;
- revisión previa de Git y conservación de cambios existentes;
- comprobación estática de rutas, nombres de tablas y columnas contra `01_rg_estructura_minima.sql`;
- revisión del código para confirmar que solo contiene consultas de lectura;
- verificación de reglas de exclusión para configuración local y volcado;
- búsqueda de posibles secretos en los archivos cambiados;
- revisión final de `git diff`.

## 9. Pruebas pendientes e incidencias

El equipo local no dispone del ejecutable `php` en `PATH`, por lo que no fue posible ejecutar `php -l`. Tampoco se proporcionaron credenciales de solo lectura ni conexión MySQL local; no se ejecutó el endpoint y no se inventó una respuesta.

Prueba pendiente en un entorno de ensayo con PHP 8.1 o posterior:

1. ejecutar `php -l` sobre `bootstrap.php`, `status.php` y la plantilla de configuración;
2. guardar la configuración real fuera del document root;
3. definir `RETICULA_DB_CONFIG` con su ruta absoluta;
4. confirmar que el usuario solo dispone de `SELECT`;
5. solicitar por HTTPS `GET /api/reticula/v1/status.php`;
6. comprobar HTTP 200, JSON válido, edición `RG2025_V1`, estado `congelado` y totales 9/244/8/27/243;
7. probar método POST y un parámetro desconocido para confirmar HTTP 405 y 400;
8. retirar temporalmente la variable/configuración y comprobar que el error no revela rutas ni secretos;
9. verificar mediante URL que configuración, volcado y logs no son descargables.

## 10. Criterios GO/NO-GO para 1D.3

### Cumplidos estáticamente

- configuración real fuera de los cambios y protegida por `.gitignore`;
- ausencia de credenciales reales;
- consultas exclusivamente de lectura y preparadas;
- formato JSON definido;
- comprobaciones diferenciadas de edición y totales;
- errores internos no expuestos por el código;
- web pública sin cambios.

### Pendientes

- sintaxis confirmada por un intérprete PHP real;
- conexión con usuario SELECT-only;
- respuesta JSON real del endpoint;
- confirmación en ejecución de la edición única, activa y congelada;
- confirmación en ejecución de los totales 9/244/8/27/243;
- comprobación del alojamiento y de la inaccesibilidad HTTP de secretos.

## 11. Decisión

**NO-GO temporal para iniciar 1D.3.** La implementación 1D.2 está preparada, pero los criterios de salida exigen una prueba real de sintaxis y del endpoint contra MySQL. Cuando esas pruebas resulten correctas, la recomendación pasa a GO sin necesidad de modificar datos ni descongelar `RG2025_V1`.

No se ejecutó SQL, no se alteró MySQL, no se crearon tablas o vistas, no se modificó la interfaz ni la web pública, no se desarrolló la Tabla de Datos Consolidados y no se realizó commit.
