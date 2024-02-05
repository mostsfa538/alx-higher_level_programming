#!/usr/bin/python3
"""a Finction"""


def add_attribute(obj, attribute_name, value):
    """Add a new attribute to an object if possible"""
    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__') and attribute_name in obj.__slots__):
        setattr(obj, attribute_name, value)
    else:
        raise TypeError("can't add new attribute")
