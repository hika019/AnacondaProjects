import ccxt
from pprint import pprint

bitmex = ccxt.bitmex()
Data = []
'''
たぶん1分足
10分前
'''
timestamp = bitmex.fetch_ticker('BTC/USD')['timestamp']
timestamp = timestamp - 10 * 1000 * 60
data = bitmex.fetch_ohlcv('BTC/USD', since=timestamp)

pprint(data)
print('')
Data.append(data)
pprint(Data)