#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 09:41:45 2019

@author: orlando
"""

import pandas as pd

def create_master_turnstile_file(filenames, output_file):
    with open(output_file, 'w') as master_file:
        header='C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n'
        master_file.write(header)
        columns=['C/A','UNIT','SCP','DATE','TIME','DESC','ENTRIES','EXITS']
        for filename in filenames:
            # your code here
            file=pd.read_csv(filename)
            file.columns=file.columns.str.replace(' ', '')
            file=file[list(columns)]
            file.to_csv(master_file, header=None, index=False)


                    
create_master_turnstile_file(['turnstile-170610.txt', 'turnstile-170617.txt', 'turnstile-170603.txt', 'turnstile-170624.txt'], 'master_file')

def filter_by_regular(filename):
    
    turnstile_data = pd.read_csv(filename)
    
    turnstile_data.loc[turnstile_data['DESCn'] == 'Regular']
    # more of your code here
    return turnstile_data
        
        
filename = "turnstile_data_master_with_weather.csv"
df = pd.read_csv(filename, sep=',')

def avg_min_temperature(df):
    avg_min_temp_rainy=df[((df.rain == 1) & (df.mintempi > 55))]
    avg_min_temp_rainy=avg_min_temp_rainy.mintempi.mean()
    
    return avg_min_temp_rainy

avg_min_temperature(df)

import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):
    
    plt.figure()
    turnstile_weather['ENTRIESn_hourly'].loc[turnstile_weather.rain == 0].hist(alpha=0.5, range=(1000, 9000)) # your code here to plot a historgram for hourly entries when it is raining
    turnstile_weather['ENTRIESn_hourly'].loc[turnstile_weather.rain == 1].hist(alpha=0.5, range=(1000, 9000)) # your code here to plot a histogram for hourly entries when it is not raining
    #plt.yscale('log')
    plt.xlabel('Entries per Hours')
    plt.legend(('Raining', 'Not Raining'))
    return plt

def max_temp_aggregate_by_fog(df):
    maxFog=df.groupby('fog').max()['maxtempi'].values

    #your code here 
    return maxFog


entries_histogram(df)
