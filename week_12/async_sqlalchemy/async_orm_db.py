import asyncio
from sqlalchemy import text, update, bindparam
from async_model import User, AsyncSessionLocal

async def print_all_users(session, status: str) -> str:
    result = await session.execute(text('SELECT * FROM users'))
    rows = result.fetchall()
    print("\n", "="*20, f" {status} ", "="*20)
    for row in rows:
        print(row)
    print("="*45, "\n")

async def main():
    users = [
        User(name="Салуки", age=25),
        User(name="Бредишь", age=27)
        ]
    
    async with AsyncSessionLocal() as session:
        
        #============= CREATE
        session.add_all(users)
        await session.commit()

        await print_all_users(session, "СREATE")

        #============= UPDATE
        keys = ["age", "name"]
        data = [[99, "Салуки"], [40, "Бредишь"]]

        upd_gen = [{key: row[i] for i, key in enumerate(keys)} for row in data]

        await session.execute(
            text('UPDATE users SET age = :age WHERE name = :name'),
                upd_gen
        )
        await session.commit()

        # stmt = update(User).where(User.name == bindparam("name")).values(age=bindparam("age"))
        # await session.execute(stmt, [{"name": "Салуки", "age": 99}, {"name": "Бредишь", "age": 40}])
        # await session.commit()

        await print_all_users(session, "UPDATE")

        #============= DELETE
        await session.execute(
            text('DELETE FROM users WHERE name = :name'),
            {"name": "Салуки"}
        )
        await session.commit()
        await print_all_users(session, "DELETE")

if __name__ == "__main__":
    asyncio.run(main())