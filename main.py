from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

genai.configure(api_key="")

model = genai.GenerativeModel("models/gemini-2.5-flash")

app = FastAPI()

class EmailRequest(BaseModel):
    prompt: str

@app.post("/generate-email")
def generate_email(data: EmailRequest):
    
    full_prompt = f"""
    Generate a professional email for the following request:
    {data.prompt}
    Include subject, greeting, body and closing.
    """

    response = model.generate_content(full_prompt)

    return {"email": response.text}