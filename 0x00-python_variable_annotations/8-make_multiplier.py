#!/usr/bin/env python3
"""module multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    arguments:
        multiplier - floating type
    returns: a Callable function
    """

    return (lambda x: x * multiplier)
