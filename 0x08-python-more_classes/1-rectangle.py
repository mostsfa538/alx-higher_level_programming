#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """A Rectangle"""

    def __init__(self, width=0, height=0):
        """constructor"""
        self.__width = width
        self.__height = height


    @width.setter
    def width(self, value):
        """set width"""
        if type(self.__width) is not int:
            raise TypeError('width must be an integer')

        if self.__width < 0:
            raise ValueError('width must be >= 0')
        self.__width = value


    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @height.setter
    def height(self, value):
        """set height"""
        if type(self.__height) is not int:
            raise TypeError('height must be an integer')

        if self.__height < 0:
            raise ValueError('height must be >= 0')
        self.__height = value


    @property
    def height(self):
        """retrieve height"""
        return self.__height
