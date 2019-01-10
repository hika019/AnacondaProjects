import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#x = np.arange(0,20,0.2)

def sin(x, T=100):
    #x = np.arange(0,2* T +1)
    #print(x.ndim)
    return  np.sin((2.0 * np.pi) / T * x)

# sin波にノイズを付与する
def toy_problem(T=100, ampl=0.05):
    x = np.arange(0, 2 * T + 1)
    noise = ampl * np.random.uniform(low=-1.2, high=1.2, size=len(x))
    return sin(x) + noise


T = 100
f = toy_problem()
#print(sin())
#plt.plot(f)
#plt.show()

length_of_sequences = 2 *T #全時系列の長さ
maxlen = 25 #一つの長さ

data = []
target = []

for i in range(0, length_of_sequences - maxlen + 1):
    data.append(f[i:i + maxlen])
    target.append(f[i + maxlen])

#print(data)
#print(target)

X = np.array(data).reshape(len(data), maxlen, 1)
Y = np.array(target).reshape(len(target), 1)


N_train = int(len(data) * 0.9)
N_validation = len(data) - N_train

X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=N_validation)



def inference(x):
    s = tf.tanh(tf.matmul(x, U) + tf.matmul(s_prev, W) + b)
    for t in range(maxlen):
        s[t] = s[t - 1]
    y = tf.matmul(s[t], V) + c
    return y