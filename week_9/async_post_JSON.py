import aiohttp
import asyncio
from asyncio import Semaphore
import json

async def create_post(session, num, sem):
    payload = {
        "title": f"Заголовок {num}",
        "body": f"Текст {num}",
        "userId": 1
    }
    async with sem:
        async with session.post("https://jsonplaceholder.typicode.com/posts", json=payload) as resp:
            data = await resp.json()
            post_id = data["id"]
            print(f"Пост {num}: создан с id = {post_id}")
            return post_id
        
async def main():
    sem = Semaphore(3)

    async with aiohttp.ClientSession() as session:
        tasks = [create_post(session, i, sem) for i in range(1, 16)]
        results = await asyncio.gather(*tasks)

    with open("post_ids.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"Сохранено {len(results)} id в post_ids.json")

asyncio.run(main())