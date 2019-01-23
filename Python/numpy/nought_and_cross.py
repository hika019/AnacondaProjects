# -*- coding: utf-8 -*-
import numpy as np

X = 3
Y = 3

def bord():
    bord = np.zeros([Y, X])    
    bord[:,:] = np.nan
    
    return bord


def select_XY():
    print('X座標Y座標')
    put = str(input())
    return put


def put():
    XY = select_XY()
    X, Y = (XY[0]), (XY[1])
    print(X, Y)
    
put()