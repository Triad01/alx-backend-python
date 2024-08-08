#!/usr/bin/env python3
"""module for task 0
"""
import asyncio
import random


async def async_generator():
    """defines a coroutine
        that returns random float numbers
    """
    for i in range(10):
        await asyncio.sleep(1)
        number = random.uniform(0, 10)
        yield number
