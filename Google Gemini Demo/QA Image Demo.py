from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
from PIL import Image
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGEL_API_KEY"))

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input,image):
    response=model.generate_content([input,image])
    return response.text

st.set_page_config("Gemini LLM Image Demo")

st.header("Gemini Application")
input=st.text_input("Input Prompt : ", key="input")

uploaded_file = st.file_uploader("Choose an image....", type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Upoaded Image", use_column_width=True)
    
submit = st.button("Tell me about the Image")

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is...")
    st.write(response)

