import numpy as np
import pandas as pd
from sklearn.datasets import load_boston

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
bostondataset= load_boston()
#print(bostondataset['DESCR'])
#print(bostondataset['feature_names'])
df = pd.DataFrame(bostondataset.data)
df.columns = bostondataset.feature_names
print(df.head())
print(df.shape)
print(bostondataset['target'])
