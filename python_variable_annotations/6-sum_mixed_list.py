#!/usr/bin/env python3
"""
sum mixed list
"""

from typing import List, Union


def sum_mixed_list(mdx_list: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats and sums it
    Attributes:
        mdx_list: list of integers and floats
    Returns: 
        the sum of mdx_list as a float
    """
    return sum(mdx_list)
