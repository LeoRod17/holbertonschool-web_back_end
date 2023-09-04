import csv
import math
from typing import List, Tuple


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
