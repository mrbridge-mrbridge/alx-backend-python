#!/usr/bin/env python3
"""basics of async"""
import asyncio
import random

async def wait_random(max_delay=10):
    """returns random value"""
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
