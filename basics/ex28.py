#Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence
#!/usr/bin/python
def even_number(numbers):
         for i in numbers:
               if i > 237:
                  break
               elif i % 2 == 0:
		  print(i)
print(even_number([2,4,6,8,198,134,137,199,238,389,556,65,68])) 
