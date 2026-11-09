"""Validación local independiente del inventario y regresión de conservación."""
from html.parser import HTMLParser
from pathlib import Path
from recomendados import collect


class Rows(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.keys = []
        self.links = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'tr' and 'selected' in attrs.get('class', '').split():
            self.keys.append(attrs['data-title-key'])
        if tag == 'a':
            self.links.append(attrs.get('href', ''))


root = Path(__file__).resolve().parents[1]
pages = {p.stem[8:]: p.read_text(encoding='utf-8') for p in root.glob('informe-????-??-??.html')}
expected = set().union(*(set(Rows(page).keys) for page in pages.values()))
catalog = Rows((root / 'recomendados.html').read_text(encoding='utf-8'))
assert len(catalog.keys) == len(set(catalog.keys)), 'Duplicados'
assert set(catalog.keys) == expected, 'Selección acumulada incorrecta'
for link in catalog.links:
    if link.startswith('informe-'):
        assert (root / link).is_file(), link
for page in [*pages.values(), (root / 'index.html').read_text(encoding='utf-8')]:
    assert page.count('class="catalog-action"') == 1
    assert 'href="recomendados.html"' in page
old = '<table><th>Vista</th><th>Título</th><th>Medio</th><tr data-title-key="fa:1" class="selected"><td>casilla</td><td>Título</td><td>Cine</td></tr></table>'
later = old.replace('class="selected"', 'class=""').replace('Cine', 'Otro')
result = collect({'2026-10-02': old, '2026-10-09': later})
assert result['fa:1']['date'] == '2026-10-02'
assert result['fa:1']['media'] == {'Cine'}
print(f'OK: {len(pages)} informes, {len(expected)} recomendaciones únicas; enlaces, exclusiones y conservación comprobados.')
