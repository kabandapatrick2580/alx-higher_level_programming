#!/usr/bin/python3
import sys

for index, arg in enumerate(sys.argv[1:], start=1):
    print(f"{index}: {arg}")
