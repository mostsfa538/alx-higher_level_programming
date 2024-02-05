#!/usr/bin/python3
"""a function"""


class MyInt(int):
    """inherits from int with inverted == and != operators"""

    def __eq__(self, other):
        """inverts == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """inverts != operator"""
        return super().__eq__(other)
