#!/usr/bin/python3
"""The function"""


class MyList(list):
    """The class that  that inherits from list"""
    def print_sorted(self):
        """"prints the list, but sorted (ascending sort)"""
        print(sorted(self))
