# Prompt para Codex — Ejecutar Fase 1C.2

Estamos en Jumalenin Support — Retícula Global 2025.

Usa el paquete `reticula_global_1c2_runner`.

Objetivo:

1. Instalar únicamente las dependencias de `requirements.txt`.
2. Ejecutar `construir_territorio_poblacion_1c2.py`.
3. Revisar los archivos generados en `output_1c2`.
4. No modificar todavía la aplicación pública.
5. No crear tablas MySQL.
6. No corregir manualmente datos sin documentarlo.

Comprobaciones:

- Deben existir nueve áreas.
- Revisar la suma mundial de población de 2025.
- Revisar población proyectada a 2050.
- Revisar China, Hong Kong, Macao y Taiwán.
- Revisar Kosovo.
- Revisar territorios `SEGUN_FUENTE`.
- Comprobar que ningún ausente se convirtió en cero.
- Comprobar que densidad = población agregada / superficie agregada.
- Comprobar que los porcentajes de población y superficie suman aproximadamente 100.

Entrega:

- Ruta de los archivos generados.
- Número de incidencias.
- Tabla resumida de las nueve áreas.
- Decisión GO/NO-GO para cerrar 1C.2.
- No iniciar 1C.3.
