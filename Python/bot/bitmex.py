#coding=utf-8
import ccxt
import time
import json
from pprint import pprint


market = 'ETH/USD'
'''
ペア
BTC/USD
ETH/USD

'''


def bitmex(): #CCXT を呼び出す関数
   
   bitmex = ccxt.bitmex({
       '''
       #APIキーをご自分のものに差し替えてください(test)
       'apiKey': 'uIQ6Bp6FFF0_kxaE2BsnkDKn',
       'secret': 'sT-17ARVuPKcMbhcIbG9QHIUdGGcq-D1JE6h7W_iAMUJ5bfs',
       '''
       #APIキーをご自分のものに差し替えてください(本番)
       'apiKey': 'cY5zFzXgMjHWgJUal5rmUKtg',
       'secret': 'YjNjCYXWF-B035ecnUyjf7FBDhEuS37vnXxFRE2eyz5cSMsV',
       
       
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
    datas = []
    #口座情報の取得
    #balance = bitmex().fetch_balance()
    #print(balance)
    
    #Tickerの取得
    ticker = bitmex().instrument(market)
    pprint(ticker)
    
    #現在価格表示されない・・・
    Bid = ticker['bid']#売り値
    Ask = ticker['ask']#買い値
    print(Bid)
    print(Ask)
    
    Low = ticker['low']#最低値
    High = ticker['high']#最高値
    print('最低{}'.format(Low))
    print('最高{}'.format(High))
    
    Open = ticker['open']#始値
    Close = ticker['close']#終値
    print('始め{}'.format(Open))
    print('終わり{}'.format(Close))
    
    AveHigh = (High + Close)/2
    
    
    datas.append(AveHigh)
    print(datas)

data()