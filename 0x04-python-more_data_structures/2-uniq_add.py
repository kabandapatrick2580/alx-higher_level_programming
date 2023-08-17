#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_sum = 0
    seen = set()  # To keep track of seen integers

    for num in my_list:
        if num not in seen:
            unique_sum += num
            seen.add(num)

    return unique_sum
