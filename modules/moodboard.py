import streamlit as st

from motor.generate_moodboard import generate_moodboard

st.title("Moodboard Aspire")

input_text = st.text_area("Me explique, conceitualmente, o que será este projeto?")

if st.button("Gerar imagens do moodboard"):
    moodboards = generate_moodboard(input_text)   
    
    cols = st.columns(4)
    for i, moodboard in enumerate(moodboards):
        with cols[i % 4]:
            st.image(moodboard.read())

