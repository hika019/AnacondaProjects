#coding=utf-8
import ccxt
import time
import json
import numpy as np
from pprint import pprint

###################################################################
market = 'ETH/USD'
Pubric_API = 'cY5zFzXgMjHWgJUal5rmUKtg'
Secret_API = 'YjNjCYXWF-B035ecnUyjf7FBDhEuS37vnXxFRE2eyz5cSMsV'

'''
ペア
BTC/USD
ETH/USD

'''
####################################################################


def setup():
    global datas
    datas = np.empty((0,6), int)
    for i in range(10):
        data()
        time.sleep(30)
    
    

def bitmex(): #CCXT を呼び出す関数
   
   bitmex = ccxt.bitmex({
       
       #APIキーをご自分のものに差し替えてください(test)
       #'apiKey': 'uIQ6Bp6FFF0_kxaE2BsnkDKn',
       #'secret': 'sT-17ARVuPKcMbhcIbG9QHIUdGGcq-D1JE6h7W_iAMUJ5bfs',
       
       #APIキーをご自分のものに差し替えてください(本番)
       'apiKey': Pubric_API,
       'secret': Secret_API,
       
   })
   #bitmex.urls['api'] = bitmex.urls['test'] #テスト用 本番口座の場合は不要
   return bitmex

   
    

def method():
    #対応メソッドの確認
    pprint(bitmex().has)


def market_data():
    market_data = bitmex().fetch_markets()
    #pprint(market_data)
    
    txt_file = open('market_data.json','w')
    json.dump(market_data, txt_file, ensure_ascii = False, indent = 4, sort_keys = True, separators = (',', ':'))
    print('終了')


def data():
    global datas
    
    #口座情報の取得
    #balance = bitmex().fetch_balance()
    #print(balance)
    
    #Tickerの取得
    ticker = bitmex().fetch_ticker(market)

    #print (bitmex().id, 'market price', {'bid': bid, 'ask': ask, 'spread': spread})
    #pprint(ticker)
    
    Low = ticker['low']#最低値
    High = ticker['high']#最高値
    print('最低:{}'.format(Low))
    print('最高:{}'.format(High))
    
    Open = ticker['open']#始値
    Close = ticker['close']#終値
    print('始め:{}'.format(Open))
    print('終わり:{}'.format(Close))
    print('-----------------------')
    
    if Open < Close:
        Ave_Low = (Open + Low)/2
        Ave_High = (Close + High)/2
    else:
        Ave_Low = (Close + High)/2
        Ave_High = (Open + Low)/2
    
    datas = np.append(datas, np.array([[Open, Close, High, Low, Ave_High, Ave_Low]]), axis=0)
    #print(datas)


def Average_data():
    global datas
    global Average_High ,Average_Low
    Average_High = np.average(datas[::,4])#Average_High
    Average_Low = np.average(datas[::,5])#Average_Low
    print('売りライン{}'.format(Average_High))
    print('買いライン{}'.format(Average_Low))


def Market_price():
    global bid, ask
    
    orderbook = bitmex().fetch_order_book(market)
    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
    spread = (ask - bid) if (bid and ask) else None
    
    print('bid:{}'.format(bid))
    print('ask:{}'.format(ask))
    print('spread:{}'.format(spread))


def Trade():
    Market_price()
    time.sleep(0.2)
    
    if ask <= Average_Low:
        #Buy()
        print('買い')
    
    elif bid >= Average_High:
        #Sell()
        print('売り')
    else:
        print('安くもなく高くもない')
    print('--------')
    time.sleep(4.8)


def data_list():
    global datas
    datas = np.delete(datas, axis = 0, obj = 0)
    data()
    time.sleep(0.8)
    Average_data()

#発注
#order = bitmex().create_order('market', type='limit', side='buy', amount=10000, price=8000)


#setup()
#print(datas)

#print('------')
for i in range(5):
    for a in range(6):
        Trade()
    data_list()
