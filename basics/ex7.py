#Accept a filename from the user and print the extension of that 
filename = raw_input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is :" + repr(f_extns[-1]))
