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
from bokeh.plotting import figure, output_notebook, show # advanced and
from bokeh.models import Range1d  # interactive plotting tools

## IMPORT FUNCTIONS
import preprocessing
import explore

## INGEST DATA
df, units = preprocessing.ingest_data('input/SolarPrediction.csv')
print(df.head())

## EXPLORE data
explore.humidity(df)
