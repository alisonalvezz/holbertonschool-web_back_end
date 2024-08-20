#!/usr/bin/env python3
"""
simple helper function
"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start and ending index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters
    Parameters:
        page(int): The page number (-1 indexed)
        page_size(int): The number of items per page
    Returns:
        a tuple containing the start index and the end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
