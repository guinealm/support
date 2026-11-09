// Ejecuta el script compartido en dos páginas simuladas del mismo origen.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = fs.readFileSync(require('node:path').join(__dirname, '../assets/estrenos.js'), 'utf8');
const saved = new Map();
const windows = [];
function page() {
  const events = {};
  const box = {dataset: {seen: 'fa:1'}, disabled: true, checked: false,
    closest: () => ({classList: {toggle: (_, value) => {box.seen = value;}}}),
    addEventListener: (name, fn) => {events[name] = fn;}};
  const window = {addEventListener: (_, fn) => {window.storage = fn;}};
  windows.push(window);
  function write(key, value) {
    if (value === null) saved.delete(key); else saved.set(key, value);
    windows.filter(w => w !== window).forEach(w => w.storage({key, newValue: value}));
  }
  vm.runInNewContext(source, {window,
    document: {querySelectorAll: () => [box], getElementById: () => ({textContent: ''})},
    localStorage: {getItem: k => saved.get(k), setItem: write, removeItem: k => write(k, null)}});
  return {box, events};
}
const weekly = page();
const catalog = page();
weekly.box.checked = true;
weekly.events.change();
assert.equal(catalog.box.checked, true);
assert.equal(catalog.box.seen, true);
assert.equal(page().box.checked, true);
catalog.box.checked = false;
catalog.events.change();
assert.equal(weekly.box.seen, false);
assert.equal(saved.size, 0);
console.log('OK: marcas compartidas, persistencia y sincronización en ambos sentidos (simulación sin navegador).');
