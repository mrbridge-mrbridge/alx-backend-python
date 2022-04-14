#!/usr/bin/env python3
"""module returns sum of list elements"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    arguments:
        input_list - list of floats
    returns: sum of elements as float
    """

    ln = len(input_list)
    summ = 0
    for i in range(ln):
        summ += input_list[i]
    return summ
