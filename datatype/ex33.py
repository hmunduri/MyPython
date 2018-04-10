#Python program to print the following intergers with Zeros on the left of specified width.
x = 3 
y = 123 
print("\n Original Number: ", x)
print("Formatted Number(Lef padding, width 2): "+"{:0>3d}".format(x));
print("Original Number: ", y)
print("Formatted Number(left padding, width 6): "+"{:0>6d}".format(y));
print()
