#!/usr/bin/env python
#coding: utf-8

from Bio import SeqIO
from Bio.PDB import PDBParser 
import itertools
from Bio.PDB import NeighborSearch, PDBParser, Selection #import networkx as nx
import numpy.random as rnd
import sys
sysargv11 = sys.argv[1].split(":")[0]
sysargv22 =  sys.argv[2].split(":")[0]
sysargvch1 = sys.argv[1].split(":")[1]
sysargvch2 = sys.argv[2].split(":")[1]
chain1 = "A"
chain2 = "D"
chain11 = sysargvch1.split("_")[0]
chain22 = sysargvch2.split("_")[0]
print(chain1)
print(chain2)
p = PDBParser()
s = p.get_structure("{}_{}".format(sysargv11,sysargv22), "{}{}_{}{}.pdb".format(sysargv11,chain11,sysargv22,chain22))
table = open("{}_{}.txt".format(sysargv11,sysargv22),"r")
table_out = open("{}_{}_out3.txt".format(sysargv11,sysargv22),"w") 
list11 = []
list22 = []
for line in table:
    line = line.strip()
    line = line.split()
    if len(line) > 1:
        line11 = line[0].split(":")
        line22 = line[1].split(":")
        list11.append(line11)
        list22.append(line22)
    elif len(line) == 1 and line[0].split(":")[1][0] == str(chain1):
        line11 = line[0].split(":")
        list11.append(line11)
    elif len(line) == 1 and line[0].split(":")[1][0] == str(chain2):
        line22 = line[0].split(":")
        list22.append(line22) #не добавляется в list22
print(list11)
print(list22)

for i in range(len(list11)):
        for j in range(len(list22)):
            for chains in s:
                for chain in chains:
                    if chain.get_id() ==  str(chain1):#стопорится здесь
                        for residue in chain:
                            for atom in residue:
                                if str(residue.get_resname()) == str(list11[i][0][0:3]) and str(residue.get_id()[1]) == str(list11[i][0][3:]) and str(atom.get_name()) == "CA":
                                    table_out.write(str(residue.get_resname())+str(residue.get_id()[1])+":"+str(chain.get_id()[-1])+" ")
                                    a1 = residue['CA']  
                    if chain.get_id() == str(chain2):
                        for residue2 in chain:
                            for atom2 in residue2:
                                if str(residue2.get_resname()) ==  str(list22[j][0][0:3]) and str(residue2.get_id()[1]) == str(list22[j][0][3:]) and str(atom2.get_name()) == "CA":
                                    table_out.write(str(residue2.get_resname())+str(residue2.get_id()[1])+":"+str(chain.get_id()[-1])+" ")
                                    a2 = residue2['CA']
                table_out.write(str(a1-a2))
                table_out.write("\n")

table.close()
table_out.close()

count = 0
list222 = []
for d in range(len(list22)):
    list222.append(str(list22[d][0])+str(":{}".format(chain2))) #список с теми ближайшими, которым должны соответствовать

chain = s[0][str(chain1)]  # Supply chain name for "center residues"
for k in range(len(list11)):
    a = list11[k][0][3:]
    a = int(a)
    center_residues = [chain[a]] #ищем остаток
    print(center_residues)
    center_atoms1 = Selection.unfold_entities(center_residues, 'A') #атомы этого остатка
    for i in range(len(center_atoms1)):
        if center_atoms1[i].name == "CA":
            center_atom = center_atoms1[i]
    atom_list = [atom for atom in s.get_atoms() if atom.name == 'CA']
    chain_list = Selection.unfold_entities(center_residues, "C")
    ns = NeighborSearch(atom_list)
    nearby_residues = {str(res)+" "+str(res.get_full_id()[2]) for res in ns.search(center_atom.coord, 5, 'R')}
    # Print just the residue number (WARNING: does not account for icodes)
    nearby_residues = list(nearby_residues)
    list1 = []
    for i in range(len(nearby_residues)):
        linek1 = nearby_residues[i].split()
        linek1[3] = linek1[3].split("=")
        if str(linek1[6]) == str(chain2):
            list1.append(str(linek1[1])+str(linek1[3][1])+":"+str(linek1[6]))
    #print(sorted(list1))
    if len(set(list222)&set(list1)) > 0:
        print (set(list222)&set(list1))
        count+=1
print(count)
print(len(list11))
print(list11)
print(float(count)/float(len(list11)))


count2 = 0
list111 = []
for d in range(len(list11)):
    list111.append(str(list11[d][0])+str(":{}".format(chain1)))
chain22 = s[0][str(chain2)]  # Supply chain name for "center residues"
#посмотреть, есть ли пересечение с list111

for k in range(len(list22)):
    a = list22[k][0][3:]
    a = int(a)
    center_residues2 = [chain22[a]] #ищем остаток
    print(center_residues2)
    center_atoms11 = Selection.unfold_entities(center_residues2, 'A') #атомы этого остатка
    for i in range(len(center_atoms11)):
        if center_atoms11[i].name == "CA":
            center_atom2 = center_atoms11[i]
    atom_list2 = [atom for atom in s.get_atoms() if atom.name == 'CA']
    chain_list2 = Selection.unfold_entities(center_residues2, "C")
    ns2 = NeighborSearch(atom_list2)
    
    nearby_residues2 = {str(res)+" "+str(res.get_full_id()[2])  for res in ns2.search(center_atom2.coord, 5, 'R')}
    # Print just the residue number (WARNING: does not account for icodes)
    nearby_residues2 = list(nearby_residues2)
    list2 = []
    for i in range(len(nearby_residues2)):
        linek2 = nearby_residues2[i].split()
        linek2[3] = linek2[3].split("=")
        if str(linek2[6]) == str(chain1):
            list2.append(str(linek2[1])+str(linek2[3][1])+":"+str(linek2[6]))  #ближайшие к соседям из цепи K
    if len(set(list111)&set(list2)) > 0:
        print (set(list111)&set(list2))
        count2+=1
print(count2)
print(len(list22))
print(float(count2)/float(len(list22)))

if float(count)/float(len(list11)) >= 0.8 or float(count2)/float(len(list22)) >= 0.8:
    print("ok")
    w = open("/home/nooroka/backup04052021/graphfile29_PF13465.txt","a")
    w.write(str(sys.argv[1])+"\t"+str(sys.argv[2])+"\t"+"ok"+"\n")
    w.close()
