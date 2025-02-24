#!/usr/bin/env python3
"""This file contains Server class"""
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
        """this function gets the page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = self.index_range(page, page_size)
        data = self.dataset()
        if start_index >= len(data):
            return []

        return data[start_index:end_index]

    @staticmethod
    def index_range(page, page_size) -> Tuple[int, int]:
        """this function returns a tuple with the start and end indexes"""
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """This function returns a dict with info of the page"""
        # Validate the input
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Calculate index range and fetch the page data
        start_index, end_index = self.index_range(page, page_size)
        page_data = self.get_page(page, page_size)

        # Calculate total pages
        total_items = len(self.dataset())
        total_pages = math.ceil(
            total_items / page_size) if page_size > 0 else 0

        # Determine the next and previous page numbers
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Return the hypermedia response
        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
