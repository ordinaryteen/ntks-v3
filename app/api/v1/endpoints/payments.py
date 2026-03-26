from fastapi import APIRouter, Depends
from app.core.security import verify_whatsapp_signature

from app.features.payments.schemas import WhatsAppPayload
from app.features.payments.service import PaymentService
from app.features.payments.dependencies import get_payment_service


router = APIRouter()

@router.post("/webhook", dependencies=[Depends(verify_whatsapp_signature)])
async def handle_whatsapp_webhook(
  payload: WhatsAppPayload,
  service: PaymentService = Depends(get_payment_service)
):
  user_text = payload.entry[0].changes[0].value.messages[0].text.body

  ai_reply = await service.process_chat(user_text)

  return {"status": "success", "ai_response": ai_reply}
