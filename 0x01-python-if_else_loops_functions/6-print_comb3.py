#!/usr/bin/python3
for number in range(1,100):
    number_check = f"{number:02}"
    if number_check [0] < number_check [1]:
        if int(number_check) < 89:
            print(number_check , end=", ")
        elif int(number_check) == 89:
            print(number_check, "\n") 
