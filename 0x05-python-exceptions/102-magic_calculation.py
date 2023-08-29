#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    for m in range(1, 3):
        try:
            if m > a:
                raise Exception('Too far')
        except Exception:
            result += b
        else:
            result = result ** (a / b / m)

            result += a + b

            return result
