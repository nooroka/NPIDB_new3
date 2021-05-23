#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import os
import re
import shutil
from collections import defaultdict
import sys
#os.mkdir("/home/nooroka/write1")         
os.chdir("/home/npidb/data/pdb_new/Hbond")
dictlist1 = defaultdict(list)
setfiles = set()
fileend = sys.argv[1]
spl = fileend.split(":")
listdigit = []
listlast = []
listresult1 = []
listresult2 = []
listresult11 = []
listresult22 = []
fileend2 = fileend.split(":")
chain = fileend2[1].split("_")[0]
diap1 = fileend2[1].split("_")[1].split("-")[0]
diap2 = fileend2[1].split("_")[1].split("-")[1]
#spl = sys.argv[1].split(":")
listfilecount = []
for filecount in sorted(os.listdir(".")):
    h = filecount.split(".")
    if str(spl[0]) == str(h[0][0:4]) and str(h[4])=="txt":
        listfilecount.append(filecount)
for k in range(len(listfilecount)):
    op5 = open(listfilecount[k])
    listchain = []
    for line5 in op5:
        if ":" in line5:
           line5 = line5.strip()
           line5 = line5.split()
           line51 = line5[1].split(":")
           line511 = line51[1].split(".")[0]
           listchain.append(str(line511))
    if str(chain) in listchain:
        h2 = listfilecount[k].split(".")
        pdb = h2[1]

os.chdir("/home/npidb/data/pdb_new/x3dna")
file1 = "{}.{}.pdb.txt".format(spl[0],h2[1])

#print(str(chain)+" "+str(diap1)+" "+str(diap2))
listdiap = []
for i in range(int(diap1), int(diap2)+1,1):
    listdiap.append(i)
#print(listdiap)
op = open(file1,"r")
for line in op:
        result1 = ""
        result2 = ""
        if ">" in line and "<" in line:
                line = line.strip()
                line = line.split()
                digit = int(line[4])   
                listdigit.append(digit)
                for k in range(len(line)):
                    setfiles.add(file1)
                    if ">" in line[k] and "<" in line[k]:
                        b = line[k]   
                        line[k] = line[k].split(":")
                        linek1 = line[k][1].split(".")[-1][:-1]
                        linek2 = line[k][3].split(".")[-1][:-1]
                        a = str(line[k][2])
                        a1 = a.split("[")
                        base1 = a1[1].split("]") #буквы
                        base2 = a1[2].split("]") 
                        base10 = base1[0].split(".")
                        base20 = base2[0].split(".")
                        #print(str(base10[-1])+" "+str(base20[-1]))  #буквы
                        #print(str(line[5][0][-1])+" "+str(line[5][-1][0])) #цепи
                        result1 = str(base10[-1])+str(linek1)+":"+str(line[k][0][-1])
                        listresult1.append(result1)
                        result2 = str(base20[-1])+str(linek2)+":"+str(line[k][-1][0]) 
                        listresult2.append(result2)
                        #print(str(result1)+" "+str(result2)) #все связывающиеся остатки
                        dictlist1[file1].append(result1)
                        num = line[k-2] #номер в цепи
                os.chdir("/home/nooroka/write1")
                w = open("{}write.txt".format(file1),"a")
                w.write(str(result1)+" "+str(result2)+"\n")
                w.close()
                os.chdir("/home/npidb/data/pdb_new/x3dna")
       
        if "Helix" in line:
            line = line.strip()
            line = line.split()
            for d in range(len(line)):
                if "(" in line[d] and ")" in line[d]:
                    line[d] = line[d].split(")")
                    line[d][0] = line[d][0].split("(")
                    helix = line[d][0][1] #длина цепи
                    #print("helix "+str(helix))
                    if len(line) > 5: #защита против одиночных номеров
                        b = str(file1)+" "+str(line[4])+" "+str(line[6])
                        listnum = []
                        for i in range(int(line[4]), int(line[6])+1,1): #список номеров в цепи
                            listnum.append(i)
                     #   print("listnum "+str(listnum))
                        for k in range(len(listdigit)):
                            if listdigit[k] in listnum and int(helix) >= 6:
                                listresult11.append(listresult1[k])
                                listresult22.append(listresult2[k])
op.close()
listresult = listresult11+listresult22
#print(listresult)
dicthbonds = defaultdict(list)
os.chdir("/home/npidb/data/pdb_new/Hbond")
file2 = "{}.{}.pdb.hb.txt".format(spl[0],h2[1])
op2 = open(file2,"r")
for line2 in op2:
    if ":" in line2:
        line2 = line2.strip()
        line2 = line2.split()
        line220 = line2[0].split(".")
        line221 = line2[1].split(".")
        dicthbonds[line220[0]].append(line221[0])
op2.close()
#print(dicthbonds.keys())
listinthbonds = list(set(listresult)&set(dicthbonds.keys()))
#print("listinthbonds "+str(listinthbonds))
os.chdir("/home/npidb/data/pdb_new/hydrophobic")
file3 = "{}.{}.pdb.regraph.txt".format(spl[0],h2[1])
dictgraph = {}
dicthydrophobic = defaultdict(list)
op2 = open(file3,"r")
for line3 in op2:
     line3 = line3.strip()
     if len(line3) == 0:
            continue #не break, иначе будет печататься только до vertices
     if str.find(line3,'vertices:') ==-1 and str.find(line3,'edges:') == -1 and line3.isspace() == False:
            line2 = line3.split()
            if len(line2) == 2:
                dictgraph.update({line2[0]:line2[1][1:-1]}) #срезом убираем кавычки   
            elif len(line2) == 6:      #line2[1] - обычно цифра для  днк, line2[2] - обычно цифра для белка, но мб и не так.      
                if line2[4] == '"WHITE:':
                    linesplhyd = re.split(':.',str(dictgraph[line2[1]])) #пишем белок или днк после white  
                    #print("linesplhyd "+str(linesplhyd[0]))
                    if linesplhyd[0][0] != "D":
                        belok = linesplhyd[0]
                      #  print(str(belok)+" "+str(dictgraph[line2[2]]))
                        dna = dictgraph[line2[2]].split(".")[0]
                        dicthydrophobic[dna].append(dictgraph[line2[1]])
                    else:
                        linesplhyd5 = re.split(':.',str(dictgraph[line2[2]])) 
                        belok = linesplhyd5[0]
                      #  print(str(belok)+" "+str(dictgraph[line2[1]]))
                        dna = dictgraph[line2[1]].split(",")[0]
                        dicthydrophobic[dna].append(dictgraph[line2[2]])


listinthydrophobic = list(set(listresult)&set(dicthydrophobic.keys()))
hbonds = []
hydrophobic = []
#print(dicthbonds)
#print(dicthydrophobic)#по несколько белков


for k in  dicthbonds:
     for d in range(len(dicthbonds[k])):
         hbonds.append(dicthbonds[k][d])
for m in  dicthydrophobic:
     for a in range(len(dicthydrophobic[m])):
         dicta = dicthydrophobic[m][a].split(".")
         hydrophobic.append(dicta[0])
op2.close()
hbonds = list(set(hbonds))
hydrophobic = list(set(hydrophobic))
#print(hbonds)
#print(hydrophobic)
hbonds2 = []
hydrophobic2 = []
for f in range(len(hbonds)):
    hbondsk = hbonds[f].split(":")
    if str(hbondsk[1]) == str(chain) and int(hbondsk[0][3:]) in listdiap:
        hbonds2.append(hbonds[f])
for f2 in range(len(hydrophobic)):
    hydrophobicsk = hydrophobic[f2].split(":")
    if str(hydrophobicsk[1]) == str(chain) and int(hydrophobicsk[0][3:]) in listdiap:
        hydrophobic2.append(hydrophobic[f2])
print(hbonds2)
print(hydrophobic2)
hbond_hyd =  list(set(hbonds2) ^ set(hydrophobic2))+list(set(hbonds2) & set(hydrophobic2))
print(list(set(hbonds2) & set(hydrophobic2)))
print(hbond_hyd)
os.chdir("/home/nooroka/")
w = open("{}.txt".format(spl[0]),"w")
for k in range(len(hbond_hyd)):
    w.write(str(hbond_hyd[k])+"\n")
w.close()
'''
for l in range(len(hbonds2)):
    w.write(str(hbonds2[l])+"\n")
for l2 in range(len(hydrophobic2)):
    w.write(str(hydrophobic2[l2])+"\n")
w.close()
'''
