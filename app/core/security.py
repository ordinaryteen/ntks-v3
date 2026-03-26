import hmac
import hashlib
from fastapi import Request, HTTPException, Header
from app.core.config import settings

async def verify_whatsapp_signature(request: Request, x_hub_signature_256: str = Header(None)):
  if not x_hub_signature_256:
    raise HTTPException(status_code=401, detail="X-Hub-Signature-256 header missing")

  body = await request.body()

  signature_hash = x_hub_signature_256.split("=")[1] if "=" in x_hub_signature_256 else ""

  expected_signature = hmac.new(
    key=settings.APP_SECRET.encode(),
    msg=body,
    digestmod=hashlib.sha256
  ).hexdigest()

  if not hmac.compare_digest(expected_signature, signature_hash):
    raise HTTPException(status_code=401, detail="Invalid signature")

  return True