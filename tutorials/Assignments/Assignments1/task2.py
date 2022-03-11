from numpy import unique
import numpy as np
import pandas as pd
from numpy import where
from sklearn.mixture import GaussianMixture
from sklearn.cluster import SpectralClustering
from sklearn.cluster import OPTICS
from sklearn.cluster import MeanShift
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.cluster import Birch
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import AffinityPropagation
from matplotlib import pyplot 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

pd.set_option('display.max_rows', None)
marketdata = pd.read_csv("MarketData.csv")
dataset=marketdata['Volume']
newdataset=[ [i, j] for i, j in enumerate(marketdata['Volume']) ]
dataset=np.array(newdataset)


model = GaussianMixture(n_components=5)
model.fit(dataset)
y_gaussian = model.predict(dataset)

plt.figure()
y=y_gaussian
clusters = unique(y)
for cluster in clusters:
  index = where(y == cluster)
  plt.scatter(dataset[index, 0],dataset[index, 1],s=0.2)
plt.xlabel('t  (days)')    
plt.ylabel('Volume (arb. unit)') 
plt.show() 

## Gaussian Mixture
model = GaussianMixture(n_components=2)
model.fit(dataset)
y_gaussian = model.predict(dataset)
        
## Spectral clustering
model = SpectralClustering(n_clusters=2)
y_spectral = model.fit_predict(dataset)

## Optics clustering
model = OPTICS(eps=0.8, min_samples=10)
y_optics = model.fit_predict(dataset)

##Mean shift
model = MeanShift()
y_meanshift = model.fit_predict(dataset)

##Minibatch k means
model = MiniBatchKMeans(n_clusters=2)
model.fit(dataset)
y_minikmean = model.predict(dataset)

##Kmeans
model = KMeans(n_clusters=5)
model.fit(dataset)
y_kmean = model.predict(dataset)

##Db scan
model = DBSCAN(eps=0.30, min_samples=9)
y_dbscan = model.fit_predict(dataset)

##Birch
model = Birch(threshold=0.01, n_clusters=2)
model.fit(dataset)
y_birch = model.predict(dataset)

##Agglomerativeclustering
model = AgglomerativeClustering(n_clusters=2)
y_agglo = model.fit_predict(dataset)

##Affinity
model = AffinityPropagation(damping=0.9)
model.fit(dataset)
y_affinity = model.predict(dataset)

 

