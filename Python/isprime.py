# -*- coding: utf-8 -*-
"""
Created on Mon May  6 08:27:15 2019

@author: hikar
"""
import time
from sympy import isprime
from multiprocessing import Pool


def m():
    p = 19937
    m = 2 ** p -1

    return isprime(m)


def m1():
    p = 19937
    m = 2 ** p -1
    s = 4
    for n in range(2, p):
        s = (s**2 - 2) % m
        if s == 0:
            print(m)

start = time.time()

print(m())
#m1()
print(time.time() - start)