const STORAGE_KEY = "reticula-global-paleta-v1";
const SVG_NS = "http://www.w3.org/2000/svg";

const map = document.querySelector("#world-map");
const countriesGroup = document.querySelector("#countries");
const legend = document.querySelector("#legend");
const filter = document.querySelector("#area-filter");
const tooltip = document.querySelector("#tooltip");
const mapWrap = document.querySelector("#map-wrap");
const comparisonBody = document.querySelector("#comparison-body");
const sortStatus = document.querySelector("#sort-status");
const fallbackNotice = document.querySelector("#data-fallback-notice");
const viewAreaLink = document.querySelector("#view-area-link");

let defaultPalette = {};
let palette = {};
let areaData = [];
let indicatorAreas = [];
let scores = {};
let sortState = { key: "orden", direction: "asc" };

const METRICS = ["POB_TOTAL", "TERR_SUP", "ECO_PIB", "MIL_GASTO", "MIL_NUC"];
const EXPECTED_AREAS = ["AFR", "APC", "CHN", "EUR", "MDE", "NAC", "RUE", "SAI", "SAM"];
const EXPECTED_EDITION = "RG2025_V1";
const API_URL = "/api/reticula/v1/datos.php";
const API_TIMEOUT_MS = 5000;
const SORT_LABELS = {
  nombre: "nombre del área",
  POB_TOTAL: "población",
  TERR_SUP: "superficie",
  ECO_PIB: "PIB nominal",
  MIL_GASTO: "gasto militar",
  MIL_NUC: "ojivas nucleares"
};
const decimalOne = new Intl.NumberFormat("es-ES", { minimumFractionDigits: 1, maximumFractionDigits: 1 });
const decimalTwo = new Intl.NumberFormat("es-ES", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const integerFormat = new Intl.NumberFormat("es-ES", { maximumFractionDigits: 0 });

function requireJson(response) {
  if (!response.ok) throw new Error(`HTTP ${response.status}: ${response.url}`);
  return response.json();
}

function validateApiPayload(payload, metric) {
  if (!payload || payload.ok !== true || payload.meta?.edicion?.codigo !== EXPECTED_EDITION || !Array.isArray(payload.data)) {
    throw new Error(`Respuesta no válida para ${metric}`);
  }
  const records = new Map();
  for (const record of payload.data) {
    const area = record?.area?.codigo;
    if (!EXPECTED_AREAS.includes(area) || record?.indicador?.codigo !== metric || records.has(area)) {
      throw new Error(`Cobertura no válida para ${metric}`);
    }
    records.set(area, record);
  }
  return records;
}

async function fetchApiIndicator(metric, signal) {
  const response = await fetch(`${API_URL}?indicador=${encodeURIComponent(metric)}`, {
    headers: { Accept: "application/json" },
    signal
  });
  return validateApiPayload(await requireJson(response), metric);
}

function apiIndicator(record, editorialFallback) {
  return {
    valor: record.valor,
    anio: record.anio_referencia,
    anio_minimo: record.anio_minimo,
    anio_maximo: record.anio_maximo,
    unidad: record.indicador?.unidad ?? null,
    fuente_codigo: record.fuente_principal?.codigo ?? null,
    fuente: record.fuente_principal?.nombre ?? null,
    fuente_url: record.fuente_principal?.url ?? null,
    cobertura: record.cobertura ?? null,
    metodo: record.metodo_calculo ?? null,
    estado: record.estado_dato ?? null,
    observaciones: record.observaciones || editorialFallback?.observaciones || "",
    observaciones_editoriales: editorialFallback?.observaciones || "",
    procedencia: "api"
  };
}

function mergeIndicatorData(fallbackData, apiResults) {
  if (fallbackData?.edicion?.codigo !== EXPECTED_EDITION || !Array.isArray(fallbackData.areas)) {
    throw new Error("El archivo de respaldo no corresponde a RG2025_V1");
  }
  let usedFallback = false;
  const areas = fallbackData.areas.map(area => {
    const indicadores = {};
    for (const metric of METRICS) {
      const fallback = area.indicadores?.[metric];
      const record = apiResults[metric]?.get(area.codigo);
      if (record && record.valor !== null && record.valor !== undefined && Number.isFinite(Number(record.valor))) {
        indicadores[metric] = apiIndicator({ ...record, valor: Number(record.valor) }, fallback);
      } else {
        usedFallback = true;
        indicadores[metric] = { ...fallback, procedencia: "respaldo" };
      }
    }
    return { ...area, indicadores };
  });
  return { areas, usedFallback };
}

async function loadIndicatorData() {
  const fallbackPromise = fetch("datos-indicadores.json").then(requireJson);
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), API_TIMEOUT_MS);
  const settled = await Promise.allSettled(
    METRICS.map(metric => fetchApiIndicator(metric, controller.signal))
  );
  clearTimeout(timeout);
  const fallbackData = await fallbackPromise;
  const apiResults = {};
  METRICS.forEach((metric, index) => {
    apiResults[metric] = settled[index].status === "fulfilled" ? settled[index].value : null;
  });
  return mergeIndicatorData(fallbackData, apiResults);
}

function equalEarth([longitude, latitude]) {
  const lambda = longitude * Math.PI / 180;
  const phi = latitude * Math.PI / 180;
  const A1 = 1.340264, A2 = -0.081106, A3 = 0.000893, A4 = 0.003796;
  const M = Math.sqrt(3) / 2;
  const theta = Math.asin(M * Math.sin(phi));
  const theta2 = theta * theta;
  const theta6 = theta2 * theta2 * theta2;
  const denominator = 3 * (9 * A4 * theta6 + 7 * A3 * theta2 * theta2 + 3 * A2 * theta2 + A1);
  return [
    (2 * Math.sqrt(3) * lambda * Math.cos(theta)) / denominator,
    theta * (A4 * theta6 + A3 * theta2 * theta2 + A2 * theta2 + A1)
  ];
}

function projectionBounds(geojson) {
  const bounds = { minX: Infinity, maxX: -Infinity, minY: Infinity, maxY: -Infinity };
  for (const feature of geojson.features) {
    const polygons = feature.geometry.type === "Polygon"
      ? [feature.geometry.coordinates]
      : feature.geometry.coordinates;
    for (const polygon of polygons) {
      for (const ring of polygon) {
        for (const coordinate of ring) {
          const [x, y] = equalEarth(coordinate);
          bounds.minX = Math.min(bounds.minX, x);
          bounds.maxX = Math.max(bounds.maxX, x);
          bounds.minY = Math.min(bounds.minY, y);
          bounds.maxY = Math.max(bounds.maxY, y);
        }
      }
    }
  }
  return bounds;
}

function geometryPath(geometry, transform) {
  const polygons = geometry.type === "Polygon" ? [geometry.coordinates] : geometry.coordinates;
  return polygons.map(polygon =>
    polygon.map(ring =>
      ring.map((coordinate, index) => {
        const [x, y] = transform(equalEarth(coordinate));
        return `${index ? "L" : "M"}${x.toFixed(2)},${y.toFixed(2)}`;
      }).join("") + "Z"
    ).join("")
  ).join("");
}

function currentPalette() {
  try {
    return { ...defaultPalette, ...JSON.parse(sessionStorage.getItem(STORAGE_KEY) || "{}") };
  } catch {
    return { ...defaultPalette };
  }
}

function setAreaColor(area, color) {
  palette[area] = color;
  sessionStorage.setItem(STORAGE_KEY, JSON.stringify(palette));
  document.querySelectorAll(`.country[data-area="${area}"]`).forEach(path => {
    path.style.fill = color;
  });
  const row = comparisonBody.querySelector(`[data-area="${area}"]`);
  if (row) row.style.setProperty("--area-color", color);
}

function renderLegend() {
  const selectedArea = filter.value;
  legend.replaceChildren();
  filter.querySelectorAll("option:not(:first-child)").forEach(option => option.remove());
  for (const area of areaData) {
    const option = new Option(`${area.codigo} — ${area.nombre}`, area.codigo);
    filter.add(option);

    const item = document.createElement("label");
    item.className = "legend-item";
    item.innerHTML = `
      <input class="color-control" type="color" value="${palette[area.codigo]}" data-area="${area.codigo}" aria-label="Color de ${area.nombre}">
      <span class="legend-name">${area.nombre}<span class="legend-code">${area.codigo}</span></span>
      <span class="legend-count">${area.paises_csv} entidades</span>
    `;
    item.querySelector("input").addEventListener("input", event => setAreaColor(area.codigo, event.target.value));
    legend.append(item);
  }
  if (selectedArea && areaData.some(area => area.codigo === selectedArea)) {
    filter.value = selectedArea;
  }
}

function showTooltip(props) {
  const areaName = areaData.find(area => area.codigo === props.area)?.nombre || props.area_name;
  tooltip.innerHTML = `<strong>${props.name}</strong><span>${props.iso3} · ${areaName}</span>`;
  tooltip.hidden = false;
}

function updateAreaLink(area) {
  viewAreaLink.hidden = !area;
  if (area) {
    const areaName = areaData.find(item => item.codigo === area)?.nombre || area;
    viewAreaLink.href = `area.html?codigo=${encodeURIComponent(area)}`;
    viewAreaLink.textContent = `Ver ficha de ${areaName}`;
    viewAreaLink.setAttribute("aria-label", `Ver ficha de ${areaName}`);
  } else {
    viewAreaLink.removeAttribute("aria-label");
  }
}

function renderMap(geojson) {
  const bounds = projectionBounds(geojson);
  const width = 1200, height = 650, padding = 24;
  const scale = Math.min(
    (width - padding * 2) / (bounds.maxX - bounds.minX),
    (height - padding * 2) / (bounds.maxY - bounds.minY)
  );
  const transform = ([x, y]) => [
    padding + (x - bounds.minX) * scale,
    height - padding - (y - bounds.minY) * scale
  ];

  const fragment = document.createDocumentFragment();
  for (const feature of geojson.features) {
    const path = document.createElementNS(SVG_NS, "path");
    const props = feature.properties;
    path.setAttribute("d", geometryPath(feature.geometry, transform));
    path.setAttribute("class", "country");
    path.setAttribute("tabindex", "0");
    path.setAttribute("role", "img");
    const areaName = areaData.find(area => area.codigo === props.area)?.nombre || props.area_name;
    path.setAttribute("aria-label", `${props.name}, ${props.iso3}, ${areaName}`);
    path.dataset.iso3 = props.iso3;
    path.dataset.area = props.area || "";
    path.style.fill = props.area ? palette[props.area] : "url(#neutral-pattern)";
    path.addEventListener("pointerenter", () => showTooltip(props));
    path.addEventListener("pointerup", () => {
      showTooltip(props);
      if (props.area) {
        filter.value = props.area;
        applyFilter(props.area);
      }
    });
    path.addEventListener("pointerleave", () => { tooltip.hidden = true; });
    path.addEventListener("focus", () => showTooltip(props));
    path.addEventListener("blur", () => { tooltip.hidden = true; });
    fragment.append(path);
  }
  countriesGroup.append(fragment);
  document.querySelector("#loading").remove();
  mapWrap.setAttribute("aria-busy", "false");
}

function applyFilter(area) {
  updateAreaLink(area);
  document.querySelectorAll(".country").forEach(path => {
    path.classList.toggle("is-muted", Boolean(area) && path.dataset.area !== area);
    path.classList.toggle("is-active", Boolean(area) && path.dataset.area === area);
  });
  comparisonBody.querySelectorAll("tr").forEach(row => {
    const selected = Boolean(area) && row.dataset.area === area;
    row.classList.toggle("is-selected", selected);
    row.setAttribute("aria-selected", String(selected));
  });
}

function calculateScores(areas) {
  const calculated = {};
  for (const metric of METRICS) {
    const valid = areas
      .map(area => area.indicadores[metric]?.valor)
      .filter(value => value !== null && value !== undefined && Number.isFinite(value));
    const transform = value => metric === "MIL_NUC" ? Math.log(value + 1) : Math.log(value);
    const transformed = valid.map(transform);
    const minimum = Math.min(...transformed);
    const maximum = Math.max(...transformed);
    calculated[metric] = {};
    for (const area of areas) {
      const value = area.indicadores[metric]?.valor;
      if (value === null || value === undefined || !Number.isFinite(value)) {
        calculated[metric][area.codigo] = null;
        continue;
      }
      const score = maximum === minimum
        ? 5.5
        : 1 + 9 * (transform(value) - minimum) / (maximum - minimum);
      calculated[metric][area.codigo] = score;
    }
  }
  return calculated;
}

function formatNaturalValue(metric, value) {
  if (value === null || value === undefined || !Number.isFinite(value)) return "No disponible";
  if (metric === "POB_TOTAL") return `${decimalOne.format(value / 1e6)} millones`;
  if (metric === "TERR_SUP") return `${decimalTwo.format(value / 1e6)} millones km²`;
  if (metric === "ECO_PIB") return `${decimalTwo.format(value / 1e12)} billones USD`;
  if (metric === "MIL_GASTO") return `${decimalOne.format(value / 1e9)} mil millones USD`;
  return `${integerFormat.format(value)} ojivas`;
}

function createMetricCell(area, metric) {
  const cell = document.createElement("td");
  const indicator = area.indicadores[metric];
  const score = scores[metric][area.codigo];
  const value = document.createElement("span");
  value.className = "metric-value";
  value.textContent = formatNaturalValue(metric, indicator?.valor);
  cell.append(value);

  if (score !== null) {
    const scoreRow = document.createElement("div");
    scoreRow.className = "score-row";
    const track = document.createElement("span");
    track.className = "score-track";
    track.setAttribute("aria-hidden", "true");
    const fill = document.createElement("span");
    fill.className = "score-fill";
    fill.style.setProperty("--score", score);
    track.append(fill);
    const label = document.createElement("span");
    label.className = "score-label";
    label.textContent = `${decimalOne.format(score)}/10`;
    scoreRow.append(track, label);
    cell.append(scoreRow);
  }
  return cell;
}

function sortedIndicatorAreas() {
  const result = [...indicatorAreas];
  if (sortState.key === "orden") return result;
  const factor = sortState.direction === "asc" ? 1 : -1;
  return result.sort((left, right) => {
    if (sortState.key === "nombre") {
      return factor * left.nombre.localeCompare(right.nombre, "es");
    }
    const leftValue = left.indicadores[sortState.key]?.valor;
    const rightValue = right.indicadores[sortState.key]?.valor;
    if (leftValue == null && rightValue == null) return 0;
    if (leftValue == null) return 1;
    if (rightValue == null) return -1;
    return factor * (leftValue - rightValue);
  });
}

function selectAreaFromTable(area) {
  const nextArea = filter.value === area ? "" : area;
  filter.value = nextArea;
  applyFilter(nextArea);
  if (nextArea) {
    const reducedMotion = window.matchMedia?.("(prefers-reduced-motion: reduce)").matches;
    mapWrap.scrollIntoView({ behavior: reducedMotion ? "auto" : "smooth", block: "center" });
  }
}

function renderComparison() {
  const selectedArea = filter.value;
  comparisonBody.replaceChildren();
  for (const area of sortedIndicatorAreas()) {
    const row = document.createElement("tr");
    row.dataset.area = area.codigo;
    row.tabIndex = 0;
    row.setAttribute("aria-selected", String(selectedArea === area.codigo));
    row.setAttribute("aria-label", `${area.nombre}. Seleccionar para resaltar en el mapa.`);
    row.style.setProperty("--area-color", palette[area.codigo]);
    row.classList.toggle("is-selected", selectedArea === area.codigo);

    const areaCell = document.createElement("td");
    areaCell.className = "sticky-column";
    const areaLabel = document.createElement("span");
    areaLabel.className = "area-cell";
    areaLabel.innerHTML = `<span><strong>${area.nombre}</strong><span>${area.codigo}</span></span>`;
    const sheetLink = document.createElement("a");
    sheetLink.className = "table-sheet-link";
    sheetLink.href = `area.html?codigo=${encodeURIComponent(area.codigo)}`;
    sheetLink.textContent = "Ver ficha";
    sheetLink.setAttribute("aria-label", `Ver ficha de ${area.nombre}`);
    sheetLink.addEventListener("click", event => event.stopPropagation());
    areaLabel.append(sheetLink);
    areaCell.append(areaLabel);
    row.append(areaCell);
    for (const metric of METRICS) row.append(createMetricCell(area, metric));
    row.addEventListener("click", () => selectAreaFromTable(area.codigo));
    row.addEventListener("keydown", event => {
      if (event.target === row && (event.key === "Enter" || event.key === " ")) {
        event.preventDefault();
        selectAreaFromTable(area.codigo);
      }
    });
    comparisonBody.append(row);
  }
}

document.querySelector("#toggle-borders").addEventListener("change", event => {
  map.classList.toggle("no-borders", !event.target.checked);
});

filter.addEventListener("change", event => applyFilter(event.target.value));

document.querySelectorAll(".sort-button").forEach(button => {
  button.addEventListener("click", () => {
    const key = button.dataset.sort;
    sortState.direction = sortState.key === key
      ? (sortState.direction === "asc" ? "desc" : "asc")
      : (key === "nombre" ? "asc" : "desc");
    sortState.key = key;
    document.querySelectorAll(".sort-button").forEach(control => {
      control.closest("th").removeAttribute("aria-sort");
    });
    button.closest("th").setAttribute("aria-sort", sortState.direction === "asc" ? "ascending" : "descending");
    const directionLabel = sortState.direction === "asc" ? "ascendente" : "descendente";
    sortStatus.textContent = `Orden: ${SORT_LABELS[key]}, ${directionLabel}.`;
    renderComparison();
  });
});

document.querySelector("#restore-colors").addEventListener("click", () => {
  sessionStorage.removeItem(STORAGE_KEY);
  palette = { ...defaultPalette };
  renderLegend();
  for (const [area, color] of Object.entries(palette)) setAreaColor(area, color);
});

document.querySelector("#download-svg").addEventListener("click", () => {
  const clone = map.cloneNode(true);
  clone.setAttribute("xmlns", SVG_NS);
  clone.querySelectorAll(".country").forEach(path => {
    path.classList.remove("is-muted", "is-active");
    const area = path.dataset.area;
    path.setAttribute("fill", area && palette[area] ? palette[area] : "#e4e4df");
    path.removeAttribute("style");
    path.removeAttribute("tabindex");
    path.removeAttribute("role");
    path.removeAttribute("aria-label");
  });
  const blob = new Blob([new XMLSerializer().serializeToString(clone)], { type: "image/svg+xml;charset=utf-8" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = "mapa-simbolico-mundial.svg";
  link.click();
  URL.revokeObjectURL(link.href);
});

Promise.all([
  fetch("paleta.json").then(requireJson),
  fetch("areas.json").then(requireJson),
  fetch("world.geojson").then(requireJson),
  loadIndicatorData()
]).then(([loadedPalette, areas, world, indicators]) => {
  defaultPalette = loadedPalette;
  palette = currentPalette();
  areaData = areas.areas;
  indicatorAreas = indicators.areas;
  fallbackNotice.hidden = !indicators.usedFallback;
  scores = calculateScores(indicatorAreas);
  renderLegend();
  renderMap(world);
  renderComparison();
}).catch(error => {
  document.querySelector("#loading").textContent = "No se pudo cargar el mapa. Ábrelo mediante el servidor local indicado en README.";
  console.error(error);
});
