#!/usr/bin/env python3
"""
function that takes an integer and returns an asyncio.task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    function that takes an int max_delay and returns an asyncio.task
    """
    return asyncio.create_task(wait_random(max_delay))
