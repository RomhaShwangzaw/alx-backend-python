#!/usr/bin/env python3
"""Basic Async Coroutine Module"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Takes in an integer argument (max_delay, with a default value of 10)
    that waits for a random delay between 0 and max_delay (included and
    float value) seconds and eventually returns it.
    """
    delay = random.uniform(0.0, max_delay + 1)
    await asyncio.sleep(delay)
    return delay
