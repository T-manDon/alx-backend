#!/usr/bin/env python3
"""
Contains the Server class with methods to create simple pagination from CSV data.
"""

import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Reads the CSV file and caches the dataset.
        
        Returns:
            List[List]: A list of lists representing the dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    @staticmethod
    def assert_positive_integer_type(value: int) -> None:
        """
        Asserts that the provided value is a positive integer.
        
        Args:
            value (int): The integer to be validated.
        """
        assert type(value) is int and value > 0

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of the dataset based on the page number and page size.
        
        Args:
            page (int): The page number, must be a positive integer.
            page_size (int): The number of records per page, must be a positive integer.
        
        Returns:
            List[List]: A list of records for the requested page.
        """
        self.assert_positive_integer_type(page)
        self.assert_positive_integer_type(page_size)
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        try:
            data = dataset[start:end]
        except IndexError:
            data = []
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieves a dictionary containing pagination details for the dataset.
        
        Args:
            page (int): The page number, must be a positive integer.
            page_size (int): The number of records per page, must be a positive integer.
        
        Returns:
            dict: A dictionary containing the current page data and metadata:
                  - page (int): The current page number.
                  - page_size (int): The actual number of records on the page.
                  - total_pages (int): The total number of pages.
                  - data (List[List]): The data for the current page.
                  - prev_page (int or None): The previous page number or None if on the first page.
                  - next_page (int or None): The next page number or None if on the last page.
        """
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        info = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": total_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= total_pages else None
        }
        return info
