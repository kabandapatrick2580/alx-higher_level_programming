#!/usr/bin/python3
for letter in range(ord('a'), ord('{'), +1):
    if chr(letter) in ['e', 'q']:
        continue
    print("{}".format(chr(letter)), end="")
