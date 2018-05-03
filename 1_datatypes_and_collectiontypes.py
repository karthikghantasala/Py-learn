#!/bin/python
#Comment here
#Built in string data types
print("Hello")  #comment here
print('Hello')  #comment here
print ("Hello".find("e"))
print("Hello".lower())
print ("Ha" * 4)
print ("pass" + "word")
print ("This is\tDelimited")
print ("This is\nNewliner")
print ("This doesn't use \ Escape character")
print ("This uses\\Escape character")
print ("This uses 'single' quotes in Double")
print ('This uses "double" quotes in Single')
print ("This uses \"double\" quotes in Double")
#Built-in datatypes
print (5 * 4)
print (5 + 4)
print (5 - 4)
print (5 / 4)
print (5.0 / 4)
print (5 // 4)
print (5.0 // 4)
print (5 % 4)
print (5 ** 4) # exponential powers
#casting
#converting string to int & float
print (int("1"))
print (float("1.0"))
#converting float and int to str
print (str(5.6))
print (str(5))
#Boolean and none (null or nothing)
print (True)
print(False)
print(None)
#Casting to Bool type
print(bool("Hello"))
print(bool(""))
print(bool(1))
print(bool(0))
#variables
a_word = 'vivaan'
print(a_word)
my_num = 5
print(my_num)
#dynamism of python eg
#assign string to a int variable works
my_num = a_word
print(my_num)
####
#
#PYTHON COLLECTION TYPES
####
#lists and tuples
#lists
my_list = [1, 'a', 2.0, True]
print(my_list)
print(my_list[0] )
print(my_list[2])
#to get last item on the list
print(my_list[-1])
#extract or slice a list starting from 0 index upto but not including 3 index
print(my_list[0:3])
print(my_list[:3])
#from 2 index to last
print(my_list[2:])
#slice every 2nd value from list starting from 0 index
print(my_list[::2])
#slice every 2nd value from list starting from 1 index
print(my_list[1::2])
#change list items...you can change lists as they are mutable..this is not possible with string vars
print(my_list)
my_list[0] = 1.95
print(my_list)
#append to a list
my_list.append(False)
print(my_list)
#concatente to a list on the fly ...but doesnt save
my_list + [9 , 10]
print(my_list)
#concatente to a list on the fly ...but saves permanantly
my_list += [9 , 10]
print(my_list)
#replace some list items
my_list[1:3] = ['b' , 'c']
print(my_list)
#you are free to add or remove or replace any number of items within the list
#it will elastically do it
my_list[1:3] = ['f' , 'g' , 'h']
print(my_list)
my_list[1:4] = []
print(my_list)
#remove items from list
my_list.remove(2.0)
print(my_list)
#removing boolean values is tricky from a list as this below doesnt reallly remove the boolean vale True from the list.
#instead, this removes first item in the list that resolves to True
my_list.remove(True)
#another way to remove list items
new_list = [1, 2, 3, 4]
#removes last item
new_list.pop()
print(new_list)
new_list.pop(0)
#Tuples are like 2-dimensional co-ordinates 
point = (2.0 , 3.0)
print(point[0]) #returns x co-ordinate
print(point[1]) #returns y co-ordinate
key , value = ('phone','apple')
print (key)
print (value)
print("My name is %s %s" % ("Karthik", "Ghantasala"))
#Dictionaries
ages = { 'karthik': 30, 'sai': 30, 'vivaan': 1}
print(ages)
print(ages['vivaan'])
#adding a new dict element
ages['kris'] = 29
#modify  a dict item
ages['karthik'] = 31
#call keys & values & items method on dict
print(ages.keys())
print(ages.values())
print(ages.items())
#delete a dict item
del ages['karthik']
ages.pop('sai')
del ages # deletes the whole dict...so use carefully
#you can use int or float also for keys in a dictionary
my_dict = { 1: 'this', 1.1: 'that', 'karthik':'sai' }
#alternative ways to create dictionaries using the keyword dict
#1
prices = dict(iphone=800,samsung=850)
print(prices)
#2
colors = dict([('iphone', 'jetblack'), ('samsung','silver')])
print(colors)


