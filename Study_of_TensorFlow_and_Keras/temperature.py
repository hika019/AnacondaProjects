import csv
import numpy as np
import pandas as pd



def data_read(file_name = 'data.csv'):
    data = pd.read_csv(file_name)
    
    data.columns = ['day', 'average_temperature']
    
    return data


#print(data_read())
    
FEATURE_VALUE = ['average_temperature']
DIMENSION = len(FEATURE_VALUE)

dfWeather = data_read()

#ソート
dfWeatherTrain = dfWeather.ix['2017-02-23':'2018-02-22', FEATURE_VALUE]
dfWeatherTrain = dfWeatherTrain.sort_index()
dfWeatherTrain = dfWeatherTrain.dropna()#欠番排除
