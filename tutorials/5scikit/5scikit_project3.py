## https://www.datacamp.com/community/tutorials/k-nearest-neighbor-classification-scikit-learn
## https://www.analyticsvidhya.com/blog/2021/04/simple-understanding-and-implementation-of-knn-algorithm/

## K Nearest neighbor is used for classification problem. 
## The idea of this method is to predict a value based on the neighbors and how far away
## The most important paramter in this method is defining neighbors and distance metric
## How to find suitable neigbors? use error graph for different k values. 
## Lower k values will overfit and higher k values will underfilt. chose optimium ones based on the error.

##plot
from mpl_toolkits import mplot3d
from matplotlib import pyplot 
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from sklearn import preprocessing
# Converting a feature or target (yes or no) into numbers (1 or 0).
#le = preprocessing.LabelEncoder()
#features=le.fit_transform(features) 

from sklearn.datasets import load_iris
from sklearn.linear_model  import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

iris_data = load_iris()

x_feature = iris_data.data
y_target = iris_data.target
print(iris_data.feature_names)
print(iris_data.target)
print(iris_data.data.shape)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_feature,y_target)
xnew= x_feature ##[0:140:5,:]
print(xnew)
#np.array([[0, 0, 0, 0.2],[0, 0, 0, 1.3],[0, 0, 0, 1.5],[0, 0, 0, 1.6],[7.3, 0, 0, 1.8]])
predicted = knn.predict(xnew)
print(predicted)

#model = LogisticRegression()
#model.fit(x_feature,y_target)
#predicted = model.predict(xnew)


ys=predicted
xs=np.array(xnew[:,3])
ys = [xf for _,xf in sorted(zip(xs, ys))]
xs.sort()

##2D plot
plt.scatter(xnew[:,3], predicted ,c='red', label='Actual')
plt.plot(xs, ys ,c='green', label='Predicted')
plt.legend(loc="best")
#plt.title('Input (x) versus Output (y)')
plt.xlabel('petal width')
plt.ylabel('Target')
plt.show()








