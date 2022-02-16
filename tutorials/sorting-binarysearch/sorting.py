import random 
from random import uniform
from random import seed
from random import random
from random import randint
import math

def sumfactorial(n):
    if n == 0:
        return 0
    else:
        return n + sumfactorial(n-1)



def bubblesort(x):
    n=len(x)
    scaling=0
    for i in range(n-1):    
        ## at the end of the first iteration, the bubble sort takes the largest number to the end of the list
        ## at the end of the second iteration, the second largest number is taken to the [-2] position
        ## the lowest number is slowly moves to the initial index iteration by iterations.
        ## scaling is sum of factorial elements of (n-1) which is n*(n-1)/2 
        ## https://stackoverflow.com/questions/44252596/big-o-complexity-for-n-n-1-n-2-n-3-1/44255732
        for j in range(0,n-1-i):            
            if x[j] > x[j + 1] :
                x[j], x[j + 1] = x[j + 1], x[j]    
            scaling+=1
    print(n, scaling, sumfactorial(n-1), n*(n-1)/2)
    

seed(1)
xint=[ randint(0, 10) for i in range(100)]


print(max(xint), min(xint))    
print(max(xfloat), min(xfloat)) 

for j in range(2,100,5):
    xfloat=[ uniform(1, 10) for i in range(j)]
    bubblesort(xfloat) 



