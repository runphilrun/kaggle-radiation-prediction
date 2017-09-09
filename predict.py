# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plotting tools
import seaborn as sns # advanced plotting tools

## preprocessing

data=pd.read_csv('input/SolarPrediction.csv')

# Data column is unused
data.drop(['Data'], axis = 1, inplace = True)

# interpret columns as appropriate data types
data['UNIXTime'] = data['UNIXTime'].astype(str)
data['Time'] = data['Time'].astype(str)
data['Radiation'] = data['Radiation'].astype(float)
data['Temperature'] = data['Temperature'].astype(float) # or int
data['Pressure'] = data['Pressure'].astype(float)
data['Humidity'] = data['Humidity'].astype(int) # or int
data['WindDirection(Degrees)'] = data['WindDirection(Degrees)'].astype(float)
data['Speed'] = data['Speed'].astype(float)
data['TimeSunRise'] = data['TimeSunRise'].astype(str)
data['TimeSunSet'] = data['TimeSunSet'].astype(str)


# convert units to SI
data.loc[:,'Temperature'] = (data.loc[:,'Temperature'] + 459.67)*5.0/9.0 # degrees F --> Kelvin
data.loc[:,'Pressure'] *= 3386.0 # inches Hg --> Pascal
data.loc[:,'WindDirection(Degrees)'] = np.rad2deg(data.loc[:,'WindDirection(Degrees)']) # degrees --> radians
data.loc[:,'Speed'] *= 0.447 # MPH --> m/s
data.rename(columns={'UNIXTime':'Date','Time':'Time of Day','WindDirection(Degrees)':'Wind Direction','Speed':'Wind Speed'}, inplace=True)

# convert times to datetime objects
data['Date'] = pd.to_datetime(data['Date'],unit='s').dt.date
data['Time of Day'] = pd.to_datetime(data['Time of Day'],format='%H:%M:%S')
data['TimeSunRise'] = pd.to_datetime(data['TimeSunRise'],format='%H:%M:%S')
data['TimeSunSet'] = pd.to_datetime(data['TimeSunSet'],format='%H:%M:%S')
unitLabels={'Time of Day':'HST','Radiation':'W/m^2','Temperature':'K','Pressure':'Pa','Humidity':'\%','Wind Direction':'rad','Wind Speed':'m/s','TimeSunRise':'HST','TimeSunSet':'HST'}

# find length of each day
data['Length of Day'] = (data['TimeSunSet']-data['TimeSunRise'])/np.timedelta64(1, 's')
unitLabels['Length of Day']='s'

## initial visualizations
data_bydate=data.groupby('Date')

# radiation over long periods of time
normalized_rad_per_day=data_bydate['Radiation'].sum()/data_bydate['Length of Day'].min()
normalized_rad_per_day.plot(), plt.title('Normalized Radiation per Day')

mean_temp_per_day=data_bydate['Temperature'].mean()
normalized_mean_temp_per_day=mean_temp_per_day/mean_temp_per_day.max()
mean_humidity_per_day=data_bydate['Humidity'].mean()
normalized_mean_humidity_per_day=mean_humidity_per_day/mean_humidity_per_day.max()
normalized_mean_temp_per_day.plot()
normalized_mean_humidity_per_day.plot()