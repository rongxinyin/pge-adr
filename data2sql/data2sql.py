
from __future__ import division

import os.path
import pandas as pd
import numpy as np
import csv
import glob

#import matplotlib.pyplot as plt
#import seaborn as sns

#import datetime

customers = pd.read_csv('../../pge/D1977customers.csv',delimiter=',')
df_said = customers[['SAID','ZIPCODE','sublap']]

count = 0
for part in glob.glob('../../pge/D19771/part*'):
    df = pd.read_csv(part,delimiter=',')
    df = df.rename(columns = {'SA':'SAID'})
    df = pd.merge(df, df_said, on = ['SAID'])
    
    for zipcode in list(set(df.ZIPCODE)):
        df_zipcode = df.loc[df.ZIPCODE == zipcode,]
        with open('../../pge/D1977ZipCode/'+str(zipcode)+'.csv', 'a') as f:
            df_zipcode.to_csv(f, header=False)
    count += 1
    print 'Processed '+ "{0:0f}%".format(count/250 * 100) + ' of the total data in D197771'

count = 0    
for part in glob.glob('../../pge/D19772/part*'):
    df = pd.read_csv(part,delimiter=',')
    df = df.rename(columns = {'SA':'SAID'})
    df = pd.merge(df, df_said, on = ['SAID'])
    
    for zipcode in list(set(df.ZIPCODE)):
        df_zipcode = df.loc[df.ZIPCODE == zipcode,]
        with open('../../pge/D1977ZipCode/'+str(zipcode)+'.csv', 'a') as f:
            df_zipcode.to_csv(f, header=False)
    count += 1
    print 'Processed '+ "{0:0f}%".format(count/250 * 100) + ' of the total data in D197772'

count = 0
for part in glob.glob('../../pge/D19773/part*'):
    df = pd.read_csv(part,delimiter=',')
    df = df.rename(columns = {'SA':'SAID'})
    df = pd.merge(df, df_said, on = ['SAID'])
    
    for zipcode in list(set(df.ZIPCODE)):
        df_zipcode = df.loc[df.ZIPCODE == zipcode,]
        with open('../../pge/D1977ZipCode/'+str(zipcode)+'.csv', 'a') as f:
            df_zipcode.to_csv(f, header=False)
    count += 1
    print 'Processed '+ "{0:0f}%".format(count/250 * 100) + ' of the total data in D197773'

count = 0
for part in glob.glob('../../pge/D19774/part*'):
    df = pd.read_csv(part,delimiter=',')
    df = df.rename(columns = {'SA':'SAID'})
    df = pd.merge(df, df_said, on = ['SAID'])
    
    for zipcode in list(set(df.ZIPCODE)):
        df_zipcode = df.loc[df.ZIPCODE == zipcode,]
        with open('../../pge/D1977ZipCode/'+str(zipcode)+'.csv', 'a') as f:
            df_zipcode.to_csv(f, header=False)
    count += 1
    print 'Processed '+ "{0:0f}%".format(count/60 * 100) + ' of the total data in D197774'