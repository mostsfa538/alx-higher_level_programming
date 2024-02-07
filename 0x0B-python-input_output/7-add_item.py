#!/usr/bin/python3
"""import sys and json"""
from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

"""script that adds all arguments to a Python list
and then save them to a file
"""

try:
    items = load_from_json_file('add_item.json')
    save_to_json_file(items + argv[1:], 'add_item.json')
except Exception:
    save_to_json_file(argv[1:], 'add_item.json')
