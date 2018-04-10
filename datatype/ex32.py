#Python program to print the following floating numbers upto  no decimal places 
import sys
x = +13.4958
y = -12.9999

print("\nOriginal Number: ", x)
print("Formatted Number with sign: "+"{:+.0f}".format(x));
print("Original Number: ", y)
print("Formatted Number with sign: "+"{:+.0f}".format(y));
print()

