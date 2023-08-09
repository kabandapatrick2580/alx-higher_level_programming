#!/usr/bin/python3
def uppercase(str):
    for charac in str:
        if ord(charac) >= 97 or ord(charac) <= 122:
            charac = chr(ord(charac) - 32)
        print("{}".format(charac), end="")
    print("")
