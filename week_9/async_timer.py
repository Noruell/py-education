import asyncio
import time

async def timer(name, seconds):
    await asyncio.sleep(seconds)
    print(f"Таймер '{name}' сработал через {seconds} сек")

async def main():
    await asyncio.gather(
        timer("средний", 3),
        timer("короткий", 1),
        timer("длинный", 5)
    )

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    result = time.time() - start
    print(f"Общее время: {round(result, 2)} сек")