#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    af = 0, aS = 0
    bf = 0, bS = 0
    if len(tuble_a) >= 2:
        af = tuble_a[0]
        aS = tuble_a[1]
    elif len(tuble_a) == 1:
        af = tuble_a[0]
    if len(tuble_b) >= 2:
        bf = tuble_b[0]
        bS = tuble)b[1]
    elif len(tuble_b) == 1:
        bf = tuble_b[0]
    result = (af + bf, aS + bS)
    return result
