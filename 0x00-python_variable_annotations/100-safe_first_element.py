#!/usr/bin/env python3
"""module augments a function with annotations"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns lst[0] or None"""

    if lst:
        return lst[0]
    else:
        return None
