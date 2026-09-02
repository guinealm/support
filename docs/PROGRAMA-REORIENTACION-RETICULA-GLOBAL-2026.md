# Programa de reorientación — Retícula Global 2025

**Dirección:** Codex, bajo decisión final del usuario  
**Inicio:** 2 de septiembre de 2026  
**Dedicación máxima:** 30 horas  
**Aplicación canónica:** `projects/mapa-mundi/`  
**Estado de datos:** `RG2025_V1` congelada

## 1. Objetivo

Reordenar el proyecto, retirar material prescindible de forma controlada y crear una portada didáctica mínima que conduzca al explorador analítico ya validado.

El programa se coordina con una segunda línea, **Jumalenin como guía de trabajo en Codex para Windows**, encargada de documentar el método general de trabajo del ecosistema sin mezclarlo con el código específico de Retícula Global.

## 2. Alcance

- inventario de las tres zonas relacionadas con Retícula Global;
- clasificación de archivos y carpetas como `CONSERVAR`, `MOVER`, `ARCHIVAR`, `BORRAR` o `REVISAR`;
- resolución planificada de dependencias que impiden limpiar el directorio histórico;
- reorganización de documentación y archivos de trabajo;
- definición y construcción mínima de una portada didáctica;
- conexión con el explorador y las fichas actuales;
- validación local esencial.

## 3. Exclusiones y puertas

Sin autorización expresa y específica no se ejecutarán:

- SQL o conexiones a bases de datos;
- cambios en API, PHP, JSON, GeoJSON, indicadores o metodología;
- borrados o movimientos materiales;
- commit, push o despliegue.

`POB_URB` permanece pendiente. `ECO_PC/MDE` conserva valor, metadatos y advertencia de comparabilidad limitada.

## 4. Plan de 30 horas

| Fase | Resultado | Horas |
|---|---|---:|
| 0A — Inventario y dependencias | Catálogo completo y mapa de referencias | 6 |
| 0B — Limpieza y reorganización | Lista aprobable y ejecución recuperable | 6 |
| 8A — Dirección de portada | Estructura, mensaje y wireframe único | 4 |
| 8B — Construcción mínima | Portada local responsive | 9 |
| 8C — Integración | Enlaces con explorador y fichas | 3 |
| 8D — Control esencial y cierre | Carga, enlaces, móvil y teclado básico | 2 |
| **Total** |  | **30** |

## 5. Orden obligatorio

1. No tocar la aplicación activa durante el inventario.
2. Detectar referencias entrantes y salientes antes de proponer movimientos.
3. Separar contenido histórico útil de duplicados técnicos.
4. Presentar una lista exacta de retirada al usuario.
5. Ejecutar borrados solo tras autorización expresa y usando una operación recuperable cuando sea posible.
6. Construir la portada después de estabilizar la topología.
7. Detenerse al completar el cierre de 30 horas; no iniciar contenidos extensos de área.

## 6. Topología objetivo provisional

```text
projects/
├── mapa-mundi/                 # producto activo y documentación vigente
│   ├── index.html              # futura portada didáctica
│   ├── explorar.html           # futuro explorador analítico
│   ├── area.html
│   ├── assets/
│   ├── data/
│   └── docs/
├── reticula-global/            # se absorbe o conserva solo si justifica función propia
└── Mapa simbólico Mundial/     # archivo temporal hasta extraer dependencias vivas
```

Esta topología no autoriza movimientos. Debe confirmarse con el inventario 0A.

## 7. Decisiones de dirección ya tomadas

- No habrá una cuarta implementación paralela.
- `projects/mapa-mundi/` seguirá siendo la fuente canónica del frontend.
- Las versiones antiguas se evaluarán como referencias, no como bases de código.
- El control de calidad se reduce a dos horas y cubre únicamente fallos bloqueantes.
- La iconografía humana queda fuera de esta primera ejecución de 30 horas; solo podrá aparecer como investigación posterior.

## 8. Criterio de cierre

- topología simplificada y documentada;
- material prescindible retirado con autorización y registro;
- portada didáctica mínima conectada al explorador;
- aplicación cargando localmente sin enlaces críticos rotos;
- backlog posterior separado;
- informe de archivos conservados, movidos, archivados y borrados.

## 9. Seguimiento

El estado ejecutivo del programa se mantiene en:

`docs/ESTADO-PROGRAMA-RETICULA-GLOBAL-2026.md`

La guía transversal de trabajo está disponible en:

`C:/jumalenin-ecosistema/docs/CODEX-WINDOWS.md`
