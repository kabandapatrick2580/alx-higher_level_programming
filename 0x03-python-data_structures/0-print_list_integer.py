#!/usr/bin/python3
def print_list_integer(my_list=[]):

    for i, n in enumerate(my_list):
        print("{}".format(n))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
