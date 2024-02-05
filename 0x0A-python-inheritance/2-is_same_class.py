#!/usr/bin/python3
"""a Function"""


def is_same_class(obj, a_class):
    """returns True if the object is same class, False"""
    if type(obj) is a_class:
        return True
    else:
        return False
