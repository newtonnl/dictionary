#!usr/bin/env /usr/local/bin/python
import time
import os

start = time.time()
startNumber = 100000
endNumber = 1000000

for i in range(startNumber,endNumber):
    p = str(i)
    cmd = "start winrar e yy.rar %s\ -y -p%s " % (p,p)

    r = os.system(cmd)
    if r == 1 or r == 0:
        print("pass = %s" % p)
#        break
		
    print("%s %d" % (p,r))
	
endtime = time.time()-start

print("%f" % endtime)
print("unrar finished")


for i in range(startNumber,endNumber):
#    filename = r'D:\study-data\python\1.txt'
    p = str(i)
#    filename = r"D:\study-data\python\%s\333.xlsx" % p
    filename = r"D:\study-data\python\%s\IMG_20140510_220009.jpg" % p
    filepath = "D:\study-data\python\%s" % p
#    if os.path.exists(r'D\study-data\python\1.TXT'):
    if os.path.isfile(filename):
        message = 'ok , the file "%s" is exit'
        print("message = %s i=%s" % (message,i))
    else:
        message = 'wrong ,the file "%s" not exit'
        os.removedirs(filepath)
        print("message = %s i=%s" % (message,i))

endtime2 = time.time()-start
print("%f" % endtime2)		
print("analysis result end")