#!/usr/bin/python3
"""here goes every thing"""


def find_peak(list_of_integers):
    """
        the peak is an element that is
        greater than or equal to its neighboring elements
    """
    if list_of_integers is None:
        return None

    length = len(list_of_integers)
    for i in range(0, length - 1):
        if i == 0 and list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]
        elif list_of_integers[i - 1] <= list_of_integers[i]\
                and list_of_integers[i + 1] <= list_of_integers[i]:
            return list_of_integers[i]
