#!/usr/bin/env python
#coding: utf-8
from collections import defaultdict
import os
op = open("/home/nooroka/backup04052021/xray.txt","r")
op4 = open("/home/nooroka/backup04052021/nmr.txt","r")
op2 = open("/home/nooroka/backup04052021/PF00046/PF00046_int.txt","r")
op5 = open("/home/nooroka/backup04052021/electron.txt","r")
##op3 = open("/home/nooroka/backupnores02102020/uniprot/structsend.txt","r") #потому что нужно для структур без разрешения посмотреть
list1 = []
list2 = []
list11 = []
list111 = []
listel = []
strnmr = []
strxray = []
strel = []
'''calculating for structures'''
dict3 = {}
count = 0
count4 = 0
countel = 0
for line in op:
    line = line.strip()
    line = line.split()
    list1.append(line[0])
op.close()
for line4 in op4:
    line4 = line4.strip()
    line4 = line4.split()
    list11.append(line4[0])
op4.close()
for line5 in op5:
    line5 = line5.strip()
    line5 = line5.split()
    listel.append(line5[0])
op5.close()
for line2 in op2:
    linex = line2.strip()
    linexx = linex.split()
    linex = linex.split(".")
    os.chdir("/home/npidb/data/pdb_new/dna")
    if os.path.exists("pdb{}.pdb".format(linex[0])): 
        if linex[0] in list1:
            count+=1
            strxray.append(linexx[0])
            line2 = line2.strip()
            line2 = line2.split(" ",1) 
            list2.append(line2[0])
        if linex[0] in list11:
            count4+=1
            strnmr.append(linexx[0])
        if linex[0] in listel:
            countel+=1
            strel.append(linexx[0])
    os.chdir("/home/nooroka/backup04052021/PF00046")
            
print(len(list11))
print(len(list1))
print(len(listel))
print("countxray " + str(count))#количество структур с xray
print("countnmr "+str(count4))#количество структур с nmr
print("countel "+str(countel))#количество структур с cryoem
'''calculating for domains'''
domnmr = []
domxray = []
domel = []
file1 = open("/home/nooroka/backup04052021/b_pfam_struct_types.txt","r")
for line in file1:
    if "INSERT" in line:
        line = line.strip()
        line = line.split()
        linef = line[4].split(",")
        lineff = linef[0][2:-1]
        os.chdir("/home/npidb/data/pdb_new/dna")
        if os.path.exists("pdb{}.pdb".format(lineff)): 
            linedom = str(linef[9][1:-1])+"_"+str(linef[12])+"-"+str(linef[13])
            lines = str(lineff)+"."+str(linef[2][1:-1])+"_"+str(linef[3])+"-"+str(linef[4])+"."+str(linef[1][1:-1])
            os.chdir("/home/nooroka/backup04052021/PF00046")
            if lines in strnmr:
                domnmr.append(linedom)
            if lines in strxray:
                domxray.append(linedom)
            if lines in strel:
                domel.append(linedom)
print(domnmr)
print("domnmr "+str(len(set(domnmr)))) #количество доменов
print(domxray)
print("domxray "+str(len(set(domxray)))) 
print(domel)
print("domel "+str(len(set(domel)))) 
