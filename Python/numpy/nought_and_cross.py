# -*- coding: utf-8 -*-
import numpy as np

nought = 0
cross = 1

user = nought #初手

X = 3
Y = 3
win = 3

def bord():
    global bord
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
            return y,x
            break
        #print(X, Y)
        print('エラーもう一度')


def nought_or_cross():
    N_or_C = user
    print(N_or_C)
    for i in range(X*Y):
        Nought_or_Cross = N_or_C % 2
        change_bord(Nought_or_Cross)
        N_or_C = N_or_C +1


def change_bord(nought_or_cross):
    y, x = put()
    print(y,x)
    bord[y, x] = nought_or_cross
    print(bord)
    

def start():
    print('初手{}'.format(user))
    print(bord())
    #bord()
    nought_or_cross()


start()