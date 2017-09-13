'''Execute solar radiation prediction machine learning algorithm.
This function has no arguments.

Philip Linden
September 10, 2017
'''
## IMPORT LIBRARIES
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plotting tools
import seaborn as sns # advanced plotting tools

## IMPORT FUNCTIONS
import preprocessing
import showme

## INGEST DATA
df, units = preprocessing.ingest_data('input/SolarPrediction.csv')
print(df.head())

# give the algorithm weather and calendar info for 2-3 days prior and let it predict a distribution over the course of a day. the answer is the area under that curve.
