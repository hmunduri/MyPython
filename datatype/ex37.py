#Python program to display a number in left, right and center aligned of width 10.
import sys 
x = 22
print("\nOriginal Number: ", x)
print("Left Aligned (width 10) :"+"{:< 10d}".format(x));
print("Right aligned (width 10) :"+"{:10d}".format(x));
print("center Aligned (width 10) :"+"{:^10d}".format(x));
print()
 
