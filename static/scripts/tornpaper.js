class TornPaper {
    constructor(options = {}) {
        this.filterName = options.filterName || "filter_tornpaper";
        this.seed = Number.isInteger(options.seed) ? options.seed : Math.floor(Math.random() * 1e7);
        this.tornFrequency = options.tornFrequency ?? 0.03;
        this.tornScale = options.tornScale ?? 7;

        this.createSvgFilter();
    }

    createSvgFilter() {
        if (document.getElementById(this.filterName)) return;

        let svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.style.position = "absolute";
        svg.style.width = "0";
        svg.style.height = "0";
        svg.innerHTML = `
            <filter id="${this.filterName}">
                <!-- Грязный эффект -->
                <feTurbulence type="fractalNoise" baseFrequency="${this.tornFrequency}" numOctaves="3" seed="${this.seed}" result="noise" />
                
                <!-- Размытие шума -->
                <feGaussianBlur stdDeviation="0.4" in="noise" result="soft_noise" />
                
                <!-- Эрозия краев -->
                <feMorphology operator="erode" radius="1.5" in="soft_noise" result="rough_edges" />
                
                <!-- Смещение краев -->
                <feDisplacementMap scale="${this.tornScale}" in="SourceGraphic" in2="rough_edges" />
                
                <!-- Смещение рваных частей -->
                <feOffset dx="1.5" dy="1.5" />
            </filter>
        `;

        document.body.appendChild(svg);
    }

    applyTo(element) {
        if (element) element.style.filter = `url(#${this.filterName})`;
    }
}
