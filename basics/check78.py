#import sys 
#import textwrap
#module_name = sys.builtin_module_names
#print module_name
##print(textwrap.fill(module_name, width=70))
print (globals.keys()) | set(__builtins__.__dict__.keys()))
