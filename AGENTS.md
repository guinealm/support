# Instrucciones de Codex — Jumalenin Support

## Alcance

- Estas reglas complementan las instrucciones globales de `C:\jumalenin-ecosistema\AGENTS.md` y se aplican a todo `sites/support`.
- Support es un repositorio Git independiente dentro del ecosistema. Trabaja desde `C:\jumalenin-ecosistema\sites\support` cuando necesites contexto Git.
- Conserva HTML, CSS y JavaScript existentes y evita incorporar frameworks o dependencias sin una decisión explícita.

## Operaciones bloqueadas sin autorización expresa

Estas prohibiciones son autosuficientes y no dependen de que Codex haya cargado las instrucciones del directorio superior. No prepares, modifiques ni ejecutes ninguna de estas operaciones salvo autorización expresa del usuario en la conversación actual:

1. **SQL y bases de datos:** consultas SQL de cualquier clase, migraciones, importaciones, cargas, volcados, cambios de esquema o datos, y comandos o scripts que puedan conectarse a una base de datos.
2. **Commit:** `git commit`, amend, creación de tags o cualquier cambio equivalente del historial Git.
3. **Push:** `git push`, publicación de ramas o tags, y cualquier escritura en un remoto Git.
4. **Despliegue:** publicación, sincronización o transferencia a producción, staging, hosting, servidor, CDN o servicio remoto; también comandos de build que formen parte directa de un despliegue.

La autorización debe nombrar la operación y su alcance. Una petición general como «continúa», «termina» o «haz la migración» no autoriza estas acciones. La autorización de una puerta no autoriza las demás ni se reutiliza para otro alcance.

## Topología de Retícula Global

- `projects/mapa-mundi/`: aplicación web activa de Retícula Global. Es la ruta funcional principal.
- `projects/mapa-mundi/docs/`: informes de seguimiento y revisión de Retícula Global.
- `projects/mapa-mundi/tools/validacion/`: soporte de validación local; no ejecutar el proxy sin autorización expresa.
- `projects/Mapa simbólico Mundial/`: archivo histórico, metodológico, documental y de preparación de datos. La API ya fue consolidada en su ruta canónica mediante A1. Trátalo como material de referencia; no lo reorganices ni lo conviertas en aplicación activa por iniciativa propia.
- `api/reticula/`: API del proyecto. Inspección de código permitida; ejecución, cambios de SQL, base de datos o datos requieren autorización expresa conforme a estas reglas.

No dupliques cambios entre estas zonas. Antes de editar, identifica cuál es la fuente canónica del elemento afectado.

## Estado de Retícula Global 2025

- La edición `RG2025_V1` y su metodología se consideran congeladas salvo decisión expresa del usuario.
- La Fase 7E figura cerrada con resultado GO en la documentación de seguimiento del 30 de julio de 2026.
- `POB_URB` permanece pendiente de incorporación.
- `ECO_PC/MDE` debe conservar su advertencia de comparabilidad limitada, metadatos y valor visible.
- No inventes datos, no sustituyas ausencias por cero y no elimines advertencias metodológicas.

## Forma de trabajo específica

- Empieza por leer `docs/MIGRACION-CODEX-RETICULA-GLOBAL.md` y el informe de fase relacionado en `projects/mapa-mundi/docs/seguimiento/`.
- Prioriza cambios pequeños y comprobables en navegador local.
- Preserva navegación por teclado, foco visible, semántica, mensajes de error, comportamiento responsive y `prefers-reduced-motion`.
- No uses la web pública como objetivo de escritura ni como sustituto de una validación local controlada.
- No ejecutes el proxy local, llamadas a la API, SQL ni scripts de datos sin autorización expresa.
- No modifiques PHP, API, JSON, indicadores, metodología ni datos cuando la tarea sea visual o editorial.
- Al cerrar, indica la fase, archivos tocados, pruebas locales, limitaciones y operaciones bloqueadas no realizadas.

## Inicio de tareas nuevas

Cada tarea debe declarar:

1. objetivo concreto;
2. rutas incluidas;
3. exclusiones, especialmente datos/API/SQL;
4. evidencia de validación esperada;
5. criterio de cierre.

No continúes automáticamente con otra fase después de cumplir el criterio de cierre.
