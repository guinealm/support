# Plan de reorganización por lotes

> Estado al 2 de septiembre de 2026: L1, L2, W1 y A1 están ejecutados. G1 y H1 permanecen pendientes de autorización específica.

**Fase:** RG-04  
**Estado:** ejecución parcial autorizada: L1, L2 y W1 cerrados  
**Principio:** una ubicación canónica por función y ningún borrado sin evidencia

## 1. Resultado buscado

Reducir las tres carpetas actuales a:

- `projects/mapa-mundi/`: producto activo, documentación vigente y herramientas propias;
- un archivo histórico no público: fuentes narrativas, prototipos y preparación de datos que deban conservarse.

`projects/reticula-global/` desaparecería como proyecto separado después de trasladar sus contenidos. `projects/Mapa simbólico Mundial/` solo podría salir de `projects/` tras extraer la API y los generadores todavía activos.

## 2. Lote L1 — residuos inequívocos

### Borrar

1. `projects/Mapa simbólico Mundial/ne_10m_admin_0_countries.zip`.
2. `projects/Mapa simbólico Mundial/Mapa simbólico v1.html.txt`.
3. `projects/reticula-global/__pycache__/`.

### Condición

Autorización expresa de borrado para esas tres rutas.

### Validación

- confirmar que `natural-earth-source/ne_10m_admin_0_countries.shp` permanece;
- confirmar que `Mapa simbolico v1.html` permanece;
- comprobar estado Git y referencias rotas.

## 3. Lote L2 — documentación y soporte local

### Crear destinos

- `projects/mapa-mundi/docs/seguimiento/`;
- `projects/mapa-mundi/docs/historico/`;
- `projects/mapa-mundi/tools/validacion/`.

### Mover a `docs/seguimiento/`

- `projects/reticula-global/INFORME-SEGUIMIENTO-RETICULA-GLOBAL-2026-07-30.md`;
- `projects/reticula-global/FASE-8-CONSOLIDACION-Y-PREPARACION-PUBLICACION-2026-09-02.md`;
- `projects/reticula-global/FASE-0A-INVENTARIO-LIMPIEZA-2026-09-02.md`;
- `projects/reticula-global/INVENTARIO-PRELIMINAR-LIMPIEZA-2026-09-02.md`;
- `projects/reticula-global/PLAN-REORGANIZACION-POR-LOTES-2026-09-02.md`;
- `projects/reticula-global/FASE-8A-DIRECCION-PORTADA-2026-09-02.md`.

### Mover a `docs/historico/`

- `FASE-7B1-INVENTARIO-FUNCIONAL-API-PAGINA-2026-07-29.md`;
- `FASE-7B2-PERFIL-MEDIO-POBLACION-2026-07-29.md`;
- `FASE-7C-PERFIL-FICHAS-AREA-2026-07-30.md`;
- `FASE-7D-ACCESIBILIDAD-PERFIL-2026-07-30.md`;
- `FASE-7E-REVISION-FUNCIONAL-Y-CIERRE-VISUAL-2026-07-30.md`;
- `informe_regionalizacion_reticula_global.docx`.

### Mover a `tools/validacion/`

- `servidor_validacion_local.py`.

### Actualizar

- enlaces en `AGENTS.md`;
- `docs/MIGRACION-CODEX-RETICULA-GLOBAL.md`;
- `Informe de seguimiento — Retícula Global.md`;
- programa, estado, registro de tareas y workspace;
- referencias internas de los informes movidos.

### Condición

Autorización expresa para mover las rutas enumeradas y actualizar referencias documentales. No incluye ejecutar el proxy.

## 4. Lote A1 — consolidación de API

### Estado actual

`api/reticula/v1/datos.php` es un puente que carga la implementación situada bajo el proyecto histórico.

### Resultado propuesto

- `api/reticula/v1/bootstrap.php`: implementación trasladada;
- `api/reticula/v1/datos.php`: implementación completa en la ruta pública canónica;
- `api/reticula/v1/status.php`: endpoint trasladado;
- `api/reticula/README.md`: documentación trasladada y corregida;
- `api/reticula/config/reticula-db.example.php`: plantilla trasladada si la resolución de configuración lo permite.

La variable externa `RETICULA_DB_CONFIG` y la ubicación privada de producción deben conservarse. No se copiarán credenciales ni configuraciones locales.

### Condición

Autorización específica para modificar PHP/API y mover su plantilla. No autoriza ejecutar consultas, conectarse a MySQL ni desplegar.

### Validación permitida después de autorizar

- `php -l` sobre los tres PHP;
- inspección de rutas y configuración;
- prueba aislada que no abra conexión, si puede garantizarse;
- no usar la API pública ni local como prueba sin otra autorización.

## 5. Lote G1 — generadores y fuentes cartográficas

### Resultado propuesto

- mover `generar_datos.py`, `generar_indicadores.py` y `generar_territorios.py` a `projects/mapa-mundi/tools/generacion/`;
- mover o referenciar los CSV maestros desde una zona de fuentes no pública;
- conservar `natural-earth-source/` porque el generador usa el Shapefile extraído;
- configurar las salidas canónicas en `projects/mapa-mundi/` o en una carpeta temporal de generación;
- retirar después las seis copias idénticas de JSON/GeoJSON del directorio histórico.

### Condición

Autorización específica para mover generadores y fuentes. Ejecutar generadores o modificar datos requerirá una autorización distinta.

## 6. Lote H1 — archivo histórico

### Conservar en archivo

- prototipos `Mapa simbolico v1.html` a `v5.html`;
- documentos narrativos `.docx` y `.pdf`;
- informes metodológicos 1A–1D y 7A;
- scripts, CSV y SQL de preparación que deban conservar trazabilidad;
- fuentes originales no reproducibles.

### Candidatos a retirada posterior

- HTML/CSS/JS de la antigua carpeta `mapa/` una vez confirmada su sustitución;
- backups idénticos de `output_1c2/`;
- archivos auxiliares `directorio`, `error link.png` y otras salidas sin referencia, tras inspección individual;
- SQL marcados como sustituidos, solo dentro de una revisión específica de datos.

### Condición

Elegir un destino de archivo fuera de la ruta pública y autorizar los movimientos. El borrado posterior será otro lote.

## 7. Lote W1 — portada y explorador

### Estado actual

- `index.html`: explorador vigente;
- `portada-prototipo.html`: portada separada validada por HTTP;
- CSS y JavaScript del prototipo también separados.

### Integración propuesta

1. conservar el explorador actual como `explorar.html`;
2. convertir el prototipo en `index.html`;
3. renombrar sus recursos a `portada.css` y `portada.js`;
4. actualizar enlaces de ida y vuelta;
5. mantener `area.html?codigo=...`;
6. no modificar archivos de datos.

### Condición

Autorización de movimientos/renombrados dentro de `projects/mapa-mundi/` después de la revisión del prototipo.

## 8. Secuencia

```text
L1 → L2 → A1 → G1 → H1 → W1 → control esencial
```

A1 y G1 pueden aplazarse, pero en ese caso `projects/Mapa simbólico Mundial/` debe conservarse explícitamente como dependencia técnica y no puede declararse archivado por completo.

## 9. Operaciones excluidas

- SQL y conexión a bases de datos;
- ejecución de scripts de datos;
- commit, push y despliegue;
- modificación de `RG2025_V1`, `POB_URB` o `ECO_PC/MDE`.
