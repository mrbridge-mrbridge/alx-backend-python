#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns a sorted list of waiting times"""
    y: List[float] = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(y)
