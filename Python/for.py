# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:56:32 2019

@author: hikar
"""
from sympy import isprime
import time

start = time.time()


number = (i for i in range(209) if isprime(i))

#for i in number:print(i)
mersenne_N = (2 ** i -1 for i in number if isprime(i))

for i in mersenne_N:print(i)

'''
for i in range(200000):
    print(i)
'''

print(time.time() - start)