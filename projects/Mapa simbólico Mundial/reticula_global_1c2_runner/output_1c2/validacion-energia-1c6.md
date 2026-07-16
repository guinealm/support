# Validacion energia 1C.6

## Estado general
- Areas: 9 (esperado 9)
- Paises/territorios en CSV base: 244 (esperado 244)
- Incidencias: 177

## Comprobaciones solicitadas
1. Nueve areas: OK
2. Ningun consumo negativo: OK
3. Ningun ausente convertido en cero: OK
4. Coherencia EJ/TWh: OK (delta_max=0.00000000)
5. ENE_PC recalculable: OK (consumo area / poblacion 2025).
6. ENE_DEP ponderado por consumo: OK (net imports derivados).
7. ENE_AUTO = 100 - ENE_DEP: OK
8. Exportadores con autosuficiencia > 100: revisado.
9. Fosiles en 0-100: OK
10. Electricidad baja carbono en 0-100: OK
11. Porcentajes calculados desde absolutos: OK (fosil_twh/consumo y lc_twh/electricidad_total).
12. Anios reales conservados: OK.
13. Datos 2024 identificados: ENE_ELEC_LC=105
14. Codigos no duplicados: OK
15. Agregados regionales de fuente excluidos: OK (solo ISO3 de maestro).
16. China/Hong Kong/Macao sin duplicidad: revisado documentalmente.
17. Rusia solo en RUE: revisado.
18. Territorios dependientes revisados: documentado por indicador.
19. Cobertura por indicador: calculada en rg_agregados_energia.csv.
20. Valores extremos documentados: incidencias-energia-1c6.csv.

## Cobertura por area

| Area | Consumo-pop % | Nivel | Dep-consumo % | Nivel | Fosil-consumo % | Nivel | Elec-generacion % | Nivel |
|---|---:|---|---:|---|---:|---|---:|---|
| AFR | 17.37 | insuficiente | 100.00 | alta | 100.00 | alta | 100.00 | alta |
| APC | 86.98 | condicionada | 93.90 | aceptable | 100.00 | alta | 100.00 | alta |
| CHN | 99.95 | alta | 100.00 | alta | 100.00 | alta | 100.00 | alta |
| EUR | 97.07 | alta | 99.68 | alta | 100.00 | alta | 100.00 | alta |
| MDE | 76.30 | insuficiente | 100.00 | alta | 100.00 | alta | 100.00 | alta |
| NAC | 84.38 | condicionada | 100.00 | alta | 100.00 | alta | 100.00 | alta |
| RUE | 90.21 | aceptable | 100.00 | alta | 100.00 | alta | 100.00 | alta |
| SAI | 96.25 | alta | 100.00 | alta | 100.00 | alta | 100.00 | alta |
| SAM | 94.35 | aceptable | 100.00 | alta | 100.00 | alta | 100.00 | alta |

## Decision preliminar
- GO condicionado a revision de incidencias y comprobaciones SQL en MySQL (sin ejecutar en esta fase).