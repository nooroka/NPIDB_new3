#!/usr/bin/env python
#coding: utf-8
import subprocess
import os
#os.remove("output4.txt")
op = open("pairs29_PF00046.txt","r")
for line in op:
    line = line.strip()
    line = line.split()
    process3 = subprocess.Popen(["python","launch.py",line[0],line[1]], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    data3,data33 = process3.communicate()
    with open('output_all.txt', 'w') as f:
       f.write(data3)

op.close()
