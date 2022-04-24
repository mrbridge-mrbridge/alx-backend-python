#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """return average runtime"""
    start = time.perf_counter()
    asyncio.gather(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return (elapsed / n)
