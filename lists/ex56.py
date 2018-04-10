#Python program to convert a string a list 
import sys 
import ast 
color = "['red', 'Green', 'White']"
print(ast.literal_eval(color))
