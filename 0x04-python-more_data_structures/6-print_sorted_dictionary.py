#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = a_dictionary.copy()
    keys = list(dic.keys())
    keys.sort()
    sdic = {i: dic[i] for i in keys}
    for key, value in sdic.items():
        print(f"{key}: {value}")
