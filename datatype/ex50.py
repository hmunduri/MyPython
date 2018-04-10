#write a python program to splita  string on the last occurence of the delimiter. 
import sys 
str1 = "w,3,r,e,s,o,u,r,c,e"
print(str1.split(',', 1))
print(str1.split(',', 2))
print(str1.split(',', 5))
