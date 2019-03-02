from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

#importing the data set
wh = pd.read_csv('weatherHistory.csv')

#searching for attributes which have null values
print(wh["Precip Type"].isnull().any())

#finding the correlation for better training of the model by selecting the appropriate features
print(wh.corr())

#dropping the columns since they have less correlation with target class
wh = wh.drop(columns=['Summary','Precip Type','Daily Summary' ],axis=1)

#replacing the null values with mean
wh.select_dtypes(include=[np.number]).interpolate().dropna()


X_train, X_test = train_test_split(wh, test_size=0.2)
y_train=X_train['Temperature (C)']

X_train=X_train.drop(columns=['Temperature (C)'])
y_test=X_test['Temperature (C)']
X_test=X_test.drop(columns=['Temperature (C)'])



#creation of regression model and training it
reg=LinearRegression().fit(X_train,y_train)


pred=reg.predict(X_test)

#evaluation of model using metrics
mean_squared_error = mean_squared_error(y_test, pred)
r2_score = r2_score(y_test,pred)
print("mean squared error is :",mean_squared_error)
print("r2_score is: ", r2_score)
