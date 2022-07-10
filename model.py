import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing

housing= fetch_california_housing()
X= pd.DataFrame(data= housing.data, columns= housing.feature_names)
X.drop(columns=['MedInc', 'AveBedrms', 'Population', 'Latitude', 'Longitude'], inplace = True)
y= pd.DataFrame(data= housing.target)


X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.3, random_state= 100)
lm= LinearRegression()
lm.fit(X_train, y_train)
pickle.dump(lm, open('model.pickle', 'wb'))
