import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def get_LLAMA_response(input_text,no_words,blog_style):
    llm=CTransformers(model = "meta-llama/Llama-2-7b-chat-hf")
    
    
    prompt_template="""
        Write a blog for {blog_style} job profile 
        for a topic name {input_text} within {no_words} words
        """
    
    prompt=PromptTemplate(template=prompt_template,
                          input_variable=["input_text","no_words","blog_style"])

    response=llm(prompt.format(input_text=input_text,no_words=no_words,blog_style=blog_style))
    print(response)
    return response
    
    
st.set_page_config(page_title = "Generate Blog",
                      layout="centered",
                      initial_sidebar_state="collapsed")
st.header("Generate Blog")
input_text=st.text_area("Enter the Blog Topic")
col1,col2=st.columns([5,5])
with col1:
    no_words=st.text_input("No of Words")
with col2:
    blog_style=st.selectbox("Writing the blog for...",
                            ("Researcher",
                            "Data Scientist",
                            "Common Man"),index=0)
    
submit=st.button("Generate")
if submit:
    st.write(get_LLAMA_response(input_text,no_words,blog_style))