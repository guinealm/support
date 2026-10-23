"""Genera la pagina local a partir del mismo Markdown usado para el correo.
Uso: python generar.py --informe RUTA --fecha YYYY-MM-DD
No consulta fuentes ni envia correo ni publica.
"""
import argparse, datetime, html, re
from pathlib import Path

def inline(text):
    text = html.escape(text, quote=True)
    text = re.sub(r'\[(.*?)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', text)
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)

def render(source, fecha):
    lines = source.splitlines()
    chunks, count, selected, group = [], 0, 0, ""
    sections = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        # El registro operativo del correo no forma parte de la pagina publica.
        if line.startswith(("El correo de la semana", "Informe preparado para publicar en este chat.",
                            "Confirmación posterior: enviado")):
            i += 1
            continue
        if line.startswith("|") or (i + 1 < len(lines) and "|" in line and
                re.fullmatch(r"[\s|:\-]+", lines[i + 1])):
            rows = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                cells = [v.strip() for v in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r"[-: ]+", c) for c in cells):
                    rows.append(cells)
                i += 1
            is_titles = rows[0][0] in ("Título", "Película", "Título / tipo", "Título (tipo)")
            caption = (group or "Películas del informe") if is_titles else "Matriz de evaluación"
            chunks.append('<div class="table-scroll" role="region" tabindex="0" aria-label="'+html.escape(caption)+'"><table><caption>'+html.escape(caption)+'</caption><thead><tr>')
            if is_titles:
                chunks.append('<th scope="col">Vista</th>')
            chunks.extend('<th scope="col">'+inline(c)+'</th>' for c in rows[0])
            chunks.append('</tr></thead><tbody>')
            for row in rows[1:]:
                if len(row) != len(rows[0]):
                    raise ValueError("Tabla irregular: "+str(row))
                attrs = ""
                checkbox = ""
                if is_titles:
                    match = re.search(r"/film(\d+)\.html", row[0])
                    if not match:
                        raise ValueError("Falta ID FilmAffinity: "+row[0])
                    title = re.sub(r"\[(.*?)\]\(https?://[^)]+\)", r"\1", row[0]).rstrip("*")
                    # La misma pelicula en varias plataformas comparte marca.
                    season = re.search(r"\bT(\d+)\b", title)
                    key = "fa:" + match[1] + (":t"+season[1] if season else "")
                    is_selected = bool(re.fullmatch(r"Seleccionad[ao](?::.*)?|Cumple(?:;.*)?", row[-1].strip().strip("*")))
                    selected += int(is_selected)
                    count += 1
                    attrs = ' data-title-key="'+key+'" class="'+("selected" if is_selected else "")+'"'
                    checkbox = '<td class="seen-cell"><input type="checkbox" disabled data-seen="'+key+'" aria-label="Marcar como vista: '+html.escape(title, quote=True)+'"></td>'
                chunks.append('<tr'+attrs+'>'+checkbox)
                chunks.extend('<td>'+inline(c)+'</td>' for c in row)
                chunks.append('</tr>')
            chunks.append('</tbody></table></div>')
            continue
        if (line.startswith("**") and line.endswith("**")) or line.startswith("#"):
            title = line[2:-2] if line.startswith("**") else line.lstrip("# ")
            if title.startswith("Seguimiento de estrenos"):
                chunks.append('<p class="report-title">'+html.escape(title)+'</p>')
            else:
                group = title
                anchor = "seccion-"+str(len(sections)+1)
                sections.append((anchor, title))
                chunks.append('<h2 id="'+anchor+'">'+html.escape(title)+'</h2>')
        else:
            chunks.append('<p>'+inline(line)+'</p>')
        i += 1
    if not count:
        raise ValueError("Informe sin registros")
    navigation = ''.join('<a href="#'+a+'">'+html.escape(t)+'</a>' for a,t in sections)
    body = '\n'.join(chunks)
    display_date = datetime.date.fromisoformat(fecha).strftime("%d/%m/%Y")
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Estrenos · Jumalenin · {display_date}</title>
<link rel="icon" href="https://common.jumalenin.com/assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="https://common.jumalenin.com/assets/css/jumalenin-core.css">
<link rel="stylesheet" href="https://common.jumalenin.com/assets/css/jumalenin-layout.css">
<link rel="stylesheet" href="https://common.jumalenin.com/assets/css/jumalenin-components.css">
<link rel="stylesheet" href="assets/estrenos.css">
<script src="assets/estrenos.js" defer></script>
</head>
<body class="site-shell">
<a class="skip-link" href="#informe">Saltar al informe</a>
<header class="site-header"><div class="header-inner">
<a class="site-brand" href="../../"><img src="https://common.jumalenin.com/assets/img/logo-horizontal.svg" alt="Jumalenin Support"></a>
<nav class="site-nav" aria-label="Principal"><a href="../../">Support</a><a href="#informe">Informe semanal</a></nav>
</div></header>
<main class="site-main">
<section class="hero"><div class="container">
<p class="eyebrow">CINE Y PLATAFORMAS</p><h1>Seguimiento de estrenos</h1>
<p>Películas y series evaluadas con las notas del público y las críticas profesionales de FilmAffinity.</p>
<p class="version">Última versión del informe: <time datetime="{fecha}">{display_date}</time></p>
</div></section>
<div class="container report-container">
<aside class="reading-note" aria-label="Tus marcas personales">
<p><strong>Tu lista de vistas.</strong> Marca lo que ya has visto. Los títulos seleccionados permanecen en negrita hasta que los marques; al desmarcarlos vuelven a destacarse.</p>
<p>Las marcas se guardan sólo en este navegador y dispositivo. Se conservan al actualizar el informe, pero se pierden si borras los datos del sitio. Las temporadas identificadas se marcan por separado.</p>
<p id="storage-status" role="status" aria-live="polite"></p>
<noscript><p>Activa JavaScript para usar las casillas. El informe completo se puede leer sin JavaScript.</p></noscript>
</aside>
<nav class="report-nav" aria-label="Secciones del informe">{navigation}</nav>
<article id="informe">{body}</article>
</div></main>
<footer class="site-footer"><div class="container"><p>Jumalenin Support · Estrenos. Disponibilidad orientativa a la fecha del informe.</p><a href="#informe">Volver al informe</a></div></footer>
</body></html>''', count, selected

def report_selector(fecha, dates):
    display = datetime.date.fromisoformat(fecha).strftime("%d/%m/%Y")
    label = "Última versión del informe" if fecha == max(dates) else "Informe seleccionado"
    links = []
    for date in sorted(dates, reverse=True):
        text = datetime.date.fromisoformat(date).strftime("%d/%m/%Y")
        current = ' aria-current="page"' if date == fecha else ''
        latest = " · Último" if date == max(dates) else ""
        links.append(f'<li><a href="informe-{date}.html"{current}>Viernes {text}{latest}</a></li>')
    return (f'<details class="version report-history"><summary>{label}: '
            f'<time datetime="{fecha}">{display}</time> · Elegir informe</summary>'
            '<nav aria-label="Informes semanales"><p>Informes por viernes de referencia</p><ul>'
            + ''.join(links) + '</ul></nav></details>')


def update_archive(root, fecha, content):
    if datetime.date.fromisoformat(fecha).weekday() != 4:
        raise ValueError("La fecha de referencia del informe debe ser un viernes")
    pages = {p.stem.removeprefix("informe-"): p.read_text(encoding="utf-8")
             for p in root.glob("informe-????-??-??.html")}
    # Conserva también la instantánea inicial al actualizar por primera vez.
    index = root / "index.html"
    if index.exists():
        previous = index.read_text(encoding="utf-8")
        match = re.search(r'<time datetime="(\d{4}-\d{2}-\d{2})">', previous)
        if match:
            pages.setdefault(match[1], previous)
    pages[fecha] = content
    for date in pages:
        if datetime.date.fromisoformat(date).weekday() != 4:
            raise ValueError("Fecha archivada no válida: " + date)
    prepared = {}
    for date, page in pages.items():
        page, matches = re.subn(
            r'<p class="version">.*?</p>|<details class="version report-history">.*?</details>',
            lambda _: report_selector(date, pages), page, count=1, flags=re.S)
        if matches != 1:
            raise ValueError("Falta la fecha del informe: " + date)
        prepared[root / f"informe-{date}.html"] = page
    prepared[index] = prepared[root / f"informe-{max(pages)}.html"]
    for target, page in prepared.items():
        temp = target.with_suffix(".html.tmp")
        temp.write_text(page, encoding="utf-8")
        temp.replace(target)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--informe", required=True, type=Path)
    p.add_argument("--fecha", required=True)
    args = p.parse_args()
    datetime.date.fromisoformat(args.fecha)
    content, count, selected = render(args.informe.read_text(encoding="utf-8-sig"), args.fecha)
    target = Path(__file__).resolve().parents[1] / "index.html"
    update_archive(target.parent, args.fecha, content)
    print(f"Generado: {count} registros, {selected} seleccionados. {target}")

if __name__ == "__main__":
    main()
