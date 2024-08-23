#!/usr/bin/env python3
"""
async generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    a coroutine async_generator
    loops 10 times, each time waits 1 second
    then yield a random number btw 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
