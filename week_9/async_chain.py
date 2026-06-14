import asyncio
import aiohttp
from asyncio import Semaphore
import json

async def fetch_users(session):
    """Получает список пользователей"""
    async with session.get("https://jsonplaceholder.typicode.com/users") as resp:
        return await resp.json()

async def fetch_posts_count(session, user_id, sem):
    """Получает количество постов для одного пользователя"""
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    async with sem:
        async with session.get(url) as resp:
            posts = await resp.json()
            return len(posts)

async def main():
    sem = Semaphore(5)
    
    async with aiohttp.ClientSession() as session:
        # 1. Получаем всех пользователей
        users = await fetch_users(session)
        
        # 2. Создаём задачи для каждого пользователя
        tasks = []
        for user in users:
            task = fetch_posts_count(session, user['id'], sem)
            tasks.append(task)
        
        # 3. Запускаем все задачи параллельно (Semaphore ограничит до 5)
        posts_counts = await asyncio.gather(*tasks)
        
        # 4. Выводим результат и сохраняем в JSON
        result = []
        for user, count in zip(users, posts_counts):
            print(f"Пользователь {user['name']}: {count} постов")
            result.append({"name": user['name'], "posts": count})
        
        with open("user_posts.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

asyncio.run(main())