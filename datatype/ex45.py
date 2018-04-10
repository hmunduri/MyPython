#Python program to check if a string contains all letters of the alphabet
import sys 
import string 
alphabet = set(string.ascii_lowercase)
input_string = 'the quick brown for jumps over the lazy dog'
print(set(input_string.lower()) >= alphabet)
input_string = 'The quick brown for jumps over the lazy cat'
print(set(input_string.lower()) >= alphabet)
