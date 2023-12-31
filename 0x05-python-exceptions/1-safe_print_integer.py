#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print(f"{int(value):d}")
        return True
    except (TypeError, ValueError):
        return False
