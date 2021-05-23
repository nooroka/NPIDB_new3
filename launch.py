#!/usr/bin/env python
#coding: utf-8

import subprocess
import os
import sys
#from boar.running import run_notebook
a1 = sys.argv[1]
a2 = sys.argv[2]
#a1 = "3d1n:K_235-290"
#a2 = "5zjs:A_21-76"
process3 = subprocess.Popen(["python","align.py",a1,a2], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data3,data33 = process3.communicate()
with open('output.txt', 'w') as f:
       f.write(data3)
process4 = subprocess.Popen(["python","receive.py",a1], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data4,data44 = process4.communicate()
with open('output2.txt', 'w') as f2:
       f2.write(data4)
process5 = subprocess.Popen(["python","receive.py",a2], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data5,data55 = process5.communicate()
with open('output3.txt', 'w') as f3:
       f3.write(data5)
sysargv11 = a1.split(":")[0]
sysargv22 = a2.split(":")[0]
file1 = "{}_{}.txt".format(sysargv11,sysargv22)


os.system("paste -d ' \t ' {}.txt {}.txt > {}".format(sysargv11,sysargv22,file1))
#outputs = run_notebook("Neighbors_3d1n_5zjs-test.ipynb")
process6 = subprocess.Popen(["python","dist.py",a1,a2], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data6,data66 = process6.communicate()
with open('output4.txt', 'a') as f4:
       f4.write(data6)


