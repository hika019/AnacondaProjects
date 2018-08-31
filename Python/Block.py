import hashlib
import datetime
import time



def block():
    
    global counter
    
    now = datetime.datetime.now()
    print(now)
    
    counter += 1
    print(counter)

    data = "Hello!"
    print(data)
    
    
    
    dataset =str(now) + str(counter) + data
    
    
    sha256 = hashlib.sha256(dataset.encode()).hexdigest()
    print(sha256)
    
    
#    Hash = sha256
    
    print()
    time.sleep(5)

for i in range(10):
    block()