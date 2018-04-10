#Python program to find largest in a list
import sys
def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max: 
            max = a 
    return max
print(max_num_in_list([1, 2, -8, 3]))
