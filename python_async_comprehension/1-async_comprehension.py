#!/usr/bin/env python3
"""
Module creates a coroutine called async_generator
that takes no arguments. The coroutine loops 10 times,
each time asynchronously waiting 1 second,
then yields a random number between 0 and 10.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns a float list"""
    num = [num async for num in async_generator()]
    return num
