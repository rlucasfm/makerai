import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="MakerAI by MergeMind", page_icon=":material/home:")

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

authenticator.login()

if st.session_state['authentication_status'] is False:
    st.error("Nome de usuário/senha incorretos")

if st.session_state['authentication_status'] is None:
    st.warning("Por favor, preencha todos os campos")

if st.session_state['authentication_status']:
    st.sidebar.write(f'Bem vindo {st.session_state["name"]}!')
    authenticator.logout('Logout', 'sidebar')

    palete_generator = st.Page("modules/palete_generator.py", title="Palete Generator", icon=":material/strategy:")
    moodboard = st.Page("modules/moodboard.py", title="Moodboard", icon=":material/strategy:")

    pg = st.navigation([palete_generator, moodboard])
    pg.run()