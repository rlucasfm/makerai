import colorsys
from PIL import Image, ImageDraw
from io import BytesIO

def hex_to_rgb(hex_color):
    """Converte uma cor hexadecimal para RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16)/255.0 for i in (0, 2 ,4))

def rgb_to_hex(rgb_color):
    """Converte uma cor RGB para hexadecimal."""
    return '#{:02x}{:02x}{:02x}'.format(
        int(rgb_color[0]*255),
        int(rgb_color[1]*255),
        int(rgb_color[2]*255)
    )
    
def adjust_hue(hue, offset):
    """Ajusta o matiz (hue) garantindo que permaneça no intervalo 0-360."""
    return (hue + offset) % 360

def generate_palette(base_hex, offsets):
    """Gera uma paleta de cores com base nos offsets fornecidos."""
    rgb_base = hex_to_rgb(base_hex)
    hsv_base = colorsys.rgb_to_hsv(*rgb_base)
    h_base, s_base, v_base = hsv_base
    hex_colors = [base_hex]  # Inclui a cor base
    for offset in offsets:
        h = (h_base + offset) % 1.0
        rgb = colorsys.hsv_to_rgb(h, s_base, v_base)
        hex_colors.append(rgb_to_hex(rgb))
    return hex_colors

def complementary_colors(base_hex):
    """Gera uma paleta de cores complementar com a mesma relação mostrada na imagem."""
    rgb_base = hex_to_rgb(base_hex)
    hsv_base = colorsys.rgb_to_hsv(*rgb_base)
    h_base, s_base, v_base = hsv_base
    
    # Definindo as proporções da imagem
    offsets = [0.0, 0.5, -0.1, 0.5, 0.4]  # Ajustando conforme os tons da paleta da imagem
    hex_colors = []
    
    for offset in offsets:
        h = (h_base + offset) % 1.0
        rgb = colorsys.hsv_to_rgb(h, s_base, v_base)
        hex_colors.append(rgb_to_hex(rgb))
        
    return hex_colors

def analogous_colors(base_hex):
    """Gera uma paleta de cores análogas com 6 cores."""
    offsets = [0.0, -1/12.0, 1/12.0, -1/6.0, 1/6.0]
    return generate_palette(base_hex, offsets)

def triadic_colors(base_hex):
    """Gera uma paleta de cores tríades com 6 cores."""
    offsets = [0.0, 1/3.0, 2/3.0, 0.0, 1/3.0]
    return generate_palette(base_hex, offsets)

def split_complementary_colors(base_hex):
    """Gera uma paleta de cores complementares divididas com 6 cores."""
    offsets = [0.0, -5/12.0, 5/12.0, 0.5, -1/12.0]
    return generate_palette(base_hex, offsets)

def square_colors(base_hex):
    """Gera uma paleta de cores em harmonia quadrada com 6 cores."""
    offsets = [0.0, 0.25, 0.5, 0.75, 0.0]
    return generate_palette(base_hex, offsets)

def compound_colors(base_hex):
    """Gera uma paleta de cores composta com 6 cores."""
    offsets = [0.0, 1/12.0, 0.5, -1/12.0, 5/12.0]
    return generate_palette(base_hex, offsets)

def shades(base_hex):
    """Gera uma paleta de sombras com 6 cores."""
    rgb_base = hex_to_rgb(base_hex)
    hsv_base = colorsys.rgb_to_hsv(*rgb_base)
    h, s, v = hsv_base
    hex_colors = []
    for i in range(6):
        v_i = v * (1 - i / 5.0)
        rgb_i = colorsys.hsv_to_rgb(h, s, v_i)
        hex_colors.append(rgb_to_hex(rgb_i))
    return hex_colors

def monochromatic_colors(base_hex):
    """Gera uma paleta de cores monocromáticas com 6 cores."""
    rgb_base = hex_to_rgb(base_hex)
    hsv_base = colorsys.rgb_to_hsv(*rgb_base)
    h, s, v = hsv_base
    hex_colors = []
    for i in range(1, 7):
        s_i = s * i / 6.0
        v_i = v * (1 + (i - 3) / 6.0)
        rgb_i = colorsys.hsv_to_rgb(h, s_i, min(1.0, max(0.0, v_i)))
        hex_colors.append(rgb_to_hex(rgb_i))
    return hex_colors

def generate_harmony_image(colors, image_size=(200, 200), circle_size=40):
    """
    Generates an image with overlapping circles for the given colors.

    Args:
    - colors (list of str): List of hex color codes.
    - image_size (tuple): Size of the image (width, height).
    - circle_size (int): Diameter of each circle.

    Returns:
    - BytesIO: Image in memory as a byte stream.
    """
    # Create a transparent image
    img = Image.new("RGBA", image_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Calculate positions for overlapping circles
    num_colors = len(colors)
    step = circle_size // 2  # Overlap by half the diameter
    x_start = (image_size[0] - (num_colors * step + circle_size - step)) // 2
    y_center = image_size[1] // 2

    # Draw each circle
    for i, color in enumerate(colors):
        x = x_start + i * step
        y = y_center - circle_size // 2
        draw.ellipse([x, y, x + circle_size, y + circle_size], fill=color)

    # Save the image to a byte stream
    byte_stream = BytesIO()
    img.save(byte_stream, format="PNG")
    byte_stream.seek(0)
    return byte_stream