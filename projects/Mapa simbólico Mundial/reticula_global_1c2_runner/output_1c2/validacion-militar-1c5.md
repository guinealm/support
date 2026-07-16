# Validacion militar 1C.5

## Estado general
- Areas: 9 (esperado 9)
- Paises/territorios en CSV base: 244 (esperado 244)
- Estados nucleares incluidos: 9
- Incidencias registradas: 3

## Comprobaciones solicitadas
1. Nueve areas: OK
2. Gasto militar sin valores negativos: OK (negativos=0)
3. Ningun ausente convertido en cero: OK
4. Porcentajes mundiales proximos a 100: OK (suma=100.000000)
5. Gasto por habitante recalculable: OK (MIL_PC = gasto area / poblacion area 2025).
6. Gasto respecto al PIB no calculado como media simple: OK (ratio agregado gasto/PIB cubierto).
7. Anios reales conservados: OK (min=2024, max=2025).
8. Datos 2024 identificados: OK (2 entidades)
9. Agregados regionales SIPRI excluidos: OK (se insertan solo ISO3 del maestro).
10. Ausencia de duplicidades ISO3: OK
11. Rusia solo en RUE: OK
12. Estados Unidos solo en NAC: OK
13. China solo en CHN: OK
13A. PRK sin gasto y documentado: OK
14. Arsenales nucleares asignados una sola vez: OK (un registro por Estado nuclear).
15. Areas sin Estado nuclear con valor cero documentado: OK.
16. Suma mundial de ojivas comparable SIPRI: 12187 (control=12187, diferencia=0).
17. Cobertura por poblacion y PIB: calculada por area en rg_agregados_militar.csv.
18. Valores nacionales extremos revisados: documentados en incidencias-militar-1c5.csv.

## Cobertura por area

| Area | Cobertura poblacion % | Nivel | Cobertura PIB % | Nivel |
|---|---:|---|---:|---|
| AFR | 95.68 | alta | 96.39 | alta |
| APC | 96.19 | alta | 99.69 | alta |
| CHN | 99.43 | alta | 97.61 | alta |
| EUR | 99.91 | alta | 99.85 | alta |
| MDE | 77.47 | insuficiente | 84.60 | condicionada |
| NAC | 97.25 | alta | 99.44 | alta |
| RUE | 82.40 | condicionada | 94.27 | aceptable |
| SAI | 97.73 | alta | 99.41 | alta |
| SAM | 93.27 | aceptable | 97.11 | alta |

## Decision preliminar
- GO: PRK queda como AUSENTE_DOCUMENTADO sin estimacion y el inventario nuclear nacional suma 12.187.