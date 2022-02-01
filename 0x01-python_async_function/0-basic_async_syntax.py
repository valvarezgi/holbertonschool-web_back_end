#!/usr/bin/env python3
"""wait_random module"""
import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """wait random number
    Args:
        max_delay (int, optional): max number. Defaults to 10.
    Returns:
        float: random float number
    """

    wait_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
