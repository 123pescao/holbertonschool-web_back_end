#!/usr/bin/env python3
"""
Module creates a function named index_range that
takes two integer arguments page and page_size. The
function should return a tuple of size two containing
a start index and an end index corresponding to the
range of indexes to return in a list for those
particular pagination parameters.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Returns a tuple containing start and end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
