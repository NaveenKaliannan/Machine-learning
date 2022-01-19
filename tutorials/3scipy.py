##scipy-extension of numpy used for scientific and advanced mathematics algo and functions
## it contains mathematical integration, linear algebra, statistics, image processing, language integration.
## characteristics -  built in mathematical libraries, high level commands for data manipulation and visulatization, efficient and fast data processing, large libraries.

## widely used packages - cluster algo (pattern), constants (mathematical and physical), fftpack (fast fourier transform), integrate (ode), spatial, interpolate (smooth splines), IO input and output, linalg (linear algebra), ndimage (N-dimensaional image processing), odr orthogonal distance regression , optimize, signal processing signal, sparse for sparse matrices, weave for c/c++ integration, stats for statistics, special for special function

## integrate function used for integration
## quad means quad library from fortran
##integrate.dblquad() .tplquad((), nquad()

from numpy as np
from scipy.integrate import quad

## Optimisation package improves the performace mathematically by controlling the parameters
## conjugate gradeint method
## optimiser.minimize(). root() gives the root of a function
## optimiser.curve_fit
## in optimizer , method used should be defined method='bfgs'

## for cuve fitting, one needs to specify the upper limit and lower limit. 


## Linear algebra 
from scipy import linalg
# linalg 
## linalg.inv(matrix)
## linalg.det(matrix)
## linalg.solve(matrixA, vecx)
## linalg.svd(matrixA)

## eigenvalue, eigenvector = linalg.eig(matrix)
## firsteigenvalue, secondeigenvalue =  eigenvalue
## print(eigenvector[:][0], eigenvector[:,1])



#statistics package
##pdf(), cdf()
## linregress()
## describe(), normaltest()

## cdf- cumulative probability total probability = 1
## pdf - probability density function of random vairable
## is the derivate of cdf with respect x

from scipy.stats import norm

## norm.rvs()
## norm.cdf()
## norm.pdf()

## weave package - includes c/c++ library - speeds up to 1.5x to 30x  compared to algorithms writen python inline() blitz() for faster execution

## IO packages. for file fomats, matlab files, idl files, matrix market files, arff files, netcdf files.

##NumPy.loadtxt()/.savetxt()
##NumPy.genfromtxt()/.recfromcsv()
##NumPy.save()/NumPy.load()


