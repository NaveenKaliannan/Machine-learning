import numpy as np
import matplotlib.pyplot as plt
import math 
## gd means gradient descendant method


## simple gd without adaptive step size
def simplegd():      
    x0=100
    alpha=0.01
    tol=0.0000001
    
    ## plotting the function    
    x=np.arange(-0.15,0.1,0.01,dtype='float')
    func=lambda x : 13*x**2 + 2*x + 7
    y= func(x)    
    plt.figure()
    plt.plot(x,y,color='red',label='y(x)=13*x*x + 2*x + 7')
    
    for i in range(100000):
        xold=x0
        xnew=x0 - alpha*(26*x0+2)  ## derivate must be added
        x0 = xnew
        if(abs(xnew-xold)<tol):
            print("Number of iterations to converge = {}".format(i))
            break        
    print(xnew)
    plt.scatter(xnew,func(xnew),color='green',label='minima')
    plt.xlabel('x')    
    plt.ylabel('y(x)') 
    plt.title('Simple gradient descent without adaptive step size') 
    plt.legend(loc='best')
    plt.show()  
         
## main implementation    
simplegd() 
