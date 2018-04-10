#Python program to get a dictionary form an objects fields 
import sys
class dictObj(object):
     def __init__(self):
	 self.x = 'red'
         self.y = 'Yellow'
         self.z = 'Green'
     def do_nothing(self):
         pass
test = dictObj()
print(test.__dict__)
