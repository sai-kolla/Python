import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

dataframe = pd.read_csv('train.csv', sep=',',usecols=(62,80))


y = dataframe['SalePrice']
x = dataframe['GarageArea']
print('original shape of datashape',dataframe.shape)
plt.scatter(x,y)
plt.title("original dataframe")
plt.ylabel("SalesPrice")
plt.xlabel("GarageArea")
plt.show()

z = np.abs(stats.zscore(dataframe))
threshold = 3
print(np.where(z > 3))
modified_df = dataframe[(z < 3).all(axis=1)]

y = modified_df['SalePrice']
x = modified_df['GarageArea']
print('after removing outliers',modified_df.shape)

plt.scatter(x,y)
plt.title("after deleting outliers")
plt.ylabel("SalesPrice")
plt.xlabel("GarageArea")
plt.show()
