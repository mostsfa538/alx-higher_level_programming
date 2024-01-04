#!/usr/bin/python3
import sys
if __name__ == "__main__":
    size = len(sys.argv) - 1
    if size == 0:
        print("0 arguments.")
    else:
        i = 1
        print("{} argument{}:".format(size, 's' if size > 1 else ''))
        while i <= size:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
