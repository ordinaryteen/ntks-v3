import json
from openai import AsyncOpenAI
from app.core.config import settings
from app.features.payments.repository import PaymentRepository
from app.features.payments.tools import PAYMENT_TOOLS

class PaymentService:
  def __init__(self, repo: PaymentRepository):
    self.repo = repo
    self.client = AsyncOpenAI(
      api_key = settings.DEEPSEEK_API_KEY,
      base_url = "https://api.deepseek.com"
    )

  async def process_chat(self, user_text: str, user_name: str = "Nafi"):
    messages = [
        {"role": "system", "content": f"Lo adalah asisten Natakos. Bos lo namanya {user_name}. Gaya bahasa: Santai, panggil 'Juragan'. Tugas lo: Mengelola pembayaran kos."},
        {"role": "user", "content": user_text}
    ]

    response = await self.client.chat.completions.create(
      model="deepseek-chat",
      messages=messages,
      tools=PAYMENT_TOOLS,
      tool_choice="auto"
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
      messages.append(response_message)

      for tool_call in tool_calls:
        function_args = json.loads(tool_call.function.arguments)

        observation = await self.execute_payment_logic(function_args)

        messages.append({
          "tool_call_id": tool_call.id,
          "role": "tool",
          "name": "record_payment",
          "content": observation,
        })

        final_response = await self.client.chat.completions.create(
          model="deepseek-chat",
          messages=messages
        )
        return final_response.choices[0].message.content

      # if there is no tools called
      return response_message.content


  async def execute_payment_logic(self, args: dict):
    room_name   = args.get("room_name")
    tenant_name = args.get("tenant_name")
    amount      = args.get("amount")

    room = await self.repo.get_room_by_name(room_name)
    if not room:
      return f"Error: Kamar {room_name} tidak ditemukan."

    tenant = await self.repo.get_tenant_by_name_and_room(tenant_name, room.id)
    if not tenant:
      return f"Error: Tidak ada penghuni bernama '{tenant_name}' di kamar {room_name}."

    tx = await self.repo.create_transaction(tenant.id, amount)
    return f"Sukses: Pembayaran {tenant.name} ({room.room_name}) sebesar {tx.amount} telah dicatat ke DB."