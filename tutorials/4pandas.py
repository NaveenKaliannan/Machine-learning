
## Pandas is more usefull than other libraries.
## different data structures -  series, data frames, panels.
## viewing, select, accesssing elements in data strcutures.
## handling vector operations

## Numpy is great for mathematic computing. Pandas uses numpy and adds more functionalities
## intrinsic data alignment, data operation functions such as merge, group-by and join method.
## much good for data wrangling and data manipulation
#offers functions for data missing

## two primary strucures of data tools of pandas: series (one dimensional) and data frame (two D)
## Pandas has powerful data strucutres such as series and data frames for data wrangling and
## manipulation

## Pandas features
## Pandas is built on top of Numpy. it is fast and effiencet when it comes to data wrangling
## function makes data data aggregation and transformation easy
## it has tools for reading or writing data in various format
## intellgient and automated data alignment
## high performance merging and joining of data sets

## Data strucutes
## four main libraries
## series (1 D labeled array, supports multiple data types)
## data frame (2D, same as above)
## panel (3D)
## panel4d (4d, no stable version)


## series - 1D array like object containing data and labels (index)
## the data set which contains the data elements and each data elements 
## has a label or index assigned to it. This is called data alignement
## data alignemet takes place automatically
## series can be created multiple way with the help of dict, scalar, list, ndarray

import numpy as np
import pandas as pd

def movie_grade(rating):
    if rating==5:
        return 'A'
    if rating==4:
        return 'B'
    if rating==3:
        return 'C'
    else:
        return 'F'


s=pd.Series(list('abcdef'))
print(s) ## data alignment is done automatically


country=np.array(['lux', 'ind', 'us', 'can', 'aus', 'pak'])
s_country = pd.Series(country)
print(s_country)

country_gdp = pd.Series([100.1, 200, 300],index=['lux', 'ind', 'us'])

scalar_series = pd.Series(5., index=['a','b'])
print(scalar_series)


print(country_gdp)
## accessing elements in series
print("accessing elements = ", country_gdp[0])
print(country_gdp[0:2])
print(country_gdp.loc['us'])
print(country_gdp.iloc[0])

## vectorized opetation in series
vec1=np.array([1,2,3,4])
vec2=np.array([5,6,7,8])
vecstr1=list('abcd')
vecstr2=list('bcad')
s1=pd.Series(vec1,index=vecstr1)
s2=pd.Series(vec2,index=vecstr2)
print(s1+s2) ## added based on the index level
## will print NaN if index doesnt match


## Data Frame - 2D label data structures with coloumns potentially different data types
## it looks like a spread sheet, SQL data tables with rows and coloumns
## data frame can be created using ndarray, dict, list, series, data frame

olymbic = {'host':['london','beijing','athens'],'year':[2012,2008,2004],'no of particpants':[205,204,201]}
df_olymbic =  pd.DataFrame(olymbic)
print(df_olymbic)

print(df_olymbic.host)
print(df_olymbic.describe)

## how to print the coloumns header in dataframe variable.coloumns.values


##data frame from dict 
olymbic = {'london':{2012:205},'beigin':{2008:204}}
df_olymbic=pd.DataFrame(olymbic)
print(df_olymbic) ## will print NaN if data is missing


## data frame from pandas series
olymbic_series=pd.Series([205, 204], index=[2012,2008])
olymbic_series_country=pd.Series(['london', 'beijing'], index=[2012,2008])

df_olymbic = pd.DataFrame({'No of participants': olymbic_series, 'Host':olymbic_series_country})
print(df_olymbic)


## data frame from ndarray
np_array =  np.array([2012, 2008])
dict_ndarray = {'year':np_array}
df_ndarray = pd.DataFrame(dict_ndarray)
print(df_ndarray)

##dataframe from another dataframe
df_new = pd.DataFrame(df_ndarray)
print(df_new)


## Missing values
## fixing data set often missing values.
## data can be missing due to several reason: data not provided by source
## network issue, software issues.
## how to handle

##variable.dropna() drops the elemenet with NaN
## variable.fillna(0) fills the element with 0 instead of Nan
## fist_series.add(second_series, fill_value==0) missing indices will
## be filled with zero. so NaN can be eliminated



## Data operations for faster data processing
df_movie = pd.DataFrame({'movie 1': [5,4,3,3,2,1], 'movie 2': [4,5,2,3,4,2] }, index=['tom','jeff','peter','ram','ted','paul'])
print(df_movie)
print(df_movie.applymap(movie_grade))

## df = pd.DataFrame([[np.nan, 2, np.nan, 0], [3, 4, np.nan, 1],  [np.nan, np.nan, np.nan, 5], [np.nan, 3, np.nan, 4]], columns=list("ABCD"))

## with statistical functions
df_test = pd.DataFrame({'test1':[95,84,73],'test2':[74,72,81]},index=['jack','nav','karth'])
print(df_test)
print(df_test.max())
print(df_test.mean())
print(df_test.std())


## Data operations using groupby
df_president = pd.DataFrame({'first':['george','bill'], 'last':['bush','clinton']})
print(df_president)
grouped=df_president.groupby('first')
grp=grouped.get_group('george')
print(grp)
print(df_president.sort_values('first'))


## Data standardization



## pandas data operation- merge, duplicate and concatentation
## merge -  pd.merge(variable1, variable2), pd.merge(vairable1,varable2,on='student')
## pd.merge(,,on='ID',how='left').fillna('x')

##concat pd.concat([variable1,variable2], ignore_index=True)
## dfnewdata.duplicated() - check for duplicate values
## dfnewdata.drop_diplicates() drops duplicate values
## dfnewdata.dro[ps_duplicates('ID') drops duplicted values by ID



##File read and write opertations -csv, json, sql, excel, hdf, html and etc
## read_excel, read_csv - to read a file
## to_excel, to_csv = to write a file

