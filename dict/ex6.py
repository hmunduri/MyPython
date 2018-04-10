#Python program to generate and print a dictionary that contains a number in the form
import sys 
n = int(input("Input a number"))
d = dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)
