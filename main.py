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

## INGEST DATA
def ingest_data(filename):
    '''Read data from a CSV file and construct a pandas DataFrame
    Inputs:
        filename as string
    Outputs:
        df as DataFrame
    '''
    # read csv file
    df = pd.read_csv(filename)

    # 'Data' column is unused. All elements contain the same value.
    df.drop(['Data','WindDirection(Degrees)','Speed'],axis=1,inplace=True)

    # interpret columns as appropriate data types to ensure compatibility
    df['UNIXTime']      = df['UNIXTime'].astype(str)
    df['Time']          = df['Time'].astype(str)
    df['Radiation']     = df['Radiation'].astype(float)
    df['Temperature']   = df['Temperature'].astype(float) # or int
    df['Pressure']      = df['Pressure'].astype(float)
    df['Humidity']      = df['Humidity'].astype(int) # or int
    df['TimeSunRise']   = df['TimeSunRise'].astype(str)
    df['TimeSunSet']    = df['TimeSunSet'].astype(str)
    # df['WindDirection(Degrees)'] = df['WindDirection(Degrees)'].astype(float)
    # df['Speed']         = df['Speed'].astype(float)

    # convert units to SI
    df.loc[:,'Temperature'] = (df.loc[:,'Temperature'] + 459.67)*5.0/9.0 # degrees F --> Kelvin
    df.loc[:,'Pressure'] *= 3386.0 # inches Hg --> Pascal
    # df.loc[:,'WindDirection(Degrees)'] = np.rad2deg(df.loc[:,'WindDirection(Degrees)']) # degrees --> radians
    # df.loc[:,'Speed'] *= 0.447 # MPH --> m/s

    # rename columns to more useful terms
    df.rename(columns={'UNIXTime':'Date'}, inplace=True)
    # df.rename(columns={'WindDirection(Degrees)':'WindDirection','Speed':'WindSpeed'},inplace=True)

    # convert times to UNIX timestamp, time zone naive
    df['Date'] = pd.to_datetime(df['Date'],unit='s')
    df['Time'] = pd.to_datetime(df['Time'],format='%H:%M:%S')
    df['TimeSunRise'] = pd.to_datetime(df['TimeSunRise'],format='%H:%M:%S')
    df['TimeSunSet'] = pd.to_datetime(df['TimeSunSet'],format='%H:%M:%S')

    # compute length of each day
    df['DayLength'] = (df['TimeSunSet']-df['TimeSunRise'])/np.timedelta64(1, 's')

    # we don't need sunrise or sunset times anymore, so drop them
    df.drop(['TimeSunRise','TimeSunSet'],axis=1,inplace=True)

    # assign unit labels to data keys
    units={'Time':'UNIX Time (HST)','Radiation':'W/m^2','Temperature':'K','Pressure':'Pa','Humidity':'\%','WindDirection':'rad','WindSpeed':'m/s','DayLength':'sec'}
    return df, units

df, units = ingest_data('input/SolarPrediction.csv')
print(df.head())

# give the algorithm weather and calendar info for 2-3 days prior and let it predict a distribution over the course of a day. the answer is the area under that curve.
