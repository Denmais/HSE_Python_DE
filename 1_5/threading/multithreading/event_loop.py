import asyncio
from asyncio import sleep

async def waiter_1():
    print("Hi to all from waiter 1")
    await sleep(2)
    print("Bye all from waiter 1")

async def waiter_2():
    await sleep(0.5)
    print("Hi to all from waiter 2")
    await sleep(2)
    print("Bye all from waiter 2")

async def waiter_3():
    await sleep(1)
    print("Hi to all from waiter 3")
    await sleep(2)
    print("Bye all from waiter 3")


async def main():
    asyncio.create_task(waiter_1())
    asyncio.create_task(waiter_2())
    await asyncio.create_task(waiter_3())

if __name__ == '__main__':
    asyncio.run(main())