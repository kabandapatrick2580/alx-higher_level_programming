#!/usr/bin/python3
alphabet = ""
for letter in range(ord('a'), ord('{'), +1):
    if chr(letter) in ['e', 'q']:
        continue
    alphabet += chr(letter)
print(f"{alphabet}", end="")
