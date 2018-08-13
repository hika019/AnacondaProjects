import time

start = time.time()
#import numba

#@numba.jit

def primeN():
    m = int(input())#キーボードから範囲指定

    primeN = [2]
    for i in range(2, m):
        for j in range(len(primeN)):
            if i % primeN[j] == 0:
                break
            else:
                if j == len(primeN) - 1:
                    primeN.append(i)
                    print(i)
    print(primeN)
    
primeN()#prime()関数の実行

#for i in primeN:
 #   print(i)


elapsed_time = time.time() - start

print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")