<?php
declare(strict_types=1);

/**
 * Copiar fuera del document root como reticula-db.php y definir la ruta
 * absoluta en RETICULA_DB_CONFIG. Para pruebas locales puede copiarse como
 * reticula-db.local.php en esta carpeta; ese archivo está excluido de Git.
 *
 * Usar siempre un usuario MySQL dedicado con permisos exclusivamente SELECT.
 */
return [
    'host' => 'mysql.example.internal',
    'port' => 3306,
    'database' => 'reticula_global_example',
    'username' => 'reticula_readonly_example',
    'password' => 'REEMPLAZAR_FUERA_DE_GIT',
];
