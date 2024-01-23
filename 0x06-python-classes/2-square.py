#!/usr/bin/python3
"""Square Class

Empty class Square that defines a square

"""


class Square:
    """A Square"""

    def __init__(self, size=0):
        """Instantiation of square
            Args:
                size (int): the size of the square
        """
        if type(size) is not int:
            raise TypeErrorr("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
