#!/usr/bin/env python3
"""
simple pagination
"""

from typing import Tuple, List
import csv
import math


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        init
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        method that takes two int args
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        method that takes the same arguments as get_page and returns
        a dictionary
        Args:
            page: the page number
            page_size: the number of items per page
        Returns:
        A dictionary containing:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from get_page)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an int
        """
        data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) / page_size
        if len(self.dataset()) % page_size:
            total_pages += 1
        page_size = len(data)
        next_page = page + 1 if page + 1 < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": int(total_pages)
        }
