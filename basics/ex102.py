# to get system command output 
import subprocess 
returned_test = subprocess.check_output("dir", shell = True, universal_newlines=True)
print(returned_test)
