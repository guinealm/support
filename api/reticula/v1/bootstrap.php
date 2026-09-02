<?php
declare(strict_types=1);

const RETICULA_API_VERSION = '1';
const RETICULA_EXPECTED_EDITION = 'RG2025_V1';

final class ApiException extends RuntimeException
{
    public function __construct(
        public readonly string $apiCode,
        public readonly int $httpStatus,
        string $publicMessage
    ) {
        parent::__construct($publicMessage);
    }
}

function request_id(): string
{
    try {
        return bin2hex(random_bytes(8));
    } catch (Throwable) {
        return hash('sha256', uniqid('', true));
    }
}

function send_json(array $payload, int $httpStatus = 200): never
{
    http_response_code($httpStatus);
    header('Content-Type: application/json; charset=utf-8');
    header('X-Content-Type-Options: nosniff');
    header('Cache-Control: no-store');

    $json = json_encode(
        $payload,
        JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_INVALID_UTF8_SUBSTITUTE
    );

    if ($json === false) {
        http_response_code(500);
        echo '{"ok":false,"data":null,"meta":{"api_version":"1"},"errors":[{"code":"JSON_ENCODING_ERROR","message":"No se pudo generar la respuesta."}]}';
        exit;
    }

    echo $json;
    exit;
}

function send_error(ApiException $exception): never
{
    send_json([
        'ok' => false,
        'data' => null,
        'meta' => [
            'api_version' => RETICULA_API_VERSION,
            'request_id' => request_id(),
        ],
        'errors' => [[
            'code' => $exception->apiCode,
            'message' => $exception->getMessage(),
        ]],
    ], $exception->httpStatus);
}

function require_get_without_parameters(): void
{
    $method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
    if ($method !== 'GET') {
        header('Allow: GET');
        throw new ApiException('METHOD_NOT_ALLOWED', 405, 'Método no permitido.');
    }

    if ($_GET !== []) {
        throw new ApiException('INVALID_PARAMETER', 400, 'Este endpoint no admite parámetros.');
    }
}

function load_database_config(): array
{
    $externalPath = getenv('RETICULA_DB_CONFIG');
    if (is_string($externalPath) && trim($externalPath) !== '') {
        $configPath = trim($externalPath);
    } else {
        $documentRoot = $_SERVER['DOCUMENT_ROOT'] ?? '';
        $privateConfig = is_string($documentRoot) && $documentRoot !== ''
            ? dirname($documentRoot, 3)
                . DIRECTORY_SEPARATOR . '.config'
                . DIRECTORY_SEPARATOR . 'reticula-global'
                . DIRECTORY_SEPARATOR . 'support'
                . DIRECTORY_SEPARATOR . 'reticula-db.php'
            : '';

        $configPath = $privateConfig !== '' && is_file($privateConfig) && is_readable($privateConfig)
            ? $privateConfig
            : dirname(__DIR__, 2)
                . DIRECTORY_SEPARATOR . 'config'
                . DIRECTORY_SEPARATOR . 'reticula-db.local.php';
    }

    if (!is_file($configPath) || !is_readable($configPath)) {
        throw new ApiException(
            'CONFIGURATION_ERROR',
            500,
            'La configuración privada de la base de datos no está disponible.'
        );
    }

    $config = require $configPath;
    if (!is_array($config)) {
        throw new ApiException('CONFIGURATION_ERROR', 500, 'La configuración privada no es válida.');
    }

    foreach (['host', 'database', 'username', 'password'] as $key) {
        if (!array_key_exists($key, $config) || !is_string($config[$key]) || trim($config[$key]) === '') {
            throw new ApiException('CONFIGURATION_ERROR', 500, 'La configuración privada está incompleta.');
        }
    }

    $port = $config['port'] ?? 3306;
    if (!is_int($port) && !(is_string($port) && ctype_digit($port))) {
        throw new ApiException('CONFIGURATION_ERROR', 500, 'La configuración privada no es válida.');
    }
    $port = (int) $port;
    if ($port < 1 || $port > 65535) {
        throw new ApiException('CONFIGURATION_ERROR', 500, 'La configuración privada no es válida.');
    }

    return [
        'host' => trim($config['host']),
        'port' => $port,
        'database' => trim($config['database']),
        'username' => trim($config['username']),
        'password' => $config['password'],
    ];
}

function database_connection(): PDO
{
    if (!extension_loaded('pdo_mysql')) {
        throw new ApiException('CONFIGURATION_ERROR', 500, 'El controlador PDO MySQL no está disponible.');
    }

    $config = load_database_config();
    $dsn = sprintf(
        'mysql:host=%s;port=%d;dbname=%s;charset=utf8mb4',
        $config['host'],
        $config['port'],
        $config['database']
    );

    try {
        return new PDO($dsn, $config['username'], $config['password'], [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ]);
    } catch (PDOException) {
        throw new ApiException('DATABASE_UNAVAILABLE', 503, 'No se pudo conectar con la base de datos.');
    }
}
