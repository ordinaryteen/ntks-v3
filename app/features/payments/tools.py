PAYMENT_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "record_payment",
            "description": "Mencatat pembayaran sewa kos dari penghuni ke database.",
            "parameters": {
                "type": "object",
                "properties": {
                    "tenant_name": {"type": "string", "description": "Nama penghuni (misal: Andi, Andrej)"},
                    "room_name": {"type": "string", "description": "Kode kamar (misal: A4, B2)"},
                    "amount": {"type": "integer", "description": "Nominal uang dalam Rupiah"}
                },
                "required": ["tenant_name", "room_name", "amount"]
            }
        }
    }
]