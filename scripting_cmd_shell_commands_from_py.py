#!/bin/python

import subprocess

### the call function below wouldn't capture output it only looks for the status code.
## which might not be desired especially if you depend on output of this step. see below for the alternate approach
code = subprocess.call(['ls','-z'])

if code == 0:
	print("Command is sucessful")
else:
	print("failed with code %i" % code)


### otherway to handle output.. that is to capture output in a variable
## works only for success scenario.. use try/except for failed scenario
output = subprocess.check_output(['ls','-l'])
print (output)

### Try Catch for the above...

try:
	output = subprocess.check_output("ls fake.txt", stderr=subprocess.STDOUT)
except OSError as err:
	print("Caught OSError")
	output = err
except subprocess.CalledProcessError as err:
    print("caught CalledProcessError")
    output = err
print (output)