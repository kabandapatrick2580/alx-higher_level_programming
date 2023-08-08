#!/usr/bin/python3
for numb_one in range(10):
    for numb_two in range(numb_one+1,10):
        if numb_one == 8 and numb_two == 9:
            print(f"{numb_one:d}{numb_two:d}")
        else:
            print("{:d}{:d}".format(numb_one, numb_two), end=", ")
