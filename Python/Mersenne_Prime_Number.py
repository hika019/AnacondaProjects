from sympy import isprime
import numpy as np
import time
import csv
#from tqdm import tqdm

def write(i, Number):
    with open('Mersenne_Number.txt', 'a', newline="\n") as f:
        f.write('2**{}-1= {}\n\n'.format(i, Number))



print('開始')
n = int(input())
print('終了')
m = int(input())

start = time.time()



mersenne_N = (2 ** i -1 for i in range(n, m+1 ,2) if isprime(i))

for i in mersenne_N:
    if isprime(i):
        print(i)
'''


for i in (range(n, m+1, 2)):
    if isprime(i):
        Mersenne_Number = 2 ** i -1
        if isprime(Mersenne_Number):
            print(Mersenne_Number)
        #Mersenne_Prime_list = np.append(Mersenne_Number)
        
        #write(i, Mersenne_Number)
'''



elapsed_time = time.time() - start

print ("time:{0}".format(elapsed_time) + "[sec]")