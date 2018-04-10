#Python program to revers words in a string
import sys 
def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse_string_words("the quick brown for jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))
