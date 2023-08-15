#!/usr/bin/python3
import hidden_4


def print_names():
    hidden_names = dir(hidden_4)
    filter_names = [name for name in hidden_names if not name.startswith("__")]
    sorted_names = sorted(filter_names)

    for name in sorted_names:
        print(name)
