#Find whether a given number is even or odd, print out an appropriate message to the user
num = int(raw_input("Enter a number:"))
mod = num % 2 
if mod > 0: 
    print ("This is an odd number. ")
else:
    print ("This is an even number.")
