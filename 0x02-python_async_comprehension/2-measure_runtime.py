#!/usr/bin/env python3
"""coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine to measure the total runtime of executing
    async_comprehension four times in parallel
    """
    start_time = asyncio.get_event_loop().time()

    # Execute async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    runtime = end_time - start_time
    return runtime
