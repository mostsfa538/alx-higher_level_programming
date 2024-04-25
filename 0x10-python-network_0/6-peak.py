#!/usr/bin/python3
"""here goes every thing"""


def find_peak(list_of_integers):
    """
        the peak is an element that is
        greater than or equal to its neighboring elements
    """
    if len(list_of_integers) == 0:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
