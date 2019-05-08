from sympy import isprime
import time
import csv
import numpy as np
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing as multi
#from tqdm import tqdm


def write(i, Number):
    with open('Mersenne_Number.txt', 'a', newline="\n") as f:
        f.write('2**{}-1= {}\n\n'.format(i, Number))


def Mersenne_N(n,m):
    for i in range(n,m+1):
        if isprime(i):
            i = np.array(i, dtype='object')
            #Mersenne_Number = (1 << i) - 1
            Mersenne_Number_np = np.array((1 << i)-1, dtype='object')
            #print(i)
            
            s = np.array(4, dtype='object')
            #s_1 = np.array(s ** 2 -2)
            for n in range(2, i+1):
                s = np.array((s**2 - 2) % Mersenne_Number_np, dtype='object')
                '''
                if n == 2:
                    s_1 = s
                    
                if n>3 and s_1 == s:
                    break
                '''
                if s == 0:
                    #pass
                    print(Mersenne_Number_np)
                    #write(i, Mersenne_Number)
                
            
            '''
            if isprime(Mersenne_Number):
                print(Mersenne_Number)
                return Mersenne_Number, i
            '''

'''
def Mersenne_prime_number():
    pool = Pool(3)
    Mersenne_Number = pool.apply_async(Mersenne_N,range(n,m+1))
    #M_N= Mersenne_Number#[0]
    #print(M_N)
'''



print('開始')
n = int(input())
print('終了')
m = int(input())

start = time.time()

pool = Pool(5)
Mersenne_N(n,m)


'''
mersenne_N = (2 ** i -1 for i in range(n, m+1 ,2) if isprime(i))

for i in mersenne_N:
    if isprime(i):
        print(i)
'''

#Mersenne_N(n,m)

elapsed_time = time.time() - start

print ("time:{0}".format(elapsed_time) + "[sec]")
