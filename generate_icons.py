import os
import sys

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Pillow not installed. Attempting to install...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageDraw

def create_icon(size, filename):
    # Create an image with a dark theme background
    image = Image.new("RGBA", (size, size), (2, 6, 23, 255)) # slate-950
    draw = ImageDraw.Draw(image)
    
    # Draw a stylish abstract icon: a hexagonal grid or file emblem in indigo
    # Let's draw an outer glowing hexagon/polygon
    padding = size // 6
    center = size // 2
    r = (size - 2 * padding) // 2
    
    # Hexagon points
    import math
    points = []
    for i in range(6):
        angle = math.radians(i * 60 - 30)
        x = center + r * math.cos(angle)
        y = center + r * math.sin(angle)
        points.append((x, y))
        
    # Draw main outline
    draw.polygon(points, outline=(99, 102, 241, 255), width=max(2, size // 24)) # indigo-500
    
    # Draw an inner geometric shape representing files / layers
    inner_r = r // 2
    inner_points = []
    for i in range(3):
        angle = math.radians(i * 120 + 90)
        x = center + inner_r * math.cos(angle)
        y = center + inner_r * math.sin(angle)
        inner_points.append((x, y))
    
    # Draw inner triangle/arrows
    draw.polygon(inner_points, fill=(168, 85, 247, 180), outline=(236, 72, 153, 255), width=max(1, size // 48)) # purple/pink
    
    # Save the file
    image.save(filename, "PNG")
    print(f"Created {filename} of size {size}x{size}")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    create_icon(192, "icon-192.png")
    create_icon(512, "icon-512.png")
