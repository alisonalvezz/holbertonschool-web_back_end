#!/usr/bin/env python3
from typing import List
"""
Type-annotated sum_list
"""


def sum_list(input_list: List[float]) -> float:
    """
    Type-annotated sum_list which takes a input list of floats
    Attributes:
        input_list: list of floats
    Returns:
        the sum of the arguments of input_list
    """
    return sum(input_list)
