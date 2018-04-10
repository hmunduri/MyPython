#Python program to find files and skip directories of a given directory 
import os 
print([f for f in os.listdir('/home/hm1584/practice') if os.path.isfile(os.path.join('/home/hm1584/practice', f))])
