#Test whether a number is within 100 of 1000 or 2000
#!/usr/bin/python
def near_thousand(n):
     return((abs(1000-n) <= 100) or (abs(2000-n) <= 100))
print(near_thousand(1000))
print(near_thousand(1100))
print(near_thousand(2000))
print(near_thousand(2200))
	
	
