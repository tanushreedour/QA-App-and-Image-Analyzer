import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import streamlit as st
from PIL import Image

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")

def get_response(input, image):
    if input!="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Google Image Demo", page_icon=":image:")

st.header("Gemini Powered Image App")

input = st.text_input("Please enter information here: ", key = "input")
# Image uploader
uploaded_file = st.file_uploader("Choose an Image", type=["jpg", "png", "jpeg"])

image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = " Uploaded image is....", use_column_width = True)

submit = st.button("Submit...")
if submit:
    response = get_response(input, image)
    st.subheader("This image shows: ")
    st.write(response)