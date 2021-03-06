# -*- coding: utf-8 -*-
from API_seting import bitmex, market, ashi, ago

from datetime import datetime
import calendar
from pprint import pprint
import csv
import numpy as np
import matplotlib.pyplot as plt


def interval():
    interval = ashi()
    
    hoge = "1m"
    hogehoge = "5m"
    hogehogehoge = "1h"
    
    if interval == hoge:
        return 1
    elif interval == hogehoge:
        return 5
    elif interval == hogehogehoge:
        return 60


def time():
    now = datetime.utcnow()
 
    #UTC→Unix時間に変換
    unixTime = calendar.timegm(now.utctimetuple())
    return unixTime

def charts_old():
    datas = np.empty((0,6), int)
    #ohlcvList = np.zeros((24*50, 0))
    unixTime = time()
    
    #xx分前の時間(ms)を算出
    minute = 60*24*ago() #1日*ago()
    
    
    intervals = interval()
    #データ取得量
    all_len = (24*60)/intervals * ago() #1日/足（一日に何本のデータをとるか）＊日数
    print(all_len)
    #minute = 150
    
    since = (unixTime - 60 * minute)
    
    #過去の取引情報(1分足)を取得
    limit = 750
    #ohlcvList = np.array(bitmex().fetch_ohlcv(market(), ashi(), since, limit))
    for i in range( int(-(-all_len // limit)) +1):
        print(i)
        print(since)
        print('{}こ'.format(since +(limit*i*1000)))
        data = np.array(bitmex().fetch_ohlcv(market(), ashi(), since +(limit * i * 1000), limit))
        
        datas = np.vstack((datas, data))
        print(len(data))
        #print(data)
    
    
    #print(unixTime)
    #ohlcvList = np.delete(ohlcvList, 744,0)
    #ohlcvList = np.delete(ohlcvList, 0,1)
    #print(ohlcvList)
    return datas


def chart_make():
    
    since = time() - (interval() *50 * 1000)
    new_data = np.array(bitmex().fetch_ohlcv(maeket(), ashi(), since, 100))


def write_old():
    with open('chart_data.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, lineterminator='\n')
        writer.writerows(chart_old())
    print('終了')

#data = charts_old()
#print(data)
#print(len(data))


#相場データ（過去）
#write_old()
print('#############################')
#pprint(chart_old())

def load_csv(file_name = 'chart_data.csv'):#読み込み
    csv_data = np.empty((0,1),float)
    csv_data = np.loadtxt(file_name, delimiter=",", usecols=(1)) #列指定
    print(csv_data)
    return csv_data


write_old()
data = load_csv()

plt.plot(data)
plt.show()
