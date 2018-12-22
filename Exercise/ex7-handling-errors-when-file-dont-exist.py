"""
Write a script that does the following:
Receives a file_name and line_number as command line parameters.
Prints the specified line_number from file_name to the screen. The user will specify this as you would expect, not using zero as the first line.
Make sure that you handle the following error cases by presenting the user with a useful message:
The file doesnt exist.
The file doesnt contain the line_number specified (file is too short).

#!/bin/python

import sys
import os

file_name = sys.argv[1]
line_number = int(sys.argv[2])

if len(sys.argv) > 1:
    print("File Name is: " + file_name)
    print("Line number to print: %i" % line_number)
else:
    print(" No arguments provided")


try:
    load_file = open(file_name, "r")
    read_line = load_file.readlines()
    load_file.close()
    print(read_line[line_number])
except IOError as e:
    print(os.strerror(e.errno))
except IndexError as e1:
    print e1
    print sys.exc_type
else:
    print("File exists")

"""
###linux academy solution

#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='the file to read')
parser.add_argument('line_number', type=int, help='the line to print from the file')

args = parser.parse_args()

try:
    lines = open(args.file_name, 'r').readlines()
    line = lines[args.line_number - 1]
except IndexError:
    print("Error: file '%s' doesn't have %i lines." % (args.file_name, args.line_number))
except IOError as err:
    print("Error: %s" % err)
else:
    print(line)