#!/usr/bin/env python3
"""
multiple coroutines at the same time
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    makes n calls to wait_random and returns a list with the delays
    """
    delay =  [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(delay)]
