import os
import requests
from fastapi import FastAPI, Request

app = FastAPI()

AGENT_API_KEY = os.getenv("WHATSAPP_API_KEY")

@app.post("/webhook")
async def handle_whatsapp_message(request: Request):
    data = await request.json()
    chat_id = data.get("chat_id")

    if chat_id:
        url = "https://graph.facebook.com/v18.0/me/agent_messages"
        headers = {
            "Authorization": f"Bearer {AGENT_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "chat_id": chat_id,
            "message": "IM MR BEAST"
        }
        requests.post(url, headers=headers, json=payload)

    return {"status": "ok"}
