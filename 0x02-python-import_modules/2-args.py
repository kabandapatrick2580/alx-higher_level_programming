#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    # Subtract 1 to exxclude the script name
    argv_len = len(sys.argv) - 1

    if argv_len == 0:
        print("0 arguments.")
    elif argv_len == 1:
        print("1 argument:")
    else:
        print(f"{argv_len} arguments:")
    for index, arg in enumerate(sys.argv[1:], start=1):
        print(f"{index}: {arg}")
