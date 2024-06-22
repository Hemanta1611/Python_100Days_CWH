'''
Asynchronus I/O, or async is a programming pattern that allow for high 
performance I/O operations in a concurrent and non-blocking manner. In Python,
async programming is achieved through the use of the asyncio module and asychronus function.
'''

import asyncio
import time


async def fun1():
    await asyncio.sleep(1)
    print("func 1")

async def fun2():
    await asyncio.sleep(2)
    print("func 2")

async def fun3():
    await asyncio.sleep(4)
    print("func 3")

async def main():
    # await fun1()
    # await fun2()
    # await fun3()
    L = await asyncio.gather(
        fun1(),
        fun2(),
        fun3()
    )
    print(L)


asyncio.run(main())

