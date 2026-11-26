# AI Email Generator

A simple AI-powered email generation application built with Streamlit, FastAPI, and Google's Gemini model. Users describe the email they need, and the application returns a professional draft.

## Features

- Generate email drafts from natural-language instructions.
- Create drafts with a subject, greeting, body, and closing.
- Streamlit interface for entering requests and viewing generated emails.
- FastAPI backend with request validation.
- Gemini 2.5 Flash integration.
- Basic handling for missing API configuration, API errors, and request timeouts.

## Project Structure

```text
Email_Generator/
├── app.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Technology Stack

- Python
- Streamlit
- FastAPI
- Google Generative AI SDK
- Gemini 2.5 Flash
- Pydantic
- Requests
- python-dotenv
- Uvicorn

## Prerequisites

- Python 3.10 or later.
- A Google Gemini API key.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/phanikumar-145/Email_Generator.git
   cd Email_Generator
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a local `.env` file by copying `.env.example`, then add your Gemini API key:

   ```env
   GEMINI_API_KEY=your_actual_api_key
   ```

   Do not upload `.env` or share your API key publicly.

## Run the Application

Open two terminals from the project directory. Activate the same virtual environment in both.

**Terminal 1: Start the FastAPI backend**

```bash
uvicorn main:app --reload
```

The API runs at `http://127.0.0.1:8000`.

Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

**Terminal 2: Start the Streamlit frontend**

```bash
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open it in your browser.

## How It Works

1. The user enters a description of the email in the Streamlit interface.
2. Streamlit sends the prompt to the FastAPI endpoint `POST /generate-email`.
3. FastAPI validates the request using Pydantic.
4. The backend sends instructions and the user's prompt to Gemini 2.5 Flash.
5. The generated email is returned as JSON and displayed in the Streamlit interface.

## API Endpoint

### `POST /generate-email`

Request body:

```json
{
  "prompt": "Write an email requesting leave for one day."
}
```

Example response:

```json
{
  "email": "Subject: Leave Request\n\nDear Manager,\n..."
}
```

Additional endpoints:

- `GET /` - API welcome message.
- `GET /health` - Basic service health and API-key configuration status.

## Important Notes

- The backend and frontend must both be running for the application to work.
- The Streamlit frontend currently connects to `http://127.0.0.1:8000`. For deployment, configure the backend URL through an environment variable or deployment settings.
- Review and edit generated emails before sending them. AI-generated content can contain mistakes.
- The application sends the user's prompt to Google's Gemini service for generation. Do not enter confidential or sensitive information unless you are permitted to share it with that service.

## Future Improvements

- Add email tone and length controls.
- Support multiple languages.
- Add copy and download options.
- Add automated tests.
- Make the backend URL configurable for deployment.
