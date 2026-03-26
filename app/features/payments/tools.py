PAYMENT_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "record_payment",
            "description": "Mencatat pembayaran uang kos dari penghuni. Gunakan ini jika user menyebutkan nama/kamar dan nominal uang.",
            "parameters": {
                "type": "object",
                "properties": {
                    "tenant_name": {"type": "string", "description": "Nama penghuni (misal: Andri)"},
                    "room_name": {"type": "string", "description": "Kode kamar (misal: A4)"},
                    "amount": {"type": "integer", "description": "Nominal uang dalam Rupiah"}
                },
                "required": ["tenant_name", "room_name", "amount"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_unpaid_list",
            "description": "Melihat daftar penghuni yang belum bayar kos bulan ini.",
            "parameters": {
                "type": "object",
                "properties": {
                    "month": {"type": "integer", "description": "Bulan dalam angka (1-12)"}
                }
            }
        }
    }
]