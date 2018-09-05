import hashlib
import datetime
import time

Hash = 0
Block_number = 0

for i in range(10):
    now = datetime.datetime.now()
    print('Timestamp: {}'.format(now))
    
    Block_number += 1
    print('Block_number: {}'.format(Block_number))

    data = "Hello!"
    print('Data: {}'.format(data))
    
    
    
    dataset =str(now) + str(Block_number) + data + str(Hash)
    print('previous_hash: {}'.format(Hash))
    
    sha256 = hashlib.sha256(dataset.encode()).hexdigest()
    print('Hash: {}'.format(sha256))
    
    
    Hash = sha256
    print()
    time.sleep(0.5)
