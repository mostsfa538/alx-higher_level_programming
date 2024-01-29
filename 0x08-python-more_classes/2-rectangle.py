#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """A Rectangle"""

    def __init__(self, width=0, height=0):
        """constructor"""
        
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

        self.__width = width

        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

        self.__height = height

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
    
    def area(self):
        """return area"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter"""
        return 2 * (self.__width + self.__height)
