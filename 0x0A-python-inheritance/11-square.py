#!/usr/bin/python3
"""multi inhinherits"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square"""

    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
