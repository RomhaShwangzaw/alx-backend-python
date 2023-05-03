#!/usr/bin/env python3
"""Measure Runtime Module"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather,
    then measures the total runtime it took and returns the result.
    """
    s = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    total_time = time.perf_counter() - s
    return total_time
