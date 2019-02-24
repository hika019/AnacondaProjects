# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:16:44 2019

@author: hikar
"""

import csv
import numpy as np



def data_read(file_name = 'data.csv'):
    a =[]
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # ヘッダーを読み飛ばしたい時
        for row in reader:
            print(row)
            a.append(row)
        return a
        

def data_organize():
    data = data_read()
    datas = np.delete(data, 1, 0)
    return datas


#a = data_organize(file_name)
#data_read()
a = data_read()
