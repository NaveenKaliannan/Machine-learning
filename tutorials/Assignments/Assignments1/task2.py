import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')


## Reading the data
df_marketdata = pd.read_csv("https://raw.githubusercontent.com/NaveenKaliannan/Machine-learning/main/tutorials/Assignments/Assignments1/MarketData.csv")

print(df_marketdata)

df_fractional=pd.DataFrame(columns=['p1','p2','p3'])

opn=np.array(df_marketdata['Open'])
close=np.array(df_marketdata['Close'])
volume=np.array(df_marketdata['Volume'])

p1 = [ (opn[i]/opn[i-1])-1 for i in range(1,df_marketdata.shape[0],1)]
p2 = [ (opn[i]/close[i])-1 for i in range(1,df_marketdata.shape[0],1)]
p3 = [ (volume[i]/volume[i-1])-1 for i in range(1,df_marketdata.shape[0],1)]


for i in range(0,df_marketdata.shape[0]-1,1):
    df_fractional = df_fractional.append({'p1': p1[i] ,'p2': p2[i], 'p3': p3[i] }, ignore_index=True)  

print(df_fractional)
newdataset=np.array(df_fractional)


from sklearn.cluster import KMeans

model = KMeans(n_clusters=3)
model.fit(newdataset)
y_kmean = model.predict(newdataset)

## Plotting the data
from numpy import unique
from numpy import where
from matplotlib import pyplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

y=y_kmean
rw=1
clm=3

fig, axs = plt.subplots(1, 3, figsize=(18,6), dpi=80)
figure(figsize=(18, 6), dpi=80 )
clusters = unique(y)

for cluster in clusters:
    index = where(y == cluster)
    
    axs[0].scatter(newdataset[index, 0],newdataset[index, 1],s=0.2)
    axs[0].set_xlabel('Fractional difference of Open(C)/Open(P)') 
    axs[0].set_ylabel('Fractional difference of Open(C)/Close(C)') 
    axs[0].set_title('P1 Vs P2')  
    
    axs[1].scatter(newdataset[index, 2],newdataset[index, 0],s=0.2)
    axs[1].set_xlabel('Fractional difference of Volume')    
    axs[1].set_ylabel('Fractional difference of Open(C)/Open(P)') 
    axs[1].set_title('P1 vs P3')

    axs[2].scatter(newdataset[index, 2],newdataset[index, 1],s=0.2)
    axs[2].set_xlabel('Fractional difference of Volume')    
    axs[2].set_ylabel('Fractional difference of Open(C)/Close(C)') 
    axs[2].set_title('P2 Vs P3') 
    
fig.savefig("Clusterparameters.png", format="png")
plt.show()
plt.close()


