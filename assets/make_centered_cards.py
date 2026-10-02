import os

def save_svg(filename, width, height, content, border_color="#ff00ff"):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <style>
      .bg {{ fill: #0d1117; stroke: {border_color}; stroke-width: 2; rx: 16px; }}
      .title {{ font-family: ui-monospace, Consolas, "Courier New", monospace; font-size: 20px; fill: #ffffff; font-weight: bold; text-anchor: middle; }}
      .subtitle {{ font-family: ui-monospace, Consolas, "Courier New", monospace; font-size: 14px; fill: {border_color}; letter-spacing: 2px; text-anchor: middle; }}
      .text {{ font-family: ui-monospace, Consolas, "Courier New", monospace; font-size: 13px; fill: #c9d1d9; text-anchor: middle; }}
      .highlight {{ fill: #00ffff; font-weight: bold; }}
    </style>
  </defs>
  <rect width="{width-4}" height="{height-4}" x="2" y="2" class="bg" />
  {content}
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)


# 1. About Card - Centered text, monospace
about_content = """
  <text class="title" x="230" y="50">Vektor010</text>
  <text class="subtitle" x="230" y="75">SOFTWARE ENGINEER</text>
  
  <text class="text" x="230" y="125">Building elegant,</text>
  <text class="text" x="230" y="150">high-performance systems.</text>
  <text class="text" x="230" y="175">Focus on <tspan class="highlight">architecture</tspan></text>
  <text class="text" x="230" y="200">and writing exceptionally fast,</text>
  <text class="text" x="230" y="225">resource-efficient code.</text>
"""
save_svg("assets/card_about.svg", 460, 260, about_content, "#ff00ff")

# 2. Focus Card - Centered text, monospace
focus_content = """
  <text class="title" x="135" y="50">DIRECTIVES</text>
  <text class="subtitle" x="135" y="75">CURRENT FOCUS</text>
  
  <text class="text" x="135" y="125">System Architecture</text>
  <text class="text" x="135" y="150" fill="#ff00ff">C++ &amp; Python</text>
  <text class="text" x="135" y="175">Zero-Latency Design</text>
  <text class="text" x="135" y="200" fill="#00ffff">Open Source</text>
"""
save_svg("assets/card_hardware.svg", 270, 260, focus_content, "#00ffff")

# 3. Detailed Skills Card - Centered columns, monospace
skills_content = """
  <text class="title" x="500" y="45">ENGINEERING PHILOSOPHY</text>
  <text class="subtitle" x="500" y="70">WHAT DRIVES MY CODE</text>
  
  <path d="M 500 100 L 500 230" stroke="#1a1a3a" stroke-width="2" />

  <g transform="translate(250, 110)">
    <text class="title" style="font-size:16px;" x="0" y="0">PERFORMANCE BY DESIGN</text>
    <text class="text" x="0" y="30">True performance comes from</text>
    <text class="text" x="0" y="50">deeply understanding architecture,</text>
    <text class="text" x="0" y="70">not from throwing hardware</text>
    <text class="text" x="0" y="90">at the problem.</text>
  </g>

  <g transform="translate(750, 110)">
    <text class="title" style="font-size:16px;" fill="#00ffff" x="0" y="0">SYSTEMS OPTIMIZATION</text>
    <text class="text" x="0" y="30">Specialized in stripping away bloat</text>
    <text class="text" x="0" y="50">and unnecessary abstractions.</text>
    <text class="text" x="0" y="70">Optimizing for the absolute</text>
    <text class="text" x="0" y="90">lowest possible latency.</text>
  </g>
"""
save_svg("assets/card_skills.svg", 1000, 260, skills_content, "#ff00ff")

print("Generated perfectly centered monospace cards!")
