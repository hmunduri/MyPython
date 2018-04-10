import sys
print()
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
    print sys.byteorder
else:
    #motorola, sparc
    print("Big-endian platform.")
print()
