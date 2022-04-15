#!/usr/bin/env python3
"""function annotation"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    arguments:
        lst - of type iterable of sequence
    returns: A list of tuples of sequence and int
    """

    return [(i, len(i)) for i in lst]
