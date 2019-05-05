from sympy import isprime
import numpy as np
import time
import csv

m = int(input())

start = time.time()

Mersenne_Prime_list = []

for i in range(1, m+1, 2):
    Mersenne_Number = 2 ** i -1 

    
    
    
    #print(Mersenne_Number)
    #print('#####')
    if isprime(Mersenne_Number):
        print(Mersenne_Number)
        #Mersenne_Prime_list = np.append(Mersenne_Number)
        
        with open('Mersenne_Number.txt', 'a', newline="\n") as f:
            f.write('{}\n'.format(Mersenne_Number))
        
        
elapsed_time = time.time() - start

print ("time:{0}".format(elapsed_time) + "[sec]")