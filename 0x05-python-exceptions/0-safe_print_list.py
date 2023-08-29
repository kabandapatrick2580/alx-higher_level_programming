#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for m in my_list:
            if counter < x:
                print(m, end="")
                counter += 1
        print()
        return counter

    except Exception as d:
        print(f"An error occurred while printing the list: {d}")
