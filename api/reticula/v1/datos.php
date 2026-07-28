<?php
declare(strict_types=1);

// Ruta pública estable. La implementación y su configuración permanecen
// en el proyecto Retícula Global para no duplicar lógica ni credenciales.
$externalConfig = getenv('RETICULA_DB_CONFIG');
if (!is_string($externalConfig) || trim($externalConfig) === '') {
    $documentRoot = $_SERVER['DOCUMENT_ROOT'] ?? '';
    if (is_string($documentRoot) && $documentRoot !== '') {
        $privateConfig = dirname($documentRoot, 3)
            . '/.config/reticula-global/support/reticula-db.php';
        if (is_file($privateConfig) && is_readable($privateConfig)) {
            putenv('RETICULA_DB_CONFIG=' . $privateConfig);
        }
    }
}

require dirname(__DIR__, 3) . '/projects/Mapa simbólico Mundial/api/reticula/v1/datos.php';
