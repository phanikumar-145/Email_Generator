import streamlit as st
import requests

st.title("AI Email Generator")

prompt = st.text_input("Describe the email you want")

if st.button("Generate Email"):

    url = "http://127.0.0.1:8000/generate-email"

    response = requests.post(
        url,
        json={"prompt": prompt}
    )

    result = response.json()

    st.subheader("Generated Email")
    st.write(result["email"])