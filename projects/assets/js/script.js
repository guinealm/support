/* Lógica General y Enrutador de Scripts */

// Funciones globales para el Mapa (deben estar fuera del DOMContentLoaded para los onclick del HTML)
window.showTooltip = function(evt, title, desc) {
    const tooltip = document.getElementById('map-tooltip');
    if (!tooltip) return;
    const ttTitle = document.getElementById('tt-title');
    const ttDesc = document.getElementById('tt-desc');
    tooltip.style.opacity = 1;
    ttTitle.textContent = title;
    ttDesc.textContent = desc;
};

window.moveTooltip = function(evt) {
    const tooltip = document.getElementById('map-tooltip');
    if (!tooltip) return;
    tooltip.style.left = evt.clientX + 'px';
    tooltip.style.top = evt.clientY + 'px';
};

window.hideTooltip = function() {
    const tooltip = document.getElementById('map-tooltip');
    if (tooltip) tooltip.style.opacity = 0;
};

window.openViewer = function(fileName, typeCode) {
    const modal = document.getElementById('pdf-viewer-modal');
    if (!modal) return;
    document.getElementById('modal-title').textContent = fileName;
    document.getElementById('doc-heading').textContent = fileName.replace('.pdf', '');
    document.getElementById('doc-name-ref').textContent = fileName;
    modal.classList.remove('hidden');
};

window.closeViewer = function() {
    const modal = document.getElementById('pdf-viewer-modal');
    if (modal) modal.classList.add('hidden');
};

// Lógica principal al cargar
document.addEventListener('DOMContentLoaded', () => {

    /* --- LÓGICA DE LANDING PAGE --- */
    if (document.body.classList.contains('landing-page')) {
        console.log("Landing Page cargada.");
        // Aquí podrías agregar efectos extra para la landing
    }

    /* --- LÓGICA DE HERENCIA (Observadores) --- */
    if (document.body.classList.contains('herencia-body')) {
        const observerOptions = { threshold: 0.2 };
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    
                    if(entry.target.id === 'contexto') {
                        const bars = entry.target.querySelectorAll('.fill-cost');
                        bars.forEach(bar => bar.style.width = bar.getAttribute('data-width'));
                    }
                    if(entry.target.id === 'veredicto') {
                        const pie = entry.target.querySelector('.pie-chart');
                        if(pie) pie.classList.add('animate');
                    }
                }
            });
        }, observerOptions);

        document.querySelectorAll('.section-card').forEach(section => {
            observer.observe(section);
        });
    }

    /* --- LÓGICA DE MAPA MUNDI (Chart.js) --- */
    // Solo ejecutamos si existe el elemento del gráfico para evitar errores
    if (document.getElementById('scatterChart')) {
        
        // Colors for Charts
        const colors = {
            na: '#3B82F6', sa: '#10B981', eu: '#8B5CF6', ru: '#EF4444',
            cn: '#EC4899', in: '#F97316', af: '#F59E0B', me: '#D946EF',
            jk: '#06B6D4', se: '#6366F1'
        };
        const areas = ['Norteamérica', 'Sudamérica', 'Europa', 'Rusia/Eurasia', 'China', 'Sur de Asia', 'África', 'MENA', 'APAC', 'ASEAN'];

        // Chart 1: Bubble
        const scatterData = [
            { x: 10, y: 505, r: 15, label: 'N. America' }, { x: 5, y: 440, r: 8, label: 'S. America' },
            { x: 9, y: 600, r: 12, label: 'Europa' }, { x: 5, y: 220, r: 10, label: 'Rusia' }, 
            { x: 9, y: 1410, r: 18, label: 'China' }, { x: 6, y: 1850, r: 16, label: 'Sur de Asia' },
            { x: 3, y: 1100, r: 10, label: 'África' }, { x: 7, y: 550, r: 8, label: 'MENA' },
            { x: 8, y: 175, r: 6, label: 'APAC' }, { x: 6, y: 680, r: 9, label: 'ASEAN' }
        ];
        
        if (typeof Chart !== 'undefined') {
            new Chart(document.getElementById('scatterChart'), {
                type: 'bubble',
                data: { datasets: areas.map((area, i) => ({ label: area, data: [scatterData[i]], backgroundColor: Object.values(colors)[i] + '80', borderColor: Object.values(colors)[i], borderWidth: 1 })) },
                options: { responsive: true, maintainAspectRatio: false, scales: { x: { title: { display: true, text: 'Poder Econ.', color: '#64748b' }, grid: { color: '#334155' }, ticks: { color: '#94a3b8' }, min: 0, max: 12 }, y: { title: { display: true, text: 'Población (M)', color: '#64748b' }, grid: { color: '#334155' }, ticks: { color: '#94a3b8' } } }, plugins: { legend: { display: false }, tooltip: { callbacks: { label: (ctx) => `${ctx.raw.label}: ${ctx.raw.y}M Hab. (Econ: ${ctx.raw.x})` } } } }
            });

            // Chart 2: Bar
            const milData = [10, 5, 7, 9, 9, 7, 4, 6, 7, 5];
            new Chart(document.getElementById('barChart'), {
                type: 'bar',
                data: { labels: areas, datasets: [{ label: 'Fuerza', data: milData, backgroundColor: Object.values(colors).map(c => c + '90'), borderColor: Object.values(colors), borderWidth: 1 }] },
                options: { responsive: true, maintainAspectRatio: false, indexAxis: 'y', scales: { x: { grid: { color: '#334155' }, ticks: { color: '#94a3b8' }, max: 10 }, y: { grid: { display: false }, ticks: { color: '#e2e8f0', font: { size: 10 } } } }, plugins: { legend: { display: false } } }
            });
        }
    }
});