#Insert a string in the middle of a string
import sys 
def insert_string_middle(str, word):
    return str[:2] + word + str[2:]
print(insert_string_middle('[[]]', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))
print(insert_string_middle('<<>>', 'HTML'))
