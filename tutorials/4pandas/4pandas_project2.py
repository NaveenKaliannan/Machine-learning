
import numpy as np
import pandas as pd

pd.set_option('display.max_rows', None)
df=pd.read_csv('FDNY.csv')
## skipping rows 1 df=pd.read_csv('FDNY.csv',skiprows=[1])

df.head()
df.describe()
df.count()
df.dtypes()
print(df.columns.values)

print(df)
df=df.drop(index=[0])

print(df['FacilityName'].shape)
newdf=df.dropna(subset=['FacilityName'])
print(newdf['FacilityName'].shape)


freq=df.groupby('Borough')
print(freq.size())
print("total facilities = ",freq.size().sum())

print(freq.get_group('Manhattan'))



#freq=df.groupby('FacilityName')
#print(freq.size())
