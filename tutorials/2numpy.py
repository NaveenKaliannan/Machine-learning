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
