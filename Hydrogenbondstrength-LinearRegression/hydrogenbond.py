import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.linear_model  import LinearRegression
from sklearn.model_selection import train_test_split


x=pd.DataFrame({"OOdistance":[3.0403,3.05448,2.76165,2.79708,2.81989,3.09176,2.84921,2.8436,2.53183,2.80706], "OH distance":[2.05667,2.10339,1.7412,1.92955,1.85736,2.13437,1.88446,1.93638,1.58517,1.77929]})
y=pd.DataFrame({"hydrogenbondstrength":[-8.39084,-5.15736,-30.0507,-9.47462,-15.1347,-6.47587,-13.2604,-13.1133,-36.0654,-18.6279]})

linreg=LinearRegression()
linreg.fit(x,y)
print("beta = ",linreg.coef_)
print("alpha = ",linreg.intercept_)

xnew=pd.DataFrame({"OOdistance":[2.81939],"OH distance":[1.86484]})

print(linreg.predict(xnew))
