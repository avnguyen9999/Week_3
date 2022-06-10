#!/usr/bin/env python
"""A program to multiply two even numbers"""
TOTAL = 0
try:
    NUMBER1 = int(input('Enter a number: '))
except ValueError:
    print("Input 1 is not a number")
if NUMBER1%2 == 0:
    try:
        NUMBER2 = int(input('Enter a number: '))
        if NUMBER2%2 == 0:
            print(NUMBER1*NUMBER2)
        else:
            print('Number not even.')
    except ValueError:
        print("Input 2 is not a number")
else:
    print('Number not even.')
