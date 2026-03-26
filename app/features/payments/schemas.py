from pydantic import BaseModel, Field
from typing import List, Optional

# --- 1. WHATSAPP WEBHOOK SCHEMAS ---
class WhatsAppText(BaseModel):
    body: str

class WhatsAppMessage(BaseModel):
    from_number: str = Field(..., alias="from") 
    id: str
    timestamp: str
    text: WhatsAppText
    type: str

class WhatsAppValue(BaseModel):
    messaging_product: str
    messages: List[WhatsAppMessage]

class WhatsAppChange(BaseModel):
    value: WhatsAppValue
    field: str

class WhatsAppEntry(BaseModel):
    id: str
    changes: List[WhatsAppChange]

class WhatsAppPayload(BaseModel):
    """Skema utama buat validasi Webhook dari Meta"""
    object: str
    entry: List[WhatsAppEntry]


# --- 2. AI EXTRACTION SCHEMAS ---
class PaymentRequest(BaseModel):
    tenant_name: str
    room_name: str
    amount: int
    raw_text: str  