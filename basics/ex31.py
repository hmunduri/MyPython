def gcd(x,y):
    if x > y:
       smaller = y
    else:
       smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0 ) and (y % i == 0)):
           gcd = i
    return gcd
print(gcd(12,17))
print(gcd(4,6))
print(gcd(8,16))
