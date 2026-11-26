# AI Email Generator Using Google Gemini

## Project Overview

The AI Email Generator is a web application that generates professional emails using artificial intelligence.

Users can describe the email they want in simple natural language. The application sends the prompt to the backend, where the Google Gemini 2.5 Flash model generates an email containing a subject, greeting, body, and closing.

The generated email is then displayed through an interactive Streamlit interface.

## Key Features

- Generate professional emails using natural language prompts.
- Integrate Google Gemini 2.5 Flash for AI-powered email generation.
- Streamlit-based user interface.
- FastAPI backend for handling requests.
- REST API integration between frontend and backend.
- Automatically generate email subject, greeting, body, and closing.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| Backend | FastAPI |
| AI Model | Google Gemini 2.5 Flash |
| AI Integration | Google Generative AI SDK |
| API Communication | REST API |
| Data Validation | Pydantic |
| HTTP Requests | Requests |

## Project Architecture

The application follows a frontend and backend architecture.

1. The user enters an email request in the Streamlit interface.
2. Streamlit sends the prompt to the FastAPI backend.
3. FastAPI validates the request using a Pydantic model.
4. The backend constructs a prompt for Google Gemini.
5. Gemini generates the professional email.
6. FastAPI returns the generated email as a JSON response.
7. Streamlit displays the generated email.

## Project Structure

```text
Email_Generator/
|
├── app.py
├── main.py
└── README.md
```

### File Description

| File | Description |
|---|---|
| app.py | Streamlit frontend for entering prompts and displaying generated emails. |
| main.py | FastAPI backend responsible for Gemini integration and email generation. |
| README.md | Project documentation. |

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/phanikumar-145/Email_Generator.git
```

### 2. Navigate to the Project Directory

```bash
cd Email_Generator
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Required Libraries

```bash
pip install streamlit fastapi uvicorn requests google-generativeai pydantic
```

### 5. Configure Google Gemini API Key

Generate a Google Gemini API key and configure it securely using an environment variable.

For Windows PowerShell:

```powershell
$env:GOOGLE_API_KEY="your_api_key"
```

Update the backend configuration to read the environment variable:

```python
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
```

Do not publish your actual API key on GitHub.

### 6. Start the FastAPI Backend

Open a terminal and run:

```bash
uvicorn main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

### 7. Start the Streamlit Frontend

Open another terminal with the same virtual environment activated:

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

## API Documentation

### Generate Email

**Endpoint:** `POST /generate-email`

**Request Body:**

```json
{
    "prompt": "Write a professional email requesting leave for two days due to personal reasons."
}
```

**Successful Response:**

```json
{
    "email": "Subject: Leave Request\n\nDear Manager,\n\nI would like to request leave for two days due to personal reasons...\n\nBest regards"
}
```

The response contains the generated email as a string.

## Example Prompts

**Leave Request**

```text
Write a professional email requesting two days of leave due to personal reasons.
```

**Job Application**

```text
Write an email applying for a Python Developer position as a fresher.
```

**Meeting Request**

```text
Write a professional email requesting a meeting with my project manager to discuss project progress.
```

**Follow-up Email**

```text
Write a polite follow-up email asking about the status of my job application.
```

## Future Improvements

- Add email tone selection, such as formal, friendly, and professional.
- Provide options for short and detailed emails.
- Add email regeneration and editing functionality.
- Include copy-to-clipboard functionality.
- Add input validation and better error handling.
- Add email templates for job applications, leave requests, business communication, and follow-ups.
- Add user authentication and email generation history.
- Support multiple languages.

## Author

**Phani Kumar**

AI/ML and Generative AI Developer

GitHub: https://github.com/phanikumar-145
