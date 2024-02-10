#!/usr/bin/python3
"""a Class"""
import json


class Base:
    """a Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """a constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is not None or list_dictionaries != []:
            return json.dumps(list_dictionaries)
        return "[]"
