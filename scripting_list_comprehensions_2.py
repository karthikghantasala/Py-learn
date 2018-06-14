#!/bin/python

## using list comprehensions , a functional programming feature

import argparse

parser = argparse.ArgumentParser(description='search for words including partial word')

parser.add_argument('snippet', help='partial (or complete) string to search for in the words file')

args = parser.parse_args()

snippet = args.snippet.lower()

words = open('/usr/share/dict/words').readlines()

'''
#without using list comprehensions
matches = []

for word in words:
    if snippet in word.lower():
        matches.append(word)

print(matches)
'''

#using list comprehensions

print([word for word in words if snippet in word.lower()])

#if you want to output much cleaner values, do below to strip new line char from the output

print([word.strip() for word in words if snippet in word.lower()])

##another example

numbers = [1,2,3,4]

##print square roots
print([x * x for x in numbers])

## print cube roots
print([x * x * x for x in numbers])
