from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import AsyncSessionLocal, engine, Base
from app.models import User
from app.schemas import UserOut
from typing import List
from sqlalchemy import text

app = FastAPI(title="Тест API + postgres")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@app.get("/users", response_model=List[UserOut])
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT * FROM users"))
    rows = result.fetchall()
    return rows

@app.post("/seed")
async def seed_users():
    async with AsyncSessionLocal() as session:
        users = [
            User(name="Максим", age=20),
            User(name="Ксюша", age=18)
        ]
        session.add_all(users)
        await session.commit()
        return {"message": "Добавлено 2 пользователся"}