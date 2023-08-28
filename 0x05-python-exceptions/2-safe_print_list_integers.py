#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for m in range(x):
            if isinstance(my_list[m], int):
                print("{:d}".format(my_list[m]), end="")
                counter += 1
    except IndexError:
        raise Exception("An exception occurred. The value of 'x' is"
                        "larger than the length of 'my_list'.")
    else:
        print()
    return counter
