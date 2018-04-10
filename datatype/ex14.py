# Python program that accepts a comma serperate sequence of words as input and prints the unique words in sorted form
import sys
items = raw_input("Input comma seperated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))
