import time

m = int(input())#キーボードから範囲指定


start = time.time()



counter = 0
counter2 = 0
minutes = 0
hour = 0


'''from multiprocessing import Pool
pool = Pool(2)#スレッド数'''


for i in range (2,m+1):
    for d in range (2,i+1):
        if (i%d==0):#あまりが0か
            if i==d:#同じ数か
                #print(i)
            
                meru = 2**i-1
                #print(meru)


                            
            else:
                break
            
            for de in range(3,meru+3, 2):
                if meru % de == 0:
                    #print(de)
                    counter2+=1
                    if counter2 <= 1:
                        if meru == de:
                            # print(meru)
                            counter+=1
                            print(counter,'番目は',meru)
                            counter2 = 0
                        else:
                            counter2 = 0
                            break
                            
                    else:
                        counter2=0


elapsed_time = time.time() - start

print ("time:{0}".format(elapsed_time) + "[sec]")