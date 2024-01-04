#!/usr/bin/python3
import sys
if __name__ == "__main__":
    size = len(sys.argv) - 1
    if size == 0:
        print(0)
    else:
        i = 1
        calc = 0
        while i <= size:
            calc += sys.argv[i]
            i += 1
        print(calc)
