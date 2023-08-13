#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for n in range(len(my_list)-1, -1, -1):
            print(f"{my_list[n]:d}")
