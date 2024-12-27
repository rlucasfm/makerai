import streamlit as st

from motor.agents.Concepter import ConcepterAgent

st.title("Concepter - Criador de Conceitos")

concept_agent = ConcepterAgent()

if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Vamos começar! Me fale um pouco mais sobre este projeto. Quais informações, objetivos e comentários importantes você pode me dizer?"}]
    
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
def generate_response(user_input):
    s_agent = concept_agent.agent
    try:
        return s_agent.chat(user_input).response
    except:
        return "Tente novamente..."

user_input = st.chat_input("Digite sua mensagem: ")

if user_input:
    st.session_state.messages.append({"content": user_input, "role": "user"})
    st.chat_message("user").write(user_input)
    
    response = generate_response(user_input)
    st.session_state.messages.append({"content": response, "role": "assistant"})
    st.chat_message("assistant").write(response)