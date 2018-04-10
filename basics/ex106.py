#Divide a path on the extension seperator
import os.path 
for path in ['test.txt', 'filename', '/home/hm1584/practice/test.txt', '/', '']:
    print('"%s" :' % path, os.path.splitext(path))
