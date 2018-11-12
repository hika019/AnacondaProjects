import numpy as np
import matplotlib.pyplot as plt


#sigmoid
def sigmoid(x):
    return 1/ (1+ np.exp(-x))

#ステップ
def step_function(x):
    return np.array(x > 0, dtype=np.int)

#ソフトプラス
def soft_plus(x):
    return np.log(1+np.exp(x))

#Relu
def relu(x):
    return np.maximum(0,x)

def Leky_ReLU(x):
    return np.maximum(0.05*x,x)

#ReLu + sigmoid
def relu_sig(x):
    return np.maximum(0,a+b)



#xの移動範囲
x = np.arange(-5, 5, 0.01)


a = sigmoid(x) #sigmoid
b = np.tanh(x) #tanh
c = step_function(x) #ステップ
d = soft_plus(x) #ソフトプラス
e = relu(x) #ReLu
f = Leky_ReLU(x)


plt.plot(x,a)
plt.plot(x,b)
plt.plot(x,c)
plt.plot(x,d)
plt.plot(x,e)
plt.plot(x,f)


plt.ylim(-1.2,2.5)
plt.show()