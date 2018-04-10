#Python program to check whether a file exists
#!/usr/bin/python
import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))
