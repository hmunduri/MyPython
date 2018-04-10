#Python function to get a string made of its first three characters of a specified string. If it less than 3 return the string
def first_three(str):
    if len(str) > 3: 
       return str[:3]
    else:
       return str
print(first_three("Himagiri"))
