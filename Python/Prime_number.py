import time

m = int(input())#キーボードから範囲指定

start = time.time()


for i in range (2,m):
    for d in range (2,i+1):
        if (i%d==0):#あまりが0か
            if (i==d):#同じ数か
                print(i)
            else:
                break
                    
            
elapsed_time = time.time() - start

print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")