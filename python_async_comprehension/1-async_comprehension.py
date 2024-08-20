#!/usr/bin/env python3
"""
async comprehensions
"""

import asyncio
async_generator = __import__('0-async_generator').async_generator
from typing import List

async def async_comprehension() -> List[float]:
    """
    collects 10 random numbers using async comprehension
    """
    return [num async for num in async_generator()][:10]
