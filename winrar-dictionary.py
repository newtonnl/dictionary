#!usr/bin/env /usr/local/bin/python
import time
import os

start = time.time()
startNumber = 100000
endNumber = 1000000

f = open("dic.txt","r")
rs = f.readlines()
f.close()


for i in range(0,len(rs)):
    p = rs[i].strip("\n")
    cmd = "start winrar  e yy.rar %s\ -y -p%s " % (p,p)
    r = os.system(cmd)
    if r == 1 or r == 0:
        print("pass = %s" % p)
#        break
    print("%s %d" % (p,r))
print("unrar finished")

endtime = time.time()-start
print("end time = %s" % endtime)
time.sleep(0.500)

for i in range(0,len(rs)):
    p = rs[i].strip("\n")
#    filename = r"D:\study-data\python\%s\333.xlsx" % p
    filename = r"D:\study-data\python\%s\IMG_20140510_220009.jpg" % p
    filepath = "D:\study-data\python\%s" % p
#    if os.path.exists(r'D\study-data\python\1.TXT'):
    if os.path.isfile(filename):
        message = 'ok , the file "%s" is exit'
#        time.sleep(0.200)
        print("message = %s i=%s" % (message,i))
    else:
        message = 'wrong ,the file "%s" not exit'
#       delay 100ms avoid not found file
        time.sleep(0.200)
        os.removedirs(filepath)
        print("message = %s i=%s" % (message,i))

endtime2 = time.time()-start
print("%f" % endtime2)		
print("analysis result end")