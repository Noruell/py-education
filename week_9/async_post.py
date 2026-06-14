import aiohttp
import asyncio
async def post_data():
    async with aiohttp.ClientSession() as session:
        payload = {"name": "Максим", "age": 25}
        async with session.post("https://httpbin.org/post", json=payload) as resp:
            result = await resp.json()
            print(result)

asyncio.run(post_data())