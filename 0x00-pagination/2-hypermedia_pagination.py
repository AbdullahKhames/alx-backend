#!/usr/bin/env python3
"""module to write simple pagination"""
from typing import List, Tuple, Dict, Any
import csv
import math


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
        """implementing Simple pagination
        """
        assert (
                isinstance(page, int)
                and isinstance(page_size, int)
                and page > 0
                and page_size > 0
        )

        total_items = len(self.dataset())
        if total_items / page_size < page:
            return []

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Hypermedia as the engine of application state (HATEOAS)
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        total_items = len(self.dataset())
        total_pages = total_items / page_size
        return {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': None if page == total_pages else page + 1,
            'prev_page': None if page == 1 else page - 1,
            'total_pages': total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function to calculate start and end indexes"""
    start = (page - 1) * page_size
    return start, start + page_size
