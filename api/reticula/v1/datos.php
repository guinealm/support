<?php
declare(strict_types=1);

require_once __DIR__ . '/bootstrap.php';

const DATA_CODE_PATTERN = '/^[A-Z0-9_]{2,30}$/';

function require_get_with_data_filters(): array
{
    $method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
    if ($method !== 'GET') {
        header('Allow: GET');
        throw new ApiException('METHOD_NOT_ALLOWED', 405, 'Método no permitido.');
    }

    $allowed = ['area', 'bloque', 'indicador'];
    foreach (array_keys($_GET) as $parameter) {
        if (!in_array($parameter, $allowed, true)) {
            throw new ApiException('INVALID_PARAMETER', 400, 'Parámetro no válido.');
        }
    }

    $filters = [];
    foreach ($allowed as $parameter) {
        if (!array_key_exists($parameter, $_GET)) {
            continue;
        }
        if (!is_string($_GET[$parameter])) {
            throw new ApiException('INVALID_PARAMETER', 400, 'Parámetro no válido.');
        }
        $value = strtoupper(trim($_GET[$parameter]));
        if (!preg_match(DATA_CODE_PATTERN, $value)) {
            throw new ApiException('INVALID_PARAMETER', 400, 'Parámetro no válido.');
        }
        $filters[$parameter] = $value;
    }

    return $filters;
}

function active_frozen_edition(PDO $pdo): array
{
    $statement = $pdo->prepare(
        'SELECT id, codigo, nombre, estado, activo
         FROM rg_periodos
         WHERE activo = :activo
         ORDER BY id'
    );
    $statement->execute(['activo' => 1]);
    $editions = $statement->fetchAll();

    if (count($editions) === 0) {
        throw new ApiException('ACTIVE_EDITION_NOT_FOUND', 503, 'No existe una edición activa.');
    }
    if (count($editions) > 1) {
        throw new ApiException('MULTIPLE_ACTIVE_EDITIONS', 503, 'Existe más de una edición activa.');
    }

    $edition = $editions[0];
    if ($edition['codigo'] !== RETICULA_EXPECTED_EDITION) {
        throw new ApiException('UNEXPECTED_ACTIVE_EDITION', 503, 'La edición activa no es la edición esperada.');
    }
    if ($edition['estado'] !== 'congelado') {
        throw new ApiException('EDITION_NOT_FROZEN', 503, 'La edición activa no está congelada.');
    }

    return $edition;
}

function nullable_int(mixed $value): ?int
{
    return $value === null ? null : (int) $value;
}

function nullable_float(mixed $value): ?float
{
    return $value === null ? null : (float) $value;
}

try {
    $filters = require_get_with_data_filters();
    $pdo = database_connection();

    try {
        $edition = active_frozen_edition($pdo);
        $where = [
            'da.activo = :activo_dato',
            'a.activo = :activo_area',
            'b.activo = :activo_bloque',
            'i.activo = :activo_indicador',
            'da.periodo_id = :periodo_id',
        ];
        $parameters = [
            'activo_dato' => 1,
            'activo_area' => 1,
            'activo_bloque' => 1,
            'activo_indicador' => 1,
            'periodo_id' => (int) $edition['id'],
        ];

        $filterColumns = [
            'area' => 'a.codigo',
            'bloque' => 'b.codigo',
            'indicador' => 'i.codigo',
        ];
        foreach ($filters as $name => $value) {
            $where[] = $filterColumns[$name] . ' = :' . $name;
            $parameters[$name] = $value;
        }

        $sql =
            'SELECT
                a.codigo AS area_codigo,
                a.slug AS area_slug,
                a.nombre AS area_nombre,
                a.nombre_corto AS area_nombre_corto,
                a.color_principal AS area_color,
                a.orden_visual AS area_orden,
                b.codigo AS bloque_codigo,
                b.nombre AS bloque_nombre,
                i.codigo AS indicador_codigo,
                i.nombre AS indicador_nombre,
                i.unidad AS indicador_unidad,
                i.descripcion AS indicador_descripcion,
                da.valor,
                da.anio_referencia,
                da.anio_minimo,
                da.anio_maximo,
                da.paises_totales,
                da.paises_con_dato,
                da.porcentaje_cobertura,
                da.metodo_calculo,
                da.tipo_procedencia,
                da.estado_dato,
                da.observaciones,
                f.codigo AS fuente_codigo,
                f.nombre AS fuente_nombre,
                f.tipo_fuente,
                f.url AS fuente_url
             FROM rg_datos_area da
             INNER JOIN rg_areas a ON a.id = da.area_id
             INNER JOIN rg_indicadores i ON i.id = da.indicador_id
             INNER JOIN rg_bloques b ON b.id = i.bloque_id
             LEFT JOIN rg_fuentes f ON f.id = da.fuente_principal_id
             WHERE ' . implode(' AND ', $where) . '
             ORDER BY b.id, i.id, a.orden_visual, a.id';

        $statement = $pdo->prepare($sql);
        $statement->execute($parameters);
        $rows = $statement->fetchAll();

        if ($filters === [] && count($rows) !== 243) {
            throw new ApiException('INCONSISTENT_TOTALS', 503, 'Los totales de la edición activa no son coherentes.');
        }

        $data = [];
        foreach ($rows as $row) {
            $data[] = [
                'area' => [
                    'codigo' => $row['area_codigo'],
                    'slug' => $row['area_slug'],
                    'nombre' => $row['area_nombre'],
                    'nombre_corto' => $row['area_nombre_corto'],
                    'color' => $row['area_color'],
                    'orden_visual' => (int) $row['area_orden'],
                ],
                'bloque' => [
                    'codigo' => $row['bloque_codigo'],
                    'nombre' => $row['bloque_nombre'],
                ],
                'indicador' => [
                    'codigo' => $row['indicador_codigo'],
                    'nombre' => $row['indicador_nombre'],
                    'unidad' => $row['indicador_unidad'],
                    'descripcion' => $row['indicador_descripcion'],
                ],
                'valor' => nullable_float($row['valor']),
                'anio_referencia' => nullable_int($row['anio_referencia']),
                'anio_minimo' => nullable_int($row['anio_minimo']),
                'anio_maximo' => nullable_int($row['anio_maximo']),
                'cobertura' => [
                    'entidades_totales' => nullable_int($row['paises_totales']),
                    'entidades_con_dato' => nullable_int($row['paises_con_dato']),
                    'porcentaje' => nullable_float($row['porcentaje_cobertura']),
                ],
                'metodo_calculo' => $row['metodo_calculo'],
                'tipo_procedencia' => $row['tipo_procedencia'],
                'estado_dato' => $row['estado_dato'],
                'fuente_principal' => $row['fuente_codigo'] === null ? null : [
                    'codigo' => $row['fuente_codigo'],
                    'nombre' => $row['fuente_nombre'],
                    'tipo' => $row['tipo_fuente'],
                    'url' => $row['fuente_url'],
                ],
                'observaciones' => $row['observaciones'],
            ];
        }
    } catch (ApiException $exception) {
        throw $exception;
    } catch (PDOException) {
        throw new ApiException('DATABASE_QUERY_FAILED', 503, 'No se pudo consultar el conjunto de datos.');
    }

    send_json([
        'ok' => true,
        'data' => $data,
        'meta' => [
            'api_version' => RETICULA_API_VERSION,
            'edicion' => [
                'codigo' => $edition['codigo'],
                'nombre' => $edition['nombre'],
                'estado' => $edition['estado'],
            ],
            'total' => count($data),
            'filtros' => $filters,
        ],
        'errors' => [],
    ]);
} catch (ApiException $exception) {
    send_error($exception);
} catch (Throwable) {
    send_error(new ApiException('INTERNAL_ERROR', 500, 'Se produjo un error interno.'));
}
