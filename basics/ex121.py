#Python program to determine if variable is defined or not
try:
  x = 1 
except NameError:
  print("Variable is not defined...!")
else:
  print("Variable is defined.")
try:
  y 
except NameError:
  print("Variable is not define...!")
else:
  print("Varilable is define.")

