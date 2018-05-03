#!/bin/python
import os
### READ

heros1 = open('heros1.txt')

for line in heros1:
	print(line)

heros1.close()

###In Above approach, print automatically inserts new line at end of string
# so, here is another way, it reads entire file as single block of string

heros = open('heros.txt')

print(heros.read())

heros.close()


### WRITE

## Change the mode to 'w' if you want to write contents into the file. By default its going to be 'r'

heros1_file = open('heros1.txt', 'w')

heros1_file.write("Beast\n")
heros1_file.write("Dr Strange\n")

heros1_file.close()

##Notice that above it overwrites the exsiting contents

##to avoid it we need to open the file in r,w mode
##and need to move the cursor to last char

heros1_file = open('heros1.txt', 'r+')

heros1_file.seek(-1, os.SEEK_END) 

## the below notation with '2' is same as the above usage os.SEEK_END
## heros1_file.seek(-1, 2) 

heros1_file.write("\nBeast\n")
heros1_file.write("\nDr Strange\n")

heros1_file.close()

## Alternative approach instead of using SEEK_END is using 'append mode'

heros1_file = open('heros1.txt', 'a')

heros1_file.writelines(['Hulk\n', 'Airbender\n'])


heros1_file.close()

heros1_file = open('heros1.txt', 'r')

print(heros1_file.read())

heros1_file.close()


## Alternative approach to avoid writing close statement is below...
## the below way of writing into files will automatically closes the file after writing

with open('heros.txt', 'a') as heros_file:
	heros_file.write("\nProf Xavier\n")

with open('heros.txt', 'r') as heros_file:
	print(heros_file.read())




