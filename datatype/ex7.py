def not_poor(str1):
  snot = str1.find('not')
  sbad = str1.find('bad')
  
  if sbad > snot: 
    str1 = str1.replace(str1[snot:(sbad+4)], 'good')

  return str1

print(not_poor('The lyrics is not that bad !'))
