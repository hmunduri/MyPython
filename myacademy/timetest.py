#!/bin/python
 
#import time 
from time import localtime, strftime, mktime

start_time = localtime()
print("Timer started at %s" % strftime("%X", start_time))


#Wait for user input 
raw_input("please press enter to continue...")

stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print("Timer stoppped at %s" %strftime("%X", stop_time))
print("Total time: %s seconds" % difference)
