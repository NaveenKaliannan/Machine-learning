import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model  import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

iris_data = load_iris()
print(type(iris_data))
#print(iris_data.DESCR)
print(iris_data.feature_names)
print(iris_data.target)
print(iris_data.data.shape)
x_feature = iris_data.data
y_target = iris_data.target
print(x_feature.shape,y_target.shape)
knn = KNeighborsClassifier(n_neighbors=1)
print(knn)
knn.fit(x_feature,y_target)
xnew=[[3,5,4,1],[5,3,4,2]]
knn.predict(xnew)
logreg = LogisticRegression()
logreg.fit(x_feature,y_target)
print("predict = " ,logreg.predict(xnew))
