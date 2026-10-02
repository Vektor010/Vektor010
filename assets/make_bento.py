import os

def create_svg(filename, width, height, content, extra_defs=""):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
    <defs>
        <style>
            .bg {{ fill: #000000; }}
            .bento-bg {{ fill: #0a0a0f; stroke: #1f1f2e; stroke-width: 1.5; rx: 16px; }}
            .text-title {{ font-family: ui-monospace, Consolas, monospace; font-size: 28px; fill: #ffffff; font-weight: bold; letter-spacing: 2px; }}
            .text-subtitle {{ font-family: ui-monospace, Consolas, monospace; font-size: 14px; fill: #00ffff; letter-spacing: 4px; text-transform: uppercase; }}
            .text-body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 14px; fill: #8b949e; line-height: 1.5; }}
            .text-highlight {{ fill: #ffffff; font-weight: bold; }}
            .text-cyan {{ fill: #00ffff; font-weight: bold; }}
            .text-magenta {{ fill: #ff00ff; font-weight: bold; }}
            
            /* Animations */
            @keyframes float {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-5px); }} }}
            @keyframes pulse-border {{ 0%, 100% {{ stroke: #1f1f2e; }} 50% {{ stroke: #00ffff; }} }}
            @keyframes type {{ from {{ stroke-dashoffset: 1000; }} to {{ stroke-dashoffset: 0; }} }}
            
            .bento-glow:hover {{ animation: pulse-border 2s infinite; }}
            .anim-float {{ animation: float 4s ease-in-out infinite; }}
        </style>
        {extra_defs}
    </defs>
    <rect width="100%" height="100%" fill="transparent"/>
    {content}
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

# 1. HERO SVG (Massive Animated Typography & Cyber Logo)
hero_content = """
    <!-- Background element -->
    <rect class="bento-bg" x="10" y="10" width="880" height="230"/>
    
    <!-- Animated Grid -->
    <g opacity="0.1">
        <path d="M 0 50 L 900 50 M 0 100 L 900 100 M 0 150 L 900 150 M 0 200 L 900 200" stroke="#00ffff" stroke-width="1"/>
        <path d="M 100 0 L 100 250 M 200 0 L 200 250 M 300 0 L 300 250 M 400 0 L 400 250 M 500 0 L 500 250 M 600 0 L 600 250 M 700 0 L 700 250 M 800 0 L 800 250" stroke="#00ffff" stroke-width="1"/>
    </g>

    <!-- Logo / Abstract shape -->
    <g transform="translate(150, 125)" class="anim-float">
        <circle cx="0" cy="0" r="60" fill="none" stroke="#ff00ff" stroke-width="2" stroke-dasharray="10 5">
            <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="10s" repeatCount="indefinite"/>
        </circle>
        <circle cx="0" cy="0" r="75" fill="none" stroke="#00ffff" stroke-width="1" stroke-dasharray="2 10">
            <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="15s" repeatCount="indefinite"/>
        </circle>
        <path d="M -30 -30 L 30 -30 L 40 0 L 30 30 L -30 30 L -40 0 Z" fill="none" stroke="#ffffff" stroke-width="3"/>
        <text font-family="ui-monospace" font-size="20" font-weight="bold" fill="#00ffff" text-anchor="middle" y="6">V10</text>
    </g>

    <text class="text-subtitle" x="300" y="80">SYSTEM ARCHITECT // NEXCORE</text>
    <text class="text-title" font-size="52" x="296" y="135" fill="#ffffff" font-weight="900" letter-spacing="4">VEKTOR010</text>
    <text class="text-body" x="300" y="170">Engineering low-latency environments, OS-level optimizations,</text>
    <text class="text-body" x="300" y="195">and uncompromised hardware performance.</text>
    
    <path d="M 300 215 L 450 215" stroke="#ff00ff" stroke-width="2"/>
"""
create_svg("assets/bento_hero.svg", 900, 250, hero_content)

# 2. ABOUT BENTO (Left box)
about_content = """
    <rect class="bento-bg" x="10" y="10" width="430" height="280"/>
    <text class="text-subtitle" x="40" y="50">01. CAPABILITIES</text>
    
    <!-- Capability Bars -->
    <g transform="translate(40, 80)">
        <text class="text-body" x="0" y="0"><tspan class="text-highlight">Windows Kernel & OS Internals</tspan></text>
        <rect x="0" y="10" width="350" height="6" fill="#1f1f2e" rx="3"/>
        <rect x="0" y="10" width="330" height="6" fill="#00ffff" rx="3"/>
        
        <text class="text-body" x="0" y="45"><tspan class="text-highlight">Hardware Tuning (Ryzen/RTX)</tspan></text>
        <rect x="0" y="55" width="350" height="6" fill="#1f1f2e" rx="3"/>
        <rect x="0" y="55" width="300" height="6" fill="#ff00ff" rx="3"/>
        
        <text class="text-body" x="0" y="90"><tspan class="text-highlight">Low-Latency Netcode (Sub-Tick)</tspan></text>
        <rect x="0" y="100" width="350" height="6" fill="#1f1f2e" rx="3"/>
        <rect x="0" y="100" width="310" height="6" fill="#00ffff" rx="3"/>
        
        <text class="text-body" x="0" y="135"><tspan class="text-highlight">Audio Engineering (PEQ / DSP)</tspan></text>
        <rect x="0" y="145" width="350" height="6" fill="#1f1f2e" rx="3"/>
        <rect x="0" y="145" width="280" height="6" fill="#ff00ff" rx="3"/>
    </g>
"""
create_svg("assets/bento_about.svg", 450, 300, about_content)

# 3. STATS BENTO (Right box)
stats_content = """
    <rect class="bento-bg" x="10" y="10" width="430" height="280"/>
    <text class="text-subtitle" x="40" y="50">02. ARSENAL</text>
    
    <!-- Code block visualization -->
    <g transform="translate(40, 80)">
        <rect x="0" y="0" width="350" height="160" fill="#05050a" stroke="#1f1f2e" stroke-width="1" rx="6"/>
        <!-- Window controls -->
        <circle cx="15" cy="15" r="4" fill="#ff5f56"/>
        <circle cx="30" cy="15" r="4" fill="#ffbd2e"/>
        <circle cx="45" cy="15" r="4" fill="#27c93f"/>
        
        <text class="text-body" font-family="Consolas" x="15" y="45" font-size="12">
            <tspan fill="#ff00ff">const</tspan> stack = [
        </text>
        <text class="text-body" font-family="Consolas" x="30" y="65" font-size="12">
            <tspan fill="#00ffff">"C++"</tspan>, <tspan fill="#00ffff">"C"</tspan>, <tspan fill="#00ffff">"PowerShell"</tspan>,
        </text>
        <text class="text-body" font-family="Consolas" x="30" y="85" font-size="12">
            <tspan fill="#00ffff">"Python"</tspan>, <tspan fill="#00ffff">"Batch"</tspan>, <tspan fill="#00ffff">"CMake"</tspan>
        </text>
        <text class="text-body" font-family="Consolas" x="15" y="105" font-size="12">];</text>
        <text class="text-body" font-family="Consolas" x="15" y="130" font-size="12">
            <tspan fill="#ff00ff">while</tspan> (latency > <tspan fill="#ff00ff">0</tspan>) { optimize(); }
        </text>
    </g>
"""
create_svg("assets/bento_stats.svg", 450, 300, stats_content)

# 4. PROJECTS WIDE BENTO (Full width)
projects_content = """
    <rect class="bento-bg" x="10" y="10" width="880" height="200"/>
    <text class="text-subtitle" x="40" y="50">03. ACTIVE DIRECTIVES</text>
    
    <g transform="translate(40, 80)">
        <!-- Project 1 -->
        <rect x="0" y="0" width="400" height="90" fill="#0a0a0f" stroke="#1f1f2e" stroke-width="1" rx="8"/>
        <text class="text-title" font-size="18" x="20" y="30">windows-optimizer</text>
        <text class="text-body" font-size="12" x="20" y="55">Ultimate Gaming &amp; Low-Latency OS Suite</text>
        <text class="text-cyan" font-family="Consolas" font-size="10" x="20" y="75">C++ • PowerShell • Telemetry Control</text>
        
        <!-- Project 2 -->
        <rect x="420" y="0" width="400" height="90" fill="#0a0a0f" stroke="#1f1f2e" stroke-width="1" rx="8"/>
        <text class="text-title" font-size="18" x="440" y="30">cs2-autoexec</text>
        <text class="text-body" font-size="12" x="440" y="55">The Ultimate CS2 Pro Autoexec (2026)</text>
        <text class="text-magenta" font-family="Consolas" font-size="10" x="440" y="75">Source 2 • Sub-Tick Sync • Audio Math</text>
    </g>
"""
create_svg("assets/bento_projects.svg", 900, 220, projects_content)

print("Generated Bento SVGs successfully.")
