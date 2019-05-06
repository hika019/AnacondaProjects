# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:56:32 2019

@author: hikar
"""

import time

start = time.time()


number = tuple(i for i in range(20000))()

#for i in number:print(i)
print(number)
'''
for i in range(200000):
    print(i)
'''

print(time.time() - start)