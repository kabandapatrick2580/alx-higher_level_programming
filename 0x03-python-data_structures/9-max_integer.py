#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None  # Base case: empty list

    # Base case: list with only one element
    if len(my_list) == 1:
        return my_list[0]

    # Recursive case: compare the first element with the maximum of the rest of the list
    else:
        rest_max = max_integer(my_list[1:])
        return my_list[0] if my_list[0] > rest_max else rest_max
