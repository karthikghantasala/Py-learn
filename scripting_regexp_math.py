#!/bin/python

## use shutil to
##try to perform file operations like unix file actions like copying etc
## by  using python code instead of using sub processes and to avoid type casting etc


### glob for pattern matching

### use reg exp and math to impovise the scripting example done in the previous file scripting_shutil_glob.py

import glob
import os
import shutil
import json
import re
import math

try:
    os.mkdir("./new/processed")
except OSError:
    print("'processed' dir already exists")

# Get a list of receipts

#receipts = glob.glob('./new/receipts/receipt-[0-9]*.json')
even_receipts = [f for f in glob.iglob('./new/receipts/receipt-[0-9]*.json')
    if re.match('./new/receipts/receipt-[0-9]*[02468].json', f)]

subtotal = 0.0



# Iterate over the reciepts
   # read content and tally a subtotal
   # mv the file to processed dir
   # print that we processed the file


for path in even_receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += math.ceil(float(content['value']))
        #or
        #subtotal += math.floor(float(content['value']))
    #name = path.split('/')[-1]
    #destination = "./new/processed/%s" % name
    destination = path.replace('receipts', 'processed')
    shutil.move(path,destination)
    print("moved '%s' to '%s'" % (path, destination))


# print the subtotal of all processed receipts

print("Receipt subtotal: $%s" % round(subtotal, 2))
