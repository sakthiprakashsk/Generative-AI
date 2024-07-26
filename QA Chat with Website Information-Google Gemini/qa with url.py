from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os

import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

import langchain
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import GoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

def get_gemini_response(input_text):
    llm= GoogleGenerativeAI(model="gemini-pro",temperature=0.3)
    embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    index=FAISS.load_local("url.index", embeddings=embedding, allow_dangerous_deserialization=True)
    retriever = index.as_retriever()
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    response=chain({"query":input_text},return_only_outputs=True)
    return response
    
def main():
    st.set_page_config("URL Q&A")
    st.header("Chat with Multiple URL using Gemini")
    input_text=st.text_input("Enter your question..")
    submit=st.button("Submit")
    if submit:
        if input_text!= "":
            response=get_gemini_response(input_text)
            st.subheader("Answer")
            st.write(response["result"])
            
if __name__ == "__main__":
    main()