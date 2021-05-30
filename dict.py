#!/usr/bin/env python
#coding: utf-8
import os
import random
from collections import defaultdict
from itertools import chain, combinations, product
import sys
dict1 = defaultdict(list)
list1 = []
op = open("b_pfam_struct_types.txt","r")
list2 = []
structgood = open("structsgood2.txt","r")
for line2 in structgood:
    line2 = line2.strip()
    line2 = line2.split(".")
    list2.append(line2[0])
structgood.close()
listr = []
for line in op:
    line = line.strip()
    if "INSERT INTO `b_pfam_struct_types` VALUES" in line:
        line = line.split()
        lineintmode = line[4].split(",")
        lineintmode[1] = lineintmode[1].split(".")
        os.chdir("/home/npidb/data/pdb_new/dna")
        if os.path.exists("pdb{}.pdb".format(lineintmode[1][0][1:])):
            os.chdir("/home/nooroka/backup04052021")
            a = str(lineintmode[1][0][1:])+":"+str(lineintmode[2][1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])
            b = str(lineintmode[9][1:-1])+"_"+str(lineintmode[12])+"-"+str(lineintmode[13])
            if str(lineintmode[5][1:-1]) == str(sys.argv[1]) and str(lineintmode[6][1:-1])!="||":
                dict1[b].append(a)
                


print(dict1)
for key in dict1:
    dictres = dict()
    for i in range(len(dict1[key])):
    #i = random.randint(0, len(dict1[key])-1)
        dict1keyi = dict1[key][i].split(":")
        if dict1keyi[0] in list2:
           os.chdir("/home/npidb/data/pdb_new/dna")
           op = open("pdb{}.pdb".format(dict1keyi[0]),"r")
           for line2 in op:
               if "REMARK   2 RESOLUTION."  in line2:
                    line2 = line2.strip()
                    line2 = line2.split()
                    dictres[dict1[key][i]] = float(line2[3])
           os.chdir("/home/nooroka/backup04052021")
    print(dictres)
    if len(dictres) > 0:
        min_value = min(dictres.values())
        min_keys = [k for k in dictres if dictres[k] == min_value]
        if "3cmy:A_2-58" not in min_keys:
           list1.append(random.choice(min_keys))
        else:
            print(dictres)
#list1 = ["2r5y:A_88-158", "5hod:A_86-142", "1b72:A_206-260"]
#print([[x,y] for i,x in enumerate(list1) for j,y in enumerate(list1) if i != j])
print(list1)
print(dict1)
#print(len(dict1.keys()))
w = open("pairs29_PF13465.txt","w")
for p in combinations(list1, 2):
    if str(p[0])!=str(p[1]):
        w.write(str(p[0])+"\t"+str(p[1])+"\n")
w.close()
print(len(list1))
print(list1)
