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

1C.6D publica cinco indicadores. ENE_FOS se aplaza por cobertura insuficiente y falta de fuente complementaria comparable para cuatro areas. Sus datos permanecen como material de trabajo, pero no se catalogan ni se cargan en MySQL.

| Area | ENE_CONS antes % | ENE_CONS despues % | ENE_FOS antes % | ENE_FOS despues % | Fosil sobre consumo cubierto % |
|---|---:|---:|---:|---:|---:|
| AFR | 17.37 | 99.92 | 17.37 | 17.37 | 61.17 |
| APC | 86.98 | 97.26 | 86.98 | 86.98 | 97.50 |
| CHN | 99.95 | 100.00 | 99.95 | 99.95 | 99.97 |
| EUR | 97.07 | 99.92 | 97.07 | 97.07 | 98.12 |
| MDE | 76.30 | 100.00 | 76.30 | 76.30 | 95.43 |
| NAC | 84.38 | 99.83 | 84.38 | 84.38 | 97.62 |
| RUE | 90.21 | 100.00 | 90.21 | 90.21 | 98.04 |
| SAI | 96.25 | 100.00 | 96.25 | 96.25 | 99.09 |
| SAM | 94.35 | 99.93 | 94.35 | 94.35 | 96.69 |

## Decision 1C.6D
- ENE_FOS queda fuera de la primera edicion y deja de ser condicion de bloqueo.
- Umbral operativo de ENE_CONS: cobertura poblacional >=90% en cada area.
- Areas bajo el umbral: ninguna.
- Decision: GO documental para ejecutar 17/18/19_rg_*_energia.sql en el orden previsto. MySQL no se ejecuta en esta fase.