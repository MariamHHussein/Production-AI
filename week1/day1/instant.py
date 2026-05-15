from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(
    api_key=os.environ.get("GEMINI_API_KEY"),  # ✅ FIX
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

@app.get("/", response_class=HTMLResponse)
def instant():
    message = """
You are on a website that has just been deployed to production for the first time!
Please reply with an enthusiastic announcement to welcome visitors to the site, explaining that it is live on production for the first time!
"""

    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )

    reply = response.choices[0].message.content.replace("\n", "<br/>")

    html = f"""
    <html>
        <head><title>Live in an Instant!</title></head>
        <body>
            <p>{reply}</p>
        </body>
    </html>
    """

    return html