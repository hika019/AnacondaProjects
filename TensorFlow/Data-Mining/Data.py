import time
import ccxt
import datetime
import csv

def setup():
    global exchanges
    exchanges = {
        "bitmex": {
            "apiKey": "BITMEXのIDをいれてください",
            "secret": "BITMEXのSecretをいれてください"
        },
    }
        
    with open('test.csv', 'w') as csv_file:
        csv_file.write('time, ask, bid, spread\n')
    
def data():
    global timedata, bid, ask, spread
    exchange = ccxt.bitmex()
    exchange.apiKey = exchanges["bitmex"]["apiKey"]
    exchange.secret = exchanges["bitmex"]["secret"]
    timedata = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    orderbook = exchange.fetch_order_book ('BTC/USD')
    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
    spread = (ask - bid) if (bid and ask) else None
    print (exchange.id, 'market price', { 'bid': bid, 'ask': ask, 'spread': spread })
    print(timedata)
    
def write():
    with open('test.csv', 'a') as csv_file:
        csv_file.write('{},{},{},{}\n'.format(timedata, bid, ask, spread))


setup()
while 0 == 0:
    data()
    write()
    time.sleep(30)