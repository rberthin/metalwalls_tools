#!/usr/bin/env python
# coding: utf-8

import sys
import argparse
import numpy as np

def cat_charges(dir_list, step, nat, freq):
    fout = open('charges_cat_1-'+str(len(dir_list))+'.out', 'w')
    header = '# Electrode atom charges in atomic unit\n'\
             '# -------------------------------------\n'\
             '# Charge:   1 au = 1.602176565e-19 C = 1 e\n'
    fout.write(header)
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



def cat_tot_charges(restart,dir_list, step, freq):
    fout = open('total_charges_cat_1-'+str(len(dir_list))+'.out', 'w')
    header = '# Total charges on electrodes in atomic unit\n'\
             '# ------------------------------------------\n'\
             '# Charge:   1 au = 1.602176565e-19 C = 1 e\n'

    if restart == 'None':
        fout.write(header)
        count = 0
    else:
        r_file = open(restart,'r')
        line = r_file.readlines()
        for k in range(len(line)-1):
            fout.write(line[k])
        count = int((line[-1]).split()[0])
    for i in range (len(dir_list)):
        fin = open(str(dir_list[i])+'/total_charges.out','r')
        print('    directory '+str(i+1)+'/'+str(len(dir_list)))
        line = fin.readline()
        line = fin.readline()
        line = fin.readline()

        if i < (len(dir_list)-1):
            for j in range(int(step[i]/freq)):
                line = fin.readline()
                fout.write('{0:8s}    {1} {2}\n'.format(
                          str(int(line.split()[0])+count), line.split()[1], 
                          line.split()[2]))
        else :
            for j in range(int(step[i]/freq)+1):
                line = fin.readline()
                fout.write('{0:8s}    {1} {2}\n'.format(
                           str(int(line.split()[0])+count), line.split()[1],
                           line.split()[2]))

        count = count + step[i]


