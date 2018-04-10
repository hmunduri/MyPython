# Program which accepts a squeuence of Comma-seperated numbers from user and genrate a list and  a tuple with those numbers 
values = raw_input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
