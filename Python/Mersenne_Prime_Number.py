from sympy import isprime
import numpy as np
import time
import csv

def write(i, Number):
    with open('Mersenne_Number.txt', 'a', newline="\n") as f:
        f.write('2**{}-1= {}\n\n'.format(i, Number))


print('開始')
n = int(input())
print('終了')
m = int(input())

start = time.time()

Mersenne_Prime_list = []

for i in range(n, m+1, 2):
    Mersenne_Number = 2 ** i -1 

    
    
    
    #print(Mersenne_Number)
    #print('#####')
    if isprime(Mersenne_Number):
        print(Mersenne_Number)
        #Mersenne_Prime_list = np.append(Mersenne_Number)
        
        write(i, Mersenne_Number)
        
        
elapsed_time = time.time() - start

print ("time:{0}".format(elapsed_time) + "[sec]")