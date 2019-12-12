# -*- coding: utf-8 -*-
import binascii
import random


data = "私は日本人です。"


def binary_data(data, byte = 3):
    binary_str = "0b"    
    for i in data:
        binary_i = str(bin(ord(i))[2:])
        #print(i, len(binary_i), binary_i)
        
        while len(binary_i) < 8*byte:
            binary_i = "0{}".format(binary_i)

            
        binary_str += binary_i
    #print("m ={}".format(binary_str))
    return binary_str


def utf_data(data, byte = 3):
    bin_data = data[2:]
    bin_array = []
    for i in range(len(bin_data)):
        
"""
def make_key(m_data):
    key = ""
    n = len(m_data) -2
    #print(n)
    for i in len(m_data)-2:
        key += str(random.randint(0,1))
    #print("key ={}".format(key))
    return ("0b{}".format(key))
"""

def XOR(bin_data, key):
    return bin(int(bin_data, 0) ^ int(key, 0))



m_data = binary_data(data)
#key = make_key(m_data)
"""
print("平文={}".format(m_data))
print("鍵={}".format(key))
print("暗号文={}".format(XOR(m_data, key)))
"""

utf_data(m_data)

#復号
#chr(int('0b100010101101', 0))


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
<<<<<<< HEAD
=======


>>>>>>> db0c6f47aecbd7c35e1012f2fcd54d4d8e72929a
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
"""