import colorsys

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
    """Gera uma paleta de cores complementar com 6 cores."""
    offsets = [0.0, 0.5, 0.0, 0.5, 0.0]  # Alterna entre cor base e complementar
    return generate_palette(base_hex, offsets)

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