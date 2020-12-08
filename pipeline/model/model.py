import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import (
    LinearRegression,
    Ridge,
    Lasso,
    ElasticNet,
    RidgeCV,
    LassoCV,
    ElasticNetCV,
)
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

import pickle

df = pd.read_csv("pipeline/model/ready_to_model_df.csv")


X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=41, test_size=0.2) 

regressor = LinearRegression()
regressor.fit(X_train, y_train)
pickle.dump(regressor, open('pipeline/model/model.pkl', 'wb'))