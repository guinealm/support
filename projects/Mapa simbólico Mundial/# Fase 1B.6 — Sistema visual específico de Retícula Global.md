# Fase 1B.6 — Sistema visual específico de Retícula Global

## Retícula Global 2025

## 1. Objetivo

Definir el sistema visual propio de Retícula Global 2025 como una evolución de la aplicación actual y como una extensión compatible con la identidad común de Jumalenin.

La fase debe establecer:

* qué elementos visuales actuales se conservan;
* cuáles se ajustan;
* cuáles deben sustituirse;
* qué componentes nuevos necesita la aplicación;
* cómo se representan las nueve áreas;
* cómo se muestran datos, advertencias y comparaciones;
* cómo se mantiene la claridad en escritorio y móvil;
* cómo se evita una interfaz excesivamente pesada.

Esta fase no implica todavía modificar HTML, CSS, JavaScript, Common ni la portada general de Support.

---

# 2. Principio visual general

Retícula Global debe tener una apariencia:

* seria;
* contemporánea;
* didáctica;
* ligera;
* reconocible;
* compatible con Jumalenin;
* adecuada para público general y joven;
* suficientemente atractiva para motivar la exploración.

No debe parecer:

* una aplicación corporativa genérica;
* un panel financiero;
* una enciclopedia escolar infantil;
* un portal estadístico saturado;
* una colección de gráficos sin hilo narrativo;
* una web independiente ajena a Support.

## Regla principal

> La visualización debe ayudar a formar una imagen mental del mundo, no demostrar cuántos datos contiene la base.

---

# 3. Relación con la identidad visual actual

Antes de diseñar componentes nuevos deberán compararse tres niveles:

## 3.1 Visual actual de Retícula Global

Inventariar:

* cabecera;
* título;
* fondos;
* colores;
* mapa;
* tarjetas;
* tablas;
* gráficas;
* botones;
* enlaces;
* tipografías;
* iconos;
* espacios;
* bordes;
* comportamiento responsive.

## 3.2 Identidad común de Jumalenin

Revisar únicamente como referencia:

* tipografía común;
* logo;
* favicon;
* cabecera;
* navegación;
* pie;
* paleta base;
* estilos de botones;
* tarjetas;
* anchos máximos;
* reglas responsive.

No se modificará Common.

## 3.3 Extensión específica de Retícula Global

Definir reglas propias para:

* colores de las nueve áreas;
* mapa;
* tablas comparativas;
* indicadores;
* gráficas;
* leyendas;
* avisos metodológicos;
* fichas de área;
* navegación temática.

---

# 4. Clasificación de elementos actuales

Cada elemento visual existente deberá clasificarse con una de estas decisiones:

| Decisión  | Criterio                                     |
| --------- | -------------------------------------------- |
| Conservar | Funciona, se entiende y encaja con Jumalenin |
| Ajustar   | La base es válida, pero necesita mejoras     |
| Sustituir | No cumple su función o genera confusión      |
| Añadir    | Es necesario y no existe                     |
| Posponer  | Puede ser útil, pero no es prioritario       |

## Resultado esperado

Crear un inventario visual con esta estructura:

| Elemento | Estado actual | Decisión               | Motivo | Prioridad |
| -------- | ------------- | ---------------------- | ------ | --------- |
| Cabecera | Descripción   | Conservar/Ajustar/etc. | Razón  | P1–P3     |

Este inventario deberá formar parte del diagnóstico o de un documento complementario de 1B.6.

---

# 5. Estructura visual de página

## 5.1 Ancho y composición

La aplicación utilizará:

* ancho máximo de lectura;
* márgenes laterales estables;
* secciones claramente separadas;
* espacios verticales generosos;
* fondos diferenciados con moderación.

La portada no deberá parecer una única página interminable sin pausas visuales.

## 5.2 Ritmo de contenido

Alternancia recomendada:

1. introducción;
2. mapa;
3. tarjetas;
4. tabla;
5. gráfica;
6. explicación;
7. acceso a detalle.

Cada bloque debe responder a una pregunta distinta.

## 5.3 Secciones

Las secciones deberán tener:

* título;
* pregunta o explicación breve;
* contenido principal;
* posible acceso a profundidad;
* fuente o nota cuando corresponda.

---

# 6. Cabecera y navegación

## 6.1 Cabecera

La cabecera deberá mantener continuidad con Jumalenin.

Elementos:

* logo o identidad Jumalenin;
* nombre Retícula Global 2025;
* navegación;
* acceso a metodología;
* edición o fecha de datos.

## 6.2 Jerarquía de nombres

Nombre principal:

> Retícula Global 2025

Subtítulo:

> Una imagen básica de la estructura del mundo

Nombre histórico o secundario:

> Mapa simbólico mundial

El nombre secundario no deberá tener el mismo peso visual que el principal.

## 6.3 Navegación

Opciones principales:

* Inicio;
* Áreas;
* Temas;
* Datos;
* Metodología.

En móvil:

* menú compacto;
* sin submenús profundos;
* acceso directo a áreas y temas;
* botón visible de regreso al mapa o inicio.

---

# 7. Paleta de las nueve áreas

## 7.1 Regla

Cada área tendrá un color estable y reconocible.

Los colores deberán:

* diferenciarse claramente;
* funcionar sobre fondo claro;
* mantener contraste suficiente;
* poder usarse en mapas y gráficas;
* no depender exclusivamente del color;
* evitar asociaciones políticas obvias cuando sea posible.

## 7.2 Codificación adicional

Cada área se identificará también mediante:

* nombre;
* código corto;
* posición estable;
* posible patrón o símbolo auxiliar.

## 7.3 Propuesta funcional de familias cromáticas

La elección definitiva deberá partir de la paleta existente, pero conceptualmente se propone:

| Área                          | Familia cromática sugerida |
| ----------------------------- | -------------------------- |
| Europa                        | Azul medio                 |
| Norteamérica y Caribe         | Azul verdoso               |
| Sudamérica                    | Verde                      |
| Rusia y Eurasia postsoviética | Violeta o ciruela          |
| China                         | Rojo oscuro moderado       |
| Subcontinente indio           | Naranja                    |
| Oriente Medio                 | Ocre o arena               |
| Asia-Pacífico                 | Turquesa                   |
| África                        | Amarillo dorado o tierra   |

Estas familias son orientativas.

No deben aplicarse sin comprobar:

* contraste;
* convivencia con la paleta Jumalenin;
* legibilidad en gráficas;
* funcionamiento para daltonismo.

## 7.4 Variantes

Cada color deberá disponer de:

* tono principal;
* tono oscuro;
* tono claro;
* fondo suave;
* borde.

Esto permitirá utilizar la misma identidad en:

* mapas;
* tarjetas;
* etiquetas;
* gráficas;
* avisos.

---

# 8. Mapa mundial

## 8.1 Proyección

Se priorizará:

1. Winkel Tripel;
2. Robinson como alternativa.

## 8.2 Estilo cartográfico

El mapa deberá ser:

* limpio;
* sin fondo geográfico innecesario;
* con límites legibles;
* sin sombreado tridimensional;
* sin etiquetas excesivas;
* sin relieve;
* sin capas decorativas.

## 8.3 Áreas

Cada área deberá aparecer:

* rellena con su color;
* delimitada con borde fino;
* resaltable al seleccionar;
* vinculada a su ficha;
* acompañada por leyenda.

## 8.4 Selección

Estado normal:

* todas las áreas visibles;
* ninguna domina.

Estado activo:

* área resaltada;
* resto atenuado ligeramente;
* tarjeta asociada;
* acceso a detalle.

## 8.5 Etiquetas

No deberán escribirse nombres extensos dentro de zonas pequeñas.

Opciones:

* códigos;
* etiquetas externas;
* leyenda;
* panel asociado.

## 8.6 Accesibilidad

El mapa no será el único medio de navegación.

Las nueve áreas deberán estar también disponibles mediante:

* tarjetas;
* lista;
* selector;
* enlaces de texto.

---

# 9. Tarjetas de área

## 9.1 Función

Permitir:

* reconocer las nueve áreas;
* consultar datos esenciales;
* acceder a sus fichas.

## 9.2 Contenido

Cada tarjeta contendrá:

* nombre;
* color;
* perfil breve;
* población;
* superficie;
* PIB;
* acceso a detalle.

## 9.3 Diseño

Las tarjetas deberán:

* mantener altura coherente;
* evitar exceso de bordes;
* utilizar el color con moderación;
* permitir lectura rápida;
* funcionar en una, dos o tres columnas según pantalla.

## 9.4 Estado seleccionado

La tarjeta correspondiente al área activa podrá:

* resaltar borde;
* aumentar contraste;
* mostrar un pequeño indicador;
* sincronizarse con el mapa.

---

# 10. Cifras destacadas

## 10.1 Regla

Una cifra destacada debe mostrar:

* valor;
* unidad;
* nombre del indicador;
* año o referencia;
* comparación cuando sea útil.

## 10.2 Ejemplo conceptual

> **1.520 millones**
> Población
> 18,5 % de la población mundial

## 10.3 Jerarquía

* valor: máximo peso;
* nombre: peso medio;
* contexto: peso menor;
* fuente: bajo demanda.

## 10.4 Prohibiciones

Evitar:

* cifras sin unidad;
* decimales innecesarios;
* colores de semáforo sin explicación;
* iconos decorativos sin función;
* tarjetas con demasiados indicadores.

---

# 11. Tabla de Datos Consolidados

## 11.1 Función visual

La tabla deberá facilitar comparación, no mostrar toda la base simultáneamente.

## 11.2 Estilo

* cabecera fija cuando sea útil;
* filas claras;
* separación horizontal suave;
* alineación numérica a la derecha;
* nombres de áreas a la izquierda;
* unidades visibles;
* colores discretos;
* resaltado de fila o columna seleccionada.

## 11.3 Color

El color del área podrá aparecer en:

* punto;
* barra lateral;
* etiqueta;
* fondo muy suave.

No se coloreará toda la fila con alta intensidad.

## 11.4 Ordenación

En escritorio podrá permitirse:

* ordenar por columna;
* seleccionar bloque;
* seleccionar indicador.

## 11.5 Móvil

En móvil se priorizará:

* selector de indicador;
* lista de nueve áreas;
* valor y posición;
* acceso a detalle.

La tabla completa horizontal será secundaria.

---

# 12. Gráficas

## 12.1 Principio general

Cada gráfica deberá responder a una pregunta concreta.

No se incorporará una gráfica solo porque exista un dato.

## 12.2 Tipos prioritarios

* barras horizontales;
* barras dobles;
* dispersión sencilla;
* línea temporal;
* pequeños múltiples, solo si son legibles;
* mapa temático, cuando aporte información distinta al mapa principal.

## 12.3 Tipos no prioritarios

* gráficos de tarta múltiples;
* velocímetros;
* donuts decorativos;
* radar con muchas variables;
* gráficos tridimensionales;
* animaciones continuas;
* visualizaciones experimentales difíciles de interpretar.

## 12.4 Uso del color

En una gráfica comparativa:

* cada área mantiene su color;
* el resto de elementos usa tonos neutros;
* la selección activa puede resaltarse;
* no se usarán colores nuevos sin función.

## 12.5 Etiquetas

Las gráficas deberán mostrar:

* unidad;
* año;
* fuente resumida;
* valores cuando no saturen;
* nota de aproximación.

---

# 13. Gini, IDH y otros índices

## 13.1 Gini

Representación recomendada:

* barra horizontal;
* escala numérica;
* explicación de extremos.

Ejemplo:

```text
Más igualdad ─────────────── Más desigualdad
0                                      100
```

No usar:

* personajes;
* ropa;
* reparto visual caricaturesco;
* etiquetas morales.

## 13.2 IDH

Representación:

* valor;
* barra de escala 0–1;
* comparación entre áreas;
* explicación de salud, educación e ingresos.

## 13.3 Indicadores aproximados

Los indicadores calculados por Retícula Global deberán mostrar una señal discreta:

* símbolo;
* etiqueta “aprox.”;
* nota emergente o desplegable;
* enlace a metodología.

---

# 14. Capacidad militar

## 14.1 Regla visual

La página militar no se representará mediante acumulación de armas o imágenes bélicas espectaculares.

Se utilizarán:

* cifras;
* barras;
* iconos técnicos;
* matrices;
* perfiles cualitativos;
* mapas de alcance, cuando resulten útiles.

## 14.2 Dimensiones

Las capacidades podrán agruparse visualmente en:

* recursos;
* industria;
* fuerzas convencionales;
* capacidad nuclear;
* misiles y drones;
* inteligencia y comunicaciones;
* logística;
* alianzas;
* proyección.

## 14.3 Perfil cualitativo

Puede utilizarse una matriz de niveles:

| Dimensión | Nivel | Explicación                           |
| --------- | ----: | ------------------------------------- |
| Drones    |   4/5 | Alta capacidad de producción y empleo |
| Logística |   2/5 | Dependencia elevada de apoyo exterior |

La escala deberá estar explicada.

## 14.4 Restricción

No crear inicialmente una puntuación militar total única.

---

# 15. Energía y autonomía

## 15.1 Representación

La autonomía energética debe descomponerse en:

* producción;
* consumo;
* importaciones;
* fuentes;
* transformación;
* redes;
* vulnerabilidad.

## 15.2 Gráficas recomendadas

* producción frente a consumo;
* dependencia importadora;
* composición energética;
* emisiones por habitante.

## 15.3 Evitar

* un único icono de batería;
* una etiqueta simple de autónomo/no autónomo;
* una puntuación sin explicación.

---

# 16. Tecnología e inteligencia artificial

## 16.1 Enfoque visual

La IA deberá mostrarse mediante dimensiones concretas:

* inversión;
* investigación;
* talento;
* modelos;
* cómputo;
* chips;
* centros de datos;
* adopción;
* regulación.

## 16.2 Componentes posibles

* barras;
* matriz de capacidades;
* cadena de valor de IA;
* diagrama desde chips hasta aplicaciones;
* comparaciones por área.

## 16.3 Cadena visual propuesta

```text
Energía
  ↓
Chips
  ↓
Centros de datos
  ↓
Modelos
  ↓
Aplicaciones
  ↓
Impacto económico y social
```

Esta representación puede explicar mejor la autonomía tecnológica que una puntuación única.

---

# 17. Iconografía

## 17.1 Función

Los iconos deben facilitar:

* reconocimiento de bloques;
* orientación;
* lectura rápida.

## 17.2 Categorías

* territorio;
* población;
* economía;
* desigualdad;
* educación;
* salud;
* desarrollo;
* defensa;
* energía;
* tecnología.

## 17.3 Estilo

* línea simple;
* misma familia;
* grosor coherente;
* sin mezcla de estilos;
* sin iconos excesivamente detallados;
* sin apariencia infantil.

## 17.4 Uso

Los iconos no sustituirán:

* títulos;
* nombres;
* unidades;
* explicaciones.

---

# 18. Advertencias y metodología

## 18.1 Tipos de aviso

### Informativo

* año diferente;
* fuente secundaria;
* dato redondeado.

### Atención

* cobertura parcial;
* media aproximada;
* comparabilidad limitada.

### Crítico

* dato insuficiente;
* metodología excepcional;
* resultado no comparable.

## 18.2 Representación

* icono;
* texto breve;
* color moderado;
* enlace a explicación.

No utilizar únicamente rojo, amarillo y verde.

## 18.3 Ejemplo

> **Dato aproximado**
> Media ponderada con una cobertura del 82 % de la población del área.

---

# 19. Tipografía

## 19.1 Regla

Se utilizará la tipografía común de Jumalenin o una opción compatible ya presente en el proyecto.

No se incorporarán nuevas familias tipográficas salvo necesidad justificada.

## 19.2 Jerarquía

* título principal;
* título de sección;
* subtítulo;
* texto;
* cifra;
* leyenda;
* fuente.

## 19.3 Legibilidad

* cuerpo mínimo cómodo;
* líneas no excesivamente largas;
* interlineado suficiente;
* cifras tabulares si la fuente lo permite;
* contraste alto.

---

# 20. Botones y enlaces

## 20.1 Tipos

### Primario

* abrir ficha;
* explorar área;
* ver datos.

### Secundario

* ver metodología;
* cambiar de tema;
* ampliar información.

### Enlace textual

* fuentes;
* notas;
* navegación secundaria.

## 20.2 Reglas

* texto descriptivo;
* área táctil suficiente;
* estados hover y foco;
* no usar botones para elementos que no realizan una acción;
* evitar demasiados botones simultáneos.

---

# 21. Responsive

## 21.1 Escritorio

* mapa amplio;
* panel lateral opcional;
* tabla comparativa;
* gráficas alineadas;
* navegación completa.

## 21.2 Tableta

* mapa a ancho completo;
* tarjetas en dos columnas;
* tablas simplificadas;
* panel debajo del mapa.

## 21.3 Móvil

* mapa simplificado;
* selección mediante lista o tarjetas;
* una gráfica por fila;
* cifras en dos columnas;
* secciones consecutivas;
* controles grandes.

## 21.4 Móvil horizontal

Deberá comprobarse:

* altura limitada;
* mapa;
* menú;
* gráficas;
* paneles desplegables.

---

# 22. Accesibilidad

## Requisitos iniciales

* contraste suficiente;
* foco visible;
* navegación mediante teclado;
* etiquetas en controles;
* textos alternativos;
* iconos acompañados de texto;
* no depender del color;
* tablas con cabeceras;
* gráficos con resumen textual;
* tamaño táctil suficiente.

## Regla didáctica adicional

Toda gráfica importante deberá tener una frase que explique su conclusión principal.

---

# 23. Animación e interacción

## Permitidas

* transición de selección;
* resaltado suave;
* desplegables;
* ordenación;
* filtros;
* cambio de indicador.

## Pospuestas

* animaciones de entrada extensas;
* movimientos continuos;
* mapas animados;
* contadores;
* efectos tridimensionales;
* desplazamientos automáticos.

La interacción debe ayudar a explorar, no distraer.

---

# 24. Componentes visuales iniciales

La primera implementación deberá disponer de:

1. cabecera;
2. navegación;
3. introducción;
4. mapa;
5. leyenda;
6. tarjeta de área;
7. cuadrícula de áreas;
8. cifra destacada;
9. tabla resumida;
10. selector de indicador;
11. gráfica de barras;
12. gráfica comparativa;
13. aviso metodológico;
14. bloque narrativo;
15. lista de fuentes;
16. pie.

Estos componentes deben cubrir la mayor parte de la primera versión.

---

# 25. Reglas CSS propias

Los estilos deberán quedar encapsulados bajo una clase raíz.

Ejemplo:

```css
.reticula-global {
  /* variables y reglas propias */
}
```

## Variables específicas

Podrán definirse:

```css
.reticula-global {
  --rg-area-europa: ...;
  --rg-area-africa: ...;
  --rg-area-china: ...;
  --rg-border: ...;
  --rg-surface-soft: ...;
  --rg-text-muted: ...;
}
```

## Restricciones

* no redefinir `body` sin necesidad;
* no modificar clases generales de Support;
* no sobrescribir estilos de Common;
* no utilizar selectores excesivamente genéricos;
* no introducir reglas `!important` salvo caso justificado;
* evitar CSS duplicado.

---

# 26. Sistema visual mínimo para la primera versión

La primera implantación visual se considerará suficiente cuando incluya:

* continuidad con la versión actual;
* paleta de nueve áreas;
* mapa no Mercator;
* tarjetas coherentes;
* tabla legible;
* tres gráficas claras;
* fichas con estructura común;
* avisos metodológicos;
* móvil;
* accesibilidad básica.

No será necesario completar inicialmente:

* todas las variantes de gráfica;
* animaciones;
* iconografía propia completa;
* personajes;
* índices compuestos;
* panel administrativo visual;
* modos oscuros específicos.

---

# 27. Control del avance visual

El avance de 1B.6 y de la futura implantación visual podrá medirse así:

| Componente                 | Peso visual |
| -------------------------- | ----------: |
| Continuidad con Jumalenin  |        10 % |
| Paleta y áreas             |        10 % |
| Mapa                       |        20 % |
| Tarjetas y cifras          |        15 % |
| Tabla                      |        10 % |
| Gráficas                   |        15 % |
| Fichas y páginas temáticas |        10 % |
| Responsive y accesibilidad |        10 % |

## Condición de cierre

La fase conceptual podrá cerrarse al 100 % cuando todas las reglas estén definidas.

La implantación visual no podrá considerarse suficiente por debajo del 65 % ponderado.

---

# 28. Riesgos

## Riesgo 1 — Pérdida de continuidad

Mitigación:

* inventariar la visual actual;
* conservar lo que funciona;
* evitar una identidad nueva completa.

## Riesgo 2 — Exceso de color

Mitigación:

* usar color intenso solo para identificar áreas;
* fondos neutros;
* tonos suaves en tarjetas.

## Riesgo 3 — Saturación de datos

Mitigación:

* profundidad progresiva;
* pocas gráficas;
* selectores;
* tablas resumidas.

## Riesgo 4 — Apariencia infantil

Mitigación:

* lenguaje claro sin simplificación visual excesiva;
* iconos funcionales;
* tipografía seria;
* colores controlados.

## Riesgo 5 — Incompatibilidad móvil

Mitigación:

* diseñar cada componente desde el principio para móvil;
* no adaptar únicamente al final.

## Riesgo 6 — Colisión con Support o Common

Mitigación:

* encapsulación CSS;
* no modificar clases compartidas;
* pruebas dentro de la ruta real.

---

# 29. Decisiones adoptadas

1. La visual será una evolución de la aplicación actual.
2. Retícula Global tendrá reglas propias encapsuladas.
3. No se modificará Common.
4. El mapa usará Winkel Tripel o Robinson.
5. Las nueve áreas mantendrán colores estables.
6. El color no será el único identificador.
7. Las tarjetas mostrarán pocos datos.
8. La tabla será comparativa y progresiva.
9. Se utilizarán pocas gráficas.
10. Gini e IDH tendrán representaciones explicadas.
11. La capacidad militar se mostrará por dimensiones.
12. La autonomía energética no se resumirá prematuramente.
13. La IA se explicará mediante su cadena tecnológica.
14. Los personajes seguirán pospuestos.
15. La comprensión infantil y general será un requisito.
16. Las gráficas tendrán explicación textual.
17. El diseño móvil se realizará desde el principio.
18. La implantación visual deberá superar el 65 % para considerarse suficiente.

---

# 30. Decisión final de la Fase 1B.6

## GO condicionado

El sistema visual queda suficientemente definido para pasar a:

# Fase 1B.7 — Selección definitiva de gráficas y representaciones

La fase siguiente deberá concretar:

* qué gráficas se utilizarán realmente;
* qué pregunta responde cada una;
* qué indicadores necesita;
* dónde aparece;
* qué alternativa tendrá en móvil;
* qué explicación textual la acompañará;
* qué gráficas existentes se conservan, sustituyen o eliminan.

## Condición previa a implementación

Antes de modificar código deberá completarse el inventario visual real de la aplicación actual y contrastarlo con estas reglas.

Todavía no corresponde:

* modificar CSS;
* generar la paleta definitiva;
* sustituir el mapa;
* crear componentes;
* diseñar las páginas completas.
