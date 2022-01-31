
## covariance and correlation -  relationship between a pair of quantitative measures

## positive covariance x and y are proportional.
## negative covariance x and y are inversely proportional . 
## zero. no relation.

## correlation is calculated from covariance divided by standard deviations. if correlation is zero, the data are uncorrelated. the correlation lies between -1 and 1 since normalized by standard deviation of each data


## https://stackabuse.com/covariance-and-correlation-in-python/:  Both covariance and correlation are about the relationship between the variables. Covariance defines the directional association between the variables. Covariance values range from -inf to +inf where a positive value denotes that both the variables move in the same direction and a negative value denotes that both the variables move in opposite directions.
#Correlation is a standardized statistical measure that expresses the extent to which two variables are linearly related (meaning how much they change together at a constant rate). The strength and directional association of the relationship between two variables are defined by correlation and it ranges from -1 to +1. Similar to covariance, a positive value denotes that both variables move in the same direction whereas a negative value tells us that they move in opposite directions.

import numpy as np

x=[-1, 3.5, 10, 20]
y=[100,7, 4, -10]

print("cov x = ", np.cov(x))
print("cov y = ", np.cov(y))


print("covariance matrix = ", np.cov(x,y))

a=np.cov(x,y)

print(" cov(x) {} cov(x,y) {} cov(y,x) {} cov(y) {} ".format(a[0,0],a[0,1],a[1,0],a[1,1]))


## once x,y related, it can be used for prediction using linear regression.



