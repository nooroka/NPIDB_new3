#!/usr/bin/env python
# coding: utf-8
import os
from collections import defaultdict

w = open("/home/nooroka/backup04052021/reschern2.txt","w")
res2 = open("/home/nooroka/backup04052021/structsres22.txt","w")
structsgood = open("/home/nooroka/backup04052021/structsgood2.txt","w")
dict2 = defaultdict(list)
dict1 = defaultdict(list)
dict3 = defaultdict(list)
#for line2 in res1:
el = open("/home/nooroka/backup04052021/electron.txt","r")
listel = []
for lineel in el:
    lineel = lineel.split()
    listel.append(str(lineel[0]))
print(listel)
print(len(listel))
liststructs = []


res11 = open("/home/nooroka/backup04052021/b_pfam_struct_types.txt","r")
countres = 0
countnores = 0
listdd = []
for line in res11:
   if "INSERT" in line:
     line = line.strip()
     line = line.split()
     linef = line[4].split(",")
     dom = str(linef[9][1:-1])+"_"+str(linef[12])+"-"+str(linef[13])
     lineff = linef[0][2:-1]
     lines = str(lineff)+"."+linef[2][1:-1]+"_"+linef[3]+"-"+linef[4]+"."+linef[1][1:-1]
     os.chdir("/home/npidb/data/pdb_new/dna")
     if os.path.exists("pdb{}.pdb".format(lineff)):
         dict2[dom].append(lines)
         op = open("pdb{}.pdb".format(lineff),"r")
         for line2 in op:
             if "REMARK   2 RESOLUTION."  in line2:
                 line2 = line2.strip()
                 line2 = line2.split()
                 if "NOT"  not in line2 and "NULL" not in line2:
                     key,value = float(line2[3]),lines
                     key3,value3 = dom,float(line2[3])
                     dict1[key].append(value)
                     dict3[key3].append(value3)
                     if float(key) < 3.0:
                         for k in range(len(dict1[key])):                            
                            dd = dict1[key][k].split(".")
                            if dict1[key][k] not in liststructs:
                               # if str(dd[0]) not in listel:#мб несколько раз
                                    structsgood.write(str(dict1[key][k])+"\n")
                                    liststructs.append(dict1[key][k])
                                    countres+=1
                     if float(key) > 3.0:
                         countnores+=1
                 
                 else:
                     if "NOT" in line2[3]:
                         key,value = float(101.0),lines
                         key3,value3 = dom,float(101.0)
                         dict1[key].append(value)
                         dict3[key3].append(value3)
                         
                     elif "NULL" in line2[3]:
                         key,value = float(102.0),lines
                         key3,value3 = dom,float(102.0)
                         dict1[key].append(value)
                         dict3[key3].append(value3)
                         
     os.chdir("/home/nooroka/backup04052021")

for key3 in dict3:
    w.write(str(key3)+"\t"+str(len(dict2[key3]))+"\t"+str(min(dict3[key3]))+"\n")
w.close()
'''
dict3 = defaultdict(list)
for key in dict2:
    for i in range(len(dict2[key])):
        if dict2[key][i] in dict1.values():
'''
   
w.close()
res2.close()
structsgood.close()     
print(countres)
print(countnores)
