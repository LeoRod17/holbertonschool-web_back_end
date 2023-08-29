#!/usr/bin/env python3
"""Import async_generator from the previous task and then write a
coroutine called async_comprehension that takes no arguments.
The coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random
numbers."""
import asyncio
from typing import Generator
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """doing the function"""
    t1 = time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    t2 = time()
    tf = t2 - t1
    return tf
