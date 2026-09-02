const AREA_DESCRIPTORS = {
  AFR: "El gran horizonte demográfico",
  APC: "El arco marítimo y tecnológico",
  CHN: "El núcleo industrial",
  EUR: "La península atlántica",
  MDE: "El pivote energético",
  NAC: "La fortaleza continental",
  RUE: "La profundidad euroasiática",
  SAI: "El núcleo demográfico",
  SAM: "La reserva estratégica"
};

const SVG_NS = "http://www.w3.org/2000/svg";
const countries = document.querySelector("#landing-countries");
const areaList = document.querySelector("#area-list");
const mapStatus = document.querySelector("#map-status");

function requireJson(response) {
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
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
    const polygons = feature.geometry.type === "Polygon" ? [feature.geometry.coordinates] : feature.geometry.coordinates;
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
  return polygons.map(polygon => polygon.map(ring => ring.map((coordinate, index) => {
    const [x, y] = transform(equalEarth(coordinate));
    return `${index ? "L" : "M"}${x.toFixed(2)},${y.toFixed(2)}`;
  }).join("") + "Z").join("")).join("");
}

function renderAreas(areas, palette) {
  const fragment = document.createDocumentFragment();
  for (const area of areas) {
    const link = document.createElement("a");
    link.className = "area-card";
    link.href = `area.html?codigo=${encodeURIComponent(area.codigo)}`;
    link.style.setProperty("--area-color", palette[area.codigo]);
    link.innerHTML = `
      <span class="area-top"><span class="area-code">${area.codigo}</span><span class="area-arrow" aria-hidden="true">↗</span></span>
      <span><h3>${area.nombre}</h3><p>${AREA_DESCRIPTORS[area.codigo]}</p></span>
    `;
    fragment.append(link);
  }
  areaList.append(fragment);
}

function renderMap(geojson, palette) {
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
    path.setAttribute("d", geometryPath(feature.geometry, transform));
    path.setAttribute("class", "landing-country");
    path.setAttribute("fill", feature.properties.area ? palette[feature.properties.area] : "url(#landing-neutral)");
    fragment.append(path);
  }
  countries.append(fragment);
  mapStatus.textContent = "Selecciona una de las nueve áreas para abrir su ficha.";
}

Promise.all([
  fetch("areas.json").then(requireJson),
  fetch("paleta.json").then(requireJson),
  fetch("world.geojson").then(requireJson)
]).then(([areasData, palette, world]) => {
  renderAreas(areasData.areas, palette);
  renderMap(world, palette);
}).catch(error => {
  mapStatus.textContent = "El mapa no se ha podido cargar. El explorador sigue disponible.";
  mapStatus.setAttribute("role", "alert");
  console.error(error);
});
