#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    size = len(sys.argv) - 1
    if size != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    sign = sys.argv[2]
    b = int(sys.argv[3])

    if sign == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif sign == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif sign == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif sign == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
