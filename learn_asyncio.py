# -*- coding: utf-8 -*-
import asyncio
import time
import functools


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # Schedule three calls *concurrently*:
    print(f"Start: {time.strftime('%X')}")
    ret = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(f"Gather return: {ret}")
    print(f"End: {time.strftime('%X')}")


asyncio.run(main())

