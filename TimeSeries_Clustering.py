!pip install tslearn
import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/gdriv')

data_path = "/content/gdriv/My Drive/Colab Notebooks/Data" 
stock = pd.read_csv(data_path + '/base123.csv')
stock.head()

name = stock.iloc[:,0]
print(name)

train = stock.iloc[:,1:].values
train

from tslearn.clustering import TimeSeriesKMeans
model = TimeSeriesKMeans(n_clusters = 15, metric = "dtw", max_iter = 10) 
model.fit(train)

res = model.fit(train)
res.labels_
cluster_res = pd.concat([name,pd.DataFrame(res.labels_)],axis=1)
cluster_res.columns = ['name','cluster']
cluster_res
cluster_res.loc[cluster_res['cluster']==1,'name']

cluster_dt = pd.concat([cluster_res,pd.DataFrame(train)],axis=1)
print(cluster_dt)

cluster0 = cluster_dt.loc[cluster_dt['cluster']==1,:]
print(cluster0)

for x in range(15):
  clu = cluster_dt.loc[cluster_dt['cluster']== x ,:]
  Win = 0
  Lose = 0
  Draw = 0
  for i in clu['name']:
    if i == '승':
      Win += 1
    elif i == '패':
      Lose += 1
    else:
      Draw += 1
  print(Win, Lose, Draw)
  
  cluster = cluster0.iloc[:,2:].reset_index(drop=True)
  
  import matplotlib.pyplot as plt
  
  for i in range(len(cluster)):
  plt.plot(cluster.iloc[i,:])
plt.show()

for k in range(15): # k는 군집수
  cluster0 = cluster_dt.loc[cluster_dt['cluster']==k,:]
  cluster = cluster0.iloc[:,2:].reset_index(drop=True)
  for i in range(len(cluster)):
    plt.plot(cluster.iloc[i,:])
  plt.title('Cluster' + str(k))
  plt.show()
  
