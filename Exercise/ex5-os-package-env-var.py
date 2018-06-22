#!/bin/python

### Exercise: Using the 'os' Package and Environment Variables

'''
Environment variables are often used for configuring command line tools and scripts. Write a script that does the following:
Prints the first ten digits of Pi to the screen.
Accepts an optional environment variable called DIGITS. If present, the script will print that many digits of Pi instead of 10.
Note: Youll want to import pi from the math package.
This task will require some more advanced string formatting. You can read the documentation here, but heres an example of how you could print a float to ten digits:
print("%.*f" % (10, my_float))
'''

import os
from math import pi

digits  = int(os.environ["DIGITS"] or 10)

print "Number of digits to be rounded to is", digits


print("%.*f" % (digits, pi))

#var_c = "Number of digits to be rounded to is", var_a, "and", var_b, "bye"
#print(*var_c)


#print(round(pi, digits))

#pi_value = round(pi, digits)

#print("pi value rounded to ten digits pi_value)


###Linux academy solution
'''
#!/usr/bin/env python

from os import getenv
from math import pi

digits = getenv("DIGITS") or 10
print("%.*f" % (int(digits), pi))
'''