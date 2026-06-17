import asyncio
from sqlalchemy import text, update, bindparam
from week_12.alembic_practice.async_model import User, AsyncSessionLocal

async def print_all_users(session, status: str) -> str:
    result = await session.execute(text('SELECT * FROM users'))
    rows = result.fetchall()
    print("\n", "="*20, f" {status} ", "="*20)
    for row in rows:
        print(row)
    print("="*45, "\n")

async def main():
    async with AsyncSessionLocal() as session:
        await print_all_users(session, "TEST")

asyncio.run(main())