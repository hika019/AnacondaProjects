import hashlib

time = "2018/08/30-20:47"
sha256 = hashlib.sha256(time.encode()).hexdigest()

print(sha256)