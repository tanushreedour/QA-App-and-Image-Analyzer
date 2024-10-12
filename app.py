import getpass
import os

os.environ["GOOGLE_API_KEY"] = getpass.getpass()
os.environ["GOOGLE_CLOUD_PROJECT"] = "Generative Language Client"

from langchain_google_vertexai import ChatVertexAI
import streamlit as st

if __name__ == "__main__":
    
    model = ChatVertexAI(model = "gemini-pro")

    def get_response(ques):
        response = model.generate_content(ques)
        return response.text

    # Initialize the streamlit application
    st.set_page_config(page_title = "Q&A Demo")
    st.header("Gemini Pro Q&A Application")
    input = st.text_input("Input: ", key= "input")

    # Submit button
    submit = st.button("Ask a question")

    # When submit button is clicked
    if submit:
        response = get_response(input)
        st.subheader("The response is : ")
        st.write(response)

    # st.title("Q&A")
    # st.header("Gemini Q&A LLM App")
    # prompt = st.text_input("Enter your prompt")
    # submit = st.button("Ask your question")
    # if submit:
    #     response = model.generate_content(prompt)
    #     st.subheader("Generated Response :")
    #     st.write(response.text)
    
#streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py