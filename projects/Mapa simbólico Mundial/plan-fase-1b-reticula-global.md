# Plan de trabajo Fase 1B

## 1) Objetivo

Ejecutar correcciones funcionales y de comprensión mínima sobre la versión activa de Retícula Global 2025, partiendo del diagnóstico 1A, sin rediseño integral ni reorganización grande del proyecto.

Archivo objetivo principal:

- `Mapa simbolico v5.html`

Documento base:

- `diagnostico-funcional-reticula-global-1a.md`

## 2) Alcance de esta fase

Incluye:

- P1 funcionales.
- P2 funcionales y conceptuales de impacto inmediato.
- Consolidación mínima de versión activa a nivel documental/técnico.

No incluye:

- Rediseño visual completo.
- Limpieza total de versiones históricas.
- Refactor estructural profundo (migración completa a CSS/JS separados).

## 3) Orden de ejecución

1. Robustez de recursos críticos.
2. Comportamiento real del visor de documentos.
3. Claridad conceptual mínima en la interfaz.
4. Consolidación técnica ligera para evitar ambigüedad de versión.
5. Validación final escritorio/móvil + regresión funcional.

## 4) Checklist operativo

### Bloque A - P1 funcional: recursos externos frágiles

- [ ] Identificar recursos remotos críticos (fondo, CDN de estilos, CDN de gráficos, fuentes).
- [ ] Definir fallback mínimo para el fondo si falla la carga remota.
- [ ] Verificar degradación aceptable cuando falle un recurso externo no crítico.

Criterios de aceptación:

- [ ] La app sigue siendo usable si falla la imagen remota de fondo.
- [ ] No hay errores JS bloqueantes por ausencia de recursos decorativos.

### Bloque B - P1/P2 funcional: visor de documentos

- [ ] Decidir comportamiento objetivo: abrir PDF real o mantener simulación explícita.
- [ ] Implementar el comportamiento elegido de forma coherente en bloques, tabla y conclusión.
- [ ] Evitar estados inconsistentes al abrir/cerrar múltiples veces.

Criterios de aceptación:

- [ ] Todas las entradas abren el mismo tipo de salida (real o simulada) sin mezcla.
- [ ] No quedan enlaces con comportamiento distinto al resto sin explicación.

### Bloque C - P2 conceptual: comprensión mínima

- [ ] Añadir contexto breve que explique qué representa la retícula.
- [ ] Añadir leyenda mínima para color y naturaleza simbólica/geopolítica de los bloques.
- [ ] Diferenciar explícitamente representación conceptual vs cartografía exacta.

Criterios de aceptación:

- [ ] Un usuario nuevo entiende en menos de 30 segundos qué está viendo.
- [ ] Se reduce la ambigüedad sobre significado de colores y bloques.

### Bloque D - P2 técnico: versión activa

- [ ] Documentar en cabecera/comentario del archivo activo que `v5` es la versión de trabajo.
- [ ] Registrar en documento breve qué archivos son históricos y no tocar en esta fase.

Criterios de aceptación:

- [ ] No hay dudas operativas sobre qué archivo modificar.

### Bloque E - QA y cierre de fase

- [ ] Probar controles (bloques, tabla, modal, cierre).
- [ ] Probar tamaños: 1440x900, 1366x768, 768x1024, 360x800, 800x360.
- [ ] Registrar incidencias residuales para Fase 1C.

Criterios de aceptación:

- [ ] Sin errores bloqueantes en consola durante flujo normal.
- [ ] Sin regresiones funcionales respecto al estado validado en 1A.

## 5) Riesgos de implementación

- Cambiar de simulación a PDF real puede introducir diferencias de experiencia entre navegadores.
- Ajustar recursos externos sin estrategia de fallback puede romper la percepción visual esperada.
- Tocar versión incorrecta (v1-v4) en vez de v5 puede dispersar el avance.

## 6) Definición de terminado (DoD) Fase 1B

- Se completan bloques A, B y C con criterios de aceptación cumplidos.
- Se deja trazabilidad mínima de versión activa (bloque D).
- Se ejecuta QA de bloque E y se documentan pendientes para la siguiente fase.

## 7) Primera iteración recomendada

Para comenzar de inmediato, el primer ciclo recomendado es:

1. Resolver Bloque B (decisión del visor).
2. Resolver Bloque A (fallback de recursos críticos).
3. Aplicar Bloque C (leyenda/contexto mínimo).
4. Pasar QA rápido en 5 tamaños.
