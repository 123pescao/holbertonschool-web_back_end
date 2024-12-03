#!/usr/bin/env python3
"""
Module annotates a function element_length that takes
an iterable of sequences and returns a list of tuples
containing each sequence and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing each sequence and its length"""
    return [(i, len(i)) for i in lst]
