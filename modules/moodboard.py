import streamlit as st

from motor.generate_harmony import complementary_colors, shades, analogous_colors, split_complementary_colors, square_colors, compound_colors, monochromatic_colors
from motor.generate_moodboard import generate_moodboard_with_harmonies
from motor.firebase.firestore import insert_image_gen

st.title("Moodboard Aspire")

color = st.color_picker("Escolha a cor principal:")
color_harmonies = {
    "complementary": complementary_colors(color),
    "analogous": analogous_colors(color),
    "split_complementary": split_complementary_colors(color),
    "square_harmony": square_colors(color),
    "compound": compound_colors(color),
    "shades": shades(color),
    "monochromatic": monochromatic_colors(color)
}

input_text = st.text_area("Me explique, conceitualmente, o que será este projeto?")

if st.button("Gerar imagens do moodboard"):
    moodboards = generate_moodboard_with_harmonies(input_text, color_harmonies)   
    
    cols = st.columns(4)
    for i, moodboard in enumerate(moodboards):
        with cols[i % 4]:
            img_generated = moodboard.read()
            st.image(img_generated)
            insert_image_gen({
                "generated_by": st.session_state["name"],
                "prompt": input_text,
                "image": img_generated
            })

