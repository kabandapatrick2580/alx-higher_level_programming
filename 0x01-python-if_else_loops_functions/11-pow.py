#!/usr/bin/python3
def pow(a, b):
    power = 1
    for _ in range(b):
        power *= a
    return power
