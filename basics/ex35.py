#Python program which will return true if the two given interger values are equal or their sum or difference is 5. 
def test_number5(x,y):
    if x ==5 or y ==5 or abs(x-y) ==5 or (x+y) == 5:
	return True
    else:
        return False
print(test_number5(7,2))
