#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_mult = []
    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            is_mult.append(True)
        else:
            is_mult.append(False)
    return is_mult
