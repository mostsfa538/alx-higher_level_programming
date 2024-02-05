#!/usr/bin/python3
"""inherits"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""

    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width

    def area(self):
        """calc the area"""
        return self.__height * self.__width

    def __str__(self):
        """returns the rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
