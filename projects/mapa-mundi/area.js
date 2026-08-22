const EDITION = "RG2025_V1";
const AREA_ORDER = ["AFR", "APC", "CHN", "EUR", "MDE", "NAC", "RUE", "SAI", "SAM"];
const API_TIMEOUT = 5000;
const CORE_METRICS = ["POB_TOTAL", "TERR_SUP", "ECO_PIB", "MIL_GASTO", "MIL_NUC"];
const PROFILE_METRICS = ["TERR_DENS", "POB_EDAD", "HUM_EV", "ECO_PC", "HUM_IDH"];
const LOCAL_HOSTNAMES = new Set(["127.0.0.1", "localhost"]);
const API_URL = LOCAL_HOSTNAMES.has(location.hostname)
  ? "/__reticula_api__/datos.php"
  : "/api/reticula/v1/datos.php";
const formatter = new Intl.NumberFormat("es-ES", { maximumFractionDigits: 1 });
const compact = new Intl.NumberFormat("es-ES", { notation: "compact", maximumFractionDigits: 2 });
const profileThree = new Intl.NumberFormat("es-ES", { minimumFractionDigits: 3, maximumFractionDigits: 3 });
const profileInteger = new Intl.NumberFormat("es-ES", { maximumFractionDigits: 0 });

function jsonResponse(response) {
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}

function validateAreaResponse(payload, code) {
  if (payload?.ok !== true || payload?.meta?.edicion?.codigo !== EDITION || !Array.isArray(payload.data)) {
    throw new Error("Contrato de API no válido");
  }
  const result = new Map();
  for (const record of payload.data) {
    const indicator = record?.indicador?.codigo;
    if (record?.area?.codigo !== code || !indicator || result.has(indicator)) {
      throw new Error("Respuesta territorial incoherente");
    }
    result.set(indicator, record);
  }
  if (!CORE_METRICS.every(metric => result.has(metric))) throw new Error("Faltan indicadores principales");
  return result;
}

async function loadApi(code) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), API_TIMEOUT);
  try {
    const response = await fetch(`${API_URL}?area=${encodeURIComponent(code)}`, {
      headers: { Accept: "application/json" },
      signal: controller.signal
    });
    return validateAreaResponse(await jsonResponse(response), code);
  } finally {
    clearTimeout(timeout);
  }
}

function localRecords(area) {
  return new Map(Object.entries(area.indicadores).map(([code, item]) => [
    code,
    {
      area: { codigo: area.codigo, nombre: area.nombre },
      indicador: { codigo: code, unidad: item.unidad },
      valor: item.valor,
      anio_referencia: item.anio,
      fuente_principal: { codigo: item.fuente_codigo, nombre: item.fuente },
      observaciones: item.observaciones,
      procedencia: "respaldo"
    }
  ]));
}

function value(records, code) {
  const number = Number(records.get(code)?.valor);
  return Number.isFinite(number) ? number : null;
}

function percentage(number, total) {
  return number == null || !total ? null : number / total * 100;
}

function scoreFor(areas, code, metric, selectedValue) {
  const values = areas.map(area => area.indicadores[metric]?.valor).filter(Number.isFinite);
  const transformed = values.map(number => Math.log(metric === "MIL_NUC" ? number + 1 : number));
  const current = Math.log(metric === "MIL_NUC" ? selectedValue + 1 : selectedValue);
  const min = Math.min(...transformed), max = Math.max(...transformed);
  return max === min ? 5.5 : 1 + 9 * (current - min) / (max - min);
}

function metricCard(label, display, meta, score) {
  const article = document.createElement("article");
  article.className = "metric";
  article.innerHTML = `<span class="metric-label">${label}</span><strong class="metric-value">${display}</strong><span class="metric-meta">${meta}</span>`;
  if (Number.isFinite(score)) {
    const scoreRow = document.createElement("div");
    scoreRow.className = "score";
    scoreRow.innerHTML = `<span class="score-track"><span class="score-fill" style="--score:${score}"></span></span><span>${formatter.format(score)}/10</span>`;
    article.append(scoreRow);
  }
  return article;
}

function addCards(target, cards) {
  const container = document.querySelector(target);
  cards.forEach(card => container.append(metricCard(...card)));
}

function profileDisplay(record, metric) {
  const number = Number(record?.valor);
  if (record?.valor === null || record?.valor === undefined || !Number.isFinite(number)) return "Dato no disponible";
  if (metric === "HUM_IDH") return profileThree.format(number);
  if (metric === "ECO_PC") return `${profileInteger.format(number)} USD/hab.`;
  return `${formatter.format(number)} ${metric === "TERR_DENS" ? "hab./km²" : "años"}`;
}

function renderAreaPopulationProfile(records, areaCode) {
  const target = document.querySelector("#area-profile-content");
  const labels = [
    ["TERR_DENS", "Densidad"],
    ["POB_EDAD", "Edad mediana"],
    ["HUM_EV", "Esperanza de vida"],
    ["ECO_PC", "PIB por habitante"],
    ["HUM_IDH", "IDH"],
    ["POB_URB", "Urbanización"]
  ];
  const list = document.createElement("dl");
  list.className = "area-profile-grid";
  for (const [metric, label] of labels) {
    const dt = document.createElement("dt");
    const dd = document.createElement("dd");
    dt.textContent = label;
    dd.textContent = metric === "POB_URB"
      ? "Pendiente de incorporación"
      : profileDisplay(records.get(metric), metric);
    const record = records.get(metric);
    if (metric === "ECO_PC" && record?.estado_dato === "LIMITACION") {
      const warning = document.createElement("p");
      warning.className = "area-profile-warning";
      warning.setAttribute("role", "note");
      warning.textContent = "Dato con cobertura incompleta. Comparabilidad limitada.";
      dd.append(warning);
    }
    list.append(dt, dd);
  }
  target.append(list);

  const details = document.createElement("details");
  details.className = "area-profile-details";
  const summary = document.createElement("summary");
  summary.textContent = "Fuente, año y observaciones";
  summary.setAttribute("aria-label", "Fuente, año y observaciones del perfil medio de la población");
  const content = document.createElement("div");
  content.className = "area-profile-details-content";
  for (const metric of PROFILE_METRICS) {
    const record = records.get(metric);
    if (!record) continue;
    const coverage = Number(record.cobertura?.porcentaje);
    const note = document.createElement("p");
    const heading = document.createElement("strong");
    heading.textContent = `${record.indicador?.nombre || metric}: `;
    note.append(heading);
    if (record.fuente_principal?.url) {
      const source = document.createElement("a");
      source.href = record.fuente_principal.url;
      source.textContent = record.fuente_principal.nombre || "Fuente";
      note.append(source);
    } else {
      note.append(record.fuente_principal?.nombre || "Fuente no disponible");
    }
    note.append(` · ${record.anio_referencia || "Año no disponible"}`);
    if (Number.isFinite(coverage)) note.append(` · cobertura ${formatter.format(coverage)} %`);
    if (record.estado_dato) note.append(` · estado ${record.estado_dato}`);
    if (record.observaciones) note.append(` · ${record.observaciones}`);
    content.append(note);
  }
  details.append(summary, content);
  target.append(details);
}

function formatType(value) {
  return value.toLowerCase().replaceAll("_", " ").replace(/^\p{L}/u, letter => letter.toUpperCase());
}

function renderTerritories(area) {
  document.querySelector("#territory-count").textContent = area.entidades.length;
  const body = document.querySelector("#territory-list");
  for (const entity of area.entidades) {
    const row = document.createElement("tr");
    row.innerHTML = `<td>${entity.nombre}</td><td>${entity.iso3}</td><td>${formatType(entity.tipo)}</td><td>${entity.incluir_calculos === "SI" ? "Incluido" : entity.incluir_calculos === "NO" ? "Excluido" : "Según fuente"}</td>`;
    body.append(row);
  }
}

function equalEarth([longitude, latitude]) {
  const lambda = longitude * Math.PI / 180, phi = latitude * Math.PI / 180;
  const theta = Math.asin(Math.sqrt(3) / 2 * Math.sin(phi)), t2 = theta * theta, t6 = t2 * t2 * t2;
  const denominator = 3 * (9 * .003796 * t6 + 7 * .000893 * t2 * t2 - 3 * .081106 * t2 + 1.340264);
  return [(2 * Math.sqrt(3) * lambda * Math.cos(theta)) / denominator, theta * (.003796 * t6 + .000893 * t2 * t2 - .081106 * t2 + 1.340264)];
}

function renderMiniMap(world, code) {
  const features = world.features.filter(feature => feature.properties.area === code);
  const points = features.flatMap(feature => {
    const polygons = feature.geometry.type === "Polygon" ? [feature.geometry.coordinates] : feature.geometry.coordinates;
    return polygons.flat(2).map(equalEarth);
  });
  const xs = points.map(point => point[0]), ys = points.map(point => point[1]);
  const bounds = [Math.min(...xs), Math.max(...xs), Math.min(...ys), Math.max(...ys)];
  const scale = Math.min(560 / (bounds[1] - bounds[0]), 260 / (bounds[3] - bounds[2]));
  const transform = point => [20 + (point[0] - bounds[0]) * scale, 280 - (point[1] - bounds[2]) * scale];
  const svg = document.querySelector("#area-map");
  for (const feature of features) {
    const polygons = feature.geometry.type === "Polygon" ? [feature.geometry.coordinates] : feature.geometry.coordinates;
    const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path.setAttribute("d", polygons.map(polygon => polygon.map(ring => ring.map((coordinate, index) => {
      const [x, y] = transform(equalEarth(coordinate));
      return `${index ? "L" : "M"}${x.toFixed(1)},${y.toFixed(1)}`;
    }).join("") + "Z").join("")).join(""));
    svg.append(path);
  }
}

async function initialize() {
  const code = new URLSearchParams(location.search).get("codigo")?.toUpperCase() || AREA_ORDER[0];
  if (!AREA_ORDER.includes(code)) throw new Error("Código de macroárea no válido");
  const [fallback, territories, palette, world] = await Promise.all([
    fetch("datos-indicadores.json").then(jsonResponse),
    fetch("territorios.json").then(jsonResponse),
    fetch("paleta.json").then(jsonResponse),
    fetch("world.geojson").then(jsonResponse)
  ]);
  const fallbackArea = fallback.areas.find(area => area.codigo === code);
  let records;
  try {
    records = await loadApi(code);
  } catch {
    records = localRecords(fallbackArea);
    document.querySelector("#data-notice").hidden = false;
  }

  const population = value(records, "POB_TOTAL"), surface = value(records, "TERR_SUP");
  const gdp = value(records, "ECO_PIB"), military = value(records, "MIL_GASTO"), nuclear = value(records, "MIL_NUC");
  const totals = metric => fallback.areas.reduce((sum, area) => sum + (area.indicadores[metric]?.valor || 0), 0);
  const militaryPerCapita = value(records, "MIL_PC") ?? military / population;
  const militaryGdp = value(records, "MIL_PIB") ?? percentage(military, gdp);
  const militaryShare = value(records, "MIL_PCT") ?? percentage(military, totals("MIL_GASTO"));
  const score = metric => scoreFor(fallback.areas, code, metric, value(records, metric));
  const areaName = fallbackArea.nombre;
  const currentIndex = AREA_ORDER.indexOf(code);
  const previousCode = AREA_ORDER[(currentIndex - 1 + AREA_ORDER.length) % AREA_ORDER.length];
  const nextCode = AREA_ORDER[(currentIndex + 1) % AREA_ORDER.length];
  const areaNameFor = areaCode => fallback.areas.find(area => area.codigo === areaCode).nombre;
  document.documentElement.style.setProperty("--area", palette[code]);
  document.title = `${areaName} · Retícula Global 2025`;
  document.querySelector("#area-name").textContent = areaName;
  document.querySelector("#area-code").textContent = code;
  document.querySelector("#footer-area").textContent = `${areaName} · ${code}`;
  const previousLink = document.querySelector("#previous-area");
  previousLink.href = `area.html?codigo=${previousCode}`;
  previousLink.textContent = `← Anterior: ${areaNameFor(previousCode)}`;
  const nextLink = document.querySelector("#next-area");
  nextLink.href = `area.html?codigo=${nextCode}`;
  nextLink.textContent = `Siguiente: ${areaNameFor(nextCode)} →`;
  document.querySelector("#area-map").setAttribute("aria-label", `Silueta territorial de ${areaName}`);

  addCards("#territory-metrics", [
    ["Entidades asignadas", territories.areas.find(area => area.codigo === code).entidades.length, "Maestro territorial RG2025", null],
    ["Superficie terrestre", `${compact.format(surface)} km²`, `${records.get("TERR_SUP").anio_referencia} · ${records.get("TERR_SUP").fuente_principal?.nombre}`, score("TERR_SUP")],
    ["Superficie de las nueve áreas", `${formatter.format(percentage(surface, totals("TERR_SUP")))} %`, "Cálculo en navegador", null]
  ]);
  addCards("#population-metrics", [
    ["Población total", compact.format(population), `${records.get("POB_TOTAL").anio_referencia} · personas`, score("POB_TOTAL")],
    ["Población de las nueve áreas", `${formatter.format(percentage(population, totals("POB_TOTAL")))} %`, "Cálculo en navegador", null],
    ["Densidad", `${formatter.format(population / surface)} hab./km²`, "Población ÷ superficie", null]
  ]);
  renderAreaPopulationProfile(records, code);
  addCards("#economy-metrics", [
    ["PIB nominal", `${compact.format(gdp)} USD`, `${records.get("ECO_PIB").anio_referencia} · USD corrientes`, score("ECO_PIB")],
    ["PIB por habitante", `${compact.format(gdp / population)} USD`, "PIB ÷ población", null],
    ["PIB de las nueve áreas", `${formatter.format(percentage(gdp, totals("ECO_PIB")))} %`, "Cálculo en navegador", null]
  ]);
  addCards("#military-metrics", [
    ["Gasto militar", `${compact.format(military)} USD`, `${records.get("MIL_GASTO").anio_referencia} · USD corrientes`, score("MIL_GASTO")],
    ["Gasto por habitante", `${formatter.format(militaryPerCapita)} USD`, records.has("MIL_PC") ? "Dato agregado validado" : "Respaldo: gasto ÷ población", null],
    ["Gasto respecto al PIB", `${formatter.format(militaryGdp)} %`, records.has("MIL_PIB") ? "PIB comparable cubierto" : "Respaldo: gasto ÷ PIB", null],
    ["Gasto de las nueve áreas", `${formatter.format(militaryShare)} %`, records.has("MIL_PCT") ? "Dato agregado validado" : "Cálculo en navegador", null],
    ["Ojivas nucleares", formatter.format(nuclear), `${records.get("MIL_NUC").anio_referencia} · ojivas`, score("MIL_NUC")]
  ]);

  const territorialArea = territories.areas.find(area => area.codigo === code);
  renderTerritories(territorialArea);
  renderMiniMap(world, code);
  const sources = document.querySelector("#sources");
  for (const metric of CORE_METRICS) {
    const record = records.get(metric);
    const item = document.createElement("p");
    item.className = "source";
    item.innerHTML = `<strong>${record.indicador.codigo}</strong><span>${record.fuente_principal?.nombre || "Fuente local documentada"} · ${record.anio_referencia}</span>`;
    sources.append(item);
  }
  document.querySelector("#loading").remove();
  document.querySelector("#content").hidden = false;
  document.querySelector("#area-sheet").setAttribute("aria-busy", "false");
}

initialize().catch(error => {
  const loading = document.querySelector("#loading");
  loading.setAttribute("role", "alert");
  loading.textContent = `No ha sido posible cargar la ficha. ${error.message}`;
  document.querySelector("#area-sheet").setAttribute("aria-busy", "false");
});
