# Write a Python program to find path refers to a file or directory when you encounter a path name.

import os.path

for file in [__file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File		:', file)
    print('Absolute	:', os.path.isabs(file))
    print('Is file? 	:', os.path.isfile(file))
    print('Is Dir? 	:', os.path.islink(file))
    print('Is link?	:', os.path.islink(file))
    print('Exists? 	:', os.path.exists(file))
    print('Linke Exists?:', os.path.lexists(file))


