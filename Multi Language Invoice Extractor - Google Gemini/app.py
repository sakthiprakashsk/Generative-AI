from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
from PIL import Image
import google.generativeai as genai
genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro-vision')

input_prompt="""
                You are an expert in understanding invoices. 
                We will upload an image as invoice and you will have to answer any questions based on the uploaded invoice image
            """

def get_gemini_response(image,input,input_prompt,):
    response=model.generate_content([input_prompt,image,input])
    return response

st.set_page_config("Invoice Extractor")

st.header("Gemini Invoice Extractor")

uploaded_file=st.file_uploader("Choose the file...", type=("jpg","jpeg","png"))
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)


input=st.text_input("Question :",key='input')

submit=st.button("Ask about Invoice")

if submit:
    response=get_gemini_response(input_prompt,image,input)
    st.subheader("Answer is...")
    st.write(response.text)
