#Program to caculate the time runs(differnce between start and current time of a program)
from timeit import default_timer 
def timer(n):
    start = default_timer()
   
    for row in range(0,n):
        print(row)
    print(default_timer() - start) 

timer(5)
timer(15)
