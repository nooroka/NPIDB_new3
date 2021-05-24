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
process3 = subprocess.Popen(["python","pymolsuper.py",a1,a2], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
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


op2 = open("{}.txt".format(sysargv22),"r")
op22 = open("{}1.txt".format(sysargv22),"w")
for line2 in op2:
    line2 = line2.strip()
    line2 = line2.split(":")
    print(line2[1])
    if str(line2[1]) == "D":
        line2[1] = "Z"
    if str(line2[1]) == "A":
        line2[1] = "X"
    if str(line2[1]) == "B":
        line2[1] = "Q"
    if str(line2[1]) == "C":
        line2[1] = "W"
    if str(line2[1]) == "E":
        line2[1] = "V"
    if str(line2[1]) == "F":
        line2[1] = "Rl"
    if str(line2[1]) == "G":
        line2[1] = "U"
    if str(line2[1]) == "J":
        line2[1] = "R"
    if str(line2[1]) == "K":
        line2[1] = "T"
    if str(line2[1]) == "O":
        line2[1] = "G"
    if str(line2[1]) == "P":
        line2[1] = "Y"
    if str(line2[1]) == "M":
        line2[1] = "S"
    if str(line2[1]) == "H":
        line2[1] = "Lk"
    if str(line2[1]) == "N":
        line2[1] = "Ln"
    print(line2[1])
    op22.write(str(line2[0])+":"+str(line2[1])+"\n")
op22.close()
op2.close()
os.system("paste -d ' \t ' {}.txt {}1.txt > {}".format(sysargv11,sysargv22,file1))
#outputs = run_notebook("Neighbors_3d1n_5zjs-test.ipynb")
process6 = subprocess.Popen(["python","dist.py",a1,a2], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data6,data66 = process6.communicate()
with open('output4.txt', 'a') as f4:
       f4.write(data6)


