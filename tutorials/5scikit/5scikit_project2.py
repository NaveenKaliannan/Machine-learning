import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.linear_model  import LinearRegression
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
bostondataset= load_boston()

#print(bostondataset['DESCR'])
#print(bostondataset['feature_names'])
df = pd.DataFrame(bostondataset.data)
df.columns = bostondataset.feature_names
df['price'] = bostondataset.target
print(df.head())
print(df.shape)


x_input_explanatory = bostondataset.data
y_output_response_target = bostondataset.target
linreg = LinearRegression()
linreg.fit(x_input_explanatory,y_output_response_target)

print("intecept =  {}".format(linreg.intercept_))
print("coeff =  {}, {}".format(linreg.coef_, len(linreg.coef_)))

x_train,x_test,y_train,y_test = train_test_split(x_input_explanatory,y_output_response_target)
linreg.fit(x_train,y_train)

print("Mean square error = %.2f ",  np.mean((linreg.predict(x_test) - y_test)**2)  )
print("variance = %.2f ",  linreg.score(x_test,y_test)  )
