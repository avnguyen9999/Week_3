# Code that checks if a given value is 5 and prints a message
x = input("Enter a number: ")
assert (x.isnumeric() == True), "Unit test failed."
x = float(x)
if x == 5:
    print(x)
else:
    print("Not 5")
