#!/bin/python

import os

stage = os.environ["STAGE"].upper()

output = "We are running in %s" % stage

if stage.startswith("PROD"):
	output = "DANGER!!!  - " + output

print(output)

## environ function is like dictionaries, if you dont have a value and if u use it, it will cause issues
##use link this to avoid issues....use getenv instead

stage1 = (os.getenv("STAGE1") or "development").upper()

output1 = "We are running in %s" % stage1

if stage1.startswith("PROD"):
	output1 = "DANGER!!!  - " + output1

print(output1)