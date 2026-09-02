# Fase 8 — Consolidación de versión y preparación de publicación

**Fecha de inicio:** 2 de septiembre de 2026  
**Estado:** preparada; ejecución documental iniciada  
**Edición de datos:** `RG2025_V1` congelada

## 1. Objetivo concreto

Convertir el GO funcional de la Fase 7E en una versión local identificable y un expediente coherente para que commit, push y despliegue puedan decidirse posteriormente como operaciones separadas y expresamente autorizadas.

## 2. Rutas incluidas

- `Informe de seguimiento — Retícula Global.md`.
- `projects/reticula-global/INFORME-SEGUIMIENTO-RETICULA-GLOBAL-2026-07-30.md`.
- Informes de 7D y 7E como evidencia de solo lectura.
- `projects/mapa-mundi/` únicamente para inventario local de archivos y futuras comprobaciones estáticas o de navegador local autorizadas por el alcance.

La aplicación canónica continúa en `projects/mapa-mundi/`. Los informes continúan en `projects/reticula-global/`.

## 3. Exclusiones

- API, PHP, MySQL, SQL y scripts de datos.
- JSON, GeoJSON, indicadores, valores y metodología.
- Incorporación de `POB_URB`.
- Modificación o eliminación de la advertencia de `ECO_PC/MDE`.
- Nuevas gráficas, contenidos o funcionalidades.
- Commit, amend, tags, push y despliegue.
- Escritura o validación contra la web pública.

## 4. Estado reconciliado

- El 78 % del informe del 30 de julio es histórico y anterior a 7D/7E.
- 7D terminó con GO.
- 7E.1, 7E.2, 7E.3 y 7E.4 terminaron con GO.
- La validación visual real de 7E.4 fue completada por el usuario.
- No quedan defectos bloqueantes conocidos dentro del alcance de 7E.
- `POB_URB` permanece pendiente y fuera del cierre.
- `ECO_PC/MDE` conserva su tratamiento metodológico limitado.
- «Preparada para publicación» no acredita que producción corresponda a la versión validada.

## 5. Identificación local inicial

- Repositorio: `sites/support`.
- Rama observada al inicio: `main`.
- Commit observado al inicio: `d6084b56bea5a3ce8d9b6a34c7a4309b35645f49`.
- Estado observado antes de estas ediciones documentales: árbol de trabajo limpio.

Esta identificación describe la copia local al iniciar la fase. No acredita por sí sola el estado de un remoto ni de producción.

## 6. Evidencia de validación esperada

- Informes sin contradicciones vigentes sobre 7D, 7E, el 78 % o las horas restantes.
- Inventario trazable de la versión local candidata.
- `git diff --check` sin errores documentales.
- Confirmación de que los cambios de esta fase se limitan a Markdown.
- Checklist posterior para página principal, nueve fichas, teclado, foco, responsive, zoom, estados de error y `prefers-reduced-motion`.
- Protección explícita de `POB_URB` y `ECO_PC/MDE`.

## 7. Checklist previo a una decisión de publicación

- [ ] Revisar el diff documental de la Fase 8.
- [ ] Identificar el commit exacto que se propondría publicar.
- [ ] Confirmar que no existen cambios funcionales ajenos al GO de 7E.
- [ ] Repetir la validación local proporcionada al riesgo, sin ejecutar API ni proxy sin autorización.
- [ ] Documentar cualquier diferencia entre la versión local, el remoto y producción.
- [ ] Solicitar por separado autorización expresa para commit, si procede.
- [ ] Solicitar por separado autorización expresa para push, si procede.
- [ ] Solicitar por separado autorización expresa para despliegue, si procede.
- [ ] Ejecutar una comprobación posterior a la publicación solo si su fase y alcance son autorizados.

## 8. Criterio de cierre

La Fase 8 podrá cerrarse cuando exista un expediente documental coherente, una versión local candidata inequívoca y una lista de comprobación satisfecha, sin defectos bloqueantes conocidos. El cierre de esta fase no ejecuta ni autoriza commit, push o despliegue.

## 9. Operaciones bloqueadas no realizadas

No se ejecutaron SQL, conexiones a base de datos, API, proxy local, commit, push ni despliegue. No se modificaron la aplicación, PHP, JSON, GeoJSON, datos, indicadores ni metodología.
