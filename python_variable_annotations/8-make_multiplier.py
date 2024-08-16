#!/usr/bin/env python3
"""
make multiplier
"""

from typing import Callable
"""
make multiplier
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that returns a function that multiplies
    Attributes:
        multiplier: the float to multiplicate
    Returns:
        the function mul that multiplicates multiplier by other float
    """

    def mul(mul: float) -> float:
        return mul * multiplier

    return mul
