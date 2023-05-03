#!/usr/bin/env python3
"""Async Comprehension Module"""
from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [n async for n in async_generator()]
