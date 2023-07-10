#!/usr/bin/env python3
"""Execute multiple coroutines"""
import asyncio
from heapq import nsmallest
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return nsmallest(n, delays)
