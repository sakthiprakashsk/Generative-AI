from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q & A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input : ", key="input")
submit=st.button("Ask the question")

if submit:
    result = get_gemini_response(input)
    st.subheader("The Response is...")
    st.write(result)
    
    