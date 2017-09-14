'''Import and prepare data for analysis.

Philip Linden
September 10, 2017
'''
## IMPORT LIBRARIES
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

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
    df.drop(['Data','WindDirection(Degrees)','Speed','Time'],axis=1,inplace=True)

    # interpret columns as appropriate data types to ensure compatibility
    df['UNIXTime']      = df['UNIXTime'].astype(str)
    df['Radiation']     = df['Radiation'].astype(float)
    df['Temperature']   = df['Temperature'].astype(float) # or int
    df['Pressure']      = df['Pressure'].astype(float)
    df['Humidity']      = df['Humidity'].astype(int) # or int
    df['TimeSunRise']   = df['TimeSunRise'].astype(str)
    df['TimeSunSet']    = df['TimeSunSet'].astype(str)

    # convert units to SI
    df.loc[:,'Temperature'] = (df.loc[:,'Temperature'] + 459.67)*5.0/9.0 # degrees F --> Kelvin
    df.loc[:,'Pressure'] *= 3386.0 # inches Hg --> Pascal

    # convert times to UNIX timestamp, time zone naive
    df['UNIXTime'] = pd.to_datetime(df['UNIXTime'],unit='s')
    df['TimeSunRise'] = pd.to_datetime(df['TimeSunRise'],format='%H:%M:%S')
    df['TimeSunSet'] = pd.to_datetime(df['TimeSunSet'],format='%H:%M:%S')

    # compute length of each day
    df['DayLength'] = (df['TimeSunSet']-df['TimeSunRise'])/np.timedelta64(1, 's')

    # we don't need sunrise or sunset times anymore, so drop them
    df.drop(['TimeSunRise','TimeSunSet'],axis=1,inplace=True)

    # break down UNIX time into calendar and time components
    df['Month'] = df['UNIXTime'].dt.month
    df['Date'] = df['UNIXTime'].dt.day
    df['Hour'] = df['UNIXTime'].dt.hour # for easier grouping and math
    df['Minute'] = df['UNIXTime'].dt.minute + 60/df['UNIXTime'].dt.second # seconds as decimal of minute

    # df.set_index('UNIXTime',inplace=True) # index by UNIXTime
    df.sort_values('UNIXTime', inplace=True) # sort by UNIXTime

    # assign unit labels to data keys
    units={'Time':'HST (UTC-10)','Radiation':'W/m^2','Temperature':'K','Pressure':'Pa','Humidity':'\%','DayLength':'sec'}
    return df, units
