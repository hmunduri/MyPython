#!/bin/python

import argparse

parser = argparse.ArgumentParser(description='search for words inlcuding partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in the words file')

args = parser.parse_args()
snippet= args.snippet.lower()

words = open('/usr/share/dict/words').readlines()
matches = []

for word in words:
    if snippet in word.lower():
        matches.append(word)
print(matches)
