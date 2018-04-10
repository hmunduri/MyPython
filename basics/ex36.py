#Python program to add two objects if both objects are an integer type
#!/usr/bin/python
def sum(a,b):
    if not(isinstance(a, int) and isinstance(b,int)):
        raise TypeError("Inputs must be intergers")
    return a + b
print(sum(10,20))

