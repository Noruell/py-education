import asyncio
from sqlalchemy import text
from models import AsyncSessionLocal, User

async def main():
    async with AsyncSessionLocal() as session:
        new_user = User(name="Ксюша", age=18)
        session.add(new_user)
        await session.commit()

        result = await session.execute(text('SELECT * FROM users'))
        rows = result.fetchall()
        for row in rows:
            print(row)

asyncio.run(main())