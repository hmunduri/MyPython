def odd_values_string(str):
  result  = " "
  for i in range(len(str)):
    if i % 2 ==1: 
       result = result + str[i]
  return result

print(odd_values_string('abcdef'))
print(odd_values_string('python'))
