# API Retícula Global — entorno de trabajo

Estado: implementación canónica consolidada mediante el lote A1. Están implementados el endpoint de estado y la consulta consolidada necesaria para la primera página conectada.

## Requisitos

- PHP 8.1 o posterior;
- extensiones `PDO` y `pdo_mysql`;
- HTTPS en producción;
- usuario MySQL dedicado con permisos exclusivamente `SELECT`.

## Configuración privada

La opción recomendada es crear `reticula-db.php` fuera del document root y hacer que la variable de entorno `RETICULA_DB_CONFIG` contenga su ruta absoluta. El archivo debe devolver las claves `host`, `port`, `database`, `username` y `password`.

Para una prueba local puede copiarse `config/reticula-db.example.php` como `config/reticula-db.local.php` y sustituir los marcadores. El archivo local está excluido de Git, pero esta alternativa no debe usarse al desplegar si la carpeta del proyecto queda bajo el document root.

En Hostinger, guardar el archivo en una carpeta privada superior o paralela a `public_html`, configurar `RETICULA_DB_CONFIG` mediante el mecanismo disponible en el alojamiento y subir a la carpeta pública únicamente `api/reticula/v1/`. Si el hosting no permite variables de entorno, el bootstrap puede recibir la ruta privada desde un archivo de arranque protegido, también fuera de Git. Verificar por HTTP que configuración, copias SQL y logs devuelven 403/404.

No usar las credenciales administrativas de phpMyAdmin.

## Prueba

Desde la raíz pública de un entorno de ensayo:

```text
GET /api/reticula/v1/status.php
```

No admite parámetros ni métodos distintos de `GET`. Una respuesta correcta tiene HTTP 200 y esta forma:

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

## Datos consolidados

```text
GET /api/reticula/v1/datos.php
```

Devuelve los 243 registros activos de área de `RG2025_V1` en formato largo, con área, bloque, indicador, valor, unidad, años, cobertura, método, fuente principal y observaciones. Solo consulta la edición activa y congelada.

Admite filtros opcionales por código, combinables entre sí:

```text
GET /api/reticula/v1/datos.php?area=AFR
GET /api/reticula/v1/datos.php?bloque=TEC
GET /api/reticula/v1/datos.php?indicador=TEC_NET
```

La interfaz histórica consumidora es `projects/Mapa simbólico Mundial/tabla-datos-consolidados.html`. La página carga los datos mediante la API, permite filtrarlos en el navegador y exportar la selección visible como CSV. No contiene una copia estática de los valores de producción.

## Errores controlados

| Código | HTTP | Significado |
|---|---:|---|
| `INVALID_PARAMETER` | 400 | se enviaron parámetros no admitidos |
| `METHOD_NOT_ALLOWED` | 405 | se usó un método distinto de GET |
| `CONFIGURATION_ERROR` | 500 | configuración privada ausente/inválida o falta `pdo_mysql` |
| `DATABASE_UNAVAILABLE` | 503 | no se pudo establecer la conexión |
| `ACTIVE_EDITION_NOT_FOUND` | 503 | no existe edición activa |
| `MULTIPLE_ACTIVE_EDITIONS` | 503 | existe más de una edición activa |
| `UNEXPECTED_ACTIVE_EDITION` | 503 | la activa no es `RG2025_V1` |
| `EDITION_NOT_FROZEN` | 503 | la edición activa no está congelada |
| `INCONSISTENT_TOTALS` | 503 | no coinciden los totales congelados |
| `DATABASE_QUERY_FAILED` | 503 | falló una consulta de comprobación |
| `INTERNAL_ERROR` | 500 | error interno no clasificable |

Las respuestas públicas no contienen mensajes PDO, SQL, servidor, usuario, contraseña, base de datos ni rutas locales. Los detalles deben registrarse únicamente en logs privados del servidor cuando se implante el registro operativo.
