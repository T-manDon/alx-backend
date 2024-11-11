#!/usr/bin/env python3
""" Module to BaseCach
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Function describes a cache class in the key-value pairs
    Methods:
        put(key, item) - stores the key value pairs
        get(key) - returns the key value
    """

    def __init__(self):
        """
        Func to initiate parent class using the__init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Store a key-value pair
        Args:
            Key
            Item
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the keylinked value.
        If key not exist, return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
