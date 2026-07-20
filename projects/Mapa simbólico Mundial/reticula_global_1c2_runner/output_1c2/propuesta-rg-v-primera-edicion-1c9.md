# Propuesta de vista `rg_v_primera_edicion`

Estado: **documentada, no creada**.

La vista existente `rg_v_datos_consolidados` debe conservarse sin cambios si SQL 26 confirma que existe y funciona.

## Campos propuestos

| Campo | Origen |
|---|---|
| area_codigo | `rg_areas.codigo` |
| area_nombre | `rg_areas.nombre` |
| bloque_codigo | `rg_bloques.codigo` |
| bloque_nombre | `rg_bloques.nombre` |
| indicador_codigo | `rg_indicadores.codigo` |
| indicador_nombre | `rg_indicadores.nombre` |
| valor | `rg_datos_area.valor` |
| unidad | `rg_indicadores.unidad` |
| anio_referencia | `rg_datos_area.anio_referencia` |
| anio_minimo | `rg_datos_area.anio_minimo` |
| anio_maximo | `rg_datos_area.anio_maximo` |
| cobertura | `rg_datos_area.porcentaje_cobertura` |
| metodo | `rg_datos_area.metodo_calculo` |
| estado | `rg_datos_area.estado_dato` |
| advertencia | `rg_datos_area.observaciones` |

La futura vista debe filtrar exclusivamente registros, indicadores, bloques y áreas activos del periodo `RG2025_V1`. No se propone SQL ejecutable hasta cerrar la auditoría y autorizar la fase de conexión de datos.
