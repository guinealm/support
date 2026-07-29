# Criterios metodológicos de indicadores complementarios — Fase 7A.2

Fecha: 2026-07-28  
Proyecto: Retícula Global 2025 — Support  
Documento de partida: `INVENTARIO-INDICADORES-COMPLEMENTARIOS-FASE-7A1.md`

## Objetivo y alcance

Este documento fija, antes de preparar o modificar datos, la definición, las fuentes, el año, la agregación y la publicación de seis indicadores complementarios del perfil medio de población.

La fase es exclusivamente metodológica. No se ha modificado MySQL, la API ni la web; tampoco se han preparado sentencias de escritura ni se ha realizado despliegue.

## Reglas transversales

1. Se mantienen los códigos existentes `TERR_DENS`, `POB_EDAD`, `HUM_EV`, `ECO_PC` y `HUM_IDH`.
2. Se mantiene `POB_URB`, ya reservado en el diccionario inicial, para la futura incorporación del porcentaje de población urbana. No se crea un código alternativo.
3. El año visible es el año estadístico del indicador, no el de publicación de la fuente ni el de consulta.
4. Los componentes de un mismo cálculo deben corresponder al mismo año. La única excepción estructural es la superficie terrestre: se usa la última observación válida disponible y se muestran por separado el año de población y el de superficie.
5. Las comparaciones entre macroáreas usarán un único año de referencia por indicador.
6. Una ausencia nunca se convierte en cero ni se sustituye por una media, un país vecino o una estimación propia no documentada.
7. Los cálculos usan valores sin redondear. El redondeo se aplica únicamente a la presentación.
8. Cada agregado debe conservar código, valor, unidad, año de referencia, años mínimo y máximo, fuente, URL, método, procedencia, estado, observaciones y métricas de cobertura.
9. Cuando intervienen datos nacionales, la selección territorial respeta exclusivamente el maestro de Retícula Global y evita dobles conteos de entidades incluidas en otra serie.

## Matriz metodológica definitiva

| Código | Definición | Pregunta didáctica | Unidad | Año | Fuente principal | Fuente auxiliar | Método de agregación | Cobertura mínima | Tratamiento de ausencias | Denominación visible | Observaciones |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `TERR_DENS` | Habitantes del conjunto territorial por cada km² de superficie terrestre. | ¿Cuánta población se concentra, en promedio, en el territorio terrestre de la macroárea? | habitantes por km² (`hab/km²`) | Población del año común elegido; superficie terrestre del último año válido, mostrado separadamente | Población: ONU, *World Population Prospects*; superficie terrestre: FAOSTAT, directamente o procesada por OWID | Banco Mundial para contraste de población y superficie terrestre | `Σ población de entidades con ambos componentes / Σ superficie terrestre de esas mismas entidades` | ≥95 % de la población del área y ≥95 % de la superficie conocida; por debajo se aplica la regla de publicación condicionada | Excluir del numerador y denominador la entidad que carezca de uno de los dos componentes; informar países y magnitudes cubiertas; nunca usar superficie total que incluya aguas interiores si el indicador se define sobre superficie terrestre | **Densidad de población** | Es un cociente de totales, no la media de las densidades nacionales. Antártida y entidades excluidas de los cálculos territoriales no entran en la fórmula. |
| `POB_URB` | Porcentaje de la población cubierta que reside en áreas clasificadas como urbanas por la fuente. | ¿Qué proporción de la población de la macroárea vive en zonas urbanas? | porcentaje de población (`%`) | Último año común con cobertura suficiente en las nueve áreas | Banco Mundial, WDI: población urbana y población total del mismo año | ONU DESA, *World Urbanization Prospects*, para completar o contrastar con metodología compatible | `100 × Σ población urbana / Σ población total`, usando exactamente las mismas entidades, año y cobertura | ≥95 % de la población del área | Omitir países sin población urbana comparable tanto del numerador como del denominador cubierto; no asignar cero. Si solo existe porcentaje nacional, convertirlo a población urbana únicamente con la población del mismo país, año y fuente compatible | **Población urbana** | El valor visible es un porcentaje, aunque el código reservado sea `POB_URB`. Deben conservarse también numerador, denominador y definición de “urbano” de la fuente. |
| `POB_EDAD` | Edad que divide en dos mitades la población por edad. Se prioriza un valor regional publicado para la agrupación exacta; en su ausencia se usa una aproximación ponderada de medianas nacionales. | ¿Qué edad separa aproximadamente a la mitad más joven de la mitad de mayor edad de la población? | años | Último año común con cobertura suficiente; población de ponderación del mismo año | ONU, preferentemente una publicación regional compatible con las nueve macroáreas; en su ausencia, serie nacional ONU/OWID | Oficinas estadísticas nacionales solo para huecos comparables y documentados | Prioridad 1: valor regional publicado para la agrupación exacta. Prioridad 2: `Σ(mediana nacional × población nacional) / Σ población cubierta` | ≥95 % de la población del área | Excluir del cálculo ponderado los países sin mediana; excluir también su población del denominador cubierto; no interpolar salvo que la fuente publique la estimación | **Edad mediana** si es regional publicada; **Edad mediana aproximada** si es media ponderada | La media ponderada de medianas nacionales no es la mediana de la distribución conjunta. El método utilizado debe acompañar siempre al valor. |
| `HUM_EV` | Promedio ponderado de la esperanza de vida al nacer publicada para los países de la macroárea. | ¿Cuántos años viviría en promedio un recién nacido si se mantuvieran las condiciones de mortalidad observadas? | años | Último año común con cobertura suficiente; población de ponderación del mismo año | Banco Mundial, WDI | ONU, OMS o fuente demográfica original citada por WDI para contraste | `Σ(esperanza de vida nacional × población nacional) / Σ población cubierta` | ≥95 % de la población del área | Excluir países sin valor y su población del denominador cubierto; no sustituir por el promedio del área | **Esperanza de vida media ponderada** | No es una esperanza de vida regional calculada desde tablas de mortalidad conjuntas. Mostrar un decimal en la web y conservar la precisión original. |
| `ECO_PC` | PIB nominal total de las entidades cubiertas dividido por su población total cubierta. | ¿Cuánto PIB nominal corresponde, en promedio, a cada habitante de la macroárea? | dólares estadounidenses corrientes por habitante (`USD corrientes/hab.`) | Un único año común para PIB y población y para las nueve macroáreas | Banco Mundial, WDI: `NY.GDP.MKTP.CD` y población total del mismo año | FMI o estadísticas nacionales solo para contraste; no mezclar en el agregado sin una conciliación metodológica previa | `Σ PIB nominal en USD corrientes / Σ población`, con idénticas entidades y año en ambos componentes | ≥95 % de la población del área y cobertura económica documentada; preferentemente ≥95 % del PIB conocido | Excluir del numerador y denominador las entidades sin pareja PIB–población del mismo año; no usar cero ni arrastrar el PIB de otro año. Si no se alcanza cobertura, aplicar la regla de publicación condicionada | **PIB nominal por habitante** | No promediar PIB per cápita nacionales. No mezclar moneda nacional, dólares constantes, PIB nominal y PIB PPA. El valor existente con PIB 2023–2024 y población 2025 requiere revisión antes de considerarse conforme a este criterio. |
| `HUM_IDH` | Media de los IDH nacionales publicados, ponderada por la población cubierta. | ¿Cuál es el nivel medio de desarrollo humano de la población representada en la macroárea? | índice de 0 a 1 | Año del IDH nacional; población de ponderación del mismo año | PNUD, *Human Development Reports* | ONU WPP para población del mismo año cuando la descarga del PNUD no aporte el ponderador necesario | `Σ(IDH nacional × población nacional) / Σ población cubierta` | ≥95 % de la población del área | Excluir países sin IDH y su población del denominador cubierto; no reconstruir el IDH, imputarlo ni sustituirlo por componentes parciales | **IDH medio ponderado** | No es un IDH oficial de la macroárea. Mostrar tres decimales y conservar la precisión original. |

## Cobertura y regla de publicación

Para `POB_URB`, `POB_EDAD`, `HUM_EV` y `HUM_IDH`, y para cualquier otro indicador ponderado o basado en población cubierta, deben registrarse como mínimo:

- número total de países y territorios computables del área;
- número de países y territorios con dato;
- población total del área para el año del indicador;
- población efectivamente cubierta;
- porcentaje de cobertura: `100 × población cubierta / población total del área`;
- año mínimo y máximo de las observaciones incluidas.

La decisión de publicación queda fijada así:

- **Cobertura ≥95 %:** publicación normal.
- **Cobertura entre 75 % y menos de 95 %:** publicación únicamente con advertencia visible de cobertura incompleta; el valor no se presenta como plenamente representativo.
- **Cobertura inferior al 75 %:** no publicar como valor comparativo de la macroárea; mostrar “NO DISPONIBLE” o reservarlo para una nota metodológica.

El umbral se evalúa por separado en cada macroárea. Para permitir una tabla comparativa homogénea de las nueve áreas, todas deben alcanzar el 95 %; si alguna queda entre 75 % y 95 %, toda comparación deberá identificar claramente qué área tiene cobertura condicionada.

En densidad se controla además la superficie cubierta. En PIB por habitante se registra también la cobertura económica cuando exista una estimación fiable de la magnitud total.

## Selección temporal

1. Se elige el año más reciente que permita aplicar el mismo año a las nueve macroáreas y alcanzar la cobertura requerida.
2. No se completa una celda con un año anterior de un solo país para aparentar homogeneidad.
3. Si no existe un año común con cobertura normal, se prueba el año inmediatamente anterior para todo el indicador.
4. Si aun así no se alcanza el umbral, se aplica la regla de publicación condicionada o se declara el valor no disponible.
5. Cualquier excepción publicada por la fuente debe conservar su año real y no integrarse en un agregado de otro año sin una serie comparable.

La superficie terrestre se considera una magnitud estructural de actualización lenta. Puede proceder de un año distinto al de población si se usa la última observación disponible para todas las áreas y ambos años se muestran expresamente.

## Reglas de cálculo y presentación

### Cocientes de totales

`TERR_DENS`, `POB_URB` y `ECO_PC` se calculan desde numeradores y denominadores agregados. No se obtiene ninguno mediante la media simple de porcentajes, densidades o valores por habitante nacionales.

### Medias ponderadas

Para `POB_EDAD` cuando no exista valor regional publicado, `HUM_EV` y `HUM_IDH`:

`valor agregado = Σ(valor nacional × población nacional del mismo año) / Σ población cubierta del mismo año`

La suma de población del denominador incluye exclusivamente países que aportan un valor nacional válido al numerador.

### Redondeo visible

- densidad: entero o un decimal, según magnitud;
- población urbana: un decimal;
- edad mediana: un decimal;
- esperanza de vida: un decimal;
- PIB nominal por habitante: dólares enteros o redondeo editorial a decenas/centenas según magnitud;
- IDH medio ponderado: tres decimales.

El valor fuente y el resultado calculado se conservan con mayor precisión.

## Discrepancias respecto del inventario 7A.1

1. **Edad mediana:** el agregado existente usa valores nacionales de 2023 ponderados con población 2025. El criterio definitivo exige población del mismo año, por lo que deberá revisarse antes de una futura publicación bajo esta metodología.
2. **Esperanza de vida:** el agregado existente combina esperanza de vida 2023 con población 2025. Debe revisarse el ponderador para utilizar población 2023.
3. **IDH:** el agregado existente combina IDH 2023 con población 2025. Debe recalcularse en una fase posterior con población 2023 y denominarse públicamente «IDH medio ponderado».
4. **PIB por habitante:** el agregado existente combina PIB principalmente de 2024, un respaldo de 2023 y población 2025. No cumple el criterio de año único y pareja PIB–población del mismo año.
5. **Población urbana:** 7A.1 confirmó que `POB_URB` no está materializado. Este documento fija su significado como porcentaje de población urbana, pero no autoriza todavía su creación ni carga.
6. **Cobertura:** la metodología histórica consideraba “alta” una cobertura superior al 90 %. Para estos indicadores complementarios se adopta el criterio más exigente solicitado en 7A.2: publicación normal a partir del 95 %.

Estas discrepancias no modifican ni invalidan automáticamente la edición congelada `RG2025_V1`; identifican los controles necesarios antes de preparar datos en una fase posterior.

## Decisiones definitivas

- Se conservan los seis códigos previstos, sin códigos alternativos.
- La urbanización se expresa como porcentaje calculado desde población urbana y total cubiertas.
- Los cocientes se calculan desde totales agregados.
- Los indicadores sociales se ponderan con población del mismo año.
- La edad mediana regional publicada tiene prioridad; la ponderación nacional se identifica como aproximación.
- El IDH se denomina «IDH medio ponderado».
- El 95 % de cobertura poblacional es el umbral para publicación normal.
- No se imputa ningún dato ausente y no se usa cero como sustituto.
- No se mezcla PIB nominal con PPA, monedas o años diferentes.

## Estado

**Criterios metodológicos definidos.**

La preparación o modificación de datos queda fuera de esta fase.
