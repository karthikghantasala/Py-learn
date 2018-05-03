#!/bin/python

#### Another way to declare timer package

from time import localtime, strftime, mktime

start_time = localtime()

print("Timer start at %s" % strftime("%X", start_time))

#Wait for user input
raw_input("Please press Enter to continue..")

stop_time = localtime()

difference = mktime(stop_time) - mktime(start_time)

print("Timer stopped at %s" % strftime("%X", stop_time))

print("Total time: %s seconds" % difference)