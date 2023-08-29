#!/usr/bin/env python3
"""Import wait_random from the previous python file that you’ve
written and write an async routine called wait_n that takes in
2 int arguments (in this order): n and max_delay. You will spawn
wait_random n times with the specified max_delay."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """making the function"""
    lista: List[float] = []
    for x in range(0, n):
        lista.append(await(wait_random(max_delay)))
    return sorted(lista)
