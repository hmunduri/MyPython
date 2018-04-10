#Python program to find largest in a list
import sys
def min_num_in_list(list):
    min = list[0]
    for a in list:
        if a < min:
            min = a
    return min
print(min_num_in_list([1, 2, -8, 3]))
