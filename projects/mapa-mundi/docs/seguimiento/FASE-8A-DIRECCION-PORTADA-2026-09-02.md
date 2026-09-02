# Fase 8A — Dirección mínima de la portada didáctica

**Estado:** dirección definida; construcción no iniciada  
**Dedicación asignada:** 4 horas  
**Fuentes examinadas:** referencias indicadas en `projects/mapa-mundi/docs/Reorientacion.md`

## 1. Objetivo concreto

Definir una única dirección de portada que haga Retícula Global más accesible y didáctica sin reconstruir el explorador analítico ni recuperar datos de demostración de los prototipos antiguos.

## 2. Rutas incluidas

- aplicación activa `projects/mapa-mundi/`, solo como referencia;
- `projects/mapa-mundi/docs/Reorientacion.md`;
- referencia `mapa_mundi.html` de OneDrive;
- referencia `Home Page/Mapa simbólico Mundial/Mapa simbolico v5.html` de OneDrive.

## 3. Exclusiones

- cambios en HTML, CSS o JavaScript de la aplicación activa;
- API, PHP, SQL, bases de datos, JSON, GeoJSON e indicadores;
- incorporación de los datos estáticos de los prototipos;
- producción de iconografía humana;
- commit, push y despliegue.

## 4. Evaluación de las referencias

### Elementos que conviene recuperar

- una entrada visual inmediata, sin comenzar por la metodología;
- identidad de atlas estratégico;
- protagonismo del mapa o retícula territorial;
- nombre y frase distintiva de cada macroárea;
- acceso directo desde cada área a su ficha;
- relación visible entre panorama general y documentación detallada;
- contraste más decidido que el tono académico de la pantalla actual.

### Elementos que no deben heredarse

- división antigua de diez bloques, incompatible con las nueve macroáreas vigentes;
- mapas esquemáticos dibujados manualmente;
- cifras estáticas o de demostración;
- índices compuestos sin metodología validada;
- Tailwind cargado desde CDN, Chart.js y fuentes externas como dependencias nuevas;
- manejadores `onclick` y controles construidos con elementos no semánticos;
- visor de PDF simulado;
- fondos cartográficos o texturas remotas;
- terminología UTM usada como recurso decorativo cuando no describe la proyección real.

## 5. Dirección elegida

**Portada editorial cartográfica de una sola pantalla inicial.**

La portada debe presentar la idea antes que los datos:

1. cabecera breve de Jumalenin;
2. título `Retícula Global 2025`;
3. explicación de dos frases;
4. mapa Equal Earth simplificado con las nueve áreas;
5. nueve enlaces breves con nombre y descriptor;
6. llamada principal `Explorar datos y comparaciones`;
7. acceso secundario a metodología.

El mapa puede reutilizar la geometría y paleta canónicas, pero en la portada no necesita selectores de color, tabla, descarga SVG ni tarjetas de indicadores.

## 6. Reparto de responsabilidades

| Portada | Explorador | Ficha |
|---|---|---|
| Explicar y orientar | Comparar y manipular | Profundizar en un área |
| Nueve áreas y descriptores | Datos, controles y metodología | Datos y territorio del área |
| Una llamada principal | Herramientas analíticas | Acceso al análisis futuro |

## 7. Wireframe textual

```text
┌─────────────────────────────────────────────────────────┐
│ ← Support                            Jumalenin · 2025   │
├─────────────────────────────────────────────────────────┤
│ RETÍCULA GLOBAL                                        │
│ Nueve espacios para leer un mundo interdependiente.    │
│                                                        │
│ [ MAPA EQUAL EARTH SIMPLIFICADO ]                      │
│                                                        │
│ AFR  APC  CHN  EUR  MDE  NAC  RUE  SAI  SAM           │
│                                                        │
│ [Explorar datos y comparaciones]   [Metodología]       │
└─────────────────────────────────────────────────────────┘
```

En móvil, el mapa permanece primero y las nueve áreas se presentan en una lista de tres columnas o una columna según el ancho.

## 8. Especificación reducida para 8B

- HTML, CSS y JavaScript existentes, sin framework;
- una nueva portada y una copia conservadora del explorador actual;
- reutilización de `world.geojson`, `areas.json` y `paleta.json` sin modificarlos;
- sin cifras nuevas en portada;
- sin animaciones complejas;
- sin iconografía humana;
- sin nuevos paquetes ni servicios externos;
- estado seleccionado solo si se obtiene sin duplicar la lógica existente.

## 9. Validación esperada

- la portada explica el proyecto antes de mostrar controles analíticos;
- aparecen exactamente nueve macroáreas;
- los enlaces conducen al explorador o a fichas existentes;
- no aparecen valores ni clasificaciones antiguas de diez bloques;
- escritorio y móvil básico son utilizables;
- teclado y foco visible se conservan.

## 10. Criterio de cierre

Existe una dirección única, suficientemente concreta para construir la portada en nueve horas sin reabrir decisiones de datos, metodología o arquitectura general.

