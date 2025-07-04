# importing the required libraries
import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

#Configre Streamlit page settings
st.set_page_config(
    page_title="CHAT WITH THE CHATBOT!:",
    page_icon=":brain",
    layout="centered",
)

GOOGLE_API_KEY= os.getenv("goggle_Api_key")

#set up google gemini - Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel("gemini-pro")

def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title(" Gemini- pro - Chat bot")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Ask Gemini pro")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)

    gemini_response =st.session_state.chat_session.send_message((user_prompt))

    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)


