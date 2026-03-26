Brochoco it aint that DDD 🥀

```
src/
├── api/
│   └── v1/
│       └── assistant/            # Endpoint buat chat/interaksi sama Agent
│           ├── router.py
│           └── schemas.py
│
├── modules/
│   ├── identity/                 # Contoh Modul Bisnis (Tetap murni)
│   │   ├── domain/ ...
│   │   ├── application/
│   │   │   ├── agents/           # <--- NEW: Agent spesifik buat fitur Identity
│   │   │   │   ├── identity_agent.py # Logic agent (pake BaseAgent)
│   │   │   │   └── tools.py      # Definisi tools (Function calling)
│   │   │   └── use_cases/ ...
│   │   └── infrastructure/
│   │       ├── persistence/ ...
│   │       └── ai_tools/         # <--- NEW: Implementasi nyata dari tools.py
│   │           └── identity_lookup_tool.py # (Misal: Agent cari user via DB)
│   │
│   └── support_agent/            # Modul Khusus Agent (Orchestrator)
│       ├── application/
│       │   └── coordinator.py    # Ngatur kapan pake IdentityAgent vs SalesAgent
│       └── domain/
│           └── prompts/          # System Prompts & Templates (Pure String/Logic)
│               ├── base_prompts.py
│               └── persona_templates.py
│
├── core/                         # SHARED AI CORE (The Engine)
│   ├── ai/                       
│   │   ├── base_agent.py         # Abstract class buat semua agent
│   │   ├── llm_client.py         # Wrapper OpenAI/Anthropic/Local LLM
│   │   ├── memory/               # Shared Memory (Redis/Postgres)
│   │   └── vector_store.py       # Integrasi Pinecone/ChromaDB/PGVector
│   ├── config.py
│   └── database.py
│
├── main.py
└── tests/
```

### 📋 Checklist Integrasi WhatsApp (Meta Cloud API)

#### 1. Persiapan Administratif (Meta Developer Dashboard)
* [ ] **Buat Akun:** Daftar di [developers.facebook.com](https://developers.facebook.com).
* [ ] **Buat App:** Pilih tipe "Other" -> "Business".
* [ ] **Tambah Produk:** Klik "Set up" pada bagian **WhatsApp**.
* [ ] **Nomor Test:** Gunakan nomor "Test Number" yang dikasih Meta untuk kirim ke nomor HP pribadi lo sendiri (biar gratis pas *development*).
* [ ] **Permanent Token:** Ini yang sering bikin orang lupa. Token bawaan Meta cuma tahan 24 jam. Lo harus buat **System User** di Business Manager buat dapet *Permanent Access Token*.

#### 2. Konfigurasi Environment (`.env`)
Lo bakal butuh 3 variabel baru:
* [ ] `WHATSAPP_TOKEN`: Token akses dari Meta.
* [ ] `PHONE_NUMBER_ID`: ID unik untuk nomor pengirim lo.
* [ ] `WABA_ID`: WhatsApp Business Account ID (biasanya buat keperluan *billing/logging*).

#### 3. Komponen Teknis (Python Logic)
* [ ] **`MessengerService`:** Bikin satu *class* baru di `app/core/messenger.py` yang isinya cuma satu fungsi: `send_text_message(to_phone, message)`.
* [ ] **HTTP Client:** Pake `httpx` untuk nembak `POST` ke endpoint Meta: `https://graph.facebook.com/v20.0/{phone_number_id}/messages`.
* [ ] **Webhook Verification:** Tambahin endpoint `GET /webhook` di FastAPI. Meta bakal nembak *challenge* (teka-teki string) ke sini buat mastiin server lo beneran aktif sebelum mereka mulai ngirim data chat.

#### 4. Wiring Terakhir
* [ ] **Integrasi Service:** Di `main.py` atau `router`, setelah dapet `ai_response` dari `PaymentService`, panggil `MessengerService.send_text_message()`.

---