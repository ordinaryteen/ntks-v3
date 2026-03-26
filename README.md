Brochoco it aint that DDD 🥀

```
app/
├── domain/                # THE HEART (Pure Python, No SQL, No FastAPI)
│   ├── identity/          # Sub-Domain
│   │   ├── entities.py    # Class User biasa (bukan SQLAlchemy model!)
│   │   ├── value_objects.py # Email, Phone (Logika validasi di level object)
│   │   ├── repository_interface.py # Cuma 'kontrak' (Abstract Base Class)
│   │   └── exceptions.py  # Domain-specific errors
├── infrastructure/        # THE TOOLS (Implementation Details)
│   ├── database/
│   │   ├── sqlalchemy_models.py # Di sini baru ada SQLAlchemy (Base)
│   │   └── repositories.py # Implementasi nyata query SQL
│   └── external_api/      # Misal: Client buat kirim SMS/WhatsApp
├── application/           # THE ORCHESTRATOR (Use Cases)
│   ├── identity/
│   │   └── register_user.py # Alur kerja: Panggil Repo -> Simpan -> Kirim Notif
└── interfaces/            # THE GATEKEEPERS (Entry Points)
    └── api/               # FastAPI Routers ada di sini
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