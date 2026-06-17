import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(
        user="postgres",
        password="1234",
        database="testdb",
        host="localhost",
        port=5432
    )
    users = [
        ("Максим", 20),
        ("Ксюша", 18),
        ("Саша", 14)
    ]

    # 1. CREATE
    await conn.executemany("INSERT INTO users (name, age) VALUES ($1, $2)", users)
    # 2. READ ALL
    rows = await conn.fetch("SELECT * FROM users")
    for row in rows:
        print(row)
    # 3. UPDATE
    await conn.execute("UPDATE users SET age = $1 WHERE id = $2", 21, 1)
    
    # 4. READ ALL (проверить обновление)
    rows = await conn.fetch("SELECT * FROM users")
    for row in rows:
        print(row)
    # 5. DELETE
    await conn.execute("DELETE FROM users WHERE name = $1", "Максим")
    # 6. READ ALL (проверить удаление)
    rows = await conn.fetch("SELECT * FROM users")
    for row in rows:
        print(row)

    await conn.close()


asyncio.run(main())