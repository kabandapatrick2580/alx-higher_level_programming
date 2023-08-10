#!/usr/bin/python3
import sys


def arguments_sum(args):
    result = sum(map(int, args))
    return result


arguments = sys.argv[1:]
summation = arguments_sum(arguments)
print(summation)
