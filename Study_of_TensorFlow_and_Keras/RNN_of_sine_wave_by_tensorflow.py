import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

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

f = toy_problem()
#print(sin())
plt.plot(f)
plt.show()
