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

st.title("Gerador de Paleta - Harmonia de Cores")

# Color selection
color = st.color_picker("Escolha uma cor:")

# Button to generate color palette
if st.button("Gerar paleta de cores"):
    st.write(f"Você selecionou a cor: {color}")
    
    # Generate and display color palettes
    st.subheader("Cores Complementares")
    comp_colors = complementary_colors(color)
    comp_image_stream = generate_harmony_image(comp_colors)
    st.image(comp_image_stream, caption="Cores Complementares")
    cols = st.columns(len(comp_colors))
    for col, hex_color in zip(cols, comp_colors):
        with col:
            st.markdown(f"<div style='display: inline-block; border-radius: 50%; width: 20px; height: 20px; background-color: {hex_color};'></div>", unsafe_allow_html=True)
            st.write(hex_color)

    st.subheader("Cores Análogos")
    anal_colors = analogous_colors(color)
    anal_image_stream = generate_harmony_image(anal_colors)
    st.image(anal_image_stream, caption="Cores Análogos")
    cols = st.columns(len(anal_colors))
    for col, hex_color in zip(cols, anal_colors):
        with col:
            st.markdown(f"<div style='display: inline-block; border-radius: 50%; width: 20px; height: 20px; background-color: {hex_color};'></div>", unsafe_allow_html=True)
            st.write(hex_color)

    st.subheader("Cores Complementares Divididas")
    split_colors = split_complementary_colors(color)
    split_image_stream = generate_harmony_image(split_colors)
    st.image(split_image_stream, caption="Cores Complementares Divididas")
    cols = st.columns(len(split_colors))
    for col, hex_color in zip(cols, split_colors):
        with col:
            st.markdown(f"<div style='display: inline-block; border-radius: 50%; width: 20px; height: 20px; background-color: {hex_color};'></div>", unsafe_allow_html=True)
            st.write(hex_color)

    st.subheader("Cores em Harmonia Quadrada")
    square_colors_list = square_colors(color)
    square_image_stream = generate_harmony_image(square_colors_list)
    st.image(square_image_stream, caption="Cores em Harmonia Quadrada")
    cols = st.columns(len(square_colors_list))
    for col, hex_color in zip(cols, square_colors_list):
        with col:
            st.markdown(f"<div style='display: inline-block; border-radius: 50%; width: 20px; height: 20px; background-color: {hex_color};'></div>", unsafe_allow_html=True)
            st.write(hex_color)

    st.subheader("Cores Compostas")
    compound_colors_list = compound_colors(color)
    compound_image_stream = generate_harmony_image(compound_colors_list)
    st.image(compound_image_stream, caption="Cores Compostas")
    cols = st.columns(len(compound_colors_list))
    for col, hex_color in zip(cols, compound_colors_list):
        with col:
            st.markdown(f"<div style='display: inline-block; border-radius: 50%; width: 20px; height: 20px; background-color: {hex_color};'></div>", unsafe_allow_html=True)
            st.write(hex_color)

    st.subheader("Sombras")
    shades_list = shades(color)
    shades_image_stream = generate_harmony_image(shades_list)
    st.image(shades_image_stream, caption="Sombras")
    cols = st.columns(len(shades_list))
    for col, hex_color in zip(cols, shades_list):
        with col:
            st.markdown(f"<div style='display: inline-block; border-radius: 50%; width: 20px; height: 20px; background-color: {hex_color};'></div>", unsafe_allow_html=True)
            st.write(hex_color)

    st.subheader("Cores Monocromáticas")
    mono_colors = monochromatic_colors(color)
    mono_image_stream = generate_harmony_image(mono_colors)
    st.image(mono_image_stream, caption="Cores Monocromáticas")
    cols = st.columns(len(mono_colors))
    for col, hex_color in zip(cols, mono_colors):
        with col:
            st.markdown(f"<div style='display: inline-block; border-radius: 50%; width: 20px; height: 20px; background-color: {hex_color};'></div>", unsafe_allow_html=True)
            st.write(hex_color)

