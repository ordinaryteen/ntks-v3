from fastapi import FastAPI, Depends, Request

from app.core.config import settings
from app.core.security import verify_whatsapp_signature

from app.features.payments.schemas import WhatsAppPayload

app = FastAPI(title=settings.PROJECT_NAME)


@app.get("/health")
async def health_check():
  return {
    "status": "online",
    "engine": "Natakos V3"
  }

@app.post("/webhook")
async def handle_whatsapp_webhook(
  payload: WhatsAppPayload, 
  authorized: bool = Depends(verify_whatsapp_signature)
):
  message = payload.entry[0].changes[0].value.messages[0]

  print(f"DEBUG: Pesan masuk dari {message.from_number}")
  print(f"DEBUG: Isi pesan: {message.text.body}")
    
  return {"status": "received"}
