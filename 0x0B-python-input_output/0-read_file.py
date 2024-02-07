#!/usr/bin/python3
"""READ"""


def read_file(filename=""):
    """reade file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end='')
