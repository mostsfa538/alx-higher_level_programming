#!/usr/bin/python3
"""Write"""


def write_file(filename="", text=""):
    """Write file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        print(f.write(text))
