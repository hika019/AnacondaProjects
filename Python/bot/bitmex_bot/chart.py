# -*- coding: utf-8 -*-
from API_seting import bitmex, market, soku, ago

from datetime import datetime
import calendar
from pprint import pprint
import csv
import time
import numpy as np

def interval():
    interval = soku()
    
    hoge = "1m"
    hogehoge = "5m"
    
    if interval == hoge:
        return 1
    elif interval == hogehoge:
        return 5

def chart_old():
    #ohlcvList = np.zeros((24*50, 0))
    now = datetime.utcnow()
 
    #UTC→Unix時間に変換
    unixTime = calendar.timegm(now.utctimetuple())
    
    #xx分前の時間(ms)を算出
    minute = 60*24*ago() #1日*ago()
    
    
    intervals = interval()
    #データ取得量
    all_len = (24*60)/intervals * ago() #1日/足（一日に何本のデータをとるか）＊日数
    print(all_len)
    #minute = 150
    
    since = (unixTime - 60 * minute) * 1000
    
    #過去の取引情報(1分足)を取得
    limit = 750
    ohlcvList = np.array(bitmex().fetch_ohlcv(market(), soku(), since, limit))
    print(unixTime)
    #ohlcvList = np.delete(ohlcvList, 744,0)
    #ohlcvList = np.delete(ohlcvList, 0,1)
    print(ohlcvList)
    return ohlcvList


def write_old():
    with open('chart_data_base.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, lineterminator='\n')
        writer.writerows(chart_old())
    print('終了')


def chart_new():
    #ohlcvList = np.zeros((24*50, 0))
    now = datetime.utcnow()
 
    #UTC→Unix時間に変換
    unixTime = calendar.timegm(now.utctimetuple())
    
    #xx分前の時間(ms)を算出
    minute = 60*2 #2時間分
    #minute = 150
    since = (unixTime - 60 * minute) * 1000
    
    #過去の取引情報(1分足)を取得
    limit = 100
    ohlcvList = np.array(bitmex().fetch_ohlcv(market(), soku(), since, limit))
    print(unixTime)
    ohlcvList_new = np.delete(ohlcvList, 1,0)
    ohlcvList_new = np.delete(ohlcvList, 0,1)
    return ohlcvList_new


def write_new():
    with open('chart_data.csv','a') as csv_file:
        writer = csv.writer(csv_file, lineterminator='\n')
        writer.writerows(chart_new)

def read_data():
    data = np.loadtxt('chart_data_base.csv', delimiter =',',usecols=(2,3))
    data = np.delete(data, 1,1)
    
    with open('chart_data.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, lineterminator='\n')
        writer.writerows(data)
    return data


#相場データ（過去）
write_old()
print('#############################')
#pprint(chart_old())
'''
write_old()
while True:
    time.sleep(60*60)
    write_new()
'''
data = (read_data())
plt.plot(data)
plt.show()