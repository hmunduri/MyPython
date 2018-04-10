x = int(input("input first nunber: "))
y = int(input("Input second number:"))
z = int(input("Input third number:"))

a1 = min(x,y,z)
a3 = max(x,y,z) 
a2 = (x + y + z ) - a1 - a3 
print("Number is sorterd order :", a1,a2,a3)
