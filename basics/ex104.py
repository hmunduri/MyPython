#Find group id, user id, real group id, supplemental group ids associated with the current process
import os 
print("\nEffective group id: ", os.getegid())
print("Effective user id: ", os.geteuid())
print("Real group ID: ", os.getgid())
print("List of supplemental group ids: ", os.getgroups())
print()
