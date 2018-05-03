#!/bin/python

#READ INPUT FROM USER
name = raw_input("Please type your name ")
dob = raw_input("Please enter your dob ")

#little dangerous as it accepts bith int and string values (basically whatever user is supplied will be parsed)
age = input("please enter your age ")

#alternative for input is use raw input and cast to int

age = int(raw_input("please enter your age "))

print("%s is born on %s" % (name,dob))
print(" ")
print("Half of %s's age is %s" %(name,(age / 2)))

