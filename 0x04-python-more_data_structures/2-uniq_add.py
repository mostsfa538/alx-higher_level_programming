#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni = []
    for i in my_list:
        if i not in uni:
            uni.append(i)
    sum = 0
    for i in uni:
        sum += i
    return sum
