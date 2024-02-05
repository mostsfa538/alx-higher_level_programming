#!/usr/bin/python3
"""Multi inherits"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square"""

    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
