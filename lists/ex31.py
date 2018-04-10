#Python program to count the number of elements in a list within a specified range. 
import sys 
def count_range_in_list(li, min, max):
   ctr =0 
   for x in li:
       if min <= x <= max:
           ctr += 1 
   return ctr 
list1 = [10,20,30,40,40,40,70,88,99]
print(count_range_in_list(list1, 40, 100))
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(count_range_in_list(list2, 'a', 'e'))
