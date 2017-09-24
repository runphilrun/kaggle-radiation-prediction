'''Execute solar radiation prediction machine learning algorithm.

Philip Linden
September 10, 2017
'''
## IMPORT LIBRARIES
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plotting tools

# IMPORT ML CLASSIFIERS
from sklearn.linear_model import LinearRegression # Linear regression
from sklearn.ensemble import RandomForestRegressor # random forest regression
from sklearn.neural_network import MLPRegressor # neural network regression
from sklearn.svm import SVR # support vector regression

## IMPORT FUNCTIONS
import preprocessing, explore, brains

## INGEST DATA
df, units = preprocessing.ingest_data('input/SolarPrediction.csv')
print(df.head())

df['WeekOfYear'] = df.index.week # add datetime components to view correlation
plt.figure(figsize=(7,7))
explore.corrPairs(df)
df.drop(['WindDirection','WindSpeed'], axis=1, inplace=True) # drop irrelevant features

## EXPLORE DATA
feature_list=['Radiation','Humidity','Temperature','Pressure']
for feature in feature_list[1:]: # radiation vs feature
    plt.figure(figsize=(18, 6))
    explore.HourlyWeeklyVs(df,feature,feature_list[0],units)

# bivariate density matrix
explore.corrMap(df,feature_list)
plt.show()

df['TimeOfDay'] = df.index.hour # add time of day to correlation

## IMPLEMENT ALGORITHM
algorithm = RandomForestRegressor()

x = df.drop('Radiation',axis=1).as_matrix()
y = df['Radiation'].as_matrix()

brains.go(x,y,algorithm,debug=True)
