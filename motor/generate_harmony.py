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
    
# Function to convert RGB to HSL
def rgb_to_hsl(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    h, s, l = colorsys.rgb_to_hls(r, g, b)
    h = h * 360  # Convert hue to degrees
    s = s  # Saturation remains the same
    l = l  # Lightness remains the same
    return h, s, l

# Function to convert HSL back to RGB
def hsl_to_rgb(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h / 360, l, s)
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    return r, g, b
    
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
    """Gera uma paleta de cores complementar com base nos ajustes finos de saturação e brilho."""
    rgb_base = hex_to_rgb(base_hex)
    hsv_base = colorsys.rgb_to_hsv(*rgb_base)
    h_base, s_base, v_base = hsv_base
    
    # Ajuste dos offsets, saturação e brilho para gerar a paleta de 6 cores
    offsets = [0.0, 0.2, 0.5, 0.3, 0.55, 0.75]  # Ajustes finos de matiz para cada cor
    saturation_factors = [1.0, 1.0, 1.0, 0.75, 0.6, 0.4]  # Saturação ajustada para tons vibrantes e mais apagados
    value_factors = [1.0, 0.85, 1.0, 0.6, 0.45, 0.3]  # Ajuste de brilho (valor)

    hex_colors = []
    
    for i, offset in enumerate(offsets):
        h = (h_base + offset) % 1.0
        s = s_base * saturation_factors[i]
        v = v_base * value_factors[i]
        
        # Garantir que os valores de saturação e brilho fiquem dentro do intervalo [0, 1]
        s = min(1.0, max(0.0, s))
        v = min(1.0, max(0.0, v))
        
        rgb = colorsys.hsv_to_rgb(h, s, v)
        hex_colors.append(rgb_to_hex(rgb))
        
    return hex_colors


import colorsys

def analogous_colors(base_hex):
    """Generate an analogous color palette with hue shifts and adjustments in saturation and brightness."""
    rgb_base = hex_to_rgb(base_hex)
    hsv_base = colorsys.rgb_to_hsv(*rgb_base)
    h_base, s_base, v_base = hsv_base
    
    # Increase the number of shifts to 6 to match the example palette
    offsets = [0.0, -2/12.0, -1/12.0, 1/12.0, 2/12.0, 3/12.0]  # Adjust hue in small increments for analogous colors
    saturation_factors = [1.0, 0.85, 0.9, 0.75, 0.85, 1.0]  # Adjust saturation for vibrant and muted tones
    value_factors = [1.0, 0.85, 0.9, 0.75, 0.9, 1.0]  # Adjust brightness for a cohesive palette

    hex_colors = []
    
    for i, offset in enumerate(offsets):
        h = (h_base + offset) % 1.0  # Apply the hue offset
        s = s_base * saturation_factors[i]
        v = v_base * value_factors[i]
        
        # Ensure the saturation and brightness values are within bounds [0, 1]
        s = min(1.0, max(0.0, s))
        v = min(1.0, max(0.0, v))
        
        rgb = colorsys.hsv_to_rgb(h, s, v)
        hex_colors.append(rgb_to_hex(rgb))
        
    return hex_colors


def triadic_colors(base_hex):
    """Gera uma paleta de cores tríades com 6 cores."""
    offsets = [0.0, 1/3.0, 2/3.0, 0.0, 1/3.0]
    return generate_palette(base_hex, offsets)

def split_complementary_colors(base_hex):
    """Gera uma paleta de cores complementares divididas com 6 cores."""
    offsets = [0.0, -5/12.0, 5/12.0, 0.5, -1/12.0]
    return generate_palette(base_hex, offsets)

def square_colors(base_hex):
    """Gera uma paleta de cores específicas a partir da cor base usando offset, saturação e brilho."""
    # Convertemos a cor base para RGB
    rgb_base = hex_to_rgb(base_hex)
    
    # Convertemos a cor base para HSV
    hsv_base = colorsys.rgb_to_hsv(*rgb_base)
    h_base, s_base, v_base = hsv_base
    
    # Offsets de matiz e ajustes de saturação e brilho para as cores desejadas
    offsets = [0.0, 0.25, 0.5, 0.75, 0.6, 0.15]  # Valores ajustados para cada cor
    saturation_factors = [1.0, 1.0, 1.0, 1.0, 0.8, 8.0]  # Saturação ajustada conforme a imagem
    value_factors = [1.0, 1.0, 1.0, 1.0, 0.8, 0.7]  # Brilho ajustado conforme a imagem
    
    hex_colors = []
    
    for i, offset in enumerate(offsets):
        h = (h_base + offset) % 1.0  # Ajuste de matiz
        s = s_base * saturation_factors[i]  # Ajuste de saturação
        v = v_base * value_factors[i]  # Ajuste de brilho
        
        # Garantir que os valores de saturação e brilho fiquem dentro do intervalo [0, 1]
        s = min(1.0, max(0.0, s))
        v = min(1.0, max(0.0, v))
        
        # Convertendo de volta para RGB e depois para Hex
        rgb = colorsys.hsv_to_rgb(h, s, v)
        hex_colors.append(rgb_to_hex(rgb))
    
    return hex_colors


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