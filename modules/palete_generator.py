import streamlit as st
from motor.generate_harmony import (
    complementary_colors,
    analogous_colors,
    split_complementary_colors,
    square_colors,
    compound_colors,
    shades,
    monochromatic_colors,
    generate_harmony_image
)
from PIL import Image, ImageDraw, ImageFont
import io

st.title("Gerador de Paleta - Harmonia de Cores")

# Color selection
color = st.color_picker("Escolha uma cor:")

# Input for uploading an image
uploaded_image = st.file_uploader("Logo da empresa:", type=["png", "jpg", "jpeg"])

# Display the uploaded image
if uploaded_image is not None:
    st.image(uploaded_image, caption="Logo", width=100)

# Function to create the image with the logo and color palettes
def create_image_with_logo_and_palettes(logo_image, color_palettes):
    # Create a blank image
    width, height = 800, 1000  # Define the size of the image
    img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Place the logo at the top center with a max size of 100x100 px
    logo = Image.open(logo_image)
    logo.thumbnail((180, 180))  # Ensure the logo does not exceed 100x100 px
    logo_width, logo_height = logo.size
    logo_x = (width - logo_width) // 2
    img.paste(logo, (logo_x, 20))  # Place logo at the top center

    # Calculate y position to start drawing color palettes
    y_offset = logo_y = 20 + logo_height + 20

    # Draw each color palette as circles
    circle_radius = 25  # Radius of the circle (smaller than before)
    x_offset = 20  # Starting x position for the first color circle
    for palette_name, palette_colors in color_palettes.items():
        font = ImageFont.truetype("open-sans.ttf", 18)  # Load Open Sans font
        draw.text((20, y_offset), palette_name, fill="black", font=font)  # Add the palette name with increased spacing
        y_offset += 30  # Space between name and colors
        # Draw colors in a single row (horizontally aligned)
        for i, color in enumerate(palette_colors):
            draw.ellipse([x_offset + i * 25, y_offset, x_offset + i * 25 + circle_radius * 2, y_offset + circle_radius * 2], fill=color)
        y_offset += 80  # Space between palettes (reduced to accomodate smaller circles)

    # Save to a BytesIO object to enable download
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    
    return img_byte_arr


# Button to generate color palette
if st.button("Gerar paleta de cores"):
    st.write(f"Você selecionou a cor: {color}")
    
    # Generate and display color palettes
    color_palettes = {
        "Cores Complementares": complementary_colors(color),
        "Cores Analogos": analogous_colors(color),
        "Cores Complementares Divididas": split_complementary_colors(color),
        "Cores em Harmonia Quadrada": square_colors(color),
        "Cores Compostas": compound_colors(color),
        "Sombras": shades(color),
        "Cores Monocromáticas": monochromatic_colors(color)
    }
    # Handle image download
    if uploaded_image is not None:
        img_byte_arr = create_image_with_logo_and_palettes(uploaded_image, color_palettes)
        st.download_button(
            label="Baixar Imagem com Paletas",
            data=img_byte_arr,
            file_name="paleta_de_cores_com_logo.png",
            mime="image/png"
        )

    # Display color palettes and harmony images
    for palette_name, palette_colors in color_palettes.items():
        st.subheader(palette_name)
        image_stream = generate_harmony_image(palette_colors)
        st.image(image_stream, caption=palette_name)
        cols = st.columns(len(palette_colors))
        for col, hex_color in zip(cols, palette_colors):
            with col:
                st.markdown(f"<div style='display: inline-block; border-radius: 50%; width: 20px; height: 20px; background-color: {hex_color};'></div>", unsafe_allow_html=True)
                st.write(hex_color)


