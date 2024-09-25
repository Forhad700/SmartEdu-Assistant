import os 
import langchain
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
import streamlit as st


os.environ['LANGCHAIN_API_KEY'] = st.secrets["LANGCHAIN_API_KEY"]
os.environ['GOOGLE_API_KEY'] = st.secrets["GOOGLE_API_KEY"]


llm=GoogleGenerativeAI(model='gemini-pro',temperature=0.1)



prompt=ChatPromptTemplate.from_messages([
    ('system','Provide a comprehensive overview of the topic that the user provides'),
    ('user','{user_query}')
])



st.title('SmartEdu Assistant')


user_query=st.text_input('Input Your Query')


if st.button('Generate'):
    if user_query:
        try:
            formatted_prompt = prompt.format(user_query=user_query)
            response = llm.invoke(formatted_prompt)
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please Input Query")
