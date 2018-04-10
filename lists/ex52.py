#Python program to compute the similarity between two lists
import sys 
from collections import Counter
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
counter1 = Counter(color1)
counter2 = Counter(color2)
print("Color1-Color2: ", list(counter1 - counter2))
print("Color2-color1:", list(counter2 - counter1))
