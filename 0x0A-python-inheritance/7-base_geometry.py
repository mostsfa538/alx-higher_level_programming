#!/usr/bin/python3
"""a Class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """vaildator"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(value))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(value))
