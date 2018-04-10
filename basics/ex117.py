# PRove that two string varilables of same value point same mmemory location
str1 = "Python"
str2 = "python"

print("Memory Location of str1 = ", hex(id(str1)))
print("Memory location of str2 =", hex(id(str2)))
