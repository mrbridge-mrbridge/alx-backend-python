#!/usr/bin/env python3
"""basics of async"""
import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """returns random value"""
    rand: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
