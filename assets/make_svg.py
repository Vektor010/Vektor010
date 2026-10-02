new_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="800" height="350" viewBox="0 0 800 350">
    <defs>
        <style>
            .bg { fill: #050510; }
            .grid { stroke: #1a1a3a; stroke-width: 1; stroke-dasharray: 20 20; }
            .grid-small { stroke: #0f0f2a; stroke-width: 0.5; }
            
            .text-main { font-family: ui-monospace, Consolas, monospace; font-size: 12px; fill: #e0e0ff; }
            .text-muted { font-family: ui-monospace, Consolas, monospace; font-size: 10px; fill: #6a6a9a; }
            .text-cyan { font-family: ui-monospace, Consolas, monospace; font-size: 12px; fill: #00ffff; font-weight: bold; text-shadow: 0 0 5px #00ffff; }
            .text-magenta { font-family: ui-monospace, Consolas, monospace; font-size: 12px; fill: #ff00ff; font-weight: bold; text-shadow: 0 0 5px #ff00ff; }
            .text-yellow { font-family: ui-monospace, Consolas, monospace; font-size: 12px; fill: #ffff00; font-weight: bold; text-shadow: 0 0 5px #ffff00; }
            
            .edge { stroke: #1f1f4f; stroke-width: 1.5; fill: none; }
            .edge-glow-cyan { stroke: #00ffff; stroke-width: 2; fill: none; opacity: 0.6; filter: drop-shadow(0 0 4px #00ffff); }
            .edge-glow-magenta { stroke: #ff00ff; stroke-width: 2; fill: none; opacity: 0.6; filter: drop-shadow(0 0 4px #ff00ff); }
            
            .node { fill: #0a0a20; stroke: #1f1f4f; stroke-width: 2; }
            
            .bar-bg { fill: #1a1a3a; }
            .bar-fill-cyan { fill: #00ffff; filter: drop-shadow(0 0 3px #00ffff); }
            .bar-fill-magenta { fill: #ff00ff; filter: drop-shadow(0 0 3px #ff00ff); }
            
            @keyframes scanline {
                0% { transform: translateY(-100%); }
                100% { transform: translateY(800%); }
            }
            .scan { opacity: 0.1; fill: #00ffff; animation: scanline 4s linear infinite; }
            
            @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }
            .anim-blink { animation: blink 2s infinite ease-in-out; }
            .anim-blink-fast { animation: blink 0.5s infinite step-end; }
        </style>
        
        <linearGradient id="cyber-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#00ffff" stop-opacity="0.2"/>
            <stop offset="50%" stop-color="#050510" stop-opacity="0"/>
            <stop offset="100%" stop-color="#ff00ff" stop-opacity="0.2"/>
        </linearGradient>
    </defs>

    <!-- Background -->
    <rect class="bg" width="100%" height="100%" rx="10"/>
    <rect fill="url(#cyber-grad)" width="100%" height="100%" rx="10"/>
    
    <!-- Grid System -->
    <g class="grid-small">
        <pattern id="smallGrid" width="10" height="10" patternUnits="userSpaceOnUse">
            <path d="M 10 0 L 0 0 0 10" fill="none"/>
        </pattern>
        <rect width="100%" height="100%" fill="url(#smallGrid)"/>
    </g>

    <!-- Scanline effect -->
    <rect width="100%" height="20" class="scan"/>

    <!-- LEFT: System Stats HUD -->
    <g transform="translate(20, 20)">
        <text class="text-cyan" x="0" y="10">[ SYSTEM_CORE_MONITOR ]</text>
        <line x1="0" y1="18" x2="180" y2="18" stroke="#00ffff" stroke-width="2" opacity="0.8"/>
        
        <!-- CPU -->
        <text class="text-muted" x="0" y="40">CPU_TICK [RYZEN]</text>
        <rect class="bar-bg" x="0" y="45" width="180" height="6"/>
        <rect class="bar-fill-cyan" x="0" y="45" width="150" height="6">
            <animate attributeName="width" values="140;160;130;150" dur="2s" repeatCount="indefinite"/>
        </rect>
        <text class="text-main" x="145" y="40">4.8 GHz</text>
        
        <!-- GPU -->
        <text class="text-muted" x="0" y="75">GPU_ALLOC [RTX]</text>
        <rect class="bar-bg" x="0" y="80" width="180" height="6"/>
        <rect class="bar-fill-magenta" x="0" y="80" width="120" height="6">
            <animate attributeName="width" values="100;130;110;120" dur="3s" repeatCount="indefinite"/>
        </rect>
        <text class="text-main" x="145" y="75">VRAM OPT</text>
        
        <!-- NET -->
        <text class="text-muted" x="0" y="110">NET_SUB_TICK_LTCY</text>
        <rect class="bar-bg" x="0" y="115" width="180" height="6"/>
        <rect class="bar-fill-cyan" x="0" y="115" width="40" height="6">
            <animate attributeName="width" values="30;50;20;40" dur="1.5s" repeatCount="indefinite"/>
        </rect>
        <text class="text-main" x="155" y="110">1ms</text>
        
        <!-- Audio -->
        <text class="text-muted" x="0" y="145">PEQ_AUDIO_STREAM</text>
        <path d="M 0 160 Q 20 140, 40 160 T 80 160 T 120 160 T 160 160" fill="none" stroke="#ff00ff" stroke-width="2">
            <animate attributeName="d" values="M 0 160 Q 20 140, 40 160 T 80 160 T 120 160 T 160 160; M 0 160 Q 20 180, 40 160 T 80 160 T 120 160 T 160 160; M 0 160 Q 20 140, 40 160 T 80 160 T 120 160 T 160 160" dur="2s" repeatCount="indefinite"/>
        </path>
    </g>

    <!-- CENTER: Rotating Cyber Core & Network -->
    <g transform="translate(400, 160)">
        <!-- Outer Rotating Rings -->
        <g stroke="#00ffff" stroke-width="1" fill="none" opacity="0.4">
            <circle cx="0" cy="0" r="100" stroke-dasharray="10 20">
                <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="20s" repeatCount="indefinite"/>
            </circle>
            <circle cx="0" cy="0" r="85" stroke-dasharray="40 10" stroke="#ff00ff">
                <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="15s" repeatCount="indefinite"/>
            </circle>
        </g>
        
        <!-- Inner Core Node -->
        <circle cx="0" cy="0" r="30" class="node anim-blink"/>
        <circle cx="0" cy="0" r="15" fill="#00ffff" class="anim-blink" filter="drop-shadow(0 0 10px #00ffff)"/>
        <text class="text-cyan" x="0" y="5" text-anchor="middle" font-size="10">NEXCORE</text>

        <!-- Connected Nodes -->
        <g stroke="#ff00ff" stroke-width="1.5" opacity="0.7">
            <line x1="0" y1="-30" x2="0" y2="-80"/>
            <line x1="26" y1="15" x2="70" y2="40"/>
            <line x1="-26" y1="15" x2="-70" y2="40"/>
        </g>
        
        <circle cx="0" cy="-80" r="10" fill="#0a0a20" stroke="#00ffff" stroke-width="2"/>
        <circle cx="0" cy="-80" r="4" fill="#00ffff" class="anim-blink"/>
        <text class="text-muted" x="0" y="-95" text-anchor="middle">WINDOWS</text>

        <circle cx="70" cy="40" r="10" fill="#0a0a20" stroke="#ff00ff" stroke-width="2"/>
        <circle cx="70" cy="40" r="4" fill="#ff00ff" class="anim-blink"/>
        <text class="text-muted" x="90" y="55">CS2_NET</text>

        <circle cx="-70" cy="40" r="10" fill="#0a0a20" stroke="#00ffff" stroke-width="2"/>
        <circle cx="-70" cy="40" r="4" fill="#00ffff" class="anim-blink"/>
        <text class="text-muted" x="-90" y="55" text-anchor="end">AUDIO</text>
        
        <!-- Packets running -->
        <circle r="3" fill="#ffffff" filter="drop-shadow(0 0 5px #ffffff)">
            <animateMotion dur="2s" repeatCount="indefinite" path="M 0 -80 L 0 -30"/>
        </circle>
        <circle r="3" fill="#ffffff" filter="drop-shadow(0 0 5px #ffffff)">
            <animateMotion dur="1.5s" repeatCount="indefinite" path="M 70 40 L 26 15"/>
        </circle>
        <circle r="3" fill="#ffffff" filter="drop-shadow(0 0 5px #ffffff)">
            <animateMotion dur="2.5s" repeatCount="indefinite" path="M -70 40 L -26 15"/>
        </circle>
    </g>

    <!-- RIGHT: Console Log -->
    <g transform="translate(600, 20)">
        <text class="text-magenta" x="0" y="10">[ TERMINAL_I/O ]</text>
        <line x1="0" y1="18" x2="160" y2="18" stroke="#ff00ff" stroke-width="2" opacity="0.8"/>
        
        <g opacity="0.8">
            <text class="text-muted" x="0" y="40">root@vektor:~#</text>
            <text class="text-main" x="0" y="55">./optimize.sh</text>
            <text class="text-muted" x="0" y="70">[+] Injecting hooks...</text>
            <text class="text-cyan" x="0" y="85">SUCCESS: 0x7FFE</text>
            <text class="text-muted" x="0" y="100">[+] Overriding timer</text>
            <text class="text-cyan" x="0" y="115">HPET Disabled</text>
            <text class="text-muted" x="0" y="130">[+] CS2 Netcode</text>
            <text class="text-magenta" x="0" y="145">SubTick Aligned</text>
            <text class="text-muted" x="0" y="160">root@vektor:~#</text>
            <!-- Blinking cursor -->
            <rect x="95" y="150" width="8" height="12" fill="#00ffff" class="anim-blink-fast"/>
        </g>
        
        <!-- Decoration Borders -->
        <path d="M 160 200 L 160 300 L 140 300" fill="none" stroke="#00ffff" stroke-width="2" opacity="0.6"/>
    </g>
    
    <!-- Top Left Decoration -->
    <path d="M 20 300 L 20 320 L 40 320" fill="none" stroke="#ff00ff" stroke-width="2" opacity="0.6"/>
</svg>"""

with open("monitoring.svg", "w", encoding="utf-8") as f:
    f.write(new_svg)
