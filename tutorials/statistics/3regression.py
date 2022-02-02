
import numpy as np
import pandas as pd

## once x,y related using correlation, it can be used for prediction using linear regression.


x=[-2,-1,0,1,2,3]
y=[-3,-1,-2,0,4,2]

a=np.cov(x,y)
print(" cov(x) {} cov(x,y) {} cov(y,x) {} cov(y) {} ".format(a[0,0],a[0,1],a[1,0],a[1,1]))

beta=a[0,1]/a[0,0]
alpha=np.mean(y) - beta * np.mean(x)
print("beta = ",beta, "alpha = ", alpha)

df_test = pd.DataFrame({'X data':x,'Y original data':y})
df_test['Y Approximation'] = df_test['X data'] * beta + alpha
df_test['Residue'] = df_test['Y Approximation'] - df_test['Y original data']

df_test.loc['total'] = df_test[['Residue']].sum()
df_test.fillna('',inplace=True)
pd.options.display.float_format = '{:.2f}'.format
print(df_test)


## https://datatofish.com/multiple-linear-regression-python/
# https://www.w3schools.com/python/python_ml_multiple_regression.asp
# https://medium.com/machine-learning-with-python/multiple-linear-regression-implementation-in-python-2de9b303fc0c
#https://www.askpython.com/python/examples/multiple-linear-regression





