##numpy - package for mathematical computingin python
## fast and efficient multidimension array
## linear algebraic operation, fourier transformation
## integrating c, c++

import numpy as np

distance = [10,15,17,26]
time=[.30, .47, .55, 1.20]

## error speed=distance/time without numpy

distance = np.array(distance)
time = np.array(time)
speed = (distance/time)
print(speed)

##ndarray - used as the primary container to exchange data between algorithms
## arrays can 1,2d, 3d or multi D
## array([5,7,8]), array([],[]) array([],[],[])

first=np.array([1,2,3,4])
print(first)
#first row, second coloumn
zeros=np.zeros((3,3))
print(zeros)
ones=np.ones((3,3))
print(ones)
arrange=np.arange(12)
print(arrange)
reshape=arrange.reshape(3,4)
print(reshape)
##linespace - linearly spaced data
linespce=np.linspace(1,6,5)
print(linespce)
oned=np.arange(15)
twod=oned.reshape(3,5)
threed=np.arange(27).reshape(3,3,3)
print('1,2,3d = ',oned, twod, threed)

##attributes, ndim = dimension of array
##attributes, shape=  shape of the array
##attributes, size = total length of array 3, 9, 27, 81 compoents
## attributes, dtype = types of element integer, float, longest element

##Basic operations
## ** exponential
print(np.add(45,22))
print(np.subtract(45,22))
print(np.array([1,2,3])*15)
print(sum(np.arange(15)))


##how to access [][] first one corresponds to row second to coloumn
#[1 2 3
#[21 3 4]
#index of 21 is [1][0]
##all elements [:][:]

## variable assigned to another variable =
## view copy original data can be manipulated by changing copied dataset
## deep copy : original dataset will be manipulated by changing the copied datsset


##mathematical functional or universal functions
##shape manipulation - split, flatten (ravel), stack (two array to one), resize, reshape
## broadcasting to carry out arithmetic operations. it works only dimesions are same and one of them is scalar
## if two arrays are not same size, valueerror operator could not be broadcased together with shapes

##Linear algegra trace, inverse, transpose


