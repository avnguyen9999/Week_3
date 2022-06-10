"""A program to divide the product of 3 numbers by their average"""
A = 7
B = 5
C = -12
PRODUCT = A*B*C
AVERAGE = (A+B+C)/3
try:
    RESULT = PRODUCT/AVERAGE
    print(RESULT)
except ZeroDivisionError:
    print(f"The average of {A}, {B} and {C} is {AVERAGE}. Encountered Zero Division case.")
