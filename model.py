import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing

housing= fetch_california_housing()
X= pd.DataFrame(data= housing.data, columns= housing.feature_names)
X.drop(columns=['MedInc', 'AveBedrms', 'Population', 'Latitude', 'Longitude'], inplace = True)
X
y= pd.DataFrame(data= housing.target)
#y
0
0	4.526
1	3.585
2	3.521
3	3.413
4	3.422
...	...
20635	0.781
20636	0.771
20637	0.923
20638	0.847
20639	0.894
20640 rows × 1 columns

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.3, random_state= 100)
lm= LinearRegression()
lm.fit(X_train, y_train)
LinearRegression()
pickle.dump(lm, open('modell.pickle', 'wb'))