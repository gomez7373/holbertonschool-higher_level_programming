#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)  # Fetch the next item from the iterator
        self.count += 1             # Increment the counter
        return item

    def get_count(self):
        return self.count           # Return the current count

    def __iter__(self):
        return self                 # Make this object an iterator itself
