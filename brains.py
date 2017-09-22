'''The brain of the Solar Radiation Predictive Algorithm.

Philip Linden
September 17, 2017
'''
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import preprocessing # ML tools
from sklearn.model_selection import train_test_split # split data

from bokeh.plotting import figure, show, output_notebook

def plot_test(clf,X_test,y_test):
    y_predicted = clf.predict(X_test)

    p = figure(tools='pan,box_zoom,reset',x_range=[0, 100], title='Model validation',y_axis_label='radiation')
    p.grid.minor_grid_line_color = '#eeeeee'

    p.line(range(len(y_test)),y_test,legend='actual',line_color='blue')
    p.line(range(len(y_test)),y_predicted,legend='prediction',line_color='red')
    output_notebook()
    show(p)
    return

def train_model(df,clf,debug=False):
    ''' Train algorithm.
    inputs:
        df      as DataFrame
        alg     as string (if unrecognized, use default)
    returns:
        clf     as trained classifier
        accuracy  as float
    '''
    X = df.drop('Radiation',axis=1).as_matrix()
    y = df['Radiation'].as_matrix()
    X =  preprocessing.scale(X)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
    model = clf.fit(X_train,y_train)
    accuracy = clf.score(X_test,y_test)
    if debug: plot_test(clf,X_test,y_test)
    return clf, model, accuracy, X_test, y_test
