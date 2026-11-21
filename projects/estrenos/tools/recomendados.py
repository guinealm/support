"""Catálogo acumulado a partir de las instantáneas HTML locales, sin red."""
import datetime
import html
import re

BUTTON = '<p class="catalog-action"><a class="catalog-button" href="recomendados.html">Todos los recomendados</a></p>'


def add_button(page):
    if 'class="catalog-action"' not in page:
        page = page.replace('</div></section>', BUTTON + '\n</div></section>', 1)
    return page


def collect(pages, selected_only=True):
    entries = {}
    for date, page in sorted(pages.items()):
        for table in re.findall(r'<table>(.*?)</table>', page, re.S):
            headers = re.findall(r'<th\b[^>]*>(.*?)</th>', table, re.S)
            caption = re.search(r'<caption>(.*?)</caption>', table, re.S)
            series_table = bool(caption and re.search(r'\bseries\b', caption[1], re.I))
            for key, classes, body in re.findall(
                    r'<tr data-title-key="([^"]+)" class="([^"]*)">(.*?)</tr>', table, re.S):
                if selected_only and 'selected' not in classes.split():
                    continue
                cells = re.findall(r'<td\b[^>]*>(.*?)</td>', body, re.S)
                if len(cells) != len(headers):
                    raise ValueError('Tabla irregular en ' + date)
                entry = entries.setdefault(key, {'dates': set(), 'media': set()})
                entry['series'] = (entry.get('series', False) or series_table or
                                   bool(re.search(r'\((?:mini)?serie\)', cells[1], re.I)))
                entry['dates'].add(date)
                for header, cell in zip(headers[2:], cells[2:]):
                    if any(word in header.lower() for word in ('medio', 'plataforma')):
                        entry['media'].add(cell)
                entry.update(date=date, checkbox=cells[0], title=cells[1],
                             details=list(zip(headers[2:], cells[2:])))
    return entries


def render_catalog(pages):
    entries = collect(pages)
    selected = set(entries)
    entries.update({key: item for key, item in collect(pages, selected_only=False).items()
                    if key not in selected})
    rows = []
    for key, item in sorted(entries.items(), key=lambda pair: (pair[1]['date'], pair[0]), reverse=True):
        details = '<dl class="recommendation-details">' + ''.join(
            f'<dt>{label}</dt><dd>{value}</dd>' for label, value in item['details']) + '</dl>'
        links = '<br>'.join(
            f'<a href="informe-{date}.html">{datetime.date.fromisoformat(date).strftime("%d/%m/%Y")}</a>'
            for date in sorted(item['dates'], reverse=True))
        media = '<br>'.join(sorted(item['media'])) or 'Consultar informe'
        title = item['title']
        if item['series']:
            title = re.sub(r'\s*\((?:mini)?serie\)', '', title, flags=re.I)
            title += ' <span class="format-badge">Serie</span>'
        attributes = 'class="selected"' if key in selected else 'data-personal-only hidden'
        rows.append(f'<tr data-title-key="{html.escape(key, quote=True)}" {attributes}>'
                    f'<td class="seen-cell">{item["checkbox"]}</td><td>{title}</td>'
                    f'<td>{media}</td><td>{details}</td><td>{links}</td></tr>')
    body = (f'<h2>Todos los recomendados · <span id="catalog-count">{len(selected)}</span> títulos y temporadas</h2>'
            '<p>Incluye las obras seleccionadas al menos una vez en los informes y las que has valorado como «Recomendable» en este navegador.</p>'
            '<p>El orden y los datos corresponden al último informe que seleccionó cada obra o, si solo la has recomendado tú, '
            'al último informe donde apareció. Las plataformas recogen las menciones históricas, '
            'no la disponibilidad actual. Consulta los informes enlazados para sus advertencias, cobertura y fechas efectivas de consulta.</p>'
            '<div class="table-scroll" role="region" tabindex="0" aria-label="Todos los recomendados"><table>'
            '<caption>Recomendaciones acumuladas</caption><thead><tr><th scope="col">Vista</th>'
            '<th scope="col">Título</th><th scope="col">Medios / plataformas registrados</th>'
            '<th scope="col">Datos del informe</th><th scope="col">Informes de referencia</th>'
            '</tr></thead><tbody>' + ''.join(rows) + '</tbody></table></div>')
    page = pages[max(pages)]
    page = re.sub(r'<title>.*?</title>', '<title>Todos los recomendados · Estrenos · Jumalenin</title>', page)
    page = page.replace('<h1>Seguimiento de estrenos</h1>', '<h1>Todos los recomendados</h1>')
    page = re.sub(r'<details class="version report-history">.*?</details>', '', page, flags=re.S)
    page = page.replace(BUTTON, '<p class="catalog-action"><a class="catalog-button" href="index.html">Volver al informe semanal</a></p>')
    page = re.sub(r'<nav class="report-nav".*?</nav>', '', page, flags=re.S)
    page = re.sub(r'<article id="informe">.*?</article>', lambda _: '<article id="informe">' + body + '</article>', page, flags=re.S)
    page = page.replace('href="#informe">Informe semanal', 'href="index.html">Informe semanal')
    return page
