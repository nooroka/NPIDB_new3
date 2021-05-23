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
            if str(lineintmode[5][1:-1]) == str(sys.argv[1]):
                dict1[b].append(a)

for key in dict1:
    for i in range(len(dict1[key])):
        dict1keyi = dict1[key][i].split(":")
        if dict1keyi[0] in list2:
            list1.append(dict1[key][i])
            break
#list1 = ["2r5y:A_88-158", "5hod:A_86-142", "1b72:A_206-260"]
#print([[x,y] for i,x in enumerate(list1) for j,y in enumerate(list1) if i != j])
print(dict1)
#print(len(dict1.keys()))
w = open("pairs29_PF03377.txt","w")
for p in combinations(list1, 2):
    if str(p[0])!=str(p[1]):
        w.write(str(p[0])+"\t"+str(p[1])+"\n")
w.close()
print(len(list1))
print(list1)
