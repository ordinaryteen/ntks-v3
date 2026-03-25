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