from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
import PyPDF2 as pdf
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=" "
    for page_num in range(len(reader.pages)):
        page=reader.pages[page_num]
        text+= page.extract_text()
    return text


input_prompt= """
    Hey Act like a skilled or very experience ATS(Application Traction System) with a deep understanding 
    of tech field,software engineering,data science,data analyst and big data engineer.
    Your task is to evaluate the resume based on the given job discription.
    You must consider the job market is very competitive and you should provide best assistance 
    for improving the resumes. Assign the percentage matching based on jd and the missing keyword with high accuracy
    
    Resume : {text}
    Description : {jd} 
    
    I want the response in string having the structure
    "JD Match" : "%","\nMissing Keywords: []","\nProfile Summary":""
    
    """
    
st.title("Smart Application Tracking System")
st.text("Improve Your Resume ATS")
jd=st.text_area("Enter your Job Description")
uploaded_file=st.file_uploader("Upload Your Resume", type="pdf",help="Please upload the PDF")
submit=st.button("Submit")

if submit :
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)


