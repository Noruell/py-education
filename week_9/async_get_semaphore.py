import aiohttp
import asyncio
from asyncio import Semaphore

async def fetch_url(session, url, num, sem):
    async with sem:
        async with session.get(url) as resp:
            status = resp.status
            print(f"Запрос {num}: статус {status}")
            return url, status

async def main():
    urls = ["https://httpbin.org/get"] * 20
    sem = Semaphore(3)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url, i, sem) for i, url in enumerate(urls, 1)]
        results = await asyncio.gather(*tasks)

    print(f"\nВсего выполнено {len(results)} запросов")

asyncio.run(main())
