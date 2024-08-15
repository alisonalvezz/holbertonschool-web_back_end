#!/usr/bin/env python3
"""
type annotated function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that takes a str 'k' and and int or float 'v'
    Attributes:
        k: str
        v: float or int
    Returns:
        A tuple
    """
    return k, v * v
