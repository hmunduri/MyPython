#Python program to print a specifi list after removing the oth, 4th and 5th elements
import sys
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'yellow']
color = [ x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)
