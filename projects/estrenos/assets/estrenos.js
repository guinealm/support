"use strict";
(() => {
  const seenPrefix = "jumalenin:estrenos:vistas:v1:";
  const ratingPrefix = "jumalenin:estrenos:valoraciones:v1:";
  const ratings = ["recommended", "neutral", "dismissed"];
  const controls = new Map();
  const status = document.getElementById("storage-status");
  let available = true;

  function announce() {
    status.textContent = available
      ? "Tus marcas y valoraciones son privadas y se guardan en este navegador."
      : "Este navegador no permite guardar las marcas y valoraciones. Funcionarán durante esta visita, pero podrían perderse al cerrar o recargar.";
  }

  function read(key) {
    try {
      return localStorage.getItem(key);
    } catch (_) {
      available = false;
      return null;
    }
  }

  function update(key, value) {
    controls.get(key)?.forEach(render => render(value));
  }

  function bind(control, key, render, getValue) {
    if (!controls.has(key)) controls.set(key, []);
    controls.get(key).push(render);
    control.addEventListener("change", () => {
      const value = getValue();
      update(key, value);
      try {
        if (value === null) localStorage.removeItem(key);
        else localStorage.setItem(key, value);
      } catch (_) {
        available = false;
      }
      announce();
    });
  }

  document.querySelectorAll("input[data-seen]").forEach(box => {
    const row = box.closest("tr");
    box.disabled = false;
    bind(box, seenPrefix + box.dataset.seen, value => {
      box.checked = value === "1";
      row.classList.toggle("seen", box.checked);
    }, () => box.checked ? "1" : null);
  });

  const tables = new Set();
  document.querySelectorAll(".seen-cell").forEach(seenCell => {
    const table = seenCell.closest("table");
    const column = seenCell.cellIndex + 1;
    if (!tables.has(table)) {
      const header = document.createElement("th");
      header.scope = "col";
      header.textContent = "Valoración";
      table.tHead.rows[0].cells[column - 1].after(header);
      tables.add(table);
    }

    const row = seenCell.parentElement;
    const title = row.cells[column].textContent.trim();
    const cell = row.insertCell(column);
    const box = seenCell.querySelector("input[data-seen]");
    if (!box) {
      cell.textContent = "—";
      return;
    }

    const select = document.createElement("select");
    select.className = "personal-rating";
    select.setAttribute("aria-label", "Valoración personal de " + title);
    select.innerHTML = '<option value="">Sin valorar</option>' +
      '<option value="recommended">Recomendable</option>' +
      '<option value="neutral">Neutra</option>' +
      '<option value="dismissed">Descartable</option>';
    cell.append(select);
    bind(select, ratingPrefix + box.dataset.seen, value => {
      select.value = ratings.includes(value) ? value : "";
      select.dataset.rating = select.value;
    }, () => select.value || null);
  });

  function restore() {
    controls.forEach((_, key) => update(key, read(key)));
    announce();
  }

  window.addEventListener("storage", event => {
    if (event.key === null) restore();
    else update(event.key, event.newValue);
  });
  restore();
})();
