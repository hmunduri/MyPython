#Python program to find missing and additional vales in two lists
import sys 
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['d', 'e', 'f', 'g', 'h']
print('Missing values in second list :', ','.join(set(list1).difference(list2)))
print('Missing values in first list :', ','.join(set(list2).difference(list1)))
