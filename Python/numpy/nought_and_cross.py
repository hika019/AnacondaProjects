# -*- coding: utf-8 -*-
import numpy as np

X = 3
Y = 3
win = 3

def bord():
    bord = np.zeros([Y, X])    
    bord[:,:] = np.nan
    
    return bord


def select_XY():
    print('X座標Y座標')
    put = str(input())
    return put


def put():
    while True:
        XY = select_XY()
        x, y = int(XY[0]), int(XY[1])
        if x <= X-1 and y <= Y-1 and x >=0 and y >=0:
            return x,y
            break
        #print(X, Y)
        print('エラーもう一度')
    
print(put())