#!usr/bin/env /usr/local/bin/python
import time
import os

start = time.time()

for i in range(0,100):
    p = str(i)
    cmd = "start winrar e *.rar -y -pwww.lxwc.com.cn"
    
    r = os.system(cmd)
    if r == 1 or r == 0:
        print("pass = %s" % p)
        break

    print("%s %d" % (p,r))



endtime = time.time() - start

print("%f" % endtime)
print("finished")