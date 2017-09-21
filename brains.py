'''The brain of the Solar Radiation Predictive Algorithm.

Philip Linden
September 17, 2017
'''
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import preprocessing, cross_validation # ML tools
from sklearn.linear_model import LinearRegression

def model(df, debug=True):

    X = np.array(df.drop(['Radiation']),1)
    
