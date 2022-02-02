import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.linear_model  import LinearRegression
from sklearn.model_selection import train_test_split


x=pd.DataFrame([-2,-1,0,1,2,3])
y=pd.DataFrame([-3,-1,-2,0,4,2])

linreg=LinearRegression()
linreg.fit(x,y)
print("beta = ",linreg.coef_)
print("alpha = ",linreg.intercept_)

xnew=pd.DataFrame([1.5,2.5,0])

print(linreg.predict(xnew))






