#!/bin/python

###Exercise: Creating and Using Functions
"""Functions are a great way to organize your code for reuse and clarity. Write a script that does the following:
Prompts the user for a message to echo
Prompts the user for the number of times to repeat the message. If no response is given, then the count should default to 1.
Defines a function that takes a message and count, then prints the message that many times.
To end the script, call the function with the user-defined values to print to the screen"""


message = raw_input("Please type in the message to be echoed.... \n")
count = int(raw_input("Please provide how many times the message need to be printed... \n") or "1")
print(" Message supplied is %s " % message)
print(" Count info supplied is %s " % count)

def print_function(message, count):
    num = 0
    while num < count:
        print ("printing message typed.... %s" % message)
        num += 1

print_function()


###Linux academy solution

'''
#!/usr/bin/env python

message = raw_input("Enter a message: ")
count = raw_input("Number of repeats [1]: ").strip()

if count:
    count = int(count)
else:
    count = 1

def multi_echo(message, count):
    while count > 0:
        print(message)
        count -= 1

multi_echo(message, count)
'''