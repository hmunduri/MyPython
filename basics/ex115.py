#Compute the product of a list of integers
from functools import reduce 
nums = [15,45,80,90,12]
nums_product = reduce( (lambda x,y: x+y), nums)
print("product of the numbers: ", nums_product)
