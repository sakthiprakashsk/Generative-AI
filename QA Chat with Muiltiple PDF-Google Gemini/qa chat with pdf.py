from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os

import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

import langchain
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain


def get_gemini_response(input_text):
    model= ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)
    embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    index=FAISS.load_local("faiss_index", embeddings=embedding, allow_dangerous_deserialization=True)
    doc_search=index.similarity_search(input_text) 

    prompt_template="""
        Answer the question as detailed as possible from the provided context, 
        make sure to provide all the details,if the answer is not in provided context just say,
        "answer is not avaiable in this context",
        don't provide the wrong answer\n\n
        Context : \n {context}? \n
        Question : \n {question} \n
        
        Answer:   
        """

    prompt=PromptTemplate(template=prompt_template, input_variables=(["context","question"]))

    chain=load_qa_chain(model,chain_type='stuff',prompt=prompt)

    response=chain({"input_documents": doc_search, "question": input_text}, return_only_outputs=True)
    return response
    
def main():
    st.set_page_config("PDF Q&A")
    st.header("Chat with Multiple PDF using Gemini")
    input_text=st.text_input("Enter your question..")
    submit=st.button("Submit")
    if submit:
        if input_text!= "":
            response=get_gemini_response(input_text)
            st.write(response["output_text"])
            
if __name__ == "__main__":
    main()