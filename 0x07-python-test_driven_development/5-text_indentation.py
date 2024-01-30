#!/usr/bin/python3
"""text indeentation"""


def text_indentation(text):
    """the function"""
    if type(text) is not str:
        raise TypeError('text must be a string')

    for char in text:
        if char in ('.', ':', '?', ','):
            print(char)
            print()
        else:
            print(char, end='', flush=True)
