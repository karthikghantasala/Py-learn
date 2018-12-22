#!/bin/python

import argparse

parser = argparse.ArgumentParser(description='Read a file in reverse')

parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0', help='Displays the version of the script')

args = parser.parse_args()

print(args.filename)

try:
	f = open(args.filename)
except IOError as err:   # This is a catch block
	print ("Error: file not found")
except OSError as err:     # Note: We can add multiple catch blocks
    print ("Error: Some OS Error")    
else:   ## Happy path for the try block
	with f:
		limit = args.limit
		lines = f.readlines()
		lines.reverse()

        if limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1])
finally:   ## Used for something like cleanup... or some mandatory step for success/fail scenario
	print ("We're finished...")





'''
USAGE:

(C:\ProgramData\Anaconda2) C:\Users\Vivaan Sai Karthik\Desktop\Py\Py-learn>python scripting_exception_handling.py fake.txt
fake.txt
Error: file not found

'''

