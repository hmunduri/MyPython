#!/bin/python

import argparse

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the fileto read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='$(prog)s 2.0')
"%(prog)s 2.0" %{'prog': 'reverse-file'}
args = parser.parse_args()
#print(args.filename)

try:
    f = open(args.filename)
except IOError as err:
    print("error: file not found")
else:
    with f: 
        limit = args.limit
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:args.limit]
        for line in lines:
            print(line.strip()[::-1]) 
finally:
    print("\nWe're finished")
