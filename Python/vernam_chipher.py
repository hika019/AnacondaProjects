# -*- coding: utf-8 -*-
import binascii
import random


data = "私は日本人です。"


def binary_data(data, byte = 3):
    binary_str = "0b"
    hex_str = ""
    
    for i in data:
        binary_i = str(bin(ord(i))[2:])
        print(i, len(binary_i), binary_i)
        
        while len(binary_i) < 8*byte:
            binary_i = "0{}".format(binary_i)
            hex_binary_i = hex(int(binary_i))
        
        binary_str += binary_i
        hex_str += str(hex_binary_i)
    #print(len(binary_str))
    return binary_str


print(binary_data(data))


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