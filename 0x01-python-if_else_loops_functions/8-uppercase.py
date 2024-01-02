#!/usr/bin/python3
def uppercase(str):
    for c in str:
        flag = 1 if 97 <= ord(c) < 123 else 0
        print("{:c}".format(ord(c) - 32 if flag == 1 else ord(c)), end='')
    print("")
