#!/usr/bin/env python3
"""module returns a tuple with arguments"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    arguments:
        k - str type
        v - int or float type
    returns: tuple
    """

    x: Tuple[str, float] = (k, v*v)
    return x
