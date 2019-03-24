# -*- coding: utf-8 -*-
import ccxt

def bitmex():
    bitmex = ccxt.bitmex({
       'apiKey': 'cY5zFzXgMjHWgJUal5rmUKtg',
       'secret': 'YjNjCYXWF-B035ecnUyjf7FBDhEuS37vnXxFRE2eyz5cSMsV',
       })
    return bitmex

def market():
    market = 'ETH/USD'
    return market

def soku():
    soku = '5m'
    return soku