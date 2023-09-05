#!/usr/bin/env python3
"""Copy index_range from the previous task and the
following class into your code"""
import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """You have to use this CSV file (same as the one
        presented at the top of the project)
        Use assert to verify that both arguments are integers greater than
        0.
        Use index_range to find the correct indexes to paginate the
        dataset correctly and return the appropriate page of the dataset
        (i.e. the correct list of rows).
        If the input arguments are out of range for the dataset, an empty
        list should be returned."""
        index_range = __import__('0-simple_helper_function').index_range
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0
        result: Tuple = index_range(page, page_size)
        self.dataset()
        return self.__dataset[result[0]:result[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        """Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary containing the
        following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        Make sure to reuse get_page in your implementation."""
        data: List = self.get_page(page, page_size)
        total_pages: int = len(self.dataset())
        if page < total_pages:
            next_page: int = page + 1
        else:
            next_page: List = None
        if page > 1:
            prev_page: int = page - 1
        else:
            prev_page: List = None
        dic = {'page_size': page_size, 'page': page, 'data': data,
               'next_page': next_page, 'prev_page': prev_page,
               'total_pages': total_pages}
        return dic
