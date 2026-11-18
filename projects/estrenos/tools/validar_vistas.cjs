// Ejecuta el script compartido en dos páginas simuladas del mismo origen.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = fs.readFileSync(require('node:path').join(__dirname, '../assets/estrenos.js'), 'utf8');
const saved = new Map();
const windows = [];
function page() {
  const events = {};
  const ratingEvents = {};
  const select = {dataset: {}, setAttribute: () => {},
    addEventListener: (name, fn) => {ratingEvents[name] = fn;}};
  const row = {classList: {toggle: (_, value) => {box.seen = value;}},
    cells: [{}, {textContent: 'Una película'}],
    insertCell: index => {
      assert.equal(index, 1);
      return {append: control => assert.equal(control, select)};
    }};
  const box = {dataset: {seen: 'fa:1'}, disabled: true, checked: false,
    closest: () => row,
    addEventListener: (name, fn) => {events[name] = fn;}};
  const header = {};
  const table = {tHead: {rows: [{cells: [{after: node => assert.equal(node, header)}]}]}};
  const seenCell = {cellIndex: 0, parentElement: row, closest: () => table,
    querySelector: () => box};
  const window = {addEventListener: (_, fn) => {window.storage = fn;}};
  windows.push(window);
  function write(key, value) {
    if (value === null) saved.delete(key); else saved.set(key, value);
    windows.filter(w => w !== window).forEach(w => w.storage({key, newValue: value}));
  }
  vm.runInNewContext(source, {window,
    document: {
      querySelectorAll: selector => selector === '.seen-cell' ? [seenCell] : [box],
      createElement: tag => tag === 'th' ? header : select,
      getElementById: () => ({textContent: ''})
    },
    localStorage: {getItem: k => saved.get(k), setItem: write, removeItem: k => write(k, null)}});
  assert.equal(header.textContent, 'Valoración');
  return {box, events, select, ratingEvents};
}
const weekly = page();
const catalog = page();
weekly.box.checked = true;
weekly.events.change();
assert.equal(catalog.box.checked, true);
assert.equal(catalog.box.seen, true);
assert.equal(page().box.checked, true);
for (const value of ['recommended', 'neutral', 'dismissed']) {
  weekly.select.value = value;
  weekly.ratingEvents.change();
  assert.equal(catalog.select.value, value);
  assert.equal(catalog.select.dataset.rating, value);
  assert.equal(page().select.value, value);
}
catalog.select.value = '';
catalog.ratingEvents.change();
assert.equal(weekly.select.value, '');
assert.equal(page().select.value, '');
assert.equal(weekly.box.checked, true);
catalog.box.checked = false;
catalog.events.change();
assert.equal(weekly.box.seen, false);
assert.equal(saved.size, 0);
console.log('OK: Vista y Valoración persisten y se sincronizan entre páginas (simulación sin navegador).');
