#!/usr/bin/env python3
"""module returns sum of mixed list elements"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    arguments:
        mxd_lst - List of Union of int and float
    returns: sum of all list elements as float type
    """

    ln = len(mxd_lst)
    summ = 0
    for i in range(ln):
        summ += mxd_lst[i]
    return summ
