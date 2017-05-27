#!usr/bin/env /usr/local/bin/python

import tarfile
import time

start = time.time()
t = tarfile.open("D:\study-data\python\123.rar","r:")
t.extractall(path = 'D:\study-data\python')
t.close()

print time.time-start
