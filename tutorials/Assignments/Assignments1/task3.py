import numpy as np
import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

## Zeroadder
def zeroadder(x):
    x=int(x)
    if(x < 10):
        x = str('0')+ str(x)
    return str(x)

## Reading the market data file
df = pd.read_csv("https://raw.githubusercontent.com/NaveenKaliannan/Machine-learning/main/tutorials/Assignments/Assignments1/MarketData.csv")    
print(df.head())

## finding the days in each month
years= [zeroadder(i) for i in range(int(min(set(pd.DatetimeIndex(df['Date']).year))), int(max(set(pd.DatetimeIndex(df['Date']).year)))+1, 1)]
months= [zeroadder(i) for i in range(1, 13, 1)]
yearmonths={i+'-'+j:[] for i in years for j in months}
for i in yearmonths:
    for k in range(1,32,1):
        tmp=df.loc[df['Date'] == i+'-'+zeroadder(k)]            
        if(len(tmp) != 0 ):
            yearmonths[i].append(k)           

## Calculating Monthly returns
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%b')
mr={}
df_mr = pd.DataFrame(columns=['Year-Month','Month','Monthinnumbers','Monthly-Return'])
for i in yearmonths:
    if(len(yearmonths[i])>0):
        imax=max(yearmonths[i])
        imin=min(yearmonths[i])
        q1 = float(df['Close'].loc[df['Date'] == i+'-'+zeroadder(imax)])
        q2 = float(df['Close'].loc[df['Date'] == i+'-'+zeroadder(imin)])
        mr[i] = mr.get(i,round((q1/q2)-1.0,4))
        mon=list(set(df['Month'].loc[df['Date'] == i+'-'+zeroadder(imin)]))
        df_mr = df_mr.append({'Year-Month':  i,'Month': mon[0], 'Monthly-Return': round((q1/q2)-1.0,4), 'Monthinnumbers':i[-2]+i[-1] }, ignore_index=True)  
print(df_mr)        

## Finding outliers from the montly returns datset
np_a = np.array(df_mr['Monthly-Return'])
print(" Monthly Returns for Entire Dataset : \n Min = {},\n 25th-quantile = {},\n 50th-quantile = {},\n 75th-quantile = {},\n Max = {},\n Mean ={}"
      .format(min(np_a), np.quantile(np_a, 0.25), np.quantile(np_a,0.5), np.quantile(np_a,0.75),  max(np_a),  np.mean(np_a)))

q3, q1 = np.percentile(np_a, [75 ,25])
iqr = q3 - q1

red_square = dict(markerfacecolor='r', marker='s')
fig1, ax1 = plt.subplots()
ax1.set_title('Distribution of Monthly-Return (Whis = 1.7)')
ax1.boxplot(np_a, vert=True, flierprops=red_square, whis=1.7)
fig1.savefig("barplot.png", format="png")
plt.show()

## whis=1, 2.025σ 95 percent
## whis=1.5, 2.7σ  99 percent
## whis=1.7, 3σ  99.72 percent
## whis=2, 3.375σ  99.99 percent

outliers=[]
whis=1.7
Ubound=q3 + whis * iqr
Lbound=q1 - whis * iqr 
for i in np_a:
    if(i > Ubound or i < Lbound ):
        outliers.append(i)
print("Outliers = {},\nUpper Bound = {},\nLower Bound = {}".format(outliers, Ubound, Lbound ) )


## Removing outliers from the dataset
print("Shape b4 removing outliers = ",df_mr.shape)
df_mr = df_mr[(df_mr["Monthly-Return"] < Ubound) & (df_mr["Monthly-Return"] > Lbound)]
print("Shape after removing outlier = ",df_mr.shape)

for key, value in dict(mr).items():
    if value in outliers:
        del mr[key]


## Finding the best and worst month to invest
mr_max= max(mr.values())
mr_min= min(mr.values())
mrdate_max= ''
mrdate_min= ''
for k,v in mr.items():
    if(mr_max==v):
        mrdate_max= k
    elif(mr_min==v):
        mrdate_min= k

plt.figure() 
gf_mon =df_mr.groupby('Month').mean().sort_values(by='Monthly-Return',ascending=False)
maxmon=list(gf_mon.max())
minmon=list(gf_mon.min())
maxmon=maxmon[0]
minmon=minmon[0]
plt.scatter(list(df_mr.loc[df_mr["Month"] == gf_mon.index[0]].index), list(df_mr["Monthly-Return"].loc[df_mr["Month"] == gf_mon.index[0]]), s = 35, marker="s", label="Best month to invest - " + gf_mon.index[0] )
plt.scatter(list(df_mr.loc[df_mr["Month"] == gf_mon.index[-1]].index), list(df_mr["Monthly-Return"].loc[df_mr["Month"] == gf_mon.index[-1]]), s = 35, marker="d", label="Worst Month to invest - " + gf_mon.index[-1] )
plt.scatter(df_mr.index,df_mr['Monthly-Return'],s=4,label="All data")
plt.xticks(np.arange(1, 250, 12), np.arange(2000, 2021, 1), rotation='vertical')
plt.xlabel('Time  (Months)')    
plt.ylabel('Monthly Returns (arb. unit)')
plt.legend(loc='best')
plt.savefig("monthlyreturn.png", format="png")
plt.show()


def monthrating(rating):
    if rating > 0.01:
        return 'A_Strongprofit'
    if rating > 0 and rating <= 0.01:
        return 'B_Profit'
    if rating == 0:
        return 'C_NoGain'    
    if  rating < 0:
        return 'D_Loss'
    
gf_mon=gf_mon.sort_values(by=['Monthly-Return'], axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
print(gf_mon)    
gf_mon=gf_mon.sort_values(by=['Month'], axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
gf_mon['Rating'] = gf_mon['Monthly-Return'].map(monthrating)


## Best Months to invest based on Decision Tree
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing


def monthrating_qr(rating):
    if rating > 0.02:
        return 'A_Strongprofit'
    if rating > 0:
        return 'B_Profit'
    if rating == 0:
        return 'C_NoGain'    
    if rating < 0:
        return 'D_Loss'


##df_mr = df_mr.sort_values(by=['Month'], axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
X =  np.array(df_mr['Month'])
le = preprocessing.LabelEncoder()
X_train=le.fit_transform(X)
Y_train= np.array(df_mr['Monthly-Return'].map(monthrating_qr))
model = DecisionTreeClassifier()
model.fit(X_train.reshape(-1, 1), Y_train)
Xtest=np.arange(0,12,1)
predictions = model.predict(Xtest.reshape(-1, 1))
df_decisiontree=pd.DataFrame({"Month":le.inverse_transform(Xtest), "Investment":predictions})
df_decisiontree.sort_values(by=['Month'], axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)


## Error metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
print(classification_report(gf_mon['Rating'], df_decisiontree['Investment']))
print(confusion_matrix(gf_mon['Rating'], df_decisiontree['Investment']))

from sklearn.metrics import accuracy_score
y_true = gf_mon['Rating']
y_predict = df_decisiontree['Investment']
print("Accuracy of my model = {}".format(accuracy_score(y_true, y_predict)))
