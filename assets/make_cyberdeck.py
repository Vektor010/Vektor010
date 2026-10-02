new_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="800" height="350" viewBox="0 0 800 350">
    <defs>
        <style>
            .bg { fill: #050510; }
            .grid { stroke: #0f0f2a; stroke-width: 1; }
            .hex { fill: none; stroke: #1a1a3a; stroke-width: 1.5; }
            .hex-active { fill: rgba(0, 255, 255, 0.1); stroke: #00ffff; stroke-width: 2; filter: drop-shadow(0 0 5px #00ffff); }
            .hex-magenta { fill: rgba(255, 0, 255, 0.1); stroke: #ff00ff; stroke-width: 2; filter: drop-shadow(0 0 5px #ff00ff); }
            
            .text-title { font-family: ui-monospace, Consolas, monospace; font-size: 24px; fill: #ffffff; font-weight: bold; letter-spacing: 4px; text-shadow: 0 0 10px #00ffff; }
            .text-sub { font-family: ui-monospace, Consolas, monospace; font-size: 10px; fill: #00ffff; letter-spacing: 2px; }
            .text-data { font-family: ui-monospace, Consolas, monospace; font-size: 10px; fill: #ff00ff; }
            .text-code { font-family: ui-monospace, Consolas, monospace; font-size: 10px; fill: #6a6a9a; }
            
            @keyframes rotate-slow { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
            @keyframes rotate-fast-rev { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }
            @keyframes pulse-glow { 0%, 100% { opacity: 0.5; filter: drop-shadow(0 0 2px #00ffff); } 50% { opacity: 1; filter: drop-shadow(0 0 12px #00ffff); } }
            @keyframes glitch { 
                0% { transform: translate(0, 0); } 
                20% { transform: translate(-2px, 1px); } 
                40% { transform: translate(2px, -1px); } 
                60% { transform: translate(-1px, 2px); } 
                80% { transform: translate(1px, -2px); } 
                100% { transform: translate(0, 0); } 
            }
            @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
            
            .anim-ring-1 { animation: rotate-slow 20s linear infinite; transform-origin: center; }
            .anim-ring-2 { animation: rotate-fast-rev 12s linear infinite; transform-origin: center; }
            .anim-pulse { animation: pulse-glow 3s infinite ease-in-out; }
            .anim-glitch { animation: glitch 0.2s infinite; }
            .anim-float { animation: float 4s infinite ease-in-out; }
            
            /* Glitch filter */
            .glitch-effect { filter: url(#glitch-filter); }
        </style>
        
        <filter id="glitch-filter" x="-20%" y="-20%" width="140%" height="140%">
            <feTurbulence type="fractalNoise" baseFrequency="0.05 0.9" numOctaves="1" result="noise" />
            <feColorMatrix type="matrix" values="1 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 3 -1" in="noise" result="coloredNoise" />
            <feDisplacementMap in="SourceGraphic" in2="coloredNoise" scale="5" xChannelSelector="R" yChannelSelector="G" result="displaced" />
            
            <!-- We only want the glitch to trigger occasionally, but SVG SMIL doesn't easily keyframe filter parameters, so we'll use CSS for motion -->
        </filter>
        
        <!-- Hexagon Path -->
        <g id="hex-shape">
            <polygon points="30,0 90,0 120,52 90,104 30,104 0,52" />
        </g>
    </defs>

    <rect class="bg" width="100%" height="100%" rx="10"/>

    <!-- Decorative Corner Lines -->
    <path d="M 20 20 L 50 20 L 70 40" fill="none" stroke="#ff00ff" stroke-width="2" opacity="0.6"/>
    <path d="M 780 20 L 750 20 L 730 40" fill="none" stroke="#00ffff" stroke-width="2" opacity="0.6"/>
    <path d="M 20 330 L 50 330 L 70 310" fill="none" stroke="#00ffff" stroke-width="2" opacity="0.6"/>
    <path d="M 780 330 L 750 330 L 730 310" fill="none" stroke="#ff00ff" stroke-width="2" opacity="0.6"/>

    <!-- Cyber-Deck Hexagonal Grid (Isometric-ish) -->
    <g transform="translate(400, 175) scale(1, 0.6) rotate(45)" opacity="0.4">
        <!-- Generative Hex Grid -->
        <use href="#hex-shape" x="0" y="0" class="hex" />
        <use href="#hex-shape" x="120" y="0" class="hex" />
        <use href="#hex-shape" x="-120" y="0" class="hex" />
        <use href="#hex-shape" x="60" y="104" class="hex" />
        <use href="#hex-shape" x="-60" y="104" class="hex" />
        <use href="#hex-shape" x="60" y="-104" class="hex" />
        <use href="#hex-shape" x="-60" y="-104" class="hex" />
        <use href="#hex-shape" x="180" y="104" class="hex" />
        <use href="#hex-shape" x="-180" y="104" class="hex" />
        <use href="#hex-shape" x="180" y="-104" class="hex" />
        <use href="#hex-shape" x="-180" y="-104" class="hex" />
        
        <!-- Active Hexes -->
        <use href="#hex-shape" x="0" y="0" class="hex-active anim-pulse" />
        <use href="#hex-shape" x="-120" y="0" class="hex-magenta" />
        <use href="#hex-shape" x="60" y="104" class="hex-active" />
    </g>

    <!-- Floating Core Rings -->
    <g transform="translate(400, 160)" class="anim-float">
        <g class="anim-ring-1">
            <circle cx="0" cy="0" r="80" stroke="#00ffff" stroke-width="2" stroke-dasharray="20 10 5 10" fill="none" opacity="0.8" filter="drop-shadow(0 0 5px #00ffff)"/>
            <circle cx="0" cy="0" r="90" stroke="#ff00ff" stroke-width="1" stroke-dasharray="5 30" fill="none" opacity="0.5"/>
        </g>
        <g class="anim-ring-2">
            <circle cx="0" cy="0" r="60" stroke="#ff00ff" stroke-width="3" stroke-dasharray="30 20 10 20" fill="none" opacity="0.8" filter="drop-shadow(0 0 5px #ff00ff)"/>
            <circle cx="0" cy="0" r="50" stroke="#00ffff" stroke-width="1" stroke-dasharray="2 10" fill="none" opacity="0.6"/>
        </g>
        
        <!-- Center Core -->
        <polygon points="0,-20 17,-10 17,10 0,20 -17,10 -17,-10" fill="#00ffff" class="anim-pulse"/>
        <circle cx="0" cy="0" r="5" fill="#ffffff" filter="drop-shadow(0 0 10px #ffffff)"/>
    </g>

    <!-- UI Overlay Left -->
    <g transform="translate(40, 80)">
        <text class="text-sub" x="0" y="0">OS :: NT_KERNEL_v11.0</text>
        <line x1="0" y1="8" x2="150" y2="8" stroke="#00ffff" stroke-width="1"/>
        
        <text class="text-data" x="0" y="30">MEM_PAGES  : [ALLOCATED]</text>
        <text class="text-data" x="0" y="50">TICK_RATE  : [SUB_TICK_SYNC]</text>
        <text class="text-data" x="0" y="70">HPET_STATE : [BYPASSED]</text>
        <text class="text-data" x="0" y="90">L3_CACHE   : [RYZEN_OPT]</text>
        
        <path d="M 0 110 L 10 100 L 140 100 L 150 110" fill="none" stroke="#ff00ff" stroke-width="1"/>
    </g>

    <!-- UI Overlay Right -->
    <g transform="translate(600, 80)">
        <text class="text-sub" x="0" y="0">SYS :: NEXCORE_PROTOCOL</text>
        <line x1="0" y1="8" x2="160" y2="8" stroke="#ff00ff" stroke-width="1"/>
        
        <g class="text-code">
            <text x="0" y="30">> initialize_peq_audio()</text>
            <text x="0" y="45">> target: FiiO_JT1</text>
            <text x="0" y="60">> status: ENGAGED</text>
            <text x="0" y="85">> hook_cs2_engine()</text>
            <text x="0" y="100">> status: <tspan fill="#00ffff" class="anim-blink">AWAITING</tspan></text>
        </g>
    </g>

    <!-- Bottom Data Stream -->
    <g transform="translate(0, 310)">
        <rect x="0" y="0" width="800" height="40" fill="#050510"/>
        <line x1="0" y1="0" x2="800" y2="0" stroke="#1a1a3a" stroke-width="1"/>
        <text class="text-code" x="20" y="20">DATA_STREAM :: 0x0A9F ... 0xFF12 ... 0x11BC ... 0x99FF ... 0x00A1</text>
        <rect x="20" y="25" width="760" height="2" fill="#1a1a3a"/>
        <rect x="20" y="25" width="200" height="2" fill="#00ffff">
            <animate attributeName="width" values="0;760" dur="2s" repeatCount="indefinite"/>
            <animate attributeName="x" values="20;780" dur="2s" repeatCount="indefinite"/>
        </rect>
    </g>
</svg>"""

with open("cyber_deck.svg", "w", encoding="utf-8") as f:
    f.write(new_svg)
