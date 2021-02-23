#!/usr/bin/env python
# coding: utf-8
# Roxanne Berthin <roxanne.berthin@sorbonne-universite.fr>, version 16/02/2021


import sys
import argparse
import numpy as np
from func.temperature import cat_temperature


def cat_charges(dir_list, step, nat, freq):
    fout = open('charges_cat_1-'+str(len(dir_list))+'.out', 'w')
    header = '# Electrode atom charges in atomic unit\n'\
             '# -------------------------------------\n'\
             '# Charge:   1 au = 1.602176565e-19 C = 1 e\n'
    for i in range (len(dir_list)):
        print('    directory '+str(i+1)+'/'+str(len(dir_list)))
        fin = open(str(dir_list[i])+'/charges.out','r')
        fin.readline()
        fin.readline()
        fin.readline()
        if i < (len(dir_list)-1):
            for j in range(int(step[i]/freq)):
                l = fin.readline()
                fout.write(l)
                for k in range(nat):   
                    line = fin.readline()
                    fout.write(line)
        else :
            for j in range(int(step[i]/freq)+1):
                l = fin.readline()
                fout.write(l)
                for k in range (nat):
                    line = fin.readline()
                    fout.write(line)

