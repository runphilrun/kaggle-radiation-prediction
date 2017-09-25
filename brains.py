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
    ''' Plot trained algorihm against test inputs.
    inputs:
        clf         as classifier   the trained algorithm
        X_test      as array        training data, unordered
        y_test      as array        outputs corresponding to training data
    '''
    y_predicted = clf.predict(X_test)

    p = figure(toolbar_location='right',x_range=[0, 100], title='Model validation',y_axis_label='radiation')
    p.grid.minor_grid_line_color = '#eeeeee'

    p.line(range(len(y_test)),y_test,legend='actual',line_color='blue')
    p.line(range(len(y_test)),y_predicted,legend='prediction',line_color='red')
    # output_notebook()
    show(p)
    return

def plot_real(clf,x,y_actual,index):
    ''' Plot predictions for actual measurements.
    inputs:
        clf         as classifier   the trained algorithm
        x           as array        timeseries of measurement inputs
        y_actual    as array        corresponding timeseries of actual results
    '''
    y_predicted = clf.predict(x)

    p = figure(toolbar_location='right', title='Predicted vs Actual',x_axis_label='time', y_axis_label='radiation',x_axis_type="datetime")
    p.grid.minor_grid_line_color = '#eeeeee'

    p.line(index,y_actual,legend='actual',line_color='blue')
    p.line(index,y_predicted,legend='prediction',line_color='red')
    # output_notebook()
    show(p)
    return

def train_model(X,y,clf,debug=False):
    ''' Train algorithm.
    inputs:
        X       as array        features
        y       as array        label(s)
        clf     as scikit-learn classifier (untrained)
    returns:
        clf     as trained classifier
        accuracy  as float
    '''
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
    model = clf.fit(X_train,y_train)
    accuracy = clf.score(X_test,y_test)
    return clf, model, accuracy, X_test, y_test

def go(x,y,algorithm,debug=True):
    ''' Easy model train and test. '''
    clf, model, accuracy, X_test, y_test=train_model(x,y,algorithm,debug=True)
    print('Accuracy: %s percent'%str(accuracy*100))

    if debug:
        plot_test(clf,X_test,y_test)
        plot_real(clf,x,y,df.index.values)
    return

def optimize_randomforest(x,y,try_n=10,try_f='auto',try_s=1):
    ''' Find best combo of tunable params for random forest regressor. '''
    best_score = float('-inf') # initialize score
    for n in try_n:
        for f in try_f:
            for s in try_s:
                clf = RandomForestRegressor(oob_score=True,n_estimators=n,max_features=f,min_samples_leaf=s,n_jobs=-1)
                clf.fit(x,y)
                if clf.oob_score_ > best_score:
                    best_score, best_clf, best_n, best_f, best_s = clf.oob_score_, clf, n, f, s
    return clf, best_n, best_f, best_s
