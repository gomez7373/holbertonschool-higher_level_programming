#!/usr/bin/python3
"""
   Class MyList that inherits from list that contain \
   Public instance method: def print_sorted(self): that \
   prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """Class MyList inherits from list"""
    def print_sorted(self):
        """Prints list, sorted (ascending)"""
        print(sorted(self))
