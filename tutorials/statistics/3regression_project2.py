#https://datatofish.com/multiple-linear-regression-python/

import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.linear_model  import LinearRegression
from sklearn.model_selection import train_test_split


Stock_Market = {'Year': [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],
                'Month': [12, 11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1],
                'Interest_Rate': [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],
                'Unemployment_Rate': [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],
                'Stock_Index_Price': [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719]        
                }
        
df=pd.DataFrame(Stock_Market)

x=pd.DataFrame(df[['Interest_Rate','Unemployment_Rate']])
y=pd.DataFrame(df['Stock_Index_Price'])

linreg=LinearRegression()
linreg.fit(x,y)
print("beta = ",linreg.coef_)
print("alpha = ",linreg.intercept_)

xnew=pd.DataFrame({'Interest_Rate': [2.75,2.5,2.5], 'Unemployment_Rate': [5.3,5.3,5.3]})

print(linreg.predict(xnew))






