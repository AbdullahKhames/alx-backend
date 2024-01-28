#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_page(self, index: int = 1, page_size: int = 10) -> Dict:
        """implementing Simple pagination
        """
        assert (
                isinstance(index, int)
                and isinstance(page_size, int)
                and index > 0
                and page_size > 0
        )
        dataset = {}
        i = 0
        while i < page_size:
            if index not in self.indexed_dataset().keys():
                index += 1
                continue
            val = self.indexed_dataset()[index]
            index += 1
            if not val:
                continue
            dataset[index] = val
            i += 1

        return dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Hypermedia as the engine of application state (HATEOAS)
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        assert index < list(self.indexed_dataset().keys())[-1]
        index = 0 if index is None else index
        data = self.get_page(index, page_size)
        return {
            'index': index,
            'next_index': list(data.keys())[-1],
            'page_size': len(data),
            'data': data,
        }
