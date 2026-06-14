import asyncio


async def timer(name, seconds):
    await asyncio.sleep(seconds)
    return f"Таймер '{name}' завершился через {seconds} сек"
    
async def main():
    tasks = [
        timer("A", 1),
        timer("B", 4),
        timer("C", 2),
        timer("D", 5)
    ]
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(result)


asyncio.run(main())

