#!/usr/bin/env python3
"""Module includes asynchronous coroutines for task 0
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function takes in an integer as argument that waits
    for a random delay.

    Args:
        max_delay (int): Maximum delay time in seconds.

    Returns:
        float: The actual delay time.
    """
    delay_time = random.random() * max_delay
    await asyncio.sleep(delay_time)
    return delay_time
