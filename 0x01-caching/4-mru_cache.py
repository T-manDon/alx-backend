#!/usr/bin/env python3
"""Modules to BaseCache
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Func FIFOCache to describe the FIFO cache syst
    """

    def __init__(self):
        """
        Initiates parents class using init method
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Caches the key-value pair
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[-1]))
                del self.cache_data[self.usage[-1]]
                del self.usage[-1]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Gives key value, or None
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None
