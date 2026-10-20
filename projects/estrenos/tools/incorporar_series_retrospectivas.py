"""Reconstrucción editorial local del 20/10/2026; sin red ni base de datos."""
from pathlib import Path
import re
from generar import render, update_archive

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = Path('C:/Users/guine/.codex/visualizations/2026/09/14/01a09f8c-7cc3-7f70-a97d-95ddb3c3b057/seguimiento-estrenos')
# Título, ficha, plataforma, incorporación, nota, votos, V/A/R.
SEP18 = [
('Neagley','573717','Prime','16/09',6.3,659,(7,0,1)),
('Catedrales [miniserie]','681724','Prime','16/09',6.9,263,None),
('La muñeca','418116','Netflix','16/09',6.4,182,None),
('La casa nostra [T2]','506258','Movistar','17/09',5.8,299,None),
('Stranger Things: Relatos del 85 [T2]','445649','Netflix','17/09',5.7,302,(8,5,5)),
('Belleza plástica','300994','Netflix','17/09',5.7,62,None),
('Monstruo: La historia de Lizzie Borden [miniserie]','970809','Netflix','17/09',5.6,1965,(4,4,4)),
('Te conozco','934886','Netflix','17/09',4.6,141,None),
('Los solucionadores','907329','Netflix','17/09',None,None,None),
('El escándalo','630814','Netflix','18/09',5.3,28,None),
]
SEP25 = SEP18 + [
('Outlander: Sangre de mi sangre [T2]','102015','Movistar','19/09',6.8,347,(10,1,1)),
('Academia Minerva','553935','Netflix','22/09',5.4,96,None),
('Such Brave Girls [T2]','677323','Filmin','22/09',6.8,1664,(16,3,0)),
('Habeas corpus','641029','Netflix','23/09',6.0,97,None),
('Mis muertos tristes [miniserie]','990946','Netflix','24/09',5.9,409,(8,4,3)),
('Un mundo diferente','170423','Netflix','24/09',None,None,(7,2,0)),
('Shaque: No confíes en nadie','620772','Netflix','24/09',None,None,None),
('El problema final [miniserie]','476943','Netflix','25/09',5.1,1709,None),
('JoJo’s Bizarre Adventure. Parte 7: Steel Ball Run [segunda y tercera etapa]','903281','Netflix','25/09',8.2,100,None),
('Veneno [miniserie]','401406','Netflix','25/09',7.5,11144,(10,1,1)),
]
OCT02 = [
('LEGO One Piece [miniserie]','688336','Netflix','29/09',5.8,43,None),
('Inspectora Ellis [T2]','978947','Filmin','29/09',5.8,234,(4,2,1)),
('Medusa [T2]','601410','Netflix','30/09',4.4,229,None),
('Al este del Edén [miniserie]','745119','Netflix','01/10',7.2,1173,(25,1,0)),
('Rompiendo el hielo','777663','Netflix','01/10',7.1,124,None),
('Reina Roja 2: Loba negra [T2]','477453','Prime','02/10',5.6,832,None),
('Prefiero la muerte','862249','Prime','02/10',4.5,26,None),
('#Amor','294503','Netflix','02/10',None,None,None),
]
OCT09 = [
('Los siete caballeros del reino Marronnier','991183','Prime','03/10',None,None,None),
('Ranma ½ [T3]','725016','Netflix','03/10',7.4,1005,None),
('La caja azul [T2]','384407','Netflix','04/10',7.1,261,None),
('El peso de la justicia','384954','Filmin','06/10',6.5,51,None),
('Carrie','878857','Prime','07/10',6.4,1914,(19,4,1)),
('Big Mood','794178','Movistar','07/10',5.9,59,(9,3,3)),
('Machos de verdad [T2]','203611','Netflix','07/10',4.4,50,None),
('El círculo','805649','Netflix','07/10',5.6,45,None),
('El castillo [miniserie]','936040','Movistar','08/10',7.5,1910,(11,0,0)),
('Bajo la superficie [miniserie]','132465','Netflix','08/10',5.3,1325,(11,2,0)),
('Aquel [miniserie]','840034','Netflix','09/10',6.2,200,None),
('El hotel embrujado [T2]','727467','Netflix','09/10',6.4,354,(5,2,1)),
('El soltero menos codiciado','577568','Netflix','09/10',None,None,None),
('La chispa del amor','388154','Netflix','09/10',5.8,55,None),
]

def section(rows, period):
    lines = []
    counts = [0, 0, 0]
    for title, fid, platform, date, rating, votes, reviews in rows:
        total = sum(reviews) if reviews else None
        percent = 100 * reviews[0] / total if total else None
        if rating is None or reviews is None:
            result = 'Pendiente: Faltan cifras' if rating is None else 'Pendiente: Falta desglose profesional'
            counts[2] += 1
        elif rating <= 6 or percent <= 70:
            result = 'No cumple: Nota ≤6' if rating <= 6 else 'No cumple: Positivas ≤70%'
            counts[1] += 1
        elif platform == 'Movistar':
            result = 'Pendiente: Cumple notas; Plan Libre sin confirmar'
            counts[2] += 1
        else:
            result = 'Seleccionada'
            counts[0] += 1
        star = '*' if (votes is not None and votes < 100) or (total is not None and total < 5) else ''
        note = str(rating).replace('.', ',') if rating is not None else '—'
        var = '/'.join(map(str,reviews)) + f' ({total})' if reviews else '— (—)'
        positive = f'{percent:.1f}'.replace('.', ',') if percent is not None else '—'
        lines.append(f'| [{title}](https://www.filmaffinity.com/es/film{fid}.html){star} | {platform} · {date} | {note} | {votes if votes is not None else "—"} | {var} | {positive} | {result} |')
    return f'''**Series de plataformas**

Ampliación retrospectiva añadida el 20/10/2026 para las incorporaciones del {period}. Las notas, votos y críticas proceden de las fichas accesibles en esta consulta posterior; no acreditan sus valores en la fecha del informe. Cobertura parcial de Netflix, Prime, Movistar y Filmin.

Balance de series: **{len(rows)} registros; seleccionadas: {counts[0]}; no cumplen: {counts[1]}; pendientes: {counts[2]}.** Este recuento se añade al balance original de películas, conservado por separado.

Criterios de series, como en el informe del 16/10: nota >6 y verdes/(verdes+amarillas+rojas) >70%. V/A/R son críticas profesionales y Σ su total; las reseñas de usuarios no sustituyen ese desglose. Si faltan cifras se mantiene pendiente, incluso con nota ≤6. — significa no confirmado, nunca cero. * señala menos de 100 votos o 5 críticas. La valoración corresponde a la ficha enlazada de la serie o miniserie, no necesariamente a la temporada incorporada. Las temporadas identificadas tienen marcas Vista separadas.

| Título | Medio · fecha | Nota | Votos | V/A/R (Σ) | % positivas | Resultado |
|---|---|---:|---:|---|---:|---|
''' + '\n'.join(lines) + '''

Fuentes de fechas: [calendario FilmAffinity de septiembre](https://www.filmaffinity.com/es/calendar-tv.php?chv=1&date=2026-09&reg=es), [calendario FilmAffinity de octubre](https://www.filmaffinity.com/es/calendar-tv.php?date=2026-10) y cabecera de cada ficha enlazada. Las fechas identifican la incorporación o temporada anunciada en España; no se verifica retirada posterior ni acceso en cuenta personal. En Movistar, cumplir los umbrales no basta para seleccionar sin confirmar el Plan Libre.

Esta ampliación no es un inventario exhaustivo. No se infiere que una temporada esté incluida en una suscripción por la mera presencia de otras temporadas o canales de pago en JustWatch. No se incorporan estrenos de otros servicios ni canales lineales sin confirmar su inclusión en las plataformas del seguimiento. Los pendientes de series no se arrastran a semanas posteriores: se muestran en su periodo de incorporación, evaluados el 20/10.

'''

def main():
    for date, rows, period in [('2026-09-18',SEP18,'14 al 18/09'), ('2026-09-25',SEP25,'14 al 25/09'), ('2026-10-02',OCT02,'26/09 al 02/10'), ('2026-10-09',OCT09,'03 al 09/10')]:
        dest = ROOT / 'docs' / f'informe-{date}.md'
        source = (dest if date == '2026-09-18' else ORIGINAL / dest.name).read_text(encoding='utf-8-sig')
        source = '\n'.join(line for line in source.splitlines() if not line.startswith(('El correo de la semana', 'Informe preparado para publicar en este chat.', 'Confirmación posterior: enviado', '## Entrega')))
        # El 18/09 es una reconstrucción local: evita duplicar la ampliación.
        source = re.sub(r'\*\*Series de plataformas\*\*.*?(?=\*\*Cobertura|## Cobertura|$)', '', source, flags=re.S) if date == '2026-09-18' else source
        source = source.replace('Series, monólogos y mediometrajes excluidos.', 'El bloque original de películas excluía series, monólogos y mediometrajes; las series se incorporan en la ampliación retrospectiva separada.')
        source = source.replace('Solo películas; series y web siguen aplazadas.', 'El balance original corresponde solo a películas; las series se incorporan en la ampliación retrospectiva separada.')
        source = source.replace('Se excluyen series y estrenos posteriores al 09/10.', 'El bloque original excluía series y estrenos posteriores al 09/10; las series del periodo se incorporan en la ampliación retrospectiva separada.')
        note = 'Los balances, matrices y comprobaciones del informe original que siguen corresponden a películas. Las series tienen una sección y un balance retrospectivo propios, consultados el 20/10/2026.\n\n'
        if note not in source:
            first, rest = source.split('\n', 1)
            source = first + '\n\n' + note + rest.lstrip('\n')
        block = section(rows,period)
        # Inserta después de las tablas de películas y antes de la cobertura.
        match = re.search(r'(?m)^(?:\*\*|#{1,3} )(?:Cobertura|Fuentes|Disponibilidad)', source)
        pos = match.start() if match else len(source)
        source = source[:pos].rstrip() + '\n\n' + block + source[pos:]
        dest.write_text(source,encoding='utf-8')
        content,count,selected = render(source,date)
        update_archive(ROOT,date,content)
        print(date,count,selected)

if __name__ == '__main__':
    main()
