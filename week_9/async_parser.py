import asyncio
import aiohttp
from asyncio import Semaphore

async def fetch_url(session, url, num, sem):
    timeout = aiohttp.ClientTimeout(
        total=10,
        connect=5
    )
    for attempt in range(1, 4):
        try:
            async with sem:
                async with session.get(url, timeout=timeout) as resp:
                    resp.raise_for_status()
                    status = resp.status
                    print(f"Запрос {num}: статус {status}")
                    return url, status
        except asyncio.TimeoutError:    
            print(f"Запрос {num}: таймаут (попытка{attempt})")
        except aiohttp.ClientResponseError as e:
            print(f"Запрос {num}: HTTP {e.status} (попытка{attempt})")
        except aiohttp.ClientConnectionError:
            print(f"Запрос {num}: не подключиться (попытка{attempt})")
        await asyncio.sleep(1)
    return url, None

async def main():
    errors = 0
    correct = 0 
    urls = [
        "https://httpbin.org/get",           # 200
        "https://ya.ru",                     # 200
        "https://google.com",                # 200
        "https://github.com",                # 200
        "https://stackoverflow.com",         # 200
        "https://vk.com",                    # 200
        "https://mail.ru",                   # 200
        "https://python.org",                # 200
        "https://pypi.org",                  # 200
        "https://httpbin.org/status/404",    # 404 Not Found
        "https://httpbin.org/status/500",    # 500 Internal Error
        "https://httpbin.org/delay/10",      # таймаут
        "https://notexist-site-12345.ru",    # не резолвится
        "http://localhost:8888",             # отказ в соединении
        "https://httpbin.org/get?test=1",    # 200 (дополнительная рабочая)
    ]
    sem = Semaphore(4)


    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url, i, sem) for i, url in enumerate(urls, 1)]
        results = await asyncio.gather(*tasks)

    for url, status in results:
        if not status: 
            errors += 1
        else:
            correct += 1
    print(f"\nВсего выполнено {len(results)} запросов\n",
        f"Успешных запросов: {correct}\n",
        f"Ошибок: {errors}\n")

asyncio.run(main())
