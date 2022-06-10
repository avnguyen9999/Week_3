x = input("Enter score: ")
assert x.isnumeric() == True, "Not an integer"
x = int(x)
assert x>=0 and x <= 100, "Range error"
# Code that prints different messages for values in different ranges
if x < 50:
    print('F')
elif x < 65:
    print('C')
elif x < 75:
    print('D')
else:
    print('HD')
