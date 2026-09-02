# Registro de tareas — Programa Retícula Global 2026

**Programa:** reorientación, limpieza y portada didáctica  
**Presupuesto máximo:** 30 horas  
**Coordinación:** `docs/ESTADO-PROGRAMA-RETICULA-GLOBAL-2026.md`

## Reglas del registro

- Una tarea produce un único resultado verificable.
- Cada tarea declara rutas, exclusiones, evidencia y criterio de cierre.
- El cierre de una tarea no inicia automáticamente la siguiente.
- Los borrados y movimientos se aprueban por lotes exactos.
- SQL, commit, push y despliegue conservan puertas independientes.

## Backlog dirigido

| ID | Tarea | Horas | Estado | Dependencia | Resultado esperado |
|---|---|---:|---|---|---|
| RG-00 | Crear infraestructura del programa | 1 | Cerrada | — | Programa, workspace y tareas VS Code |
| RG-01 | Crear guía Jumalenin/Codex Windows | 1 | Cerrada | — | Manual, plantilla y backlog transversal |
| RG-02 | Inventariar carpetas y dependencias | 4 | Cerrada | — | Informe preliminar con hashes y tamaños |
| RG-03 | Aprobar y ejecutar limpieza segura | 2 | Cerrada | RG-02 | Primer lote borrado y verificado |
| RG-04 | Definir topología final | 2 | Cerrada | RG-03 | Árbol final y mapa de movimientos |
| RG-05 | Reubicar documentación y herramientas | 4 | Cerrada | RG-04 y autorización | Una ruta funcional principal |
| RG-06 | Consolidar dependencia de API | 2 | Cerrada | autorización API/PHP | Directorio histórico sin dependencia viva |
| RG-07 | Retirar duplicados restantes | 2 | Pendiente | RG-05 y RG-06 | Copias redundantes eliminadas |
| RG-08 | Definir portada mínima | 2 | Cerrada | — | Dirección y wireframe único |
| RG-09 | Construir portada y conservar explorador | 6 | Cerrada | RG-05 | Portada local y explorador separado |
| RG-10 | Integrar portada, explorador y fichas | 2 | Cerrada | RG-09 | Navegación coherente |
| RG-11 | Control esencial y cierre | 2 | Cerrada para W1 | RG-10 | Prueba local y cierre documental |
| **Total** |  | **30** |  |  |  |

## Puertas pendientes

### Puerta L1 — borrado seguro

Rutas propuestas:

- `projects/Mapa simbólico Mundial/ne_10m_admin_0_countries.zip`;
- `projects/Mapa simbólico Mundial/Mapa simbólico v1.html.txt`;
- `projects/reticula-global/__pycache__/`.

Estado: **ejecutado y verificado el 2 de septiembre de 2026**.

Conformidad: **otorgada por el usuario el 2 de septiembre de 2026**.

### Puerta L2 — reorganización

Alcance: movimientos de informes, herramienta de validación, generadores y archivo histórico.  
Estado: **lote documental y herramienta de validación ejecutados; referencias actualizadas**. A1 está cerrado; G1 y H1 siguen pendientes y requieren sus autorizaciones específicas.

Conformidad L2 y W1: **otorgada por el usuario el 2 de septiembre de 2026**.

### Puerta A1 — API/PHP

Alcance previsto: eliminar la dependencia desde `api/reticula/v1/datos.php` hacia `projects/Mapa simbólico Mundial/api/reticula/v1/datos.php`.  
Estado: **autorizado, ejecutado y verificado estáticamente el 2 de septiembre de 2026**. PHP no está instalado en el entorno local, por lo que `php -l` queda pendiente; no se ejecutó la API ni se abrió conexión a base de datos.

### Puertas de entrega

- Commit: no autorizado.
- Push: no autorizado.
- Despliegue: no autorizado.

## Criterio de cierre del programa

RG-03 a RG-11 están cerradas, el total no supera 30 horas y el informe final enumera archivos conservados, movidos, archivados, borrados y modificados.
