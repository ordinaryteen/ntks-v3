import asyncio
import sys
import os
from pathlib import Path

# Fix ModuleNotFoundError when running the script directly
root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.core.database import engine, Base, AsyncSessionLocal
from app.domain.identity import User
from app.domain.properties import Room
from app.domain.members import Tenant
from app.features.payments.models import Transaction

async def seed_data():
    print("Starting Database Initialization...")
    
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        
        # Create Tables
        await conn.run_sync(Base.metadata.create_all)
        print("Tables created successfully.")

    async with AsyncSessionLocal() as session:
        async with session.begin():
            juragan = User(phone_number="6289513788350", name="Nafi")
            session.add(juragan)
            await session.flush() 

            # 4. Create Rooms A1 - C5
            rooms = []
            for i in range(1, 6):
                rooms.append(Room(room_name=f"A{i}", price=1000000, owner_id=juragan.id))
            for i in range(1, 6):
                rooms.append(Room(room_name=f"B{i}", price=1500000, owner_id=juragan.id))
            for i in range(1, 6):
                rooms.append(Room(room_name=f"C{i}", price=2000000, owner_id=juragan.id))
            
            session.add_all(rooms)
            print(f"[OK] {len(rooms)} Rooms seeded.")

        await session.commit()
    print("Database is ready to rock!")

if __name__ == "__main__":
    asyncio.run(seed_data())