#!/usr/bin/env python3
"""
insert variable annotations
"""

from typing import Sequence, Iterable, List, Tuple

def element_length(lst: Iterable[Sequence]) ->List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with their sequence and longitude
    """
    return [(i, len(i)) for i in lst]
