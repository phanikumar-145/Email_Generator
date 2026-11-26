import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/generate-email"

st.set_page_config(page_title="AI Email Generator", page_icon=None, layout="centered")

st.title("AI Email Generator")
st.write(
    "Describe the email you need. The application will generate a professional "
    "draft with a subject, greeting, body, and closing."
)

prompt = st.text_area(
    "Describe the email you want",
    placeholder=(
        "Example: Write an email to my manager requesting one day of leave "
        "on 15 December because of a personal appointment."
    ),
    height=150,
    max_chars=4000,
)

if st.button("Generate Email", type="primary"):
    if not prompt.strip():
        st.warning("Please describe the email you want to generate.")
    else:
        with st.spinner("Generating your email..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"prompt": prompt.strip()},
                    timeout=60,
                )
                response.raise_for_status()
                result = response.json()
                email = result.get("email")

                if email:
                    st.subheader("Generated Email")
                    st.text_area(
                        "Your email draft",
                        value=email,
                        height=350,
                    )
                else:
                    st.error("The API response did not contain an email draft.")

            except requests.exceptions.ConnectionError:
                st.error(
                    "Could not connect to the API. Start the FastAPI server "
                    "before generating an email."
                )
            except requests.exceptions.Timeout:
                st.error("The request timed out. Please try again.")
            except requests.exceptions.HTTPError as exc:
                try:
                    detail = response.json().get("detail", str(exc))
                except ValueError:
                    detail = str(exc)
                st.error(f"Email generation failed: {detail}")
            except requests.exceptions.RequestException as exc:
                st.error(f"Request failed: {exc}")
