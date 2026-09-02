# Traspaso a Codex — Jumalenin Support / Retícula Global 2025

## Decisión

El trabajo del proyecto de ChatGPT **«Jumalenin support - Retícula Global 2025»** continuará en un proyecto local nuevo de Codex, con una tarea separada para cada resultado concreto.

No se copia automáticamente el historial completo del chat al contexto de Codex. El contexto duradero debe quedar en este repositorio: instrucciones, informes, decisiones, fuentes y archivos de trabajo.

## Proyecto local recomendado

- **Nombre:** `Jumalenin Support — Retícula Global 2025`
- **Carpeta principal:** `C:\jumalenin-ecosistema\sites\support`
- **Instrucciones globales:** `C:\jumalenin-ecosistema\AGENTS.md`
- **Instrucciones locales:** `C:\jumalenin-ecosistema\sites\support\AGENTS.md`

La carpeta `sites/support` debe ser la principal porque contiene el repositorio Git independiente y permite descubrir automáticamente sus instrucciones locales. Al tratarse de la raíz Git del proyecto, no se debe depender de que Codex descubra el `AGENTS.md` situado en `C:\jumalenin-ecosistema`; por eso las cuatro puertas de autorización están repetidas íntegramente en el `AGENTS.md` local. No es necesario crear una copia de los archivos ni mover Retícula Global fuera de su estructura actual.

## Contexto canónico inicial

Leer en este orden:

1. `AGENTS.md` de la raíz del ecosistema.
2. `sites/support/AGENTS.md`.
3. `sites/support/Informe de seguimiento — Retícula Global.md`.
4. `sites/support/projects/mapa-mundi/docs/seguimiento/INFORME-SEGUIMIENTO-RETICULA-GLOBAL-2026-07-30.md`.
5. El informe de la fase concreta que se vaya a continuar.

Consultar `projects/Mapa simbólico Mundial/` solo cuando la tarea necesite antecedentes metodológicos o históricos. No cargar todo ese archivo como contexto inicial.

## Mapa de trabajo

| Zona | Función | Tratamiento inicial |
|---|---|---|
| `projects/mapa-mundi/` | Aplicación activa | Fuente canónica del frontend |
| `projects/mapa-mundi/docs/` | Seguimiento y validación | Consultar el informe de fase pertinente |
| `projects/Mapa simbólico Mundial/` | Archivo histórico y metodológico | Solo lectura salvo encargo específico |
| `api/reticula/` | API | No ejecutar ni modificar sin autorización específica |

## Estado heredado

- Retícula Global 2025 figura aproximadamente al 78 % en el informe general del 30 de julio de 2026.
- La Fase 7E se documenta posteriormente como cerrada con GO y sin defectos bloqueantes conocidos.
- La aplicación activa incluye mapa de nueve macroáreas, fichas dinámicas, perfil medio y comparación general.
- `RG2025_V1` está congelada.
- `POB_URB` sigue pendiente.
- `ECO_PC/MDE` mantiene comparabilidad limitada documentada.

Antes de iniciar desarrollo nuevo, la primera tarea debe reconciliar el porcentaje histórico del informe general con el cierre posterior de 7E y establecer el siguiente objetivo funcional vigente. Esa revisión será documental y de solo lectura.

## Información que conviene rescatar del proyecto de ChatGPT

Solo hace falta añadir manualmente aquello que no esté ya documentado en los archivos:

- decisiones posteriores al 30 de julio de 2026;
- conversaciones con criterios o acuerdos no volcados a documentos;
- archivos adjuntos que no existan en `sites/support`;
- prioridades actuales del usuario;
- incidencias conocidas todavía abiertas.

No es necesario trasladar saludos, intentos fallidos, mensajes repetidos ni todo el historial conversacional.

## Primera tarea recomendada

**Título:** `Retícula Global — reconciliar estado y definir siguiente fase`

**Prompt de inicio:**

> Revisa en modo de solo lectura las instrucciones globales y locales, el informe general de seguimiento y el cierre completo de la Fase 7E. Reconcilia el estado heredado de Retícula Global 2025, identifica contradicciones o pendientes reales y propón una única siguiente fase con alcance, exclusiones, validación y criterio de cierre. No modifiques la aplicación, API, PHP, JSON, datos ni metodología. No ejecutes SQL, commit, push o despliegue.

## Criterio de preparación completada

- proyecto local apuntando a `sites/support`;
- instrucciones globales y locales disponibles;
- topología y fuentes canónicas identificadas;
- contexto histórico reducido a documentos pertinentes;
- primera tarea independiente definida;
- SQL, commit, push y despliegue todavía bloqueados.
