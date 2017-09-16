'''Return plots used to explore the data.

Philip Linden
September 12, 2017
'''
## IMPORT LIBRARIES
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # plotting tools
import seaborn as sns # advanced plotting tools

def humidity(df):
    '''Plot humidity vs radiation over time'''
    plt.figure(figsize=(18, 6))
    plt.subplot(121) # hourly
    df_hourly = df.groupby('Hour')
    h_humidity = df_hourly['Humidity'].mean()
    h_humidity_errorpos =  h_humidity+df_hourly['Humidity'].std()/2
    h_humidity_errorneg =  h_humidity-df_hourly['Humidity'].std()/2
    plt.plot(h_humidity)
    plt.fill_between(range(24), h_humidity_errorpos.values, h_humidity_errorneg.values, alpha=0.3, antialiased=True)
    h_rad = df_hourly['Radiation'].mean()
    h_rad *= 1/h_rad.max()*100 # normalize to percent
    h_rad_errorpos =  (h_rad+df_hourly['Radiation'].std()/2) * 1/h_rad.max()*100 # normalize to percent
    h_rad_errorneg =  (h_rad-df_hourly['Radiation'].std()/2) * 1/h_rad.max()*100 # normalize to percent
    plt.plot(h_rad,'r')
    plt.fill_between(range(24), 0, h_rad, alpha=0.3, antialiased=True, color='red')
    plt.ylim((0,101))
    plt.legend(), plt.xlabel('Hour of Day (Local Time)'), plt.ylabel('Percent')
    plt.title('Average Daily Humidity vs. Average Daily Radiation')

    plt.subplot(122) # daily
    df_daily = df.groupby('Day')
    d_humidity = df_daily['Humidity'].mean()
    d_humidity_errorpos =  d_humidity+df_daily['Humidity'].std()/2
    d_humidity_errorneg =  d_humidity-df_daily['Humidity'].std()/2
    plt.plot(d_humidity)
    plt.fill_between(df['Day'].unique(), d_humidity_errorpos.values, d_humidity_errorneg.values, alpha=0.3, antialiased=True)
    d_rad = df_daily['Radiation'].mean()
    d_rad *= 1/d_rad.max()*100 # normalize to percent
    d_rad_errorpos =  (d_rad+df_daily['Radiation'].std()/2) * 1/d_rad.max()*100 # normalize to percent
    d_rad_errorneg =  (d_rad-df_daily['Radiation'].std()/2) * 1/d_rad.max()*100 # normalize to percent
    plt.plot(d_rad,'r')
    plt.fill_between(df['Day'].unique(), 0, d_rad, alpha=0.3, antialiased=True, color='red')
    plt.ylim((0,101))
    plt.legend(), plt.xlabel('Day of Year'), plt.ylabel('Percent')
    plt.title('Daily Humidity vs. Daily Radiation')

    plt.figure() # bivariate density
    sns.jointplot(x='Humidity',y='Radiation',data=df,kind='kde',cmap='coolwarm',n_levels=30,shade=True)
    plt.title('Radiation vs. Humidity Bivariate Density')
    sns.plt.show()
    plt.show()
