# Entrega manual de estrenos — 08/11/2026

El paquete contiene una web estática y sus fuentes. No requiere base de datos,
instalación de dependencias ni compilación. La entrega incorpora el informe parcial
del 06/11/2026: 58 títulos y 7 seleccionados. Las limitaciones están en el informe.

## Contenido

- `publicar/`: index.html, informes históricos y assets. Es la carpeta para Hostinger.
- `fuente/`: la misma web, el generador Python, README y documentación. Es el código
  fuente para conservar en GitHub dentro de la ruta del proyecto estrenos.
- `LEEME.md`: estas instrucciones.

El historial operativo, destinatarios y confirmaciones de Gmail quedan fuera del ZIP.
La web conserva sus dependencias visuales ya existentes de common.jumalenin.com.
No se ha realizado ninguna publicación remota.

## GitHub, por el usuario

1. Descomprime el ZIP en una carpeta nueva.
2. En tu repositorio de Support, abre `projects/estrenos`.
3. Incorpora el contenido de `fuente/` manteniendo sus carpetas y revisa los cambios.
4. Confirma tú la actualización mediante tu procedimiento habitual. No subas
   el historial privado `estado.json` ni archivos de correo.

## Hostinger, por el usuario

1. En el administrador de archivos del sitio Support, localiza la carpeta que sirve
   `support.jumalenin.com/projects/estrenos/`. Usa la raíz real de ese dominio;
   no presupongas que coincide con la de otros sitios.
2. Descarga una copia de la carpeta actual antes de actualizarla.
3. Sube el contenido de `publicar/` a esa carpeta, preservando `assets/` y todos
   los archivos `informe-YYYY-MM-DD.html`. No subas la carpeta contenedora publicar
   como un nivel adicional. No modifiques otros proyectos.
4. Abre la página y comprueba que la versión del selector es 06/11/2026, que hay
   58 títulos y 7 seleccionados, que las fechas anteriores se abren y que una
   casilla Vista mantiene su marca al recargar en ese mismo navegador.

Las marcas Vista existentes se conservan si mantienes el mismo dominio y navegador
y no borras el almacenamiento local. No se transfieren desde una vista local a otro
dominio. El informe, el correo y su historial ya están preparados independientemente
de este traspaso manual.
