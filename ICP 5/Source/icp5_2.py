import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')


dataset = pd.read_csv('College.csv')
x = dataset.iloc[:,[9,10]]



#Standardize features by removing the mean and scaling to unit variance.
scaler = preprocessing.StandardScaler()
#Compute the mean and std to be used for later scaling.
scaler.fit(x)
#Perform standardization by centering and scaling
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)


nclusters = 2 # this is the k in kmeans
seed = 0

km = KMeans(n_clusters=nclusters, random_state=seed)
km.fit(X_scaled)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(X_scaled)
print(y_cluster_kmeans)

#calculating the silhouette score
from sklearn import metrics
score = metrics.silhouette_score(X_scaled, y_cluster_kmeans)
print('silhouette_score :', score)

#plotting the clusters
LABEL_COLOR_MAP = {0 : 'r',
                   1 : 'y',
                   2 : 'g',
                   3 : 'k',
                   4 : 'b'
                   }
label_color = [LABEL_COLOR_MAP[l] for l in km.predict(X_scaled)]
plt.scatter(X_scaled_array[:, 0], X_scaled_array[:, 1], c=label_color)
plt.show()