import sys
import platform

print(sys.version)
print(platform.python_version())

## Basic arithmetic operations
## A variable can be assigned to any value. By assigning
## we creating a references. A variable can be accessed only
## if it assigned.
## when a variable is assigned a value, it refers to the value's
## memory location or address. it does not equal the value itself
x=7
oldaddress=id(x)
##7 is stored in memeory location. x is the address to the 7
## by current following expresion, we create a new address in where 
## the 7+1 addition is performed. old address is forgotten
x=x+1
newaddress=id(x)
print(oldaddress, newaddress, oldaddress==newaddress)

## Basic data types: int, float, string, None, boolean (true or false)

## if both numerator and denominator are integer, the result would be
## integer too. 


## Data strucutres: tuple (one dimensional, immutable ordered sequnece of items which can be of mixed data types, () bracket)
## immutable means the value cannot be changed.
## postive index starts from zero, negative index starts from the end and used to access the last data
first_tuple = (12,'Jack',45.6,'new',(3,2),'test')
print(first_tuple)
print(first_tuple[2], first_tuple[-3], first_tuple[-2])
## slicing into subset. only the first index is included, second index is neglected
print(first_tuple[1:4], first_tuple[0:-2])
## Important: You can't add elements to a tuple because of their immutable property.
## There's no append() or extend() method for tuples, 
## You can't remove elements from a tuple, also because of their immutability
## But two different tupes can be added and a new tuple can be created
## * doesnt not multiply the value, it only repeats the value in tuple

## Data strucutres: List (one dimensional, mutable ordered sequnce of items which can be of mixed data types, square bracket)
## mutable means the value can be changed.
first_list=['Mark',101,23.5,'test',None,11]
print(first_list)
first_list.append('jack')
print(first_list)
first_list.remove('jack')
print(first_list)
first_list.pop(2)
print(first_list)
first_list.insert(5,'Hello')
print(first_list)
#first_list.insert(-1,'Hello')
#print(first_list)
##Important: check -1 negative location for insert. not the expexted results
print(first_list[2:-1], first_list[-1])

## Data strucute: Dictionary (dict) stores a mapping between a set of key and a set of values, { :, :} brackets
## it contains: key and value
first_dict={'jon':1,'nav':2}
print(first_dict, first_dict.keys(), first_dict.values(),first_dict['jon'])
first_dict.update({'hey':3})
print(first_dict)
del first_dict['jon']
print(first_dict)

## Data strucures: Set (unordered collections of unique elements)
auto = set(['audi','bmw'])
var = {'audi'}
print(var,type(var) )
## set operations

##Boolean operator 
## in means given value is present in list or not
print('Nick' in ['Nick','Hello'])


## function can return single, or multiple values. 
## functions make the faster


## enumerate gives the position, name of the list or tuple
store=[2,3,4,5]
for position, name in enumerate(store):
    print(position, name)
print( dict((name, position) for position, name in enumerate(store)) )

##sorted function can sort numbers or letters
## reversed function reverse the dataset
## zip function pair the data elements, type will reuturn the type of dataset used 

## valueerror

