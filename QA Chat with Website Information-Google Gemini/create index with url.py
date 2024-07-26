from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS

def enter_url(urls):
    loader=UnstructuredURLLoader(urls)
    docs=loader.load()

    split=RecursiveCharacterTextSplitter(separators=["\n\n","\n",","], chunk_size=1000, chunk_overlap=100)
    text_spliter=split.split_documents(docs)

    embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_documents(documents=text_spliter, embedding=embedding)
    vector_store.save_local("url.index")

def main():
    st.set_page_config("URL Loader")
    st.header("URL Loading for Q&A")

    urls=[]
    for i in range(3):
        url = st.text_input(f"Enter url....{i+1}")
        urls.append(url)

    process=st.button("Process URL")
    if process:
        enter_url(urls)
        st.success("Done")
        
if __name__ == "__main__":
    main()