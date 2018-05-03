##below statements with comparision operators print true or false
#comparision operators with integers & floats
print ( 1 < 2)
print ( 2 > 0)
print ( 1 == 2)
print ( 1.0 == 1)
print ( 1 !=2 )
print ( 1.0 != 1)
print ( 3.0 >= 3.0)
print ( 3.1 <= 3.0)
#comparision operators with strings
print ( "this" == "this")
print ( "this" == "This")
#comparision operators with lists --- this works with tuples as well
print (2 in [1,2,3])
print (4 in [1,2,3])

#### IF  / ELSE
if True:
    print ("something is true")

if False:
	print("something is false")

name = "Karthik"

if len(name) >= 8:
	print("name is long")
elif len(name) == 7:
	print("name is average")
else:
	print("name is short")

if "test":
    print ("this is a test")

###same as below!!!

if bool("test"):
    print ("this is a test")

###### WHILE LOOPS
count = 0
while count < 10:
	print ("we are counting...")
	count +=1

num = 0
while num < 10:
	if num % 2 == 0:
		num += 1
		continue
	print ("we are counting odd numbers %s" % num)
	num += 1
#### FOR LOOP
colors =['white','black','red']
for color in colors:
	print (color)

point = (2.1,3.1,4.1)
for val in point:
	print (val)

ages = {'kevin':55,'vivaan':1}
for key,value in ages:
	print (key)
	print (value)


#### LOGIC operators
## use not --> for negation
not 1 # returns false
not True  ## returns false
if not len("something") > 10:
	print ("its not")
### is operator ( unique to python) compares exact spot in memory

1 is 1 # return true
'a' is 'a'  ## return true

{} is {}  #--> return false because, above string and int are immutable but, dict items are mutable ( it does not have same memory in python virtual machine)

### AND operator
###returns first falsy vaule if there is one or it returns last truthy value 
### second expression wont be evaluated if 1st expression is not true
1 and 2 ## returns 2
0 and 1 ## returns 0  , because bool (0) is false

### OR operator
## returns the first truthy item or the right most item if everything is falsy
## its going to go search until it finds a truthy value and stop there
1 or 2 ## returns 1
0 or 2 ## returns 2
 
0 or {} or 3 or True ## returns 3 as both 0 and empty dictionary {} returns false 