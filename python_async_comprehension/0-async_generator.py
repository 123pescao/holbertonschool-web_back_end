#!/usr/bin/env python3
"""
Module creates a coroutine called async_generator
that takes no arguments. The coroutine loops 10 times,
each time asynchronously waiting 1 second, then yields
a random number between 0 and 10.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times, waiting 1 second each time, then
    returns a float"""
    for i in range(10):
        yield random.uniform(0.0, 10.0)
        await asyncio.sleep(1)
