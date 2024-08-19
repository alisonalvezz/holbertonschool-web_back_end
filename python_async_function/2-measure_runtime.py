#!/usr/bin/env python3
"""
measure the runtime
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the time of execution of wait_n
    """
    total_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - total_time) / n
