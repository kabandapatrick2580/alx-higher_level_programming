#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string


if __name__ == "__main__":
    string = ("You can't c me")
    new_string = no_c(string)
    print(new_string)
