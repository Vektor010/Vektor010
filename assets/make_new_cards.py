import os

def save_svg(filename, width, height, content, border_color="#ff00ff"):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <style>
      .bg {{ fill: #0d1117; stroke: {border_color}; stroke-width: 2; rx: 16px; }}
      .title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 24px; fill: #ffffff; font-weight: 800; }}
      .subtitle {{ font-family: ui-monospace, Consolas, monospace; font-size: 14px; fill: #00ffff; letter-spacing: 2px; }}
      .subtitle-mag {{ font-family: ui-monospace, Consolas, monospace; font-size: 14px; fill: #ff00ff; letter-spacing: 2px; }}
      .text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; font-size: 15px; fill: #c9d1d9; line-height: 1.6; }}
      .highlight {{ fill: #00ffff; font-weight: bold; }}
      .term {{ font-family: ui-monospace, Consolas, monospace; font-size: 13px; fill: #c9d1d9; }}
      .term-cmd {{ fill: #ff00ff; font-weight: bold; }}
      .term-path {{ fill: #00ffff; }}
    </style>
  </defs>
  <rect width="{width-4}" height="{height-4}" x="2" y="2" class="bg" />
  {content}
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)


# 1. About Card (Professional, clean)
about_content = """
  <text class="title" x="30" y="50">Vektor010</text>
  <text class="subtitle" x="30" y="80">SOFTWARE ENGINEER &amp; OPTIMIZER</text>
  
  <text class="text" x="30" y="120">Dedicated to building elegant,</text>
  <text class="text" x="30" y="145">high-performance systems. I focus</text>
  <text class="text" x="30" y="170">on <tspan class="highlight">low-level architecture</tspan> and</text>
  <text class="text" x="30" y="195">writing exceptionally fast,</text>
  <text class="text" x="30" y="220">resource-efficient code.</text>
  
  <path d="M 400 30 L 430 30 M 400 45 L 430 45 M 400 60 L 430 60" stroke="#ff00ff" stroke-width="3" />
"""
save_svg("assets/card_about.svg", 460, 260, about_content, "#ff00ff")

# 2. Focus Card (Replaces the "Specs" card)
focus_content = """
  <text class="subtitle-mag" x="25" y="40">CURRENT DIRECTIVES</text>
  
  <rect x="25" y="60" width="220" height="40" fill="#151525" rx="5" />
  <text class="text" x="35" y="85" font-weight="bold" fill="#ffffff">Focus:</text>
  <text class="text" x="90" y="85" fill="#00ffff">System Architecture</text>
  
  <rect x="25" y="115" width="220" height="40" fill="#151525" rx="5" />
  <text class="text" x="35" y="140" font-weight="bold" fill="#ffffff">Code:</text>
  <text class="text" x="80" y="140" fill="#ff00ff">C++ &amp; Python</text>

  <rect x="25" y="170" width="220" height="40" fill="#151525" rx="5" />
  <text class="text" x="35" y="195" font-weight="bold" fill="#ffffff">Goal:</text>
  <text class="text" x="80" y="195" fill="#00ffff">Zero-Latency Design</text>

  <circle cx="135" cy="235" r="4" fill="#00ffff" />
  <circle cx="165" cy="235" r="4" fill="#ff00ff" />
  <circle cx="195" cy="235" r="4" fill="#00ffff" />
"""
save_svg("assets/card_hardware.svg", 270, 260, focus_content, "#ff00ff")

# 3. Detailed Skills Card (Replaces the long technical rant with clean professional skills)
skills_content = """
  <text class="title" x="40" y="50">ENGINEERING PHILOSOPHY</text>
  <text class="subtitle" x="40" y="80">WHAT DRIVES MY CODE</text>
  
  <path d="M 450 30 L 450 220" stroke="#1a1a3a" stroke-width="2" />

  <g transform="translate(40, 110)">
    <text class="text" x="0" y="0"><tspan class="highlight">PERFORMANCE BY DESIGN</tspan></text>
    <text class="text" x="0" y="25">I believe that true performance doesn't come from throwing</text>
    <text class="text" x="0" y="50">more hardware at a problem. It comes from deeply understanding</text>
    <text class="text" x="0" y="75">the underlying architecture and writing code that respects it.</text>
    
    <text class="text" x="0" y="115"><tspan class="highlight">OPEN SOURCE ADVOCATE</tspan></text>
    <text class="text" x="0" y="140">Committed to building tools that empower other developers.</text>
    <text class="text" x="0" y="165">Transparency, clean documentation, and robust architecture.</text>
  </g>

  <g transform="translate(490, 110)">
    <text class="text" x="0" y="0"><tspan class="cyan-text">SYSTEMS OPTIMIZATION</tspan></text>
    <text class="text" x="0" y="25">Specialized in stripping away bloat and unnecessary</text>
    <text class="text" x="0" y="50">abstractions. Whether it's network routing or OS-level</text>
    <text class="text" x="0" y="75">processes, I optimize for the lowest possible latency.</text>

    <text class="text" x="0" y="115"><tspan class="cyan-text">CONTINUOUS EVOLUTION</tspan></text>
    <text class="text" x="0" y="140">Constantly experimenting with new frameworks, languages,</text>
    <text class="text" x="0" y="165">and paradigms to stay at the cutting edge of tech.</text>
  </g>
"""
save_svg("assets/card_skills.svg", 1000, 260, skills_content, "#00ffff")

print("Generated new professional cards!")
