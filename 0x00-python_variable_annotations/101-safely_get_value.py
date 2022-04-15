#!/usr/bin/env python3
"""module augments a function with type annotation"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')
X = Union[Any, T]

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> X:
    """return dct key or return None"""

    if key in dct:
        return dct[key]
    else:
        return default
