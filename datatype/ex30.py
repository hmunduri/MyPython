#Python program to print the following floating numbers upto 2 decimal places
import sys 
x = 3.1415926
y = 12.9999

print("\nOriginial number: ", x)
print("Formatted Number:  "+"{:.4f}".format(x));
print("Original Number: ", y)
print("Formatted NUmber: "+"{:.2f}".format(y));
print()
