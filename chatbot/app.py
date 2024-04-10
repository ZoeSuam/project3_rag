from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os

openai_api_key = os.getenv("OPENAI_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
os.environ["Digledu"] = "true"
project1 = os.getenv("Digledu")
# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful Tutor for Students in a business adminsitration course.Please response to the user queries"),
        ("user","question:{question}")
    ]
)

#streamlit framework

st.title("Langchain Demo with OpenAI API")
input_text = st.text_input("Search the topic u want")

#openAI llm
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))