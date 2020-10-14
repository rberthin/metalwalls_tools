#!/usr/bin/env python
# coding: utf-8


import os
from itertools import islice
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("value", help = "the value you want to add/take of on each side")
args = parser.parse_args()
cut = float(args.value)

filein = open('data.inpt', 'r')
fileout = open('new_data.inpt', 'w')

head = list(islice(filein, 2))
for n in range(2):
   fileout.write(str(head[n]))

ligne = filein.readline()
natom_tot = int(ligne.split()[1])
fileout.write(ligne)

ligne = filein.readline()
natom_elec = int(ligne.split()[1])
fileout.write(ligne)

natom_bulk = natom_tot - natom_elec

head = list(islice(filein, 3))
for n in range(3):
   fileout.write(str(head[n]))

atname, atx, aty, atz = np.loadtxt(filein, dtype='str', unpack= True, comments='#',)
atx = atx.astype(float)
aty = aty.astype(float)
atz = atz.astype(float)

for atom in range(natom_bulk):
   fileout.write("{0}   {1}  {2}  {3}\n".format(
         atname[atom], atx[atom], aty[atom], atz[atom]+cut))

for elec in range(natom_bulk,natom_tot):
   print(elec)
   if elec < (natom_bulk + (natom_elec/2)):
      fileout.write("{0}   {1}  {2}  {3}\n".format(
             atname[elec], atx[elec], aty[elec], atz[elec]))

   else:
      fileout.write("{0}   {1}  {2}  {3}\n".format(
             atname[elec], atx[elec], aty[elec], atz[elec]+cut))

filein.close()
fileout.close()

