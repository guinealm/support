# Inventario preliminar de reorganización y limpieza

> Nota de ejecución (2 de septiembre de 2026): L1 fue retirado y el contenido aprobado de L2 fue trasladado a `projects/mapa-mundi/docs/` y `projects/mapa-mundi/tools/validacion/`. Las rutas antiguas que siguen en este informe documentan el inventario previo y no describen la topología vigente.

**Fase:** 0A  
**Fecha:** 2 de septiembre de 2026  
**Estado:** inventario histórico; L1 y L2 ejecutados con autorización posterior

## 1. Resumen ejecutivo

Actualmente existen tres zonas locales relacionadas:

| Zona | Archivos | Tamaño aproximado | Decisión preliminar |
|---|---:|---:|---|
| `projects/mapa-mundi/` | 14 | 4,3 MB | `CONSERVAR` — aplicación activa y canónica |
| `projects/reticula-global/` | 10 | 0,1 MB | `MOVER` parcialmente — informes y soporte local |
| `projects/Mapa simbólico Mundial/` | 266 | 84,1 MB | `REVISAR` por bloques — archivo histórico con dependencias vivas |

No es seguro borrar en bloque ninguna de las dos carpetas auxiliares. Sí existen duplicados y salidas sustituibles que permiten una primera limpieza controlada.

## 2. Dependencias vivas que bloquean un borrado general

### API

La ruta pública estable:

`api/reticula/v1/datos.php`

ejecuta mediante `require`:

`projects/Mapa simbólico Mundial/api/reticula/v1/datos.php`

El directorio histórico contiene además `bootstrap.php`, `status.php` y documentación de la API. Antes de retirar ese árbol hay que trasladar la implementación a una ubicación canónica y modificar PHP. Esa operación queda fuera de esta fase y requiere autorización expresa para cambios de API/PHP.

### Generación de datos estáticos

`projects/Mapa simbólico Mundial/mapa/` sigue documentado como fuente de trabajo de los generadores del mapa. La salida de navegador está en `projects/mapa-mundi/`, pero los generadores leen materiales de `reticula_global_1c2_runner/` y Natural Earth.

Por ello se debe separar:

- código generador y fuentes reproducibles: conservar o mover;
- copias de resultados ya presentes en la aplicación activa: candidatas a borrar;
- versiones históricas HTML/CSS/JS: archivar o retirar después de comparar.

## 3. Duplicados confirmados mediante SHA-256

Los siguientes archivos de `projects/Mapa simbólico Mundial/mapa/` son idénticos a los de `projects/mapa-mundi/`:

- `areas.json`;
- `correspondencias-cartograficas.json`;
- `datos-indicadores.json`;
- `paleta.json`;
- `territorios.json`;
- `world.geojson`.

Estas seis copias ocupan aproximadamente **4,26 MB**. Son candidatas a retirada del árbol histórico cuando se documente que la copia canónica es la de `projects/mapa-mundi/` y se ajuste el flujo de los generadores para escribir allí o en una carpeta temporal.

Los archivos `index.html`, `mapa.css`, `mapa.js`, `area.html`, `area.css` y `area.js` tienen el mismo nombre pero contenido diferente. No se consideran duplicados exactos. La versión activa es la de `projects/mapa-mundi/`; las copias históricas deben compararse antes de decidir `ARCHIVAR` o `BORRAR`.

## 4. Candidatos preliminares

### BORRAR — alta confianza, pendiente de autorización

| Elemento | Motivo | Recuperación estimada |
|---|---|---:|
| `projects/Mapa simbólico Mundial/ne_10m_admin_0_countries.zip` | El contenido ya está extraído y el generador usa `natural-earth-source/` | 4,70 MB |
| `projects/Mapa simbólico Mundial/Mapa simbólico v1.html.txt` | Hash idéntico a `Mapa simbolico v1.html` | 0,03 MB |
| `projects/reticula-global/__pycache__/` | Caché reproducible de Python | mínima |

**Total inmediato de alta confianza: aproximadamente 4,73 MB.**

### BORRAR — confianza media, requiere adaptar primero el flujo

| Elemento | Condición previa | Recuperación estimada |
|---|---|---:|
| Seis JSON/GeoJSON idénticos de `projects/Mapa simbólico Mundial/mapa/` | Fijar `projects/mapa-mundi/` como salida canónica de los generadores | 4,26 MB |
| Backups repetidos de `reticula_global_1c2_runner/output_1c2/` | Identificar la última copia válida y conservar trazabilidad suficiente | 0,40 MB aprox. |

### ARCHIVAR — no borrar ahora

- `Mapa simbolico v1.html` a `Mapa simbolico v5.html`: muestran la evolución conceptual; ocupan poco y pueden reunirse en un archivo histórico.
- Documentos `.docx` y `.pdf` de introducción, bloques y conclusión: son fuentes previstas para contenidos futuros. Los `.docx` concentran unos 58 MB, pero no son residuos demostrados.
- Informes de fases cerradas: conservar como trazabilidad, agrupados por etapa.
- SQL históricos: no ejecutarlos; decidir su política de archivo en una fase específica de datos.

### MOVER — estructura objetivo pendiente de autorización

1. Informes vigentes de `projects/reticula-global/` a `projects/mapa-mundi/docs/seguimiento/`.
2. Informes cerrados a `projects/mapa-mundi/docs/historico/`.
3. `servidor_validacion_local.py` a `projects/mapa-mundi/tools/validacion/`.
4. Generadores del mapa a `projects/mapa-mundi/tools/generacion/`, manteniendo las fuentes fuera de la salida pública.
5. Documentos narrativos extensos a un archivo explícito, no mezclado con la aplicación activa.

Estos movimientos reducirían la topología funcional a una sola carpeta de producto. Antes de ejecutarlos deben actualizarse todas las referencias internas.

## 5. Topología propuesta tras la limpieza

```text
projects/mapa-mundi/
├── index.html
├── explorar.html
├── area.html
├── assets/
├── data/
├── tools/
│   ├── generacion/
│   └── validacion/
└── docs/
    ├── seguimiento/
    └── historico/

archive/reticula-global/
├── prototipos-v1-v5/
├── documentos-fuente/
└── preparacion-datos/
```

La ubicación final de `archive/` debe decidirse antes de mover archivos para no convertir material histórico en contenido público accidental.

## 6. Orden de ejecución recomendado

1. Autorizar únicamente el lote de borrado de alta confianza.
2. Definir el destino no público del archivo histórico.
3. Autorizar movimientos documentales y actualizar referencias Markdown.
4. Autorizar por separado la consolidación de PHP/API.
5. Trasladar generadores y fijar una única salida canónica.
6. Volver a calcular hashes y retirar las copias estáticas duplicadas.
7. Comprobar carga local, enlaces y ausencia de referencias a rutas retiradas.

## 7. Plan de reversión

- ejecutar movimientos y borrados en lotes pequeños y enumerados;
- registrar cada ruta de origen y destino;
- preferir traslado a archivo sobre borrado cuando exista valor histórico incierto;
- comprobar el estado local después de cada lote;
- no combinar limpieza, modificación de API y rediseño visual en una misma actuación.

## 8. Decisión necesaria

La primera autorización futura puede limitarse al lote de alta confianza: ZIP de Natural Earth ya extraído, duplicado textual de `v1` y caché de Python. No se requiere todavía decidir sobre los 58 MB de documentos fuente ni sobre la API.
