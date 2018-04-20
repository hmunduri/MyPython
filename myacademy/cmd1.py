#!/bin/python 

import subprocess
try: 
   output = subprocess.check_output(
           'ls', 'fake.txt',
           stderr=subprocess.STDOUT
           )
except OSError as err:
    print("Caught OSError")
    output = err
except subprocess.CalledProcessError as err:
    print("Caught called processError")
    output = err
print(output)
