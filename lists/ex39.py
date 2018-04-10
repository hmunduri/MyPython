#Python program to convert a list of multiple intergers into a single interger 
import sys 
L = [11, 33, 50]
print("Original List: ", L)
x = int("".join(map(str, L)))
print("single Integer: ", x)
