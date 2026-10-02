import numpy as np
import imageio.v3 as iio
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import os

width, height = 800, 250
frames = []
n_frames = 60 # 60 frames for a 2-second loop at 30fps

# Try to load a monospace font, fallback to default
try:
    font = ImageFont.truetype("consola.ttf", 16)
    font_large = ImageFont.truetype("consola.ttf", 36)
except:
    font = ImageFont.load_default()
    font_large = ImageFont.load_default()

for i in range(n_frames):
    img = Image.new('RGB', (width, height), color=(5, 5, 12))
    draw = ImageDraw.Draw(img)
    
    # Progress 0 to 1
    t = i / n_frames
    angle_offset = t * 360
    
    # Draw Grid
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=(15, 15, 30), width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(15, 15, 30), width=1)
        
    # Draw Center Radar (MS-1 Style)
    cx, cy = 400, 125
    
    # Outer Ring
    draw.arc([cx-100, cy-100, cx+100, cy+100], start=angle_offset, end=angle_offset+270, fill=(0, 255, 255), width=3)
    # Inner Ring
    draw.arc([cx-80, cy-80, cx+80, cy+80], start=-angle_offset*1.5, end=-angle_offset*1.5+180, fill=(255, 0, 255), width=4)
    # Core Ring
    draw.arc([cx-50, cy-50, cx+50, cy+50], start=angle_offset*2, end=angle_offset*2+300, fill=(0, 255, 255), width=2)
    
    # Radar sweep line
    sweep_rad = math.radians(angle_offset)
    sx = cx + math.cos(sweep_rad) * 90
    sy = cy + math.sin(sweep_rad) * 90
    draw.line([(cx, cy), (sx, sy)], fill=(0, 255, 255), width=2)
    
    # Data Bars Left
    draw.text((40, 40), "SYS_PERFORMANCE", fill=(0, 255, 255), font=font)
    
    bar_width = 150 + math.sin(t * math.pi * 4) * 20
    draw.rectangle([40, 70, 240, 75], fill=(20, 20, 30))
    draw.rectangle([40, 70, 40 + bar_width, 75], fill=(0, 255, 255))
    
    bar_width2 = 120 + math.cos(t * math.pi * 2) * 40
    draw.rectangle([40, 100, 240, 105], fill=(20, 20, 30))
    draw.rectangle([40, 100, 40 + bar_width2, 105], fill=(255, 0, 255))
    
    # Text Right
    draw.text((600, 40), "NEXCORE PROTOCOL", fill=(255, 0, 255), font=font)
    draw.text((600, 70), f"TICK: {int(t*1000):04d}", fill=(255, 255, 255), font=font)
    draw.text((600, 100), "STATUS: ONLINE", fill=(0, 255, 255), font=font)
    
    # Sine wave
    wave_pts = []
    for wx in range(600, 780, 5):
        wy = 150 + math.sin((wx / 20) + (t * math.pi * 4)) * 15
        wave_pts.append((wx, wy))
    draw.line(wave_pts, fill=(0, 255, 255), width=2)

    # Core text
    draw.text((cx-35, cy-15), "MS-1", fill=(255, 255, 255), font=font_large)

    # Apply a slight glow
    glow = img.filter(ImageFilter.GaussianBlur(3))
    final = Image.blend(img, glow, 0.4)
    
    frames.append(np.array(final))

# Save as GIF
print("Saving GIF...")
iio.imwrite("ms1_animation.gif", frames, duration=1000/30, loop=0)
print("Saved ms1_animation.gif successfully!")
