x = input("Desired new length: ")
assert x.isnumeric() == True, "Not a number"
my_string = input("Input string: ")
x = int(x)
# Code that pads a string with spaces until it is a certain length
while len(my_string) < x:
    my_string += "-"
print(my_string)
