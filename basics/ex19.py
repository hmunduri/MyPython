#Get a new string from a given string where 'Is' has been added to the front. If the given string already begins with 'Is' then return the string unchanged
#!/usr/bin/python
def new_string(str):
  if len(str) >= 2 and str[:3] == "Its":
     return str
  return "Its" + str 

print(new_string("Array"))
print(new_string("ItsEmpty"))
