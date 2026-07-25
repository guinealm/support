<?php
declare(strict_types=1);

require_once __DIR__ . '/bootstrap.php';

const EXPECTED_TOTALS = [
    'areas' => 9,
    'paises_territorios' => 244,
    'bloques' => 8,
    'indicadores' => 27,
    'datos_area_activos' => 243,
];

try {
    require_get_without_parameters();
    $pdo = database_connection();

    try {
        $editionStatement = $pdo->prepare(
            'SELECT id, codigo, nombre, estado, activo
             FROM rg_periodos
             WHERE activo = :activo
             ORDER BY id'
        );
        $editionStatement->execute(['activo' => 1]);
        $activeEditions = $editionStatement->fetchAll();

        $activeCount = count($activeEditions);
        if ($activeCount === 0) {
            throw new ApiException('ACTIVE_EDITION_NOT_FOUND', 503, 'No existe una edición activa.');
        }
        if ($activeCount > 1) {
            throw new ApiException('MULTIPLE_ACTIVE_EDITIONS', 503, 'Existe más de una edición activa.');
        }

        $edition = $activeEditions[0];
        if ($edition['codigo'] !== RETICULA_EXPECTED_EDITION) {
            throw new ApiException('UNEXPECTED_ACTIVE_EDITION', 503, 'La edición activa no es la edición esperada.');
        }
        if ($edition['estado'] !== 'congelado') {
            throw new ApiException('EDITION_NOT_FROZEN', 503, 'La edición activa no está congelada.');
        }

        $totalsStatement = $pdo->prepare(
            'SELECT
                (SELECT COUNT(*) FROM rg_areas WHERE activo = :activo_areas) AS areas,
                (SELECT COUNT(*) FROM rg_paises WHERE activo = :activo_paises) AS paises_territorios,
                (SELECT COUNT(*) FROM rg_bloques WHERE activo = :activo_bloques) AS bloques,
                (SELECT COUNT(*) FROM rg_indicadores WHERE activo = :activo_indicadores) AS indicadores,
                (SELECT COUNT(*)
                 FROM rg_datos_area
                 WHERE activo = :activo_datos AND periodo_id = :periodo_id) AS datos_area_activos'
        );
        $totalsStatement->execute([
            'activo_areas' => 1,
            'activo_paises' => 1,
            'activo_bloques' => 1,
            'activo_indicadores' => 1,
            'activo_datos' => 1,
            'periodo_id' => (int) $edition['id'],
        ]);
        $totalsRow = $totalsStatement->fetch();
        if (!is_array($totalsRow)) {
            throw new ApiException('DATABASE_QUERY_FAILED', 503, 'No se pudo comprobar el conjunto de datos.');
        }

        $totals = [];
        foreach (EXPECTED_TOTALS as $key => $expected) {
            $totals[$key] = (int) $totalsRow[$key];
            if ($totals[$key] !== $expected) {
                throw new ApiException('INCONSISTENT_TOTALS', 503, 'Los totales de la edición activa no son coherentes.');
            }
        }
    } catch (ApiException $exception) {
        throw $exception;
    } catch (PDOException) {
        throw new ApiException('DATABASE_QUERY_FAILED', 503, 'No se pudo comprobar el conjunto de datos.');
    }

    send_json([
        'ok' => true,
        'data' => [
            'estado' => 'ok',
            'origen' => 'mysql',
            'edicion' => [
                'codigo' => $edition['codigo'],
                'nombre' => $edition['nombre'],
                'activa' => (int) $edition['activo'] === 1,
                'estado' => $edition['estado'],
            ],
            'totales' => $totals,
        ],
        'meta' => [
            'api_version' => RETICULA_API_VERSION,
        ],
        'errors' => [],
    ]);
} catch (ApiException $exception) {
    send_error($exception);
} catch (Throwable) {
    send_error(new ApiException('INTERNAL_ERROR', 500, 'Se produjo un error interno.'));
}
