"""A program to add numbers until the user enters 0, then print the total"""
TOTAL = 0
CURRENT = -1
while CURRENT!=0:
    try:
        CURRENT = int(input('Enter a number: '))
    except ValueError:
        print("Input is not a number.")
        continue
    TOTAL = TOTAL + CURRENT
print(TOTAL)
# Hint: What happens if a user types in something other than a number?
