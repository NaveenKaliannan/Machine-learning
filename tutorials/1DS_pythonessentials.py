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
## Important list(first_dict) will give you only the keys
country = ['Algeria','Angola','Argentina','Australia','Austria','Bahamas','Bangladesh','Belarus','Belgium','Bhutan','Brazil','Bulgaria','Cambodia','Cameroon','Chile','China','Colombia','Cyprus','Denmark','El Salvador','Estonia','Ethiopia','Fiji','Finland','France','Georgia','Ghana','Grenada','Guinea','Haiti','Honduras','Hungary','India','Indonesia','Ireland','Italy','Japan','Kenya', 'South Korea','Liberia','Malaysia','Mexico', 'Morocco','Nepal','New Zealand','Norway','Pakistan', 'Peru','Qatar','Russia','Singapore','South Africa','Spain','Sweden','Switzerland','Thailand', 'United Arab Emirates','United Kingdom','United States','Uruguay','Venezuela','Vietnam','Zimbabwe']
gdp=[2255.225482,629.9553062,11601.63022,25306.82494,27266.40335,19466.99052,588.3691778,2890.345675,24733.62696,1445.760002,4803.398244,2618.876037,590.4521124,665.7982328,7122.938458,2639.54156,3362.4656,15378.16704,30860.12808,2579.115607,6525.541272,229.6769525,2242.689259,27570.4852,23016.84778,1334.646773,402.6953275,6047.200797,394.1156638,385.5793827,1414.072488,5745.981529,837.7464011,1206.991065,27715.52837,18937.24998,39578.07441,478.2194906,16684.21278,279.2204061,5345.213415,6288.25324,1908.304416,274.8728621,14646.42094,40034.85063,672.1547506,3359.517402,36152.66676,3054.727742,33529.83052,3825.093781,15428.32098,33630.24604,39170.41371,2699.123242,21058.43643,28272.40661,37691.02733,9581.05659,5671.912202,757.4009286,347.7456605]
## zipping using dictionary
zusammen = dict(zip(country, gdp))



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
### Important zip function
## valueerror




## important question: what happens
list('kdskndks')
tuple('kdskndks')

