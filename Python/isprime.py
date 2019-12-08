# -*- coding: utf-8 -*-
"""
Created on Mon May  6 08:27:15 2019

@author: hikar
"""
import time
from sympy import isprime
from multiprocessing import Pool


p = 55009

def m(p):
    
    m = 2 ** p -1

    return isprime(m)


def m1(p):
    s = 4
    M = (1 << p) - 1 #左シフトで2^pを作る

    for n in range(2, p):
        s = (s ** 2 - 2) % M
        if s == 0:
            print(p)

start = time.time()
pool = Pool(3)
#print(m(p))
m1(p)
print(time.time() - start)