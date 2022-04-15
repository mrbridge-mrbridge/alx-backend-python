#!/usr/bin/env python3
"""module augments a function with type annotation"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')
X = Union[Any, T]
Y = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Y = None) -> X:
    """return value with key or return None"""

    if key in dct:
        return dct[key]
    else:
        return default
