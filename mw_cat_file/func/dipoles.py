#!/usr/bin/env python
# coding: utf-8
# Roxanne Berthin <roxanne.berthin@sorbonne-universite.fr>, version 16/02/2021


import sys
import argparse
import numpy as np
from func.temperature import cat_temperature


def cat_dip(dir_list, step, nat, freq):
    fout = open('trajectories_cat_1-'+str(len(dir_list))+'.xyz', 'w')
    header = '# Dipoles on mobile particles in atomic unit\n'\
             '# -----------------------------------------\n'\
             '# Dipole:   1 au = 2.541746 D\n'\
             '#          mux                     muy                     muz'
    fout.write(header)
    for i in range (len(dir_list)):
        print('    directory '+str(i+1)+'/'+str(len(dir_list)))
        fin = open(str(dir_list[i])+'/dipoles.out','r')

        if i < (len(dir_list)-1):
            for j in range(int(step[i]/freq)):
                l = fin.readline()
                fout.write(l)
                for k in range(nat):   
                    line = fin.readline()
                    fout.write('{0}   {1}   {2}\n'.format(
                           line.split()[0], line.split()[1], line.split()[2]))
        else :
            for j in range(int(step[i]/freq)+1):
                l = fin.readline()
                fout.write(l)
                for k in range (nat):
                    line = fin.readline()
                    fout.write('{0}   {1}   {2}\n'.format(
                           line.split()[0], line.split()[1], line.split()[2]))



