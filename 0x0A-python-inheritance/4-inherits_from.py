#!/usr/bin/python3
"""a Function"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited; False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
