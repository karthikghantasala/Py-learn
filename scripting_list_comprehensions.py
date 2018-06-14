#!/bin/python

## list comprehension using functional programming

import argparse

parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial or complete string to search for words in file')

args = parser.parse_args()
snippet = args.snippet.lower()

words = open('/usr/share/dict/words').readlines()
matches = []

for word in words:
	if snippet in word.lower():
		matches.append(word)

print(matches)


## or the above for loop can be written in one line using list comprehension

print([word for word in words if snippet in word.lower()])

## to remove new line

print([word.strip() for word in words if snippet in word.lower()])

## eg: filename John 

## searches for word John in /usr/share/dict/words

'''
another use case for list comprehension with numbers

'''
numbers = [1,2,3,4]
[x * x for x in numbers]
