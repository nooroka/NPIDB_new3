#!/usr/bin/env python
# coding: utf-8

import __main__
__main__.pymol_argv = [ 'pymol', '-x' ]
import sys
import pymol
from pymol import cmd,stored
pymol.finish_launching()
sys.argv1 = sys.argv[1].split(":")
sys.argv2 = sys.argv[2].split(":")
if sys.argv1[0]!=sys.argv2[0]:
    cmd.fetch(sys.argv1[0])
    cmd.fetch(sys.argv2[0])
    cmd.save("{}.pdb".format(sys.argv1[0]))
    cmd.save("{}.pdb".format(sys.argv2[0]))
elif sys.argv1[0] == sys.argv2[0]:
    cmd.fetch(sys.argv1[0],"{}".format(sys.argv1[0]))
    cmd.fetch(sys.argv2[0],"{}2".format(sys.argv2[0]))
    sys.argv2[0] = "{}2".format(sys.argv2[0])
    cmd.save("{}.pdb".format(sys.argv1[0]))
    cmd.save("{}.pdb".format(sys.argv2[0]))
    '''
    cmd.fetch(sys.argv1[0])
    cmd.save("{}.pdb".format(sys.argv1[0]))
    sys.argv2[0] = "{}_2".format(sys.argv1[0])
    cmd.load("{}.pdb".format(sys.argv1[0]),"{}".format(sys.argv2[0]))
    cmd.save("{}.pdb".format(sys.argv1[0]))
    cmd.save("{}.pdb".format(sys.argv2[0]))
    '''
sys.argv11 = sys.argv1[1].split("_")
sys.argv22 = sys.argv2[1].split("_")

if str(sys.argv11[1]).count("-") == 1:
    sys1ch1 = sys.argv11[1].split("-")[0]#цифры
    sys1ch2 = sys.argv11[1].split("-")[1]
elif str(sys.argv11[1]).count("-") == 2 and sys.argv11[1][0] == "-":
    sys1ch1 = "-"+str(sys.argv11[1].split("-")[1])
    sys1ch2 = sys.argv11[1].split("-")[2]
elif str(sys.argv11[1]).count("-") == 2 and sys.argv11[1][0] != "-":
    sys1ch1 = str(sys.argv11[1].split("-")[0])
    sys1ch2 = "-"+str(sys.argv11[1].split("-")[2])
elif str(sys.argv11[1]).count("-") == 3:
    print(sys.argv11[1].split("-"))
    sys1ch1 = "-"+str(sys.argv11[1].split("-")[1])
    sys1ch2 = "-"+str(sys.argv11[1].split("-")[3])
if str(sys.argv22[1]).count("-") == 1:
    sys2ch1 = sys.argv22[1].split("-")[0]
    sys2ch2 = sys.argv22[1].split("-")[1]
elif str(sys.argv22[1]).count("-") == 2 and sys.argv22[1][0] == "-":
    print(sys.argv22[1].split("-"))
    sys2ch1 = "-"+str(sys.argv22[1].split("-")[1])
    sys2ch2 = sys.argv22[1].split("-")[2]
elif str(sys.argv22[1]).count("-") == 2 and sys.argv22[1][0] != "-":
    print(sys.argv22[1].split("-"))
    sys2ch1 = str(sys.argv22[1].split("-")[0])
    sys2ch2 = "-"+str(sys.argv22[1].split("-")[2])
elif str(sys.argv22[1]).count("-") == 3:
    print(sys.argv22[1].split("-"))
    sys2ch1 = "-"+str(sys.argv22[1].split("-")[1])
    sys2ch2 = "-"+str(sys.argv22[1].split("-")[3])
 

cmd.hide("everything")
cmd.bg_color("white")

cmd.select("{}_D".format(sys.argv2[0]),"{} and chain D".format(sys.argv2[0]))
cmd.alter('{}_D'.format(sys.argv2[0]), 'chain = "Z"')
cmd.select("{}_A".format(sys.argv2[0]),"{} and chain A".format(sys.argv2[0]))
cmd.alter('{}_A'.format(sys.argv2[0]), 'chain = "X"')
cmd.select("{}_B".format(sys.argv2[0]),"{} and chain B".format(sys.argv2[0]))
cmd.alter('{}_B'.format(sys.argv2[0]), 'chain = "Q"')
cmd.select("{}_C".format(sys.argv2[0]),"{} and chain C".format(sys.argv2[0]))
cmd.alter('{}_C'.format(sys.argv2[0]), 'chain = "W"')
cmd.select("{}_E".format(sys.argv2[0]),"{} and chain E".format(sys.argv2[0]))
cmd.alter('{}_E'.format(sys.argv2[0]), 'chain = "V"')
cmd.select("{}_F".format(sys.argv2[0]),"{} and chain F".format(sys.argv2[0]))
cmd.alter('{}_F'.format(sys.argv2[0]), 'chain = "Rl"')
cmd.select("{}_G".format(sys.argv2[0]),"{} and chain G".format(sys.argv2[0]))
cmd.alter('{}_G'.format(sys.argv2[0]), 'chain = "U"')
cmd.select("{}_J".format(sys.argv2[0]),"{} and chain J".format(sys.argv2[0]))
cmd.alter('{}_J'.format(sys.argv2[0]), 'chain = "R"')
cmd.select("{}_K".format(sys.argv2[0]),"{} and chain K".format(sys.argv2[0]))
cmd.alter('{}_K'.format(sys.argv2[0]), 'chain = "T"')
cmd.select("{}_O".format(sys.argv2[0]),"{} and chain O".format(sys.argv2[0]))
cmd.alter('{}_O'.format(sys.argv2[0]), 'chain = "Gk"')
cmd.select("{}_P".format(sys.argv2[0]),"{} and chain P".format(sys.argv2[0]))
cmd.alter('{}_P'.format(sys.argv2[0]), 'chain = "Y"')
cmd.select("{}_M".format(sys.argv2[0]),"{} and chain M".format(sys.argv2[0]))
cmd.alter('{}_M'.format(sys.argv2[0]), 'chain = "S"')
cmd.select("{}_H".format(sys.argv2[0]),"{} and chain H".format(sys.argv2[0]))
cmd.alter('{}_H'.format(sys.argv2[0]), 'chain = "Lk"')
cmd.select("{}_N".format(sys.argv2[0]),"{} and chain N".format(sys.argv2[0]))
cmd.alter('{}_N'.format(sys.argv2[0]), 'chain = "Ln"')
cmd.select("{}_L".format(sys.argv2[0]),"{} and chain L".format(sys.argv2[0]))
cmd.alter('{}_L'.format(sys.argv2[0]), 'chain = "Ll"')
cmd.select("{}_I".format(sys.argv2[0]),"{} and chain I".format(sys.argv2[0]))
cmd.alter('{}_I'.format(sys.argv2[0]), 'chain = "Li"')


if sys.argv22[0] == "D":
    sys.argv22[0] = "Z"
if sys.argv22[0] == "A":
    sys.argv22[0] = "X"
if sys.argv22[0] == "B":
    sys.argv22[0] = "Q"
if sys.argv22[0] == "C":
    sys.argv22[0] = "W"
if sys.argv22[0] == "E":
    sys.argv22[0] = "V"
if sys.argv22[0] == "F":
    sys.argv22[0] = "Rl"
if sys.argv22[0] == "G":
    sys.argv22[0] = "U"
if sys.argv22[0] == "J":
    sys.argv22[0] = "R"
if sys.argv22[0] == "K":
    sys.argv22[0] = "T"
if sys.argv22[0] == "O":
    sys.argv22[0] = "Gk"
if sys.argv22[0] == "P":
    sys.argv22[0] = "Y"
if sys.argv22[0] == "M":
    sys.argv22[0] = "S"
if sys.argv22[0] == "H":
    sys.argv22[0] = "Lk"
if sys.argv22[0] == "N":
    sys.argv22[0] = "Ln"
if sys.argv22[0] == "L":
    sys.argv22[0] = "Ll"
if sys.argv22[0] == "I":
    sys.argv22[0] = "Li"
 


print(sys2ch1)
print(sys2ch2)
cmd.select("{}_{}_{}-{}".format(sys.argv1[0],sys.argv11[0],sys1ch1,sys1ch2), "{} and resi {}-{} and chain {}".format(sys.argv1[0],sys1ch1,sys1ch2,sys.argv11[0]))
cmd.show("cartoon","{}_{}_{}-{}".format(sys.argv1[0],sys.argv11[0],sys1ch1,sys1ch2))
cmd.select("{}_{}_{}-{}".format(sys.argv2[0],sys.argv22[0],sys2ch1,sys2ch2), "{} and resi {}-{} and chain {}".format(sys.argv2[0],sys2ch1,sys2ch2, sys.argv22[0]))#другой chain
cmd.show("cartoon","{}_{}_{}-{}".format(sys.argv2[0],sys.argv22[0],sys2ch1,sys2ch2))
cmd.color("red","{}_{}_{}-{}".format(sys.argv1[0],sys.argv11[0],sys1ch1,sys1ch2))
cmd.color("blue","{}_{}_{}-{}".format(sys.argv2[0],sys.argv22[0],sys2ch1,sys2ch2))
cmd.super("{}_{}_{}-{}".format(sys.argv1[0],sys.argv11[0],sys1ch1,sys1ch2),"{}_{}_{}-{}".format(sys.argv2[0],sys.argv22[0],sys2ch1,sys2ch2))
cmd.set("seq_view",1) 
cmd.set("label_size","40")

cmd.label("chain {} and n. CA and i. {}".format(sys.argv11[0],sys1ch1),"'{}_{}_{}-{}'".format(sys.argv1[0],sys.argv11[0],sys1ch1,sys1ch2))
cmd.label("chain {} and n. CA and i. {}".format(sys.argv22[0],sys2ch1),"'{}_{}_{}-{}'".format(sys.argv2[0],sys.argv22[0],sys2ch1,sys2ch2))
cmd.save("{}_{}_domains_changed.pse".format(sys.argv1[0],sys.argv2[0]))
cmd.save("{}_{}_domains_changed.pdb".format(sys.argv1[0],sys.argv2[0]))


cmd.quit()



