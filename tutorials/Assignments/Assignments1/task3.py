
import numpy as np
import pandas as pd
from matplotlib import pyplot 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def zeroadder(x):
    x=int(x)
    if(x < 10):
        x = str('0')+ str(x)
    return str(x)
    
def mothly_grade(rating):
    if rating > 0.4 :
        return 'Profit L'
    if rating > 0.0:
        return 'Profit S'
    if rating == 0.0:
        return 'Null'
    if rating > -0.2:
        return 'Loss S'
    else:
        return 'Loss L'    

df = pd.read_csv("MarketData.csv")
years= [zeroadder(i) for i in range(2000, 2021, 1)]
months= [zeroadder(i) for i in range(1, 13, 1)]
yearmonths={i+'-'+j:[] for i in years for j in months}
for i in yearmonths:
    for k in range(1,32,1):
        tmp=df.loc[df['Date'] == i+'-'+zeroadder(k)]            
        if(len(tmp) != 0 ):
            yearmonths[i].append(k)

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%b')

mr={}
df_mr = pd.DataFrame(columns=['Year-Month','Month','Monthly-Return'])
for i in yearmonths:
    if(len(yearmonths[i])>0):
        imax=max(yearmonths[i])
        imin=min(yearmonths[i])
        q1 = float(df['Close'].loc[df['Date'] == i+'-'+zeroadder(imax)])
        q2 = float(df['Close'].loc[df['Date'] == i+'-'+zeroadder(imin)])
        mr[i] = mr.get(i,round((q1/q2)-1.0,4))
        mon=list(set(df['Month'].loc[df['Date'] == i+'-'+zeroadder(imin)]))
        df_mr = df_mr.append({'Year-Month':  i,'Month': mon[0], 'Monthly-Return': round((q1/q2)-1.0,4) }, ignore_index=True)


mr_max= max(mr.values())
mr_min= min(mr.values())
mrdate_max= ''
mrdate_min= ''
for k,v in mr.items():
    if(mr_max==v):
        print("max monthly returns = ", k, v)
        mrdate_max= k
    elif(mr_min==v):
        print("min montly returns = ", k, v)
        mrdate_min= k

plt.figure()
plt.scatter(list(mr).index(mrdate_min), mr_min, s=25,label="Minimum montly returns")
plt.scatter(list(mr).index(mrdate_max), mr_max, s=25,label="Maximum montly returns")
plt.scatter(df_mr.index,df_mr['Monthly-Return'],s=4,label="All data")
plt.xlabel('Time  (Months)')    
plt.ylabel('Monthly Returns (arb. unit)') 
plt.legend() 
plt.show()   


print(df_mr.groupby('Month').sum().applymap(mothly_grade))

