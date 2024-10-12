from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai 
import os

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

# Function to load model and get responses
model = genai.GenerativeModel("gemini-pro")

def get_response(ques):
    response = model.generate_content(ques)
    return response.text

# Initialize the streamlit application
st.set_page_config(page_title = "Gemini LLM App")
st.header("Gemini Pro Q&A Application")
input = st.text_input("Please provide a prompt here : ", key= "input")

# Submit button
submit = st.button("Ask a question")

# When submit button is clicked
if submit:
    response = get_response(input)
    st.subheader("The response is : ")
    st.write(response)

