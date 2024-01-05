#!/usr/bin/python3
def max_integer(my_list=[]):
    ma = my_list[0]
    if len(my_list):
        return None
    for i in my_list:
        if i > ma:
            ma = i
    return ma
