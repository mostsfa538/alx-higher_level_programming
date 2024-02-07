#!/usr/bin/python3
"""a class"""


class Student:
    """a class"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        if attrs is None:
            return (self.__dict__)
        else:
            dict = {}
            for i in attrs:
                if hasattr(self, i):
                    dict[i] = getattr(self, i)
            return dict
