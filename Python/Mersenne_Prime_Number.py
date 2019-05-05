from sympy import isprime
import numpy as np

m = int(input())


for i in range(3, m+1, 2):
    Mersenne_Number = 2 ** i -1
    
    
    
    #print(Mersenne_Number)
    #print('#####')
    if isprime(Mersenne_Number):
        print(Mersenne_Number)
        Mersenne_Prime_list = np.apend(Mersenne_Number)