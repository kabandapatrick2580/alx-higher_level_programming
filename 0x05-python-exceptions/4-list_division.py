#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for d in range(list_length):
            try:
                numer = my_list_1[d]
                denom = my_list_2[d]
                if not isinstance(numer, (int, float)) or \
                   not isinstance(denom, (int, float)):
                    raise TypeError("wrong type")
                if denom == 0:
                    raise ZeroDivisionError("division by 0")
                result.append(numer / denom)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except TypeError:
                print("wrong type")
                result.append(0)
            except IndexError:
                print("out of range")
                result.append(0)
    finally:
        return result
