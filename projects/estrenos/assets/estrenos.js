"use strict";
(() => {
  const prefix = "jumalenin:estrenos:vistas:v1:";
  const boxes = [...document.querySelectorAll("input[data-seen]")];
  const status = document.getElementById("storage-status");
  const memory = new Map();
  let available = true;
  function read(key) {
    if (memory.has(key)) return memory.get(key);
    try {
      const value = localStorage.getItem(prefix + key) === "1";
      memory.set(key, value);
      return value;
    } catch (_) {
      available = false;
      return false;
    }
  }
  function announce() {
    status.textContent = available
      ? "Tus marcas son privadas: no cambian las de otros visitantes."
      : "Este navegador no permite guardar las marcas. Funcionarán durante esta visita, pero podrían perderse al cerrar o recargar.";
  }
  function sync(key, value) {
    memory.set(key, value);
    boxes.filter(box => box.dataset.seen === key).forEach(box => {
      box.checked = value;
      box.closest("tr").classList.toggle("seen", value);
    });
  }
  boxes.forEach(box => {
    box.disabled = false;
    const key = box.dataset.seen;
    sync(key, read(key));
    box.addEventListener("change", () => {
      sync(key, box.checked);
      try {
        if (box.checked) localStorage.setItem(prefix + key, "1");
        else localStorage.removeItem(prefix + key);
      } catch (_) {
        available = false;
      }
      announce();
    });
  });
  window.addEventListener("storage", event => {
    if (event.key === null) {
      memory.clear();
      boxes.forEach(box => sync(box.dataset.seen, read(box.dataset.seen)));
    } else if (event.key.startsWith(prefix)) {
      sync(event.key.slice(prefix.length), event.newValue === "1");
    }
  });
  announce();
})();
