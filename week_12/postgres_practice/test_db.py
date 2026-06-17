import asyncio
import asyncpg

async def connect_and_query():
    conn = await asyncpg.connect(
        user="postgres",
        password="1234",
        database="testdb",
        host="localhost",
        port=5432
    )

    rows = await conn.fetch("SELECT * FROM users")
    for row in rows:
        print(row)

    await conn.close()

asyncio.run(connect_and_query())