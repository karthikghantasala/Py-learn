#!/bin/python

import random
import os
import json


#generate receipts


count = os.getenv("FILE_COUNT") or 100
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for identifier in range(1, count + 1):
    amount = random.uniform(1.0, 1000.0)
    content = {
        'topic' : random.choice(words),
        'value' : "%.2f" % amount
    }
    with open('./new/receipts/receipt-%s.json' % identifier, 'w') as f:
        json.dump(content, f)
