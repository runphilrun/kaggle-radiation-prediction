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
    # df_month = df.groupby('Month')
    # df_day = df.groupby('Date')
    # df_hour = df.groupby('Hour')
    plt.figure(figsize=(18, 6))
    plt.subplot(131)
    sns.barplot(x='Hour',y='Humidity',data=df)
    plt.subplot(132)
    sns.barplot(x='Month',y='Humidity',data=df)
    plt.subplot(133)
    sns.jointplot(x='Humidity',y='Radiation',data=df,kind='kde',cmap='coolwarm',n_levels=30,shade=True)
    sns.plt.show()
    # https://stackoverflow.com/questions/32899463/how-can-i-overlay-two-graphs-in-seaborn
