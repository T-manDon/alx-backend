#!/usr/bin/env python3
"""
Defines the index_range helpercode  function
"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Acquires two int argmts to  return tuple of size two
    with the start and end index corresponding with the  index rang
    indexes to list pagination parameters
    Args:
        page (int): page number to return (pages are 1-indexed)
        page_size (int): number of items per page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0

    for i in range(page):

        start = end
        end += page_size

    return (start, end)
