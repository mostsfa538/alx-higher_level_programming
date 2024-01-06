#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nlist = []
    for i in my_list:
        nlist.append(True if i % 2 == 0 else False)
    return nlist
