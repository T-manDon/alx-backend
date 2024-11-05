#!/usr/bin/env python3
"""
Provides a class for deletion-resilient pagination of CSV data.
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a dataset of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Loads the dataset from the CSV file and caches it.
        
        Returns:
            List[List]: The dataset, with each row as a list of values.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Excludes the header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Creates a dictionary of dataset items indexed by their original position.
        
        Returns:
            Dict[int, List]: A mapping of index positions to dataset rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves paginated data starting from a specific index, allowing for
        deletion-resilience by skipping missing records.
        
        Args:
            index (int): The starting index for the page.
            page_size (int): The number of records per page.
        
        Returns:
            Dict: Contains pagination information and page data, including:
                  - index (int): The starting index of this page.
                  - next_index (int or None): The starting index for the next page,
                    or None if no more data.
                  - page_size (int): The number of items on this page.
                  - data (List[List]): The list of records for this page.
        """
        dataset = self.indexed_dataset()
        data_length = len(dataset)
        assert 0 <= index < data_length
        response = {}
        data = []
        response['index'] = index
        for i in range(page_size):
            while True:
                curr = dataset.get(index)
                index += 1
                if curr is not None:
                    break
            data.append(curr)

        response['data'] = data
        response['page_size'] = len(data)
        response['next_index'] = index if dataset.get(index) else None
        return response
