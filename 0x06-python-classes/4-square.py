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
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """return size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Instantiation of size
            Args:
                value (int): the value of size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
