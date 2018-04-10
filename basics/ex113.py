# Input a number, if it is not a number generate an error message
while True:
    try:
        n = raw_input("Input a number: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print "This is a integernumber"
