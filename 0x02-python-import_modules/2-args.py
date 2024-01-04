#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv) - 1
    if length == 0:
        printt("0 arguments.")
    else:
        i = 1
        print("{0} {1}:".format(length, 's' if length > 1 else ''))
        while i <= length:
            print("{0}: (1}".format(i, sys.argv[i]))
            i += 1
