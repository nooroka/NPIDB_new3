#!/usr/bin/env python
#coding: utf-8
import os
op = open("/home/nooroka/backup04052021/PF00046/PF00046_structs.txt","r")
w = open("/home/nooroka/backup04052021/PF00046/PF00046_int.txt","w")
w1 = open("/home/nooroka/backup04052021/PF00046/pdbPF00046.txt","w")
listresstructs = []
opl = open("/home/nooroka/backup04052021/structsgood2.txt","r")
list1 = []
countstructs = 0 #подсчет количества структур
#если убрать часть с listresstructs, то без учета разрешения 
for linel in opl:
    linel = linel.strip()
    listresstructs.append(linel)
'''calculating the number of structures'''
liststructs = []

for line in op:
    line = line.strip()
    line = line.split()
    for i in range(len(line)):
        op2 = open("/home/nooroka/backup04052021/result_sqldatabase_updated_new_sorted.txt","r")
        for line2 in op2:
            #if str(line[i]) in line2:
            if str(line[i]) in line2 and str(line[i]) in listresstructs:
                liststructs.append(line[i])
                line2 = line2.strip()
                w.write(str(line2)+"\n")
                line2 = line2.split(".")
                os.chdir("/home/npidb/data/pdb_new/dna")
                if os.path.exists("/home/npidb/data/pdb_new/dna/pdb{}.pdb".format(line2[0])):
                    countstructs+=1
                os.chdir("/home/nooroka/backup04052021")
                list1.append(line2[0])
                w1.write(str(line2[0])+";"+" ")
        op2.close()
w1.close()
w.close()
op.close()
listdomains = []
'''calculating the number of domains'''
file1 = open("/home/nooroka/backup04052021/b_pfam_struct_types.txt","r")
countlines = 0
for line in file1:
    if "INSERT" in line:
        line = line.strip()
        line = line.split()
        linef = line[4].split(",")
        lineff = linef[0][2:-1]
        lines = str(lineff)+"."+str(linef[2][1:-1])+"_"+str(linef[3])+"-"+str(linef[4])+"."+str(linef[1][1:-1])
        os.chdir("/home/npidb/data/pdb_new/dna")
        if os.path.exists("/home/npidb/data/pdb_new/dna/pdb{}.pdb".format(lineff)):
            if lines in liststructs:
                countlines+=1
                linedom = str(linef[9][1:-1])+"_"+str(linef[12])+"-"+str(linef[13])
                listdomains.append(linedom)
        os.chdir("/home/nooroka/backup04052021")
'''for particular interaction mode'''
count2 = 0
op3 = open("/home/nooroka/backup04052021/PF00046/PF00046_int.txt","r")
for line3 in op3:
    line3 = line3.strip()
    line3 = line3.split(" ",1)
    if len(line3) > 1:
        if "L-Mj" in line3[1]:
        #if  line3[1] == "H-Bb H-Mj L-Bb":
            print(line3)
            count2+=1
op3.close()

print(liststructs)
#print("len(liststructs) "+str(len(liststructs)))
print(set(listdomains))
print("len(setlistdomains)"+str(len(set(listdomains))))
print("countstructs "+str(countstructs))
#print("count(lines)"+str(countlines))
print("count2 "+str(count2))   
