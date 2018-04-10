#Python program to find the list of words that are longer than n from a given list of words 
import sys
def long_words(n, str): 
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x)> n : 
            word_len.append(x)
    return word_len
print(long_words(3, "The quick brown for jumps over the lazy dog"))
