# -*- coding: utf-8 -*-
import binascii
import random

#data = 'あいうえお'
data = 'abcd'

hogehoge = ord("ぢ")


"""
hoge = data.encode('utf-8')
print(hoge)
print(type(hoge))
hoge = binascii.hexlify(hoge)
print(hoge)
print(type(hoge))

m= hoge
print(m)

n = len(hoge)
"""
a = random.randrange(1,100)
b = random.randrange(1,100)
x = random.randrange(100) %10
key = 0

#print(hogehoge)
n =(len(str(hogehoge)))


while(len(str(key)) < n):
    key += x
    x = a*x +b

c = hogehoge ^ key


print("平文={}".format(hogehoge))
print("暗号文={}, key={}".format(c,key))

m_n = c ^ key
print("平文={}, key={}".format(m_n, key))
print("")
print("m={}, key={}, c={}".format(bin(hogehoge), bin(key), bin(c)))
print("m_n={}, key_n={}".format(n, len(str(key))))