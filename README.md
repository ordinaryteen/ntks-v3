Brochoco it aint that DDD 🥀

```
your-fav-backend/
├── src/
│   ├── api/                        # LAYER: INTERFACES (Gatekeepers)
│   │   ├── v1/
│   │   │   ├── identity/           # Endpoint User/Auth
│   │   │   │   ├── router.py
│   │   │   │   └── schemas.py      # Pydantic DTOs
│   │   │   ├── assistant/          # Endpoint Chat Utama Agent
│   │   │   │   ├── router.py
│   │   │   │   └── schemas.py
│   │   │   └── knowledge/          # Endpoint buat upload dokumen (RAG)
│   │   │       ├── router.py
│   │   │       └── schemas.py
│   │   └── dependencies.py         # Global DI (Auth, DB Session)
│   │
│   ├── modules/                    # LAYER: THE HEART (Feature-First)
│   │   ├── identity/               # -- Fitur: User Management --
│   │   │   ├── domain/             # Pure Logic (Entities, Repo Interface)
│   │   │   ├── application/
│   │   │   │   ├── use_cases/      # RegisterUser, LoginUser
│   │   │   │   ├── agents/         # AI as "Power User"
│   │   │   │   │   ├── identity_agent.py
│   │   │   │   │   └── tools.py    # List tools (get_user_profile, etc)
│   │   │   └── infrastructure/
│   │   │       ├── persistence/    # SQLAlchemy Models & Repos
│   │   │       └── ai_tools/       # Impl: Tool panggil Repo
│   │   │
│   │   ├── assistant/              # -- Fitur: AI Orchestration --
│   │   │   ├── domain/
│   │   │   │   ├── prompts/        # Persona & System Prompt Templates
│   │   │   │   │   ├── agent_persona.py
│   │   │   │   │   └── tool_instructions.py
│   │   │   ├── application/
│   │   │   │   └── chat_manager.py # Ngatur alur chat & memory strategy
│   │   │   └── infrastructure/     
│   │   │       └── memory_store.py # Implementasi simpen chat ke Redis
│   │   │
│   │   └── knowledge/              # -- Fitur: RAG & Documents --
│   │       ├── domain/
│   │       │   └── entities.py     # Document Entity
│   │       ├── application/
│   │       │   └── ingest_doc.py   # Use Case: File -> Embedding -> VectorStore
│   │       └── infrastructure/
│   │           └── vector_repo.py  # Impl: Panggil core/ai/vector_store.py
│   │
│   ├── core/                       # LAYER: SHARED ENGINE (Cross-Cutting)
│   │   ├── ai/                     # -- AI AGENCY BASE ENGINE --
│   │   │   ├── base_agent.py       # Class utama yang di-extend semua agent
│   │   │   ├── llm_client.py       # Wrapper OpenAI/Claude (Singleton)
│   │   │   ├── vector_store.py     # Wrapper PGVector/Pinecone (RAG)
│   │   │   └── memory/             # -- MEMORY & SUMMARIZATION --
│   │   │       ├── base.py
│   │   │       ├── strategies.py   # (The "Compact" logic is here!)
│   │   │       └── window.py       # Slidding window memory
│   │   ├── database.py             # SQLAlchemy Engine setup
│   │   ├── config.py               # Env vars (API_KEYS, DB_URL)
│   │   └── exceptions.py           # Global Error Handling
│   │
│   ├── main.py                     # App Entry Point
│   └── alembic/                    # DB Migrations
│
├── tests/                          # Mirrored Test Suite
│   ├── unit/
│   ├── integration/
│   └── agents/                     # Khusus ngetes akurasi tool-calling
├── .env
├── pyproject.toml
└── README.md
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