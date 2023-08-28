#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print(f"{value:d}")
        return True
    except Exception as d:
        return False
