from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,)
    return response

st.set_page_config("Q & A Demo")

st.header("Gemini LLM Application")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    
input=st.text_input("Input...", key='input')
submit=st.button("Ask the question")

if submit and input:
    response=get_gemini_response(input)
    st.session_state['chat_history'].append(("You : ",input))
    st.subheader("The Response is...")
    st.write(response.text)
    st.session_state['chat_history'].append(("Bot : ",response.text))
    
st.subheader("The Chat History...")    
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")    