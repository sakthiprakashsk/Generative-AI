from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
import sqlite3
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,input_prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content([question,input_prompt])
    return response.text

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

    
input_prompt = """
You are an expert in converting English questions to SQL queries!
The SQL database has the name student and has the following columns - NAME, CLASS, SECTION.

For example,
Example 1 - How many entries of record are present?
The SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;

Example 2 - Tell me all the students studying in Data Science class?
The SQL command will be something like this: SELECT * FROM STUDENT where CLASS="Data Science";

also the sql code should not have ``` in beginning or end and sql word in output

"""


st.set_page_config("Reterieve any SQL query")
st.header("Gemini App To Reterieve SQL Data")

question=st.text_input("Input...", key="input")
submit=st.button("Submit")

if submit:
    res=get_gemini_response(question,input_prompt)
    st.write(res)
    response=read_sql_query(res,"student.db")
    st.subheader("The Response is..")
    for row in response:
        st.write(row)
    