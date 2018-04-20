#!/bin/python

import subprocess

code = subprocess.call(['ls', '-l'])
if code ==0: 
    print("command finished succesffully")
else:
    print("Failed with code: %i" %code)
