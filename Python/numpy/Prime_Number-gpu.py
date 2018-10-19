import time
import cupy as cp

def PrimeN():
    m = int(input())#キーボードから範囲指定

    primeN = []

    Number_list = cp.arange(2,m+1)
    
    print(Number_list)#数字のリスト
    
    for i in range(len(Number_list)):
    
        b = Number_list[0]#Number_lsitの最初の要素＆割る数
        c = Number_list[(Number_list % b !=0)]#Number_list / bが0でないものをcとする（素数候補）
        primeN.append(b) #ｂが素数
        #print(b)
        Number_list = cp.asnumpy(c)
        
        if len(Number_list) == 0:#Number_listが空になったら終了
            break
    
    print(primeN)


start = time.time()

PrimeN()

elapsed_time = time.time() - start


print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
