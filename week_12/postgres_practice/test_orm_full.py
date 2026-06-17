import asyncio
from sqlalchemy import text
from models import AsyncSessionLocal, User




async def main():
    async with AsyncSessionLocal() as session:
        new_user = User(name="Леха", age=23)
        session.add(new_user)
        await session.commit()

        result = await session.execute(text('SELECT * FROM users'))
        rows = result.fetchall()
        for row in rows:
            print(row)

        #update
        new_age = 25
        user_id = 3
        await session.execute(
            text("UPDATE users SET age = $1 WHERE id = $2"),
            (new_age, user_id)
        )
        await session.commit()

        result = await session.execute(text('SELECT * FROM users'))
        rows = result.fetchall()
        for row in rows:
            print(row)

        #delete
        name = "Максим"
        await session.execute(
            text("DELETE FROM users WHERE name = $1"),
            (name,)
        )
        await session.commit()

        result = await session.execute(text('SELECT * FROM users'))
        rows = result.fetchall()
        for row in rows:
            print(row)

asyncio.run(main())