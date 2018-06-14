#!/bin/python

## use shutil to
##try to perform file operations like unix file actions like copying etc
## by  using python code instead of using sub processes and to avoid type casting etc


### glob for pattern matching

import glob
import os
import shutil
import json

try:
    os.mkdir("./new/processed")
except OSError:
    print("'processed' dir already exists")

# Get a list of receipts

receipts = glob.glob('./new/receipts/receipt-[0-9]*.json')

subtotal = 0.0



# Iterate over the reciepts
   # read content and tally a subtotal
   # mv the file to processed dir
   # print that we processed the file


for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split('/')[-1]
    destination = "./new/processed/%s" % name
    shutil.move(path,destination)
    print("moved '%s' to '%s'" % (path, destination))


# print the subtotal of all processed receipts

print("Receipt subtotal: $%.2f" % subtotal)
