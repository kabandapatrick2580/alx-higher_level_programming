#!/usr/bin/python3
for number in range(0, 99):
    print(f"{number:02d}, ", end="")
    if number == 98:
        print((number) + 1)
