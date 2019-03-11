#https://qiita.com/sasayabaku/items/b7872a3b8acc7d6261bf
#同じ量のノードなら層が多いほうが早いかもしれない（一層と二層の場合）

from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random

def sin(x, T=100):#T*2の長さ
    return np.sin(2.0 * np.pi * x / T)

# sin波にノイズを付与する
def toy_problem(T=150, ampl=0.05):
    x = np.arange(0, 2 * T + 1)
    noise = ampl * np.random.uniform(low=-1.0, high=1.0, size=len(x))
    return sin(x) + noise

f = toy_problem()
#plt.plot(f)
#plt.show()


def make_dataset(low_data, n_prev=100):
    global maxlen
    data, target = [], []
    maxlen = 50

    for i in range(len(low_data)-maxlen):
        data.append(low_data[i:i + maxlen])
        target.append(low_data[i + maxlen])

    re_data = np.array(data).reshape(len(data), maxlen, 1)
    re_target = np.array(target).reshape(len(data), 1)

    return re_data, re_target

#a, b = make_dataset(f)
#print(a,b)


#g -> 学習データ，h -> 学習ラベル
g, h = make_dataset(f)

future_test = g[300-maxlen].T #300は def(sin)のT
#↑
# 1つの学習データの時間の長さ -> 25 ↓
time_length = future_test.shape[1]
# 未来の予測データを保存していく変数
future_result = np.empty((0))

# モデル構築

# 1つの学習データのStep数(今回は25)
length_of_sequence = g.shape[1] 

in_out_neurons = 1
n_hidden = 512 #隠れ層のノード数

model = Sequential()
model.add(LSTM(n_hidden, batch_input_shape=(None, length_of_sequence, in_out_neurons), return_sequences=True))
model.add(Dropout(0.15))
model.add(LSTM(n_hidden, return_sequences=True))
model.add(Dropout(0.15))
model.add(LSTM(n_hidden, return_sequences=False))


model.add(Dense(in_out_neurons))
model.add(Activation("linear"))
optimizer = Adam(lr=0.001)
model.compile(loss="mean_squared_error", optimizer=optimizer)


early_stopping = EarlyStopping(monitor='val_loss', mode='auto', patience=40)
model.fit(g, h,
          batch_size=100,
          epochs= 500,
          validation_split=0.1,
          callbacks=[early_stopping]
          )

predicted = model.predict(g)

'''
plt.figure()
plt.plot(range(maxlen,len(predicted)+maxlen),predicted, color="r", label="row_data")
plt.plot(range(0, len(f)), f, color="b", label="predict_data")
plt.legend()
plt.show()


'''
# 未来予想
for step2 in range(400):

    test_data = np.reshape(future_test, (1, time_length, 1))
    batch_predict = model.predict(test_data)

    future_test = np.delete(future_test, 0)
    future_test = np.append(future_test, batch_predict)

    future_result = np.append(future_result, batch_predict)


# sin波をプロット
plt.figure()
plt.plot(range(maxlen,len(predicted)+maxlen),predicted, color="r", label="predict")
plt.plot(range(0, len(f)), f, color="b", label="row")
plt.plot(range(0+len(f), len(future_result)+len(f)), future_result, color="g", label="future")
plt.legend()
plt.show()
