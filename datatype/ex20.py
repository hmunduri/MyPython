#Python function to reverse a string if its lenth is a multiple of 4.
def reverse(str):
    if len(str) == 4:
       return ''.join(reversed(str))
    return str 
print(reverse("Hima"))
