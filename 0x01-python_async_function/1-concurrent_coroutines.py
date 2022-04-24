#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """returns a sorted list of waiting times"""
    y: list[float] = [await wait_random(max_delay) for _ in range(n)]
    return y
