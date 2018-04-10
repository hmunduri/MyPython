#List all files in a directory in Python
from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/hm1584/') if isfile(join('/home/hm1584', f))]
print(files_list);
