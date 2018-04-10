#Python program to swap command and dot in a string. 
import sys 

amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)
