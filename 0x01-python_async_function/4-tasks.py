#!/usr/bin/env python3
"""Execute multiple coroutines"""
import asyncio
from heapq import nsmallest
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return nsmallest(n, delays)
