#!/usr/bin/python3

def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
