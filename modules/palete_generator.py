import streamlit as st
from motor.generate_harmony import (
    complementary_colors,
    analogous_colors,
    split_complementary_colors,
    square_colors,
    compound_colors,
    shades,
    monochromatic_colors
)

st.title("Gerador de Paleta de Cores")

# Color selection
color = st.color_picker("Escolha uma cor:")

# Button to generate color palette
if st.button("Gerar paleta de cores"):
    st.write(f"Você selecionou a cor: {color}")
    
    # Generate and display color palettes
    st.subheader("Cores Complementares")
    comp_colors = complementary_colors(color)
    cols = st.columns(len(comp_colors))
    for col, hex_color in zip(cols, comp_colors):
        with col:
            st.markdown(f"<div style='background-color: {hex_color}; width: 100px; height: 50px;'></div>", unsafe_allow_html=True)
            st.write(hex_color)

    st.subheader("Cores Análogas")
    anal_colors = analogous_colors(color)
    cols = st.columns(len(anal_colors))
    for col, hex_color in zip(cols, anal_colors):
        with col:
            st.markdown(f"<div style='background-color: {hex_color}; width: 100px; height: 50px;'></div>", unsafe_allow_html=True)
            st.write(hex_color)

    st.subheader("Cores Complementares Divididas")
    split_colors = split_complementary_colors(color)
    cols = st.columns(len(split_colors))
    for col, hex_color in zip(cols, split_colors):
        with col:
            st.markdown(f"<div style='background-color: {hex_color}; width: 100px; height: 50px;'></div>", unsafe_allow_html=True)
            st.write(hex_color)

    st.subheader("Cores em Harmonia Quadrada")
    square_colors_list = square_colors(color)
    cols = st.columns(len(square_colors_list))
    for col, hex_color in zip(cols, square_colors_list):
        with col:
            st.markdown(f"<div style='background-color: {hex_color}; width: 100px; height: 50px;'></div>", unsafe_allow_html=True)
            st.write(hex_color)

    st.subheader("Cores Compostas")
    compound_colors_list = compound_colors(color)
    cols = st.columns(len(compound_colors_list))
    for col, hex_color in zip(cols, compound_colors_list):
        with col:
            st.markdown(f"<div style='background-color: {hex_color}; width: 100px; height: 50px;'></div>", unsafe_allow_html=True)
            st.write(hex_color)

    st.subheader("Sombras")
    shades_list = shades(color)
    cols = st.columns(len(shades_list))
    for col, hex_color in zip(cols, shades_list):
        with col:
            st.markdown(f"<div style='background-color: {hex_color}; width: 100px; height: 50px;'></div>", unsafe_allow_html=True)
            st.write(hex_color)

    st.subheader("Cores Monocromáticas")
    mono_colors = monochromatic_colors(color)
    cols = st.columns(len(mono_colors))
    for col, hex_color in zip(cols, mono_colors):
        with col:
            st.markdown(f"<div style='background-color: {hex_color}; width: 100px; height: 50px;'></div>", unsafe_allow_html=True)
            st.write(hex_color)
