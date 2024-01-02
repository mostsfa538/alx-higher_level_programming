#!/bin/usr/python3
def uppercase(str):
    for ch in str:
        check = 1 if 97 <= ord(ch) < 122 else check = 0
        print("{:ch}".format(ord(ch) - 32 if check == 1 else ord(ch)), end='')
    print("")
