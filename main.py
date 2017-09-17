'''Execute solar radiation prediction machine learning algorithm.

Philip Linden
September 10, 2017
'''
## IMPORT LIBRARIES
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plotting tools
from bokeh.plotting import figure, output_notebook, show # advanced and
from bokeh.models import Range1d  # interactive plotting tools

## IMPORT FUNCTIONS
import preprocessing
import explore
import brains

## INGEST DATA
df, units = preprocessing.ingest_data('input/SolarPrediction.csv')
print(df.head())

df['Month'] = df.index.month # add month to view correlation
plt.figure(figsize=(7,7))
explore.corrPairs(df)
df.drop(['Month'], axis=1, inplace=True) # drop temporary column, dates are indexed
df.drop(['WindDirection','WindSpeed'], axis=1, inplace=True) # drop irrelevant features

## EXPLORE data
feature_list=['Radiation','Humidity','Temperature','Pressure']
for feature in feature_list[1:]: # radiation vs feature
    plt.figure(figsize=(18, 6))
    explore.HourlyWeeklyVs(df,feature,feature_list[0],units)

# bivariate density matrix
explore.corrMap(df,feature_list)
plt.show()
