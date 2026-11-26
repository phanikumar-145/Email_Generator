import os

import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

app = FastAPI(
    title="AI Email Generator API",
    description="Generate professional emails from short user instructions.",
    version="1.0.0",
)

model = genai.GenerativeModel("gemini-2.5-flash")


class EmailRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=3,
        max_length=4000,
        description="Describe the email you want to generate.",
    )


@app.get("/")
def root():
    return {"message": "AI Email Generator API is running."}


@app.get("/health")
def health():
    return {"status": "ok", "api_key_configured": bool(api_key)}


@app.post("/generate-email")
def generate_email(data: EmailRequest):
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GEMINI_API_KEY is not configured. Add it to your local .env file.",
        )

    full_prompt = f"""
You are a professional email-writing assistant.

Write a clear, polite, and well-structured email based on the user's request.
Include an appropriate subject line, greeting, body, and closing.
Do not invent names, dates, or facts that the user has not provided.

User request:
{data.prompt}
"""

    try:
        response = model.generate_content(full_prompt)
        email_text = getattr(response, "text", None)

        if not email_text:
            raise HTTPException(
                status_code=502,
                detail="The AI provider returned an empty response. Please try again.",
            )

        return {"email": email_text}

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Email generation failed. Check the API configuration and try again.",
        )
