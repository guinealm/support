# Informe de seguimiento — Retícula Global 2025

**Fecha:** 30 de julio de 2026  
**Entorno:** `support.jumalenin.com`  
**Edición de datos:** `RG2025_V1` congelada

## 1. Estado general

La aplicación ya dispone de una base funcional sólida:

- mapa mundial dividido en nueve macroáreas;
- fichas individuales por macroárea;
- comparación general de territorio, población, economía y dimensión militar;
- API pública conectada a MySQL;
- bloque «Perfil medio de la población» en la página principal;
- bloque equivalente en las fichas de área;
- fuentes, años y observaciones metodológicas consultables;
- tratamiento visible de datos limitados;
- navegación entre mapa y fichas.

**Avance funcional estimado de la aplicación: 78 %.**

La estimación se refiere a la aplicación prevista actualmente, no a todas las ampliaciones posibles de indicadores, gráficas y contenidos didácticos.

> **Actualización del 2 de septiembre de 2026:** este porcentaje es una fotografía histórica anterior a las fases 7D y 7E. No debe utilizarse como medida del estado vigente. La Fase 7E quedó posteriormente cerrada con **GO** y sin defectos bloqueantes conocidos en su alcance.

## 2. Estado de las fases recientes

| Fase | Resultado | Estado |
|---|---|---|
| 7A — Preparación de indicadores complementarios | Cinco indicadores disponibles; `POB_URB` pendiente; limitación de `ECO_PC/MDE` documentada | Cerrada con limitaciones |
| 7B — Perfil medio en la página principal | Nueve tarjetas, cinco valores, urbanización pendiente y observaciones desplegables | **GO** |
| 7C — Perfil medio en fichas de área | Perfil incorporado a las fichas y navegación desde las tarjetas | **GO** |
| 7D — Revisión funcional y accesibilidad | Pendiente de ejecución | Siguiente fase |

### Actualización posterior

| Fase | Resultado | Estado vigente |
|---|---|---|
| 7D — Revisión funcional y accesibilidad | Accesibilidad, estados, metadatos y comportamiento responsive revisados | **GO** |
| 7E — Revisión funcional y cierre visual | Inventario, correcciones limitadas y validación visual real completados | **GO — cerrada** |

## 3. Datos actualmente visibles

El perfil muestra:

- densidad;
- edad mediana;
- esperanza de vida;
- PIB por habitante;
- IDH;
- urbanización como «Pendiente de incorporación».

En Oriente Medio, `ECO_PC` conserva:

- valor numérico;
- estado de limitación;
- advertencia de comparabilidad;
- fuente;
- año;
- cobertura;
- observación metodológica.

No se han realizado nuevas cargas ni cambios en MySQL durante 7B y 7C.

## 4. Situación técnica

### Elementos estables

- `/api/reticula/v1/datos.php`
- MySQL `RG2025_V1`
- regionalización de nueve áreas
- página principal `projects/mapa-mundi/`
- fichas mediante `area.html?codigo=...`
- respaldo local existente
- Tabla de Datos Consolidados

### Decisiones vigentes

- no volver ahora a tareas de carga MySQL;
- mantener `POB_URB` como pendiente;
- priorizar trabajo visible en navegador;
- no modificar la metodología congelada;
- realizar cambios pequeños, comprobables y versionados.

## 5. Trabajo pendiente estimado

| Bloque pendiente | Dedicación estimada |
|---|---:|
| 7D — Funcionalidad y accesibilidad | 3–5 h |
| Revisión móvil completa del mapa y fichas | 3–4 h |
| Gráficas y comparaciones visuales adicionales | 6–10 h |
| Revisión editorial y metodológica | 4–6 h |
| Prueba real de usuario | 4–6 h |
| Correcciones y cierre de edición | 5–8 h |

**Trabajo restante estimado:** 25–39 horas.

Con una dedicación aproximada de diez horas semanales, el núcleo actual podría cerrarse en unas **tres o cuatro semanas**, sin incorporar nuevos bloques importantes de datos.

> **Actualización del 2 de septiembre de 2026:** esta estimación también es histórica. 7D, la revisión móvil, la validación visual y las correcciones de cierre fueron absorbidas por 7D y 7E. Las gráficas adicionales y otras ampliaciones pasan a considerarse mejoras opcionales, no requisitos de cierre del núcleo actual.

## 6. Próxima fase

### Fase 7D — Revisión funcional y accesibilidad

Objetivo:

- revisar el bloque del perfil en la página principal y en las fichas;
- comprobar navegación por teclado;
- mejorar foco visible, semántica y contraste;
- revisar el comportamiento responsive;
- conservar sin cambios los datos, la API, MySQL y la metodología;
- mantener `POB_URB` como pendiente;
- mantener visible la limitación de `ECO_PC/MDE`.

## 7. Estado de cierre del informe

- **Fase 7B:** GO.
- **Fase 7C:** GO.
- **Siguiente fase:** 7D.
- **Estado global estimado:** 78 %.

## 8. Reconciliación del 2 de septiembre de 2026

- **Fase 7D:** GO.
- **Fase 7E:** GO y cerrada.
- **Estado vigente:** núcleo funcional cerrado, sin defectos bloqueantes conocidos y preparado para consolidación previa a publicación.
- **Siguiente fase:** Fase 8 — Consolidación de versión y preparación de publicación.
- `POB_URB` continúa pendiente y fuera del cierre.
- `ECO_PC/MDE` mantiene valor, metadatos y advertencia de comparabilidad limitada.
- No consta en estos informes que la versión validada haya sido publicada.

El alcance completo de la siguiente fase figura en `FASE-8-CONSOLIDACION-Y-PREPARACION-PUBLICACION-2026-09-02.md`.
