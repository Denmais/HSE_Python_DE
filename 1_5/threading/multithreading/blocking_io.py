import asyncio
import requests
import aiohttp
import time


def timed(func):
    async def inner(*args, **kwargs):
        t0 = time.time()
        await func(*args, **kwargs)
        print(time.time() - t0)
    return inner


async def some_network_activity():
    resp = requests.get('https://ya.ru')
    print(resp)


async def some_async_network_activity():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://ya.ru') as resp:
            print(resp.status)


@timed
async def main():
    await asyncio.gather(*[some_async_network_activity() for _ in range(10)])

if __name__ == '__main__':
    asyncio.run(main())